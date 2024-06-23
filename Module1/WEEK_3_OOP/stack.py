class ArrayStack:
    """LIFO"""
    def __init__(self):
        "Create empty Stack"
        self.data = []
    def __len__(self):
        "Lenght stack "
        return len(self.data)
    def is_empty(self):
        if len(self.data) is None:
            return "list is empty"
        return "List is not empty"
    def push(self, new_data):
        "push elements in stack"
        self.data.append(new_data)
    def top(self):
        "frist elements"
        if self.is_empty():
            print("list is empty")
        else:
            return self.data[-1]
    def pop(self):
        if self.is_empty():
            print("list is empty")
        return self.data.pop()

