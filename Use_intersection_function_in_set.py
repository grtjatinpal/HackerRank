
number = int(input())
setA = set(map(int, input().split()))

number = int(input())
setB = set(map(int, input().split()))

# both are same
setA = setA & setB
# setA = setA.intersection(setB)

print(len(setA))