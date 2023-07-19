def odd_number(mylist):
    oddnumbers=[]
    for numbers in mylist:
        if numbers % 2 == 1:
         oddnumbers.append(numbers)
    return oddnumbers
print(odd_number([1,2,99,98,9,97,96,95,94,93,61,62,63,64,65,66]))
        
        
      