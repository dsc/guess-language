#! python
from setuptools import setup, find_packages

setup(
    name = "guess-language",
    version = "1.0.0",
    description = "A library to guess the natural language of some text.",
    long_description = """
        Attempts to determine the natural language of a selection of Unicode (utf-8) text.
        
        Based on guesslanguage.cpp by Jacob R Rideout for KDE which itself is based on Language::Guess by Maciej Ceglowski.
    """,
    url = "http://code.google.com/p/guess-language",
    
    author = "David Schoonover",
    author_email = "dsc@less.ly",
    
    packages = ['guess_language'],
#   package_dir = {'':'src'},
#   packages=find_packages('src', exclude=['ez_setup']),
    keywords = [],
    classifiers = [],
    zip_safe = True,

)
