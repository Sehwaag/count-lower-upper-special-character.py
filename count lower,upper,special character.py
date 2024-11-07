def char_cal(s):
    c= 0
    k=0
    h=0
    j=0
    for char in s:
        if char.islower():
           c += 1
        elif char.isnumeric():
            k += 1
        elif char.isupper():
            h += 1 
        else:
            j += 1
    return {'LOWER':c,'NUMBER':k,'UPPER':h,'SPECIAL':j}
string=str(input())
print(char_cal(string))
