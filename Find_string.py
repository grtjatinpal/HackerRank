def count_substring_WhileLoop(string, sub_string):
    i, index = 0, 0
    length = len(string) - len(sub_string)
    count = 0
    while (i <= length):
        j = 0
        print(f"{string[i]} == {sub_string[j]}")
        if string[i] == sub_string[j]:
            count += 1
            while(j < len(sub_string)):
                print(f"{string[i+j]} != {sub_string[j]}")
                if string[i+j] != sub_string[j]:
                    count -= 1
                    break
                j += 1
        i = i + 1
    return count


def count_substring_ForLoop(string, sub_string):
    count=0
    for i in range(0, len(string)-len(sub_string)+1):
        print(f"{string[i]} == {sub_string[0]}")
        if string[i] == sub_string[0]:
            flag=1
            for j in range (0, len(sub_string)):
                print(f"{string[i+j]} != {sub_string[j]}")
                if string[i+j] != sub_string[j]:
                    flag=0
                    break
            if flag==1:
                count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring_WhileLoop(string, sub_string)
    # count = count_substring_ForLoop(string, sub_string)
    print(count)