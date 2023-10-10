line = list(input().lower())
count = 0

for i in range (len(line)):
    line2 = line.copy()
    line2.pop(i)
    line3 = line2.copy()
    line3.reverse()
    if line3 == line2:
        count += 1

print(count)
        
