
def match(string):
    stack = []

    for i in string:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        else:
            if stack == []:
                return False
            top = stack.pop()
            if not check_pair(top, i):
                return False

    return stack == []


def check_pair(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


print(match("({()}[)]"))
print(match("{{([][])}()}"))
