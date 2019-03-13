#List is mutable datatype
# String is immutable datatype

a =list('Hello')

print(a)

name = 'Zophie'

print(name[0])

if 'Zo' in name:
    print (True)
else:
    print (False)


if 'xxx' in name:
    print (True)
else:
    print (False)


for letter in name:
    print(letter)


name = 'Zophie the cat'

print(name[7])

try:
    name[7] = 'x'
except TypeError:
    print("YOU CAN NOT MODIFY A STRING!!")

name = ['a','b','c','d']

try:
    name[0] = 'z'
    print("List is a mutable datatype: Value changed to: " +name[0])
except:
    print('List blablabla')

# Strings can be sliced

name = 'Zophie a cat'

newName = name[0:7] + 'The'+  name[8:12]

print(newName)
