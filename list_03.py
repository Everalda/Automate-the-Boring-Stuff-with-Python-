spam = ['Hello','Hi','Howdy','heyas']

print(spam.index('Hello'))

spam.append('some text')

print(spam)

spam.insert(1, 'another text')

print(spam)

spam.remove('another text')

print(spam)

repeated_list = ['cat','rat','bat','cat','rat','bat','cat','rat','bat']


repeated_list.remove('cat')

print(repeated_list)


sort_list = [2, 5, 3.14, 1, -7]
sort_list.sort()
print(sort_list)

sort_strings = ['elephant','cat','dogs','badgers']
sort_strings.sort(reverse = True)
print(sort_strings)

sort_in_alphabetical_order = ['a','z', 'A','Z']
sort_in_alphabetical_order.sort(key = str.lower)
print(sort_in_alphabetical_order)