class MinStack:

    def __init__(self):
        self.arr = []
        self.min = None

    def _set_min(self, val):
        if self.min == None or val < self.min:
            self.min = val

    def push(self, val: int) -> None:
        self.arr.append(val)
        self._set_min(val)
        

    def pop(self) -> None:
        popped = self.arr.pop()
        if popped == self.min:
            self.min = None
            for val in self.arr:
                self._set_min(val)

        return popped

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min
