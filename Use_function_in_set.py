# number = int(input())
setA = set(map(int, input().split()))

# number = int(input())
setB = set(map(int, input().split()))


# for i in range(int(input)):
#     number = int(input())
#     setA.add(number)
    
# for i in range(int(input)):
#     number = int(input())
#     setB.add(number)
    
# both are same
setA = setA.union(setB)
# setA = setA | setB

print(len(setA))