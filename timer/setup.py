longdesc = '''
This is a library calculating time taken by any peace of code.
'''

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Version info -- read without importing
kw = {}


setup(
    name = "timer",
    version = 1.0,
    description = "Timer library",
    long_description = longdesc,
    author = "Srinivas Garlapati",
    author_email = "srinivasa.b.garlapati@gmail.com",
    url = "https://github.com/gsb-eng/timer/",
    packages = [ 'timer' ],
    license = 'LGPL',
    platforms = 'Posix; MacOS X; Windows',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    **kw
)
