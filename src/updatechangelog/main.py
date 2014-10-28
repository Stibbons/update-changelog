from argh import ArghParser, arg, expects_obj

from updatechangelog.version import getVersionString
from updatechangelog.updater import Updater


@arg('--config',
     dest='config',
     default='.update-changlog',
     help='Set the path to the .update-changelog file (default ".update-changelog')
@expects_obj
def execute(args):
    r = Updater()
    r.run()

epilog = """Copyright 2014 Gaetan Semet <gaetan@xeberon.net>.

Licensed under the terms of the Apache license, version 2.0. Please see
LICENSE in the source code for more information."""


parser = ArghParser(epilog=epilog)
parser.add_commands([execute])
parser.add_argument('--version',
                    action='version',
                    version='%(prog)s ' + getVersionString())


def main():
    """Entry-point function."""
    parser.dispatch()

if __name__ == '__main__':
    main()
