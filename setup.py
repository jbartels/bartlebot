#
#   Copyright [2011] [Jason Bartels]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import os
import sys

from setuptools import setup, find_packages
from distutils.core import Command
from subprocess import call


class Pep8Command(Command):
    description = "run pep8 script"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            import pep8
            pep8
        except ImportError:
            print 'Missing "pep8" library. You can install it using pip: ' + \
                    'pip install pep8'
            sys.exit(1)

        cwd = os.getcwd()
        retcode = call(('pep8 %s/bartlebot/ %s/test/' % (cwd, cwd)).split(' '))
        sys.exit(retcode)


setup(name='bartlebot',
        version=__import__('bartlebot').__version__,
        description='BartleBot',
        long_description=''' ''',
        classifiers=[],
        keywords='',
        author='Jason Bartels',
        author_email='jbartels@gmail.com',
        url='http://www.github.com/jbartels/bartlebot',
        license='LICENSE',
        packages=find_packages(
            exclude=[
                'ez_setup',
                'examples',
                'tests'
            ]
        ),
        include_package_data=True,
        zip_safe=False,
        install_requires=[],
        data_files=[],
        entry_points={},
        cmdclass={
            'pep8': Pep8Command
        }
)
