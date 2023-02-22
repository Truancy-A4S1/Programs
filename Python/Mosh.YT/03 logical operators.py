#01:07:09

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("You are eligible for loan")
else:
    print("You are NOT eligible for loan")

#01:11:43 comparison operatots
print("")
temperature = 30
if temperature > 30:
    print("It it a hod day!")
elif temperature < 10:
    print("It is a cold day!")
else:
    print("It is neither hot nor cold")

print("")

name = "Sumisu Johun"

if len(name) < 3:
    print("Name must be atleast 3 characters long")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters long")
else:
    print("Name looks good")

 
    
weight = 57 #int(input("Weight: "))
kg_or_lb = "k" #input("(L)bs or (K)g: ")

if kg_or_lb.upper() == "L":
    conv_weight = weight * .45
    print(f"weight: {conv_weight}Kg")
elif kg_or_lb.upper() == "K":
    conv_weight = weight / .45
    print(f"weight: {conv_weight}Lb")


#01:24:00 while loop
attempt = 1
secret_number = 6
while attempt <= 3:
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("You guessed it right!")
        break
    attempt = attempt + 1

else:
    print("You lose haha!")

