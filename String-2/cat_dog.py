"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""

def cat_dog(str):
    dog = 0
    cat = 0
    for i in range(len(str)-1):
        if str[i:i+3] == 'dog':
            dog += 1
        elif str[i:i+3] == 'cat':
            cat += 1
    if dog == cat:
        return True
    return False