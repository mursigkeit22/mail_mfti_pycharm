from functools import reduce
initial_capacity = 11
class HashTable:
    def __init__(self):
        self.capacity = initial_capacity  # determine the size of our internal array
        self.size = 0  # the number of elements that have been inserted
        self.buckets = [None] * self.capacity
        self.load_factor = self.size / self.capacity

# The hash function will take any item in the collection and return an integer in the range of slot names, between 0 and m-1.

    def hash_module(self, key): #TODO: we should add weights
        key = str(key)
        hashsum = 0
        for el in key:
            hashsum = hashsum + ord(el)
        hashsum = hashsum % self.capacity
        print('hash_module', hashsum)
        return hashsum
    def hash_folding(self, key):
        key = str(key)
        temp_str = ''
        for el in key:
            temp_str += str(ord(el))
        temp_int = 0
        for i in range(0,len(temp_str)-2,2):
            temp_int += int(temp_str[i:i+2])
        return temp_int


        pass
    def hash_square(self, key):
        pass

def hash_folding1(key):
    key = str(key)
    temp_str = ''
    for el in key:
        temp_str += str(ord(el))
    print(temp_str)
    # temp_str = temp_str[0:-1]
    print(temp_str)
    flag = 1
    new_temp_str =''
    for i in range(len(temp_str)):
        if flag == 1:
            new_temp_str += temp_str[i]
            flag = 2
        else:
            new_temp_str += temp_str[i]+' '
            flag = 1
    print(new_temp_str)
    list_int = 0
    my_int_list =list(map(int, new_temp_str.split()))
    hashsum = sum(my_int_list)
    return(hashsum)




def hash_folding2(key):
    key = str(key)
    temp_str = ''
    for el in key:
        temp_str += str(ord(el))
    print(temp_str)
    # temp_str = temp_str[0:-1]
    print(temp_str)
    temp_int = 0
    for i in range(0,len(temp_str),2):
        print(temp_str[i:i+2])
        temp_int += int(temp_str[i:i+2])
    return temp_int

print(hash_folding1(15234))
print('-------')
print(hash_folding2(15234))

