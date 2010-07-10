#!/usr/bin/env python
# vim: set filencoding=utf8

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
SnakePlan Setup Script

@author: Mike Crute (mcrute@gmail.com)
@organization: SoftGroup Interactive, Inc.
@date: July 09, 2010
"""

import snakeplan
from setuptools import setup, find_packages


setup(
    name='snakeplan',
    version=snakeplan.__version__,
    packages=find_packages(),
    description='Open source agile project management',
    author='Mike Crute',
    author_email='mcrute@gmail.com',
    url='http://snakeplan.googlecode.com',
    include_package_data=True,
    install_requires=[
        'django>=1.0',
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development",
        "Programming Language :: Python",
    ],
    long_description=open('README', "r").read(),
)
