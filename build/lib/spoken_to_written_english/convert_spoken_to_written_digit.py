# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:11:08 2021

@author: asagar
"""


def static_rules():
    # rules defined and more can be added
    # ref: https://en.wikipedia.org/wiki/Tuple
    # ref:https://www.proz.com/kudoz/english/other/526192-2%3Ddouble3%3Dtriplewhats-for-456etc.html

    rules = {'numbers': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                         'nine': 9, 'ten': 10},
             'tuples': {'double': 2, 'triple': 3, 'quadruple': 4, 'quintuple': 5, 'sextuple': 6, 'septuple': 7,
                        'octuple': 8}}

    # To handle C M/ P M values

    other_rules = {"C M": 'CM',
                   "P M": 'PM'}

    labels = {'currencies': {'dollars': '$'}}

    return rules, other_rules, labels


def convert(text):
    """ 
    Input : Str : String text
    Output: Str : String output 
    """

    # get rules
    rules, other_rules, labels = static_rules()
    text = text.split()
    updated_text = []

    i, j = 0, 0
    while i < len(text)-1:
        first, last = text[i].lower(), text[i + 1]
        j = i + 2 if i + 2 <= len(text) else -1
        concat_text = " ".join(text[i:j])

        if concat_text in other_rules.keys():
            upd_text = other_rules[concat_text]
            updated_text.append(upd_text)
            i = i + 2

        elif first in rules['tuples'].keys():
            # check if its in tuples
            num_first = rules['tuples'][first]
            new_text = ""
            for _ in range(num_first):
                new_text = new_text + last
            updated_text.append(new_text)
            i = i + 2

        elif first in rules['numbers'].keys():
            num_first = rules['numbers'][first]

            # check if last word is related to currency
            last = last.lower()
            if last in labels['currencies'].keys():
                last = labels['currencies'][last]
                updated_text.append(last + str(num_first))

                i = i + 2

        else:
            updated_text.append(first)
            i = i + 1
    return " ".join(updated_text)

