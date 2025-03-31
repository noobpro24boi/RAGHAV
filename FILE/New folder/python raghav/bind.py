my_int = 56

print(bin(my_int)[2:])
def decimal_to_binary(decimal_num):
    binary_str = format(int(decimal_num), 'b')
    return binary_str
 
print(decimal_to_binary(0.80))  
print(decimal_to_binary(10)) 
