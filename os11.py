import sys,os

file = open('spam.txt', 'w')
file.write(('spam\n'*5))
file.close()

file = open('spam.txt')
text = file.read()
print(text)