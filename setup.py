# -*- coding: utf-8 -*-
import re
import ast
try:
    from setuptools import setup
except (ImportError):
    from distutils.core import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('jmessage/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='jmessage',
    version=version,
    description='JMessage\'s officially supported Python client library',
    keywords=('JMessage', 'JMessage API', 'Android JMessage', 'iOS JMessage',
              'JMessage', 'JMessage API', 'Android IM', 'iOS IM'
    ),
    license='MIT License',
    long_description=open("README.rst", "r").read(),

    url='https://github.com/jpush/jmessage-api-python-client',
    author='jpush',
    author_email='support@jpush.cn',

    packages=['jmessage', 'jmessage.groups', 'jmessage.messages', 'jmessage.users'],
    platforms='any',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],

    install_requires=[
        'requests>=1.2',
    ],
)
