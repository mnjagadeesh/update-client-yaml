#!/usr/bin/env python

# Read config
# Read generic config
# update in all client folder

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(module)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s',
                    )

class Update(object):
    def __init__(self):
        pass

class ReadConfig(object):
    """

    This class collects customization and generic yaml for given clients

    """
    def __init__(self, config_filename):
        self.config_filename = config_filename
        logging.info("Will Read " + self.config_filename)
