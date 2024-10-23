class Stack:
    def __init__(self) -> None:
        self.stack = []
    def push(self, item) -> None:
        self.stack.append(item)
    def pop(self):
        if len(self.stack)==0:
            return None
        return self.stack.pop()
    def peek(self):
        if(len(self.stack)==0):
            return None
        return self.stack[-1]
    def is_empty(self) -> bool:
        return len(self.stack)==0
    def size(self) -> int:
        return len(self.stack)
    
    # You can implement this class however you like