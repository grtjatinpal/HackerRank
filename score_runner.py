def find_max_number(arr):
    maximum = arr[0]
    for number in range(1, len(arr)):
        if maximum < arr[number]:
            maximum = arr[number]
            
    return maximum
    
def count_occurrences(arr, target):
    count = 0
    for number in arr:
        if target == number:
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    target = find_max_number(arr)
    count = count_occurrences(arr, target)
    
    for i in range(count):
        arr.remove(target)

    print(find_max_number(arr))