import textwrap

def wrap(string, max_width):
    Words = []
    word = ""
    count = 0
    for char in string:
        count += 1
        # jo phele likhe ge woh phele he add hoga
        # word = str(char) + word
        word = word + str(char)
        if count == max_width:
            Words.append(word)
            Words.append("\n")
            count = 0
            word = ""
    
    if count != 0:
        Words.append(word)
        # Words.append("\n")
        
    return Words

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)