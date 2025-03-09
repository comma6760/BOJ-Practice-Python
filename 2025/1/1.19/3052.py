Input = 0
result = 0
remain = [0] * 10

for i in range(10):
    Input = int(input(""))
    remain[i] = Input % 42
    
for i in range(10):
    count = 0
    
    for j in range(i+1, 10):
        if remain[i] == remain[j]:
            count += 1
            
    if count == 0:
        result += 1
        
print(result)