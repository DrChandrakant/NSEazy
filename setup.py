from setuptools import setup
from setuptools import find_packages

pkg_location = 'src'
pkg_name     = 'nseazyaaaa'


with open('README.md') as f:
    long_description = f.read()

setup(name='NSEazy',
      version='0.0.1b1',
      author='Dr Chandrakant',
      author_email='nseazy-users@python.org',
      maintainer_email='DrChandrakant.github@gmail.com',
      description='Utilities for the NSE India API',
      long_description=long_description,
      long_description_content_type='text/markdown; charset=UTF-8',
      url='https://github.com/DrChandrakant/NSEazy',
      platforms='Cross platform (Linux, Mac OSX, Windows)',
      install_requires=['pandas'],
      license="BSD-style",
      packages=setuptools.find_packages(),
      classifiers=['Development Status :: 4 - Beta',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Education',
                   'Intended Audience :: Financial and Insurance Industry',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: BSD License',
                   'Topic :: Office/Business :: Financial',
                   'Topic :: Office/Business :: Financial :: Investment',
                   'Topic :: Scientific/Engineering :: Visualization',
                   'Topic :: Scientific/Engineering :: Information Analysis',
                   ],
      keywords=['finance','candlestick','ohlc','market','investing','technical analysis'],
      )
