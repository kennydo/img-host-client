from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    readme = f.read()


setup(
    name='img-host-client',
    version='0.0.1',
    description='Client for various image-sharing websites',
    long_description=readme,
    url='https://github.com/kennydo/img-host-client',
    author='Kenny Do',
    author_email='kedo@ocf.berkeley.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: File Sharing',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
    ],
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
