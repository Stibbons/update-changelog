# Leave extra space to ease eventual merges
#
#
VERSION_MAJOR = 0
#
#
VERSION_MINOR = 1
#
#
VERSION_BUILD = 0
#
#

VERSION_INFO = (VERSION_MAJOR, VERSION_MINOR, VERSION_BUILD)
VERSION_STRING = "%d.%d.%d" % VERSION_INFO
__version__ = VERSION_INFO


__all__ = ['getVersion', 'getVersionString']


def getVersion():
    return __version__


def getVersionString():
    return VERSION_STRING
