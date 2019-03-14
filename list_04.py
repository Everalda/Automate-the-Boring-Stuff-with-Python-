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

#modifing by reference

spam = 42
cheese = spam
spam = 100
print("Spam is modified to : " + str(spam))
print("Cheese is not modified: "+str(cheese))


#FOR LISTS because of thre reference it will also change

spam = [0,2,3,4,5]
cheese = spam
cheese[1] = 'Hello!!'

print('This is the value for cheese: '+str(cheese))

print('This is the value for spam:'+ str(spam))

def eggs(someParameter):
    someParameter.append('Hello')

l = [0,1,2,3]
eggs(l)

print(l)


import copy

spam = ['A','B','C','D']

cheese = copy.deepcopy(spam)
print(cheese)
cheese[0] = 'XX'

print(cheese)

