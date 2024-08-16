# #Given a string, you have to return a string in 
# which each character (case-sensitive) is repeated once.

def double_char(s):
    ss = ""
    for e in s:
        ss = ss + e + e
    return ss
