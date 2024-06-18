number = int(input())
setA = set(map(int, input().split()))

number = int(input())
setB = set(map(int, input().split()))

# both are same
# setA = setA ^ setB
setA = setA.symmetric_difference(setB)

print(setA)
print(len(setA))

# 1 2 3 4 5 6 7 8 9
# 10 1 2 3 11 21 55 6 8