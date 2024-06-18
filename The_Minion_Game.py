def minion_game_With_print(string, vowel = "AEIOU", Kevin = 0, Stuart = 0):
    for i in range(len(string)):
        # check vowel
        if string[i] in vowel:
            for _ in range(i, len(string)):
                # print substrings
                print(string[i:1+_], end=" ")
                # score update
                Kevin = Kevin + 1
            print(f"Kevin Score: {Kevin}\n")
        else:
            for _ in range(i, len(string)):
                # print substrings
                print(string[i:1+_], end=" ")
                # score update
                Stuart = Stuart + 1
            print(f"Stuart Score: {Stuart}\n")
            
    print_Result(Kevin, Stuart)
            
def minion_game(string, vowel = "AEIOU", Kevin = 0, Stuart = 0):
    for i in range(len(string)):
        # check vowel
        if string[i] in vowel:
            Kevin = len(string) - i + Kevin
        else:
            # Stuart = Stuart + 1
            Stuart = len(string) - i + Stuart
            
    print_Result(Kevin, Stuart)

            
def print_Result(Kevin, Stuart):
    if Kevin == Stuart:
        print("Draw")
    elif Kevin > Stuart:
        print(f"Kevin {Kevin}")
    elif Kevin < Stuart:
        print(f"Stuart {Stuart}")

            
if __name__ == '__main__':
    s = input().upper()
    minion_game(s)
    # minion_game_With_print(s)