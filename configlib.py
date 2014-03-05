#!/usr/bin/env python
import ConfigParser
from optparse import OptionParser
import os

def setConfig(option,value,configfile):
    """write an option/value pair to our config file"""
    if os.path.isfile(configfile):
        config = ConfigParser.ConfigParser()
        configfp=open(configfile,'r')
        config.readfp(configfp)
        configfp.close()
        
        config.set('options',option,value)
        configfp=open(configfile,'w')        
        config.write(configfp)
        configfp.close()
def delConfig(option,configfile):
    """delete an option from our config file"""
    if os.path.isfile(configfile):
        config = ConfigParser.ConfigParser()
        configfp=open(configfile,'r')
        config.readfp(configfp)
        configfp.close()
        
        config.remove_option('options',option)
        configfp=open(configfile,'w')        
        config.write(configfp)
        configfp.close()
def getConfig(optionname,thedefault,configfile):
    """read an option from a config file or set a default
       send 'thedefault' as the data class you want to get a string back
       i.e. 'True' will return a string
       True will return a bool
       1 will return an int       
    """
    #getConfig('something','adefaultvalue')
    retvalue=thedefault
    opttype=type(thedefault)
    if os.path.isfile(configfile):
        config = ConfigParser.ConfigParser()
        config.readfp(open(configfile))
        if config.has_option('options',optionname):
            if opttype==bool:
                retvalue=config.getboolean('options',optionname)
            elif opttype==int:
                retvalue=config.getint('options',optionname)
            elif opttype==float:
                retvalue=config.getfloat('options',optionname)
            else:
                retvalue=config.get('options',optionname)
    return retvalue
