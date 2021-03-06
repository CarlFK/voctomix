import os.path
from configparser import SafeConfigParser
from lib.args import Args

__all__ = ['Config']

def getlist(self, section, option):
	return [x.strip() for x in self.get(section, option).split(',')]

SafeConfigParser.getlist = getlist

files = [
	os.path.join(os.path.dirname(os.path.realpath(__file__)), '../default-config.ini'),
	os.path.join(os.path.dirname(os.path.realpath(__file__)), '../config.ini'),
	'/etc/voctomix/voctocore.ini',
	'/etc/voctomix.ini', # deprecated
	'/etc/voctocore.ini',
	os.path.expanduser('~/.voctomix.ini'), # deprecated
	os.path.expanduser('~/.voctocore.ini'),
]

if Args.ini_file is not None:
	files.append(Args.ini_file)

Config = SafeConfigParser()
Config.read(files)
