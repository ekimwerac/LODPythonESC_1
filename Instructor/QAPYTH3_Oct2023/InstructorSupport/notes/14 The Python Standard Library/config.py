
#[DEFAULT]
#
#name = pythontest
#path = /tmp/test

from configparser import *
config = ConfigParser()

config.add_section('GLOBALS')
config.set ('GLOBALS', 'TRACE', True)
config.add_section('FILENAMES')
config.set ('FILENAMES', 'DIR','C:\\myapp')
config.set ('FILENAMES', 'MASTER','%(dir)s\\master.qa')
config.set ('FILENAMES', 'SLAVE','%(dir)s\\slave.qa')

fh = open("config.ini", "w")
config.write(fh)
fh.close()

config.read('config.ini')
master = config.get ('FILENAMES','master', 0)
print (master)
print (config.getboolean('GLOBALS', 'TRACE') )