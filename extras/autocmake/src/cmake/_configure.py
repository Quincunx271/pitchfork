from __future__ import print_function, absolute_import

def setup_configure_parser(parser):
    parser.add_argument('--build-type', default='Debug', help='The CMAKE_BUILD_TYPE (default: Debug)')
    parser.add_argument('-G', default='Ninja', help='The generator to use (default: Ninja)', metavar='GENERATOR', dest='generator')
    parser.add_argument('--std', help='The C++ standard version to use')
    parser.add_argument('--extensions', action='store_true', help='Use the compilers extensions to the C++ standard (not recommended)')
    parser.add_argument('--c-compiler', help='The C compiler to use')
    parser.add_argument('--cxx-compiler', help='The C++ compiler to use')


def configure(cm):
    cm._execute(members=cm._BASE_MEMBERS + cm._CONFIGURE_MEMBERS, unbound=cm.rest)


def add_configure(CMake):
    CMake._CONFIGURE_MEMBERS = [
        'build_type',
        'generator',
        'std',
        'extensions',
        'c_compiler',
        'cxx_compiler',
    ]
    CMake._MEMBERS += CMake._CONFIGURE_MEMBERS
    CMake._TR_MEM_TO_ARG.update({
        'generator': '-G',
        'c_compiler': '-DCMAKE_C_COMPILER=',
        'cxx_compiler': '-DCMAKE_CXX_COMPILER=',
        'build_type': '-DCMAKE_BUILD_TYPE=',
        'std': '-DCMAKE_CXX_STANDARD=',
        'extensions': '-DCMAKE_CXX_EXTENSIONS=',
    })

    CMake._add_subcommand('configure',
        CMake._SubcommandParser(setup=setup_configure_parser, help='Configure the project'),
        run=configure)
    return CMake
