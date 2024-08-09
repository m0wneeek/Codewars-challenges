# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string 
# that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    string = string.lower()
    letter_count = {}
    
    if len(string) == 0:
        return True
    
    for letter in string:
        if letter in letter_count:
            return False
        letter_count[letter] = 1
    return True
    
