class Hastable:
    def __init__(self):
        self.max = 10
        self.array = [None for index in range(self.max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if None not in self.array:
            print("Hash Table is Full")
        elif self.array[h] is None:
            self.array[h]=key, value
        elif self.array[h] !=None and self.array[h][0]==key:
            self.array[h] = key, value
        elif self.array[h] != None and self.array[h][0]!=key:
            self.probing(key, value)
            
    def probing(self, key, value):
        for index in range(len(self.array)):
            if self.array[index] != None and self.array[index][0]==key:
                self.array[index]=key,value
                break
        else:
            count = 0
            while count < len(self.array):
                if self.array[count] == None:
                    self.array[count] = key, value
                    break
                count += 1
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.array[h][0] == key:
            print(self.array[h][1])
        else:
            for element in self.array:
                if element[0] == key:
                    print(element[1])
                    break
            else:
                print("No such Key in Hash Table")
                    
    def __delitem__(self, key):
        h = self.get_hash(key)
        if self.array[h][0] == key:
            del self.array[h]
        else:
            for index,element in enumerate(self.array):
                if element[0] == key:
                    del self.array[index]
                    break
            else:
                print("No such Key in Hash Table")

ht = Hastable()
ht["march 6"] = 876
ht["march 17"] = 850
ht["march 6"] = 500
ht["march 17"] = 980
ht['march 8'] = 345
ht["march 1"] = 365
ht["march 1"]=225
ht['march 3'] = 420
ht["march 30"] = 378
ht["march 12"]=410
ht["march 7"]=210
ht["march 21"]=310
ht["march 31"] = 470
ht["march 1"]
del ht["march 17"]
ht["march 19"]=190
print(ht.get_hash("march 30"))
print(ht.array)