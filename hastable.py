class HashTable:
    def __init__(self):
        self.Max=10
        self.arr=[[] for i in range(self.Max)]

    def get_hash(self,key):
        h=0
        for i in key:
            h=h+ord(i)
            return h%(self.Max)

    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found = False
        for k,v in enumerate(self.arr[h]):
            if len(v)==2 and v[0]==key:
                self.arr[h][k]=(key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))
        

    def __getitem__(self,key):
        h=self.get_hash(key)
        for i in self.arr[h]:
            if i[0]==key:
                return i[1]

    def __delitem__(self,key):
        h=self.get_hash(key)
        for k,v in enumerate(self.arr[h]):
            if v[0]==key:
                del self.arr[h][k]

t=HashTable()
t['march 9']=130
t['march 6']=120
print(t.arr)
print(t['march 9'])
