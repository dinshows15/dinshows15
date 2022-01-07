def reverse_1(s):
    str =''
    for i in s:
        str= i +str
    return str

def reverse_2(string):
    string = string[::-1]
    return string

def reverse_3(string):
    string = "".join(reversed(string))
    return string

s= input('Enter Original String: ')
print(reverse_1(s))
print(reverse_2(s))
print(reverse_3(s))
