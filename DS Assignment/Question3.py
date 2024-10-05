#Insert Delete Get Random O(1)  Leetcode-1279647415

class RandomizedSet:

    def __init__(self):
        self.val_index={}
        self.value = []

    def insert(self, val: int) -> bool:
        if val in self.val_index:
            return False
        self.val_index[val] = len(self.value)
        self.value.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.val_index:
            return False
        index = self.val_index[val]
        last_element = self.value[-1]
        self.value[index] = last_element
        self.val_index[last_element] = index
        self.value.pop()
        del self.val_index[val]
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.value)
        