# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:


# def solution(N)


# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

def solution(N):
    binary_rep = format(N, 'b')
    gap = ""
    longest_gap = 0
    index = 0

    while index < len(binary_rep):
        if binary_rep[index] == "1" and gap == "":
            gap += binary_rep[index]
        elif binary_rep[index] == "1" and gap[-1] == "0":
            if len(gap) - 1 > longest_gap:
                longest_gap = len(gap) - 1
            gap = "1"
        elif binary_rep[index] == "0":
            gap += binary_rep[index]

        index += 1

    return longest_gap


print(solution(1041))  # 5
