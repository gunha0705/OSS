task = []
n = int(input())
for i in range(n):
    task.append(list(map(int, input().strip().split())))
task.sort(key=lambda x: (x[1],x[0]))

a = 0
for i in range(n):
    if len(task)==0:
        break
    d = 0
    ed = task[0][1]
    del task[0]
    a += 1
    b = len(task)
    while 
    for i in range(b):
        c = b-1-d
        d += 1
        if c<0:
            break
        elif task[c][0]<=ed:
            del task[c]
            b-=1
            d-=1
print(a)