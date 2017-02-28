# -*- coding:utf-8 -*-

import sys
from str_define import *
reload(sys)
sys.setdefaultencoding(USE_CODE)

from optparse import OptionParser
_cmd_parser = OptionParser(usage="usage: %prog [options]")
_opt = _cmd_parser.add_option
_opt("-n", "--addName", action="store", type="string", default='', help="add game name")
_opt("-p", "--addPath", action="store", type="string", default='', help="add game path")
_opt("-r", "--remove", action="store", type="string", default='', help="remove game num")
_opt("-g", "--go", action="store", type="int", default=1, help="just run")
_cmd_options, _cmd_args = _cmd_parser.parse_args()

from statistics import GameStatistics

if _cmd_options.addName and _cmd_options.addPath:
    GameStatistics(False).addGame(_cmd_options.addName, _cmd_options.addPath)
elif _cmd_options.remove:
    GameStatistics(False).removeGame(_cmd_options.remove)
elif _cmd_options.go:
    GameStatistics()