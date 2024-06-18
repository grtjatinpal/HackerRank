# solution 1
store_set = []
set_A = set(map(int, input().split()))
for other_set in range(int(input())): # number of Other set 
    other_set = set(map(int, input().split()))
    store_set.append(other_set)

for index in range(len(store_set)):
    if not set_A.issuperset(store_set[index]):
        print(False)
        break
else:
    print(True)


# solution 2
set_A = set(map(int, input().split()))
No_of_set = int(input())
for number_of_other_set in range(No_of_set): # number of Other set 
    other_set = set(map(int, input().split()))
    
    if not set_A.issuperset(other_set):
        print(False)
        break
else:
    print(True)
