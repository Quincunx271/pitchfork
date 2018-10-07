import os
import subprocess

from collections import namedtuple
from os import path

from ._configure import add_configure


@add_configure
class CMake(object):
    _BASE_MEMBERS = [
        'src_dir',
        'build_dir',
    ]
    _MEMBERS = ['cmake_exe'] + _BASE_MEMBERS

    _TR_MEM_TO_ARG = {
        'src_dir': '-H',
        'build_dir': '-B',
    }

    _SubcommandParser = namedtuple('__SubcommandParser', ['setup', 'help'])
    __Subcommand = namedtuple('__Subcommand', ['parser', 'run'])
    __subcommands = dict()


    def __init__(self, rest, **kwargs):
        self.rest = rest
        for name in CMake._MEMBERS:
            setattr(self, name, kwargs[name])

        if self.src_dir is None: self.src_dir = os.getcwd()
        if self.build_dir is None: self.build_dir = path.join(self.src_dir, 'build', 'default')

    def __repr__(self):
        return repr(self.__dict__)

    def run_subcommand(self, name):
        self.__subcommands[name].run(self)

    @classmethod
    def _add_subcommand(cls, name, subparser, run):
        cls.__subcommands[name] = cls.__Subcommand(subparser, run)

    @classmethod
    def setup_argparser(cls, parser):
        parser.add_argument('--src-dir', help='The project root directory')
        parser.add_argument('--build-dir', help='The project build directory. If not specified, defaults to a directory under SRC_DIR/build/')
        parser.add_argument('--cmake', default='cmake', help='The path the cmake executable (default: cmake)', metavar='PATH', dest='cmake_exe')
        subparsers = parser.add_subparsers(dest='subcommand')

        for name, sp in cls.__subcommands.items():
            sp.parser.setup(subparsers.add_parser(name, help=sp.parser.help))

    def _execute(self, members, unbound):
        cmd_args = [CMake._TR_MEM_TO_ARG[member] + str(getattr(self, member)) for member in members
            if getattr(self, member) is not None]
        cmd_args += unbound
        print('{} {}'.format(self.cmake_exe, cmd_args))
