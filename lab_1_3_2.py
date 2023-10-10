from collections import defaultdict
logs = defaultdict(list)
n = int(input())
for i in range (n):
    s = list(input().split(" "))
    temp = (s[1],s[2])
    logs[s[0]].append(temp)

users = list(logs.keys())
nums = 0
user = ""

for x in users:
    temp2 = 0
    check = list(logs[x])
    for a in range(len(check)):
        for b in range(len(check)):    
            if check[a][0] == check[b][0]:
                if check[a][1] != check[b][1]:
                    temp2 += 1
    if temp2 >= nums:
        nums = temp2
        user = x 
print(user)