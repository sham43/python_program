def merge(dict1, dict):  
    result = dict1 | dict2 # use merge operator (|)  
    return result  
  
dict1 = {'A' : 'Apple', 'B' : 'Ball', 'C' : 'Cat' } # define dict1  
dict2 = {'D' : 'Dog', 'E' : 'Elephant', 'F' : 'Fish' } # define dict2  
dict3 = merge(dict1, dict2) # call merge() function  
print (dict3)    # print dict3 
