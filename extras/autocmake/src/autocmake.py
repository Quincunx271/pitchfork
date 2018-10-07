from __future__ import print_function

from collections import namedtuple

import argparse
import inspect
import os.path
import sys

from cmake import CMake


def find(collect, el):
    return collect.index(el) if el in collect else None


def dict_key_intersect(the_dict, key_list):
    return {key: the_dict[key] for key in key_list if key in the_dict}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Make CMake easier to use")
    CMake.setup_argparser(parser)

    passthrough_index = find(sys.argv, '--')
    before = sys.argv[:passthrough_index]
    after = sys.argv[passthrough_index + 1:] if passthrough_index else []

    result = parser.parse_args(before[1:])

    cm = CMake(after, **vars(result))
    cm.run_subcommand(result.subcommand)
