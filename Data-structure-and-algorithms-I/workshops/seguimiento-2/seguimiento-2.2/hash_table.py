class Hash_table:
    def __init__(self):
        self.table = [None]*127

    def hash_function(self, value):
        key = 0
        value = str(value)
        for i in range(len(value)):
            key += ord(value[i])
        return key%127

    def insert(self, value):
        hash = self.hash_function(value)
        l1=[]
        if self.table[hash] is None:
            l1.append(value)
            self.table[hash]=l1
        else:
            self.table[hash].append(value)

    def search(self, value):
        hash = self.hash_function(value)
        if self.table[hash] is None:
            return None
        else:
            return hash

    def remove(self, value):
        hash = self.hash_function(value)
        if self.table[hash] is None:
            return None
        else:
            self.table[hash].remove(value)


H = Hash_table()
H.insert('A')
H.insert('B')
H.insert('CC')
H.insert('B')
print(H.search('B'))
print(H.table[66])