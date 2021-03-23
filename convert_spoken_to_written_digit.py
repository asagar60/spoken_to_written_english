# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:11:08 2021

@author: asaga
"""

def static_rules():
    
    #rules defined and more can be added
    rules = {}
    rules['numbers'] = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10}
    
    #ref: https://en.wikipedia.org/wiki/Tuple
    #ref:https://www.proz.com/kudoz/english/other/526192-2%3Ddouble3%3Dtriplewhats-for-456etc.html
    rules['tuples'] = {'double':2,'triple':3, 'quadruple':4, 'quintuple':5, 'sextuple':6, 'septuple':7,'octuple':8}
    rules['currencies'] = {'dollars': '$'}
    
    return rules


def convert_spoken_to_written_english(text):
    """ 
    Input : Str : String text [ Assuming the text will have 2 words]
    Output: Str : String output 
    """
    
    
    #get rules
    rules = static_rules()
    
    updated_text = ""
    first, last = text.split()
    
    
    #check if its in tuples
    first = first.lower()
    if first in rules['tuples'].keys():
        num_first = rules['tuples'][first]
        for i in range(num_first):
            updated_text = updated_text + last
     
    elif first in rules['numbers'].keys():
            num_first = rules['numbers'][first]
            
            #check if last word is related to currency
            last = last.lower()
            if last in rules['currencies'].keys():
                last = rules['currencies'][last]
                updated_text = last + str(num_first)
    
    else:
        #handling C M abbreviations
        updated_text = "".join(text.split())
        
    return updated_text             

print(convert_spoken_to_english("Triple A"))
print(convert_spoken_to_english("two dollars"))
print(convert_spoken_to_english("C M"))
