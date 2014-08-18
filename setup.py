#from distutils.core import setup
from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as \
        description_file:
    long_description = description_file.read()
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as \
        requirements_file:
    requirements = [line.rstrip() for line in requirements_file]


setup(name='center_dmenu',
      version='0.1.0',
      author='Ryan McGowan',
      author_email='ryan@ryanmcg.com',
      description="A script to center dmenu.",
      long_description=long_description,
      url='https://github.com/RyanMcG/center_dmenu',
      install_requires=requirements,
      py_modules=['center_dmenu'],
      entry_points={
          'console_scripts': [
              'center_dmenu = center_dmenu:console_main'
          ]
      },
      classifiers=['Development Status :: 4 - Beta',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2']
      )
