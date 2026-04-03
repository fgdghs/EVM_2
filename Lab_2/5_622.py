class MyCircularQueue:

    def __init__(self, k: int):
        self.in_stack = []
        self.out_stack = []
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.in_stack.append(value)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.prepare_out_stack()
        self.out_stack.pop()
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        self.prepare_out_stack()
        return self.out_stack[-1]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        if self.in_stack:
            return self.in_stack[-1]
        return self.out_stack[0]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

    def prepare_out_stack(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
