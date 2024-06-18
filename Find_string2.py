def count_substring(string, sub_string):
    string_len = len(string)
    sub_string_len = len(sub_string)
    count = 0
    for i in range(string_len+1 - sub_string_len):
        match = True
        for j in range(sub_string_len):
            if string[i+j] != sub_string[j]:
                match = False
                break
        
        if match == True:
            count = count + 1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)