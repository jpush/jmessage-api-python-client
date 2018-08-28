from setuptools import setup, find_packages
from jmessage import __version__ as version


with open('README.md') as f:
    desc = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='jmessage',
    version=version,
    license = license,
    url='https://github.com/jpush/jmessage-api-python-client',
    author='jiguang',
    author_email='support@jiguang.cn',
    keywords=('JMessage', 'JMessage API', 'Android JMessage', 'iOS JMessage', 'Android IM', 'iOS IM'),
    description='JMessage\'s officially supported Python client library',
    long_description=desc,
    long_description_content_type="text/markdown",
    install_requires=[
        'requests',
    ],
    packages=find_packages(),
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
