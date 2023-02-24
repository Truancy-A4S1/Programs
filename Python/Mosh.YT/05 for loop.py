#01:43:00 For loop
for item in 'Pyhton':
    print(item)

#range function
            #1st argument is inital value
            #2nd argument is the limit value
            #3rd argument is the increment value
for item in range(0, 10, 2):
    print(item)

#list
price = [10,20,30]
total = 0
for item in price:
    total += item

print(f"Total is: {total}")


#nested loop
print("Nested Loops")
for item in range(2+1):
    for item2 in range(3):
        print(f"({item} , {item2})")

#challenge 01:51:00
#print F, height = 5 lines using all I've learned so far

#solution 1
print("Solution 1")
letterF = ['xxxxx','xx','xxxxx','xx','xx']
for i in letterF:
    print(i)


#solution 2
print("\n\nSolution 2")
letterF = [5,2,5,2,2]
for i in letterF:
    print('x' * i)

#solution 3
print("\n\nSolution 3, write L")
pattern = [2,2,2,2,5]
for i in pattern:
    output = ''
    for j in range(i):
        output += 'x'
    print(output)


#lists
print('\n\nlists (index)')
names = ['Arthur', 'Seris', 'Caera', 'Varay', 'Bairon']
print(f"print(names): {names}")

print(f"names[0] = 'Gray'")
names[0] = 'Gray'

print(f"print(names): {names}")

print(f"\nprint(names[0]): {names[0]}")
print(f"print(names[1]): {names[1]}")

print(f"\nprint(names[0][0]): {names[0][0]}")
print(f"print(names[0][1]): {names[0][1]}")

print(f"\nprint(names[-1]): {names[-1]}")
print(f"print(names[-2]): {names[-2]}")

print('\n\nlists (range)')
print(f"print(names[1:4]): {names[1:4]}")
print(f"print(names[1:]): {names[1:4]}")
print(f"print(names[:2]): {names[:2]}")

print('\n\n')
#01:59:00
#task: find the larget element in a list
num_list = [7,3,7,9,2,9,12,4,6,73,34,5,64,34,23]
largest = num_list[0]
for num in num_list:
    if num > largest:
        largest = num

print(f"largest = {largest}")    


#matrix
matrix = [
    [ 1, 2, 3],
    [ 4, 5, 6],
    [ 7, 8, 9]
]
print('Matrix 2d list')
print("""
matrix = [
    [ 1, 2, 3],
    [ 4, 5, 6],
    [ 7, 8, 9]
]
""")
print(f"matrix[0][0] = {matrix[0][0]}")
print(f"matrix[2][2] = {matrix[2][2]}")