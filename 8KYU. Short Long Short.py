#Given 2 strings, a and b, return a string of the form short+long+short, 
#with the shorter string on the outside and the longer string on the inside. 
#The strings will not be the same length, but they may be empty ( zero length ).

def solution(a, b):
    return b + a + b if len(a)>len(b) else a + b + a

#test
solution('9', '16')
