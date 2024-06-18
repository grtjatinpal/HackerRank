if __name__ == '__main__':
    s = input()
    checks = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]

    for check in checks:
        # print(any(check(c) for c in s))
        for char in s:
            if check(char):  # Use the function 'check' on the character 'char'
                print(True)
                break
        else:
            print(False)
            
            print("jatin\n")