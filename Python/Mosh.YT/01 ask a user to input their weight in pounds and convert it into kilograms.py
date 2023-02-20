#1
# weight_pounds = input('Enter your weight in pounds: ')
# weight_kilo = int(weight_pounds) * 0.45
# print('Your weight in kilo is:', weight_kilo)

#2
email = '''
Hilu Wurld!

Goodbye wurld..

See you soon wurld..

Your frind,
Mun
'''
print(email)

#3 
str = 'Index checkpoints'
print('String = ' + str)
print('First index = ' + str[0])
print('We can also get the last index')
print('Last index = ' + str[-1])

#4 
print('We can also print the range of the index')
print(str[0:5]) #this will print the range of the index from 0 to 5
print(str[5:]) #this will print the range of the index from 5 to the end

#we can also copy a string using this method
str_copy = str[:]
print('str_copy = ' + str_copy)

#5 (39:33 Formatted String)
fname = 'John'
lname = 'Smith'

#we can concatenate the string (less easier to read)
message = fname + ' [' + lname + '] is a python coder'
print(message)

#or we can use formatted strings
msg = f'{fname} [{lname}] is a python coder'
print(msg)

#6 (41:23 String methods)
gem_name = 'Katawa Shoujo'
print('Len(gem_name): ', len(gem_name))

#this won't change the gem_name string
print('gem_name.upper(): ' + gem_name.upper())
print('gem_name.upper(): ' + gem_name.lower())

#so the original string remains unchanged
print('gem_name: ' + gem_name)

#.find will return the index of the first occurrence of the character
print("gem_name.find('S'): ", gem_name.find('S'))
print("gem_name.find('awa'): ", gem_name.find('awa'))

print("gem_name.replace('Katawa', 'Disability'): ", gem_name.replace('Katawa', 'Disability'))

print("Shoujo'in' gem_name", 'Shoujo' in gem_name)
