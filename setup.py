# -*- coding: utf-8 -*-
"""
Lucas Ou 2014 -- http://lucasou.com

Setup guide: http://guide.python-distribute.org/creation.html
python setup.py sdist bdist_wininst upload
"""
import sys
import os
import site
from distutils.sysconfig import get_python_lib
 
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')  # bdist_wininst
    sys.exit()


packages = [
    'newspaper',
]


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='newspaper',
    version='0.0.9.8',
    description='Simplified python article discovery & extraction.',
    author='Lucas Ou-Yang',
    author_email='lucasyangpersonal@gmail.com',
    url='https://github.com/groeneveld91/newspaper/',
    packages=packages,
    include_package_data=True,
    install_requires=required,
    license='MIT',
    zip_safe=False,
)

os.system("cp -r ./newspaper/resources /usr/local/lib/python2.7/dist-packages/newspaper-0.0.9.8-py2.7.egg/newspaper/")

os.system("cp -r ./newspaper/videos /usr/local/lib/python2.7/dist-packages/newspaper-0.0.9.8-py2.7.egg/newspaper/")

os.system("cp ./download.js /usr/local/bin/")





