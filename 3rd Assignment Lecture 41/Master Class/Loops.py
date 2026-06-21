# Master Class — Loops examples
# for loop over list
for i in [10,20,30]:
    print('Item', i)

# while loop example
count = 0
while count < 3:
    print('count', count)
    count += 1

# nested loops
for i in range(1,4):
    for j in range(1,4):
        print(i, j)

# break & continue
for k in range(1,6):
    if k == 3:
        continue
    if k == 5:
        break
    print('k=', k)
