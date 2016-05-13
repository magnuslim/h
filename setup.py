# -*- coding: utf-8 -*-

from __future__ import print_function

from codecs import open
from contextlib import contextmanager
from setuptools import find_packages
from setuptools import setup
from setuptools.command.sdist import sdist as _sdist
from setuptools.command.test import test as _test

###############################################################################

NAME = 'h'
DESC = 'Annotate with anyone, anywhere'
AUTHOR = 'Hypothes.is Project & contributors'
AUTHOR_EMAIL = 'contact@hypothes.is'
URL = 'https://docs.hypothes.is'
LICENSE = 'Simplified (2-Clause) BSD License'
KEYWORDS = ['annotation', 'storage', 'hosting']
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Environment :: Web Environment',
    'Framework :: Pyramid',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
]
INSTALL_REQUIRES = [
    'PyJWT>=1.0.0,<2.0.0',
    'SQLAlchemy>=0.8.0',
    'alembic>=0.7.0',
    'annotator>=0.14.2,<0.15',
    'blinker>=1.3,<1.4',
    'celery>=3.1.23,<3.2',
    'click>=6.6,<7.0',
    'cryptacular>=1.4,<1.5',
    'cryptography>=0.7',
    'deform>=0.9,<1.0',
    'deform-jinja2>=0.5,<0.6',
    'elasticsearch>=1.1.0,<2.0.0',
    'gevent>=1.1,<1.2',
    'gunicorn>=19.2,<20',
    'itsdangerous>=0.24',
    'jsonpointer==1.0',
    'jsonschema>=2.5.1,<2.6',
    'kombu>=3.0.35,<3.1',
    'pyramid>=1.6,<1.7',
    'psycogreen>=1.0',
    'psycopg2>=2.6.1',
    'pyramid_mailer>=0.13',
    'pyramid_tm>=0.7',
    'python-dateutil>=2.1',
    'python-slugify>=1.1.3,<1.2.0',
    'pyramid-jinja2>=2.3.3',
    'raven>=5.10.2,<5.11.0',
    'requests>=2.7.0',
    'statsd>=3.2.1,<3.3.0',
    'unicodecsv>=0.14.1,<0.15',
    'ws4py>=0.3,<0.4',
    'zope.sqlalchemy>=0.7.6,<0.8.0',

    # Version pin for known bug
    # https://github.com/repoze/repoze.sendmail/issues/31
    'repoze.sendmail<4.2',
]
EXTRAS_REQUIRE = {
    'dev': [
        'honcho',
        'pyramid_debugtoolbar>=2.1',
        'prospector[with_pyroma]',
        'pep257',
        'sphinxcontrib-httpdomain'
    ],
}
ENTRY_POINTS = {
    'paste.app_factory': [
        'main=h.app:create_app',
        'websocket=h.websocket:create_app',
    ],
    'console_scripts': [
        'hypothesis=h.cli:main',
        'hypothesis-buildext=h.buildext:main',
    ],
}

with open('README.rst', encoding='utf-8') as fp:
    LONGDESC = fp.read()

###############################################################################

VERSION = __import__('h').__version__
VERSION_FILE = 'h/_version.py'
VERSION_TPL = ("# This version file is autogenerated from Git data.\n"
               "def get_version():\n"
               "    return '{version}'\n")


@contextmanager
def static_version_file():
    with open(VERSION_FILE) as fp:
        previous = fp.read()
    with open(VERSION_FILE, 'w') as fp:
        fp.write(VERSION_TPL.format(version=VERSION))
    print('updated {} with version {}'.format(VERSION_FILE, VERSION))
    yield
    with open(VERSION_FILE, 'w') as fp:
        fp.write(previous)
    print('replaced original {}'.format(VERSION_FILE))


class sdist(_sdist):
    def run(self):
        with static_version_file():
            return _sdist.run(self)


class test(_test):
    def run(self):
        print('please run tox instead')


if __name__ == "__main__":
    setup(name=NAME,
          version=VERSION,
          description=DESC,
          long_description=LONGDESC,
          classifiers=CLASSIFIERS,
          keywords=KEYWORDS,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          url=URL,
          license=LICENSE,
          install_requires=INSTALL_REQUIRES,
          extras_require=EXTRAS_REQUIRE,
          entry_points=ENTRY_POINTS,
          cmdclass={'sdist': sdist,
                    'test': test},
          packages=find_packages(exclude=['*.test']),
          zip_safe=False)
