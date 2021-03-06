from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "VERSION"), encoding="utf-8") as f:
    VERSION = f.read().strip()

setup(author="Andrew Michaud",
      author_email="bots@mail.andrewmichaud.com",

      classifiers=["Development Status :: 3 - Alpha",
                   "Environment :: Console",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: MacOS :: MacOS X",
                   "Operating System :: POSIX :: Linux",
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: Implementation :: CPython",
                   "Topic :: Software Development :: Libraries"
                   ],

      entry_points={},

      install_requires=["Pillow"],

      license="BSD3",

      name="nonogen",

      packages=find_packages(),

      python_requires=">=3.6",

      url="https://github.com/alixnovosi/nonogen",

      version=VERSION)
