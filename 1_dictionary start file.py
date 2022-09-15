import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook) #print whole dictionary
print(type(phonebook)) #print obj type attr/methods, what are we dealing with
#print(phonebook(['Chris']))
phone = phonebook['Chris'] #'Chri' = keyerror (doesnt exist in dict)
print(phone)

mydictionary = {}
print(mydictionary)

mydictionary = dict(m=8, n=9)
print(mydictionary)


print()
print('*****  end section 1 ********')
print()




print()
print('*****  start section 2 - search dictionary ********')
print()


name = 'Chri'

if name in phonebook:
    print(phonebook[name])
else:
    print(name, 'is not in phonebook')




print()
print('*****  end section 2 ********')
print()




print()
print('*****  start section 3 - edit/append dictionary ********')
print()


print(phonebook)
phonebook['Chris'] = '555-0123'
phonebook['Joe'] = '555-4444'
print(phonebook)


print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


#del phonebook['Chris']
print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for k in phonebook: #keys method = default, phonebook.keys():
    print(k)
    print(phonebook[k])

for value in phonebook.values():
    print(value)

for k,v in phonebook.items():
    print('key: ',k,' value:' ,v)

for tuple in phonebook.items():
    print(tuple)

print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get('Chris','key not found')
print(phone)

#phonebook.clear()
#print(phonebook)


print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

#a = phonebook.pop('Chris','not found')

#print(a)

print(phonebook)


print()
print('*****  end section 7 ********')
print()


print()
print('*****  start section 8 - using popitem ********')
print()

print(phonebook)
#a = phonebook.popitem() #pops out last element of dicitonary
#random.choice = random lement in list

#print(a)
print(phonebook)


print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook) #turns dict/variable into list
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
random_value = phonebook[random_key]
print(random_value)

#alt
random_value = phonebook[random.choice(list(phonebook))] #keys in brackets
print(random_value)

print()
print('*****  end section 9 ********')
print()




