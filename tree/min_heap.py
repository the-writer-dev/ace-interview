class MinHeap:
    def __init__(self):
        self.q = []

    def push(self, item):
        self.q.append(item)
        self.shiftup(item)

    def pop(self):
        if len(self.q) == 1:
            return self.q.pop()

        pop_item = self.q[0]
        self.q[0] = self.q.pop()
        self.shiftdown()
        return pop_item

    def shiftup(self, item):
        pos = len(self.q) - 1
        while pos > 0:
            parent = (pos-1)//2
            if self.q[parent] > item:
                self.q[pos] = self.q[parent]
            else:
                break
            pos = parent

        self.q[pos] = item

    def shiftdown(self):
        pos = 0
        l_child = pos * 2 + 1
        while l_child < len(self.q):
            r_child = l_child + 1
            if r_child < len(self.q) and self.q[l_child] > self.q[r_child]:
                l_child = r_child
            if self.q[l_child] < self.q[pos]:
                self.q[l_child], self.q[pos] = self.q[pos], self.q[l_child]
            pos = l_child
            l_child = pos * 2 + 1

    def isleaf(self, pos):
        return pos*2 > len(self.q)


heap = MinHeap()
heap.push(2)
heap.push(3)
heap.push(5)
heap.push(1)
heap.push(7)

print(heap.q)
print(heap.pop())
print(heap.q)
print(heap.pop())
print(heap.q)
print(heap.pop())
print(heap.q)
print(heap.pop())
print(heap.q)
print(heap.pop())
