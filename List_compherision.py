x = int(input())
y = int(input())
z = int(input())
n = int(input())

List = []
# outter loop
for i in range(x+1):
        
    # inner loop 
    for j in range(y+1):

        # inner loop --> inner loop
        for k in range(z+1):
            if( (i+j+k) != n):
                List.append([i,j,k])
                # List.extend([i,j,k])
                
print(List)
