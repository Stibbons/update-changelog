import os
import re

from setuptools import find_packages
from setuptools import setup


v = open(
    os.path.join(os.path.dirname(__file__), 'src', 'updatechangelog', 'version.py'))

vc = v.read()
VERSION_MAJOR = None
VERSION_MINOR = None
VERSION_BUILD = None

print "=>", re.compile(r"VERSION_MAJOR = (.*)$", re.M).match(vc).group(1)
#
VERSION_MAJOR = re.compile(r".*VERSION_MAJOR = '(.*?)'", re.S).match(vc).group(1)
VERSION_MINOR = re.compile(r".*VERSION_MINOR = '(.*?)'", re.S).match(vc).group(1)
VERSION_BUILD = re.compile(r".*VERSION_BUILD = '(.*?)'", re.S).match(vc).group(1)
v.close()

print "VERSION_BUILD", VERSION_BUILD


readme = os.path.join(os.path.dirname(__file__), 'README.rst')

requires = [
    'unittest',
    'argh',
]


setup(name='updatechangelog',
      version=VERSION_BUILD,
      description="Update Changelog from commit messages",
      long_description=open(readme).read(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
      ],
      keywords='update changelog',
      author='Gaetan Semet',
      author_email='gaetan@xeberon.net',
      url='https://github.com/Stibbons/update-changelog/',
      license='BSD',
      packages=find_packages('.', exclude=['test*']),
      include_package_data=True,
      tests_require=['nose >= 0.11', 'mock'],
      test_suite="nose.collector",
      zip_safe=False,
      install_requires=requires,
      entry_points={
          'update-changelog': ['updatechangelog = updatechangelog.main:main'],
      })
