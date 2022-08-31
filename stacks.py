class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def match(string):
    s = Stack()

    for i in string:
        if i == "(" or i == "[" or i == "{":
            s.push(i)
        else:
            if s.is_empty():
                return False
            top = s.pop()
            if not check_pair(top, i):
                return False

    return s.is_empty()


def check_pair(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


print(match("({()}[)]"))
print(match("{{([][])}()}"))
