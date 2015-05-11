#!/usr/bin/env python
from setuptools import setup, find_packages

from oscar_easy_thumbnail import VERSION


setup(name='django-oscar-easy-thumbnail',
      version=VERSION,
      author="Jorik Kraaikamp",
      author_email="jorik.kraaikamp@maykinmedia.nl",
      description="Easy-thumbnail replaces sorl-thumbnail",
      long_description=open('README.md').read(),
      license=open('LICENSE').read(),
      packages=find_packages(),
      include_package_data=True,
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 1 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: Unix',
          'Programming Language :: Python'],
      install_requires=['django-oscar>=0.5',
                        'easy-thumbnails>=2.2'])
