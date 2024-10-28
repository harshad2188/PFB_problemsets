#!/usr/bin/env python3
import sys

fav_dict = {'book' : 'Sapiens', 'song' : 'Rehman', 'tree' : 'cedar'}
print(fav_dict['book'])
fav_thing = 'book'
print(fav_dict[fav_thing])
print(fav_dict['tree'])
fav_dict['organism'] = 'amoeba'
print(fav_dict)
fav_dict = {'book' : 'Sapiens', 'song' : 'Rehman', 'tree' : 'cedar'}
fav_dict['organism'] = 'amoeba'
print(fav_dict)

#Question 6
for fav in fav_dict:
    print(fav)
for fav in fav_dict:
    items = fav_dict[fav]
    print(fav, items)
for fav in fav_dict:
    items = fav_dict[fav]
    print(fav, items[:3])

#Question 7
'''fav_thing1 = sys.argv[1]
fav_thing2 = sys.argv[2]
print(fav_thing1)
print(fav_thing2)
print(fav_dict[fav_thing1])
print(fav_dict[fav_thing2])'''

#Question 8
for items in fav_dict:
    print(items)
print('Enter your key:')
x = input()
print(fav_dict[x])

#Question 9
fav_dict['organism'] = 'drosophila'
print(fav_dict)

for items in fav_dict:
    print(items)
print('Enter your key:')
x = input()
y = input()
fav_dict[x] = y
print(fav_dict[x])

