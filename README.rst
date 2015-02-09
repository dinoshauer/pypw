PyPW
====

Generates a random password. Can be used as a stand-alone CLI program or
imported into projects.

Installation:
~~~~~~~~~~~~~

``python setup.py install``

``pip install pypw``

Usage:
~~~~~~

``pypw -l 20`` - Generate a random password that is 20 characters long
``pypw -s "TurnTh1sIntoMyP4ssW()RD" --no-mixed`` - Generate a password
from -s without mixed casing ``pypw -h`` - Display the help screen

API:
~~~~

::

    pypw.RandomPassword(sequence=None, mixedCases=True)
        sequence(str): The string you want to create a password from
        mixedCases(bool): Generate mixed casing on letters

        returns: <pypw.RandomPassword instance>

        randomBool()
            returns: True/False

        randCase(sequence)
            - Randomizes the casing on a string or list

            sequence(str/list): The string to randomize casing on

            returns: List of characters

        generateRandomPW(length=None, alpha=True, digits=True, symbols=True)
            - Generate a random password chosen by PyPW

            length(int): Defines how many characters you want in the generated password
            alpha(bool): Choose to use alphabetical characters in randomly generated password or not
            digits(bool): Choose to use digits (0-9) in randomly generated password or not
            symbols(bool): Choose to use symbols in randomly generated password or not

            returns: Dict with result, score, ranking and phonetic

        generatePW()
            - Generate password from the arguments passed to RandomPassword

            returns: Dict with result, score, ranking and phonetic

        phonetic(sequence)
            - Generate a 'phrase' to (hopefully) help the user remember the password. (Not guaranteed to make sense!)

            sequence(str): The string you want to generate a phonetic phrase on

            returns: Str

        strength(sequence)
            - Calculate the strength of the password based on length, digits, symbols and casing

            returns: Tuple
