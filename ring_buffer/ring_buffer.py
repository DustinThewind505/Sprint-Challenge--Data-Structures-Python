class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        ### ===== current is the index as we progress through the list =====
        self.current = 0
        self.data = []

    def append(self, item):
        if len(self.data) == self.capacity:
            print(f"data: {self.data}, current:{self.current}")
            self.data[self.current] = item

            if [self.current] == [self.capacity-1]:
                self.current = 0
            else:
                self.current += 1
                
        else:
            self.data.append(item)

    def get(self):
        return self.data