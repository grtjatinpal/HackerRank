# print function
def Print(List):
    for i in List:    
        print(i)
     
     
        
# solution 1
def merge_the_tools(string, k):
    # Convert the string to a list of characters
    string = list(string)
    for i in range(len(string)):
        # Check remainder character length is eqaul to k
        if(len(string)-i >= k):
            # Create a substring of length k
            str = "".join(string[:k])
            
            string.append(str)
            # Remove the processed characters from the original string
            del string[:k]
        
        # Check if there are no characters remaining
        elif(len(string)-i == 0):
            break
        
        # Process the remaining characters
        else:
            # Create a substring with the remaining characters
            str = "".join(string[:len(string)-i])
            string.append(str)
            # Remove the processed characters from the original string
            del string[:len(string)-i-1]
            break
    Remove_duplicate(string)
    
def Remove_duplicate(string, count = 0):
    # Iterate over each item in the list
    for index, i in enumerate(string):
        string[index] = string[index][0]  # Keep the first character in the item
        
        # Iterate over each character
        for j in i:
            # If the character is not already in the item, append it
            if j not in string[index]:
                string[index] = string[index]+j
    # call function
    Print(string)                



# solution 2
def merge_the_tools_2(string, k, count = 0):
    Sub_string = ""
    store_list = []
    for index in range(len(string)):
            
        if string[index] not in Sub_string:
            Sub_string = Sub_string + string[index]
        
        count += 1
        
        if count == k:
            store_list.append(Sub_string)
            count = 0
            Sub_string = ""
    
    # call function
    Print(store_list)                
    
    
    
     
# solution 3            
import textwrap
    
def merge_the_tools3(string, k):
    wrapped_string = textwrap.wrap(string, width=k)
    unique_chars_with_word = []
    for chunk in wrapped_string:
        unique_chars = ''
        for char in chunk:
            if char not in unique_chars:
                unique_chars += char
        # print(unique_chars)
        unique_chars_with_word.append(unique_chars + "\n")
     
    print("".join(unique_chars_with_word))
     
         
if __name__ == '__main__':
    string, k = input().upper(), int(input())
    # merge_the_tools(string, k) # solution 1
    # merge_the_tools_2(string, k) # solution 2
    merge_the_tools3(string, k)
    
    
    