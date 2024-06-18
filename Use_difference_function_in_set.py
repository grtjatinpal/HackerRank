# Enter your code here. Read input from STDIN. Print output to STDOUT
number = int(input())
setA = set(map(int, input().split()))

number = int(input())
setB = set(map(int, input().split()))

# both are same
setA = setA - setB
# setA = setA.difference(setB)

print(len(setA))