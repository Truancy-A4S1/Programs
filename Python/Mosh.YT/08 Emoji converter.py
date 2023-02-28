#02:25:00
emoji = {
    ":)" : "🙂",
    ":(" : "☹️",
    ":D" : "😀",
    ":P" : "😋",
    ":O" : "😲",
}

message = input(" >")
converted = ""

#split(' ') makes a list of words separated by ' '
for word in message.split(' '):
    converted = converted + emoji.get(word, word) + " "

print(converted)
#02:31:00 functions
def greet_user(fname_param , lname_param):
    print(f'Hello there {fname_param} {lname_param}')
    print(f'Welcome Aboard!')


fname = input("Enter fname: ")
lname = input("Enter lname: ")
greet_user(fname_param=fname, lname_param=lname)

#name_list = input("Enter a string of names: ")
#for word in name_list.split(' '):
#    greet_user(word)

#02:45:00 return value
def square(num):
    return num * num


square_root = int(input("enter a number ang get its square: "))
print(f'Square of {square_root} is : {square(square_root)}')