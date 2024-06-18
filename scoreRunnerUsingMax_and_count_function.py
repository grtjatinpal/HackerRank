# Running score


n = int(input())
# arr = map(int, input().split())
# print(arr)
arr = list(map(int, input().split()))

count = arr.count(max(arr))
print(count)
for i in range(count):
  arr.remove(max(arr))  

print(max(arr))