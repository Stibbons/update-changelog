import sys


class UpdateChangeLog(object):

    def run(self):
        pass


def main(argv):
    instance = UpdateChangeLog()
    instance.run()

if __name__ == '__main__':
    main(sys.argv[1:])
