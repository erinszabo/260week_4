

class Queue:  # a line, obviously
    def __init__(self):
        self.items = []

    def __str__(self):
        st = []
        if not self.isEmpty():
            for i in range(self.size()):
                st.append(self.dequeue())
        return str(st)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):  # someone entering the line must pass every person in line O(n)
        self.items.insert(0, item)

    def dequeue(self):  # the first person in line just steps forward O(1)
        return self.items.pop()

    def size(self):
        return len(self.items)
