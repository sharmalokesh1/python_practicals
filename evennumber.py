def even_number(mylist):
    evennumbers = []
    for numbers in mylist:
        if numbers % 2 == 0:
            evennumbers.append(numbers)
    return evennumbers
print(even_number([1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,99,98,66,67,69,54,55]))

