# Author CJP 11/2/21

string = input('Enter a string: ')

x = len(string)

newx = x // 2

print(string[0:newx])
print(string[newx:x])