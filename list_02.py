#loops in lists
for i in range(4):
	print(i)

supplies =['pens','staplers','flame-thowers','bin']

for i in range(len(supplies)):
	print('Index '+str(i)+" in supplies is : " + supplies[i])

cat = ['fat', 'orange', 'loud']

size, color, disposition = cat
print(size)
print(color)
print(disposition)