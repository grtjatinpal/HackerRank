def GroupBy(arr):
    List = list()
    group_Size = 0
    duplicate_key = None  # Use None instead of "null" for comparison
    for key in arr:
        if key == duplicate_key or group_Size == 0:
            group_Size += 1
            duplicate_key = key
        else:
            List.append(f"({group_Size}, {duplicate_key})")
            group_Size = 1
            duplicate_key = key
    List.append(f"({group_Size}, {duplicate_key})")
    return List


def Group_By(arr):  # Hacker Rank Test Fail this Code
    result = list()
    count = 1
    for key in range(1, len(arr)):
        if arr[key] == arr[key - 1]:
            count += 1
        else:
            result.append((count, arr[key - 1]))
            count = 1

    result.append((count, arr[key - 1]))  # Append the final group
    return result


# Input the array
arr = list(input("Enter the array elements separated by spaces: "))
# output = GroupBy(arr)
output = Group_By(arr)


for result in output:
    print(result, end=" ")
