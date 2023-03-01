#02:51:00
def emoji_converter(input_string):
    message = input_string.split(' ')

    converted = ""
    emoji_dict = {
        ":)" : "🙂",
        ":(" : "☹️",
        ":D" : "😀",
        ":P" : "😋",
        ":O" : "😲"
    }
    for word in message:
        converted += emoji_dict.get(word, word) + " "

    return converted


str = input("Enter a string: ")
print(emoji_converter(str))

#Exception
try:
    age = int(input("Enter age: "))
    quocient = 230 / age;
    print(f'age: {age}\nquocient: {quocient}')
    
except ValueError:
    print("ERROR: Please enter a number")
except ZeroDivisionError:
    print("ERROR: Age must not be 0")

#class! 03:00:00
