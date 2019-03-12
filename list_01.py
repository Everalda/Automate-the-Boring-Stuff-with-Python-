#this is an example of a simple list in Python

spam = ['cat','dog','rat', 'elephant']

print(spam[0])
print(spam[1:3])
print(spam[-1])

del spam[2]
print(spam)


if ('cat' in spam):
	print("cat is in the spam")
else:
	print("cat is not in spam")