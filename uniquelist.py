def unique_list(mylist):
    new_list=[]
    for numbers in mylist:
        if numbers not in new_list:
            new_list.append(numbers)
    return new_list
print(unique_list([6,7,8,5,4,7,8,9,5,5,5,5,6,6,7,8,9,2,]))