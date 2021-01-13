class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))
            
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] == []:
            print("No such key in Hash Table")
        for element in self.arr[h]:
            if element[0] == key:
                print(element[1])

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                print("{} deleted from the Hash table ".format(self.arr[h][index][0]))
                del self.arr[h][index]

ht = HashTable()
ht['march 6'] = 450
ht['march 3'] = 120
ht['march 17'] = 350
ht['march 6'] = 250
ht["march 2"] = 100
ht["march 9"] = 400
ht["march 11"] = 190
ht["march 31"] = 800
ht["march 29"] = 790
ht["march 19"] = 581
ht["march 21"] = 812
ht["april 8"] = 547
ht["april 20"] = 139
ht["march 32"] = 126
ht["march 16"] = 126
ht["march 15"] = 126
ht["march 14"] = 126
ht["march 13"] = 460
ht["march 21"]
ht["april 4"] = 310
del ht["april 4"]
del ht['march 2']
del ht['march 17']
del ht['march 29']
print(ht.arr)
