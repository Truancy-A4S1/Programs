#02:06:00
numbers = [5,1,2,7,5,3]
print(f'numbers: {numbers}\n')

#copy()
numbers1 = numbers.copy()
print(f'numbers1 = numbers.copy():\n')

numbers.append(20)
print(f'append(20) :\nnumbers = {numbers}\nnumbers1 = {numbers1}\n')

#0 is the index and 12 is the element to be inserted
numbers.insert(0, 12)
print(f'numbers.insert(0, 12): {numbers}\n')

#index() returns the index of the first instance of the element
print(f'To check the existence of an element in the list:')
print(f'numbers.index(1): {numbers.index(1)}')
print(f'50 in numbers: {50 in numbers}\n')

#remove() removes the first instance of the element
numbers.remove(1)
print(f'numbers.remove(1): {numbers}\n')

#pop() removes the last element
numbers.pop()
print(f'numbers.pop(): {numbers}\n')

#count() returns the number of elements in the list
print(f'numbers.count(5): {numbers.count(5)}\n')

#sort() sorts the list
numbers.sort()
print(f'numbers.sort(): {numbers}\n')

#reverse() reverses the list.
numbers.reverse()
print(f'numbers.reverse(): {numbers}\n')

#clear() removes all elements
numbers.clear()
print(f'numbers.clear(): {numbers}\n')

#exercise: remove all the duplicates in the list
this_list = [4,6,7,9,1,6,8,3,1,6,8,9,4,2,3]
this_list_len = len(this_list) - 1

#reverse the list so that the last duplicates are removed
#this_list.reverse()

for i in range(this_list_len):
    for j in range(i+1,this_list_len,1):
        if this_list[i] == this_list[j]:
            this_list.remove(this_list(this_list.index()))



#reverse the list to get back to the original order
#this_list.reverse()
print(f'Output: {this_list}\n')