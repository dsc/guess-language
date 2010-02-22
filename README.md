# guess-language

Attempts to determine the natural language of a selection of Unicode (utf-8) text.

Based on [guesslanguage.cpp](http://websvn.kde.org/branches/work/sonnet-refactoring/common/nlp/guesslanguage.cpp?view=markup) by Jacob R Rideout for KDE which itself is based on [Language::Guess](http://languid.cantbedone.org/) by Maciej Ceglowski. Original repo is at [Google Code](http://code.google.com/p/guess-language/); repackaged with package metadata [here](http://github.com/dsc/guess-language).

Detects over 60 languages; Greek (el), Korean (ko), Japanese (ja), Chinese (zh) and all the languages listed in the trigrams directory.


## Install from Github

I recommend using [Pip](http://pip.openplans.org/):

    $ pip install -e 'git://github.com/dsc/guess-language.git#egg=guess-language'

If you prefer `easy_install`:

    $ git clone git://github.com/dsc/guess-language.git
    $ easy_install guess-language

The old-school way also works:

    $ git clone git://github.com/dsc/guess-language.git
    $ cd guess-language
    $ python setup.py install

