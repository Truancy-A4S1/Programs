def find_max(lis):
    maxxx = lis[0]
    for element in lis:
        if element > maxxx:
            maxxx = element
    return maxxx