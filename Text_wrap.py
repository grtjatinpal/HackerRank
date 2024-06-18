import textwrap
def Self_wrap(string, max_width):
    # Type casting
    string_list = list(string)
    count = 0
    for i in range(len(string)):
        if i % max_width == 0 and i != 0:
            string_list.insert(i+count, "\n")
            count = count + 1
    string = "".join(string_list)
    return string

def wrap_function(string, max_width):
    # return textwrap.wrap(string, max_width) # Output: ['asdf', 'ghjk', 'lzxc', 'vbnm']
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    
    result = Self_wrap(string, max_width)
    # result = wrap_function(string, max_width)
    print(result)