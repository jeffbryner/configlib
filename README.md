configlib
=========

simple python wrapper for .conf file get, set, delete operations.

Use thusly: 

.conf file:
```
[options]
somesetting=aDifferentValue

```

python code: 
```
    from configlib import getConfig,OptionParser
    def initConfig():
        #initialize config options
        #sets defaults or overrides from config file.
        options.something=getConfig('somesetting','defaultvalue',options.configfile)
    
    if __name__ == "__main__":
        parser=OptionParser()
        parser.add_option("-c", dest='configfile' , default='', help="configuration file to use")
        (options,args) = parser.parse_args()
        initConfig()
```

pip install configlib
