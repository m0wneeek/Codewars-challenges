#Write a function, isItLetter or is_it_letter or IsItLetter, which tells us if a given character is a letter or not.

#I could have done this much more cleanly, without using the alphabet string - but it was a fun solution.

def is_it_letter(s):
    letter = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    if s in letter:
        return True
    else:
        return False

#the simpler, more efficient solution being:

def is_it_letter(s):
    return s.isalpha()
