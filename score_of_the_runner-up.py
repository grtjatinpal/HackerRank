def Find_larger(arr: list):
    larger = arr[0]
    i = 1
    while(i < len(arr)):
        if( larger == arr[i] ):
            arr.remove(arr[i])
            i = i - 1
        elif( larger < arr[i] ):
            larger = arr[i]
        
        i = i + 1

    return larger

n = int(input())
arr = list(map(int, input().split()))

larger = Find_larger(arr)
arr.remove(larger)
        
print(Find_larger(arr))