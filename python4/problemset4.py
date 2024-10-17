#!/usr/bin/env python3
#no paranthesis for strings
#[] for lists
taxa_list = ['sapiens','erectus','neanderthalensis']
taxa_string = 'sapiens : erectus : neanderthalensis'
print(taxa_string)

taxa_list = taxa_string.split(' : ')
print(taxa_list)

print(type(taxa_string))
print(type(taxa_list))

#question2g

sorted(taxa_list)
print(sorted(taxa_list))
print()
sorted_list = sorted(taxa_list, key=len)
print(sorted_list)

