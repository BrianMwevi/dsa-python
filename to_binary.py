def to_binary(N):
    index = 0
    binary_stack = []
    binary_rep = ""

    while N > 0:
        binary_stack.append(N % 2)
        N = N//2
        index += 1

    while binary_stack != []:
        binary_rep += str(binary_stack.pop())

    return binary_rep


print(to_binary(1041))
