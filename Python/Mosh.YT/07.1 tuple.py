#02:14:00
#tuples are immutable or cannot be modified
numbers = (1,2,3)
print(numbers)
print(numbers[0], numbers[1], numbers[2])

#unpacking
coordinates = (1,2,3)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(f'{x}, {y}, {z}')

x,y,z = coordinates 
print(f'{x}, {y}, {z}')


#dictionary
customer = {
    "name" : "Art",
    "age" : 66,
    "is_OP" : True
}
#check the values in the dictionary
print(customer["name"])

#set/update name to different value
customer["name"] = "Gray"
print(customer["name"])

#add a new key to store the value
customer["gender"] = ""         #we can define a key later
customer["gender"] = "Male"
print(customer["gender"])

#get a random key and return something if that key doesn't exist
#print(customer["birthdate"]) #returns 'KeyError'
print(customer.get("birthdate", "b-baka! that's not a key!") )


#exercise: print int to english equivalent
num_to_eng = {
   "1" : "one ",
   "2" : "two ",
   "3" : "three ",
   "4" : "four ",
   "5" : "five ",
   "6" : "six ",
   "7" : "seven ",
   "8" : "eight ",
   "9" : "nine ",
   "0" : "zero "
}

phone = input("Phone: ")
#solution 1: unwanted new lines are created
for i in range(len(phone)):
    print(num_to_eng[phone[i]])

#solution 2: specific digits are allowed
#print(f'{num_to_eng[phone[0]]}{num_to_eng[phone[1]]}{num_to_eng[phone[2]]}')

#solution 3: from most.yt
output = ""
for ch in phone:
    output += num_to_eng[ch]

print(output)

#end 02:26:00







