myCat = {'size':'fat','color':'orange','disposition': 'loud'}

print(myCat['size'])

print('My cat have '+ myCat['color'] + " fur.")

if ([1,2,3] == [3,2,1]):
    print("List has unordered elements")
else:
    print("List has ordered elements")

eggs = { 'age': 8,'name':'zophie','species':'cat'}
ham = {'name':'zophie','species':'cat','age': 8}

if (eggs == ham ):
    print("Dictionaries has unordered elements")
else:
    print("Dictionaries has ordered elements")

try:
    print(eggs['color'])
except KeyError:
    print("There is no color in eggs dictionaries")

if ('name' in eggs):
    print("Name is in eggs")


if ('name' not in eggs):
    print("Name is not in eggs")
else:
     print("Name is in eggs")

# methods for Dictionaries

print(eggs.keys())
print(eggs.values())
print(eggs.items())
# ways to access elements in the dictionaries
for k in eggs.keys():
    print (k)

for v in eggs.values():
    print (v)

for k, v in eggs.items():
    print((k,v))
for k, v in eggs.items():
    print(k,v)


for i in eggs.items():
    print(i)

if('cat' in eggs.values()):
    print("Cat is in dictiornary eggs")

#return value for a key or return default value with get method

print(eggs.get('age', 0)) # return 8, if there is no age key it returns 0

print(eggs.get('color','')) # returns '' because there is no color in eggs

picniqItems ={ 'apples': 5, 'cups': 5}
print("I am bringing "+ str(picniqItems.get('napkins', 0))+ " to the picnic")


# SetDefult Method
eggs.setdefault('color', 'black')

print(eggs['color'])
print(eggs)

#character counting program
import pprint
message = "The quick brown fox jumped over the lazy dog"
count = {}

for char in message.upper():
    #if there is no value set it to zero
    count.setdefault(char, 0)
    #count the quantity of elements in the message
    count[char] = count[char]+1
pprint.pprint(count)
#use pprint to order the elements
text = pprint.pformat(count)
print(text)