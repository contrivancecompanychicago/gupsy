from setuptools import setup

setup(
    name = "python-flowdock",
    version = "0.1",
    py_modules = ['flowdock'],
    scripts = ['influx'],
    install_requires = ['requests'],
    package_data = {
        '': ['*.txt', '*.rst'],
    },
    author = "Joshua Ginsberg",
    author_email = "jag@flowtheory.net",
    description = "Python client for FlowDock API",
    license = "LGPLv3",
    keywords = "flowdock api",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Topic :: Communications'
    ]
)
from distutils.core import setup
import my

setup(name='nightscout-fda-presubmission-01'
  , version=my.VERSION
  , description="Nightscout FDA meeting 1"
  , author="Ben West"
  , author_email="bewest@gmail.com"
  )
