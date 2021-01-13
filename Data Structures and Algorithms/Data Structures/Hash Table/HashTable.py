class Hashtable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]
    
# Getting the hash value for the given key
    def get_hash(self, key):
        h=0
        for char in key:
            h += ord(char)
        return h%self.max

# Adding the key and value based on hash value
    # def add_item(self, key, value):
        # h = self.get_hash(key)
        # self.arr[h] = value
    
    # instead of specifying our own method,Python having inbuilt fn __setitem__
    # By using __setitem__ we can add the key and value  just like dictionary
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value        


# Know the value associated to given key
    # def get_item(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    # instead of specifying our own method we can use __getitem__ inbuilt in Python
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]       
    

# Deleting the key 
    # def delete_item(self, key):
    #     h = self.get_hash(key)
    #     self.arr[h] = None

    # instead of specifying our own method we can use __delitem__ inbuilt in Python
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h]=None
        

ht = Hashtable()
print(ht.arr)       #[None, None, None, None, None, None, None, None, None, None]
ht["march 6"]= 420  
print(ht.arr)       #[None, None, None, None, None, None, None, None, None, 420]
ht["march 11"]=390  
print(ht.arr)       #[None, None, None, 390, None, None, None, None, None, 420]
del ht["march 11"]  
print(ht.arr)       #[None, None, None, None, None, None, None, None, None, 420]
