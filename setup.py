from distutils.core import setup
from votesmart import __version__,__license__,__doc__

long_description = open('README.rst').read()

setup(name="python-votesmart",
      version=__version__,
      py_modules=["votesmart"],
      description="Libraries for interacting with the Project Vote Smart API",
      author="James Turk",
      author_email = "jturk@sunlightfoundation.com",
      license=__license__,
      url="http://github.com/sunlightlabs/python-votesmart/",
      long_description=long_description,
      platforms=["any"],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
       install_requires=["simplejson >= 1.8"]
      )

