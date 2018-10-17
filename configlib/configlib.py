#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from everett.manager import ConfigManager
from everett.manager import ConfigIniEnv
from everett.manager import ConfigOSEnv


def getEverettManager(configfile):
    return ConfigManager(
        # Specify one or more configuration environments in
        # the order they should be checked
        [
            # Looks in OS environment first
            ConfigOSEnv(),

            # Looks in INI files in order specified
            ConfigIniEnv([
                configfile,
            ]),
        ],

    )


def getConfig(optionname, default_value=None, configfile=None):
    config = getEverettManager(configfile)
    return config(optionname, namespace='options', default=default_value)
