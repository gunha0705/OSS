task = []
n = int(input())
for i in range(n):
    task.append(list(map(int, input().split())))
task.sort(key=lambda x: (x[1]))

a = 0
while len(task)>0:
    d = 0
    ed = task[0][1]
    task.remove(task[0])
    a += 1
    while d < len(task):
        if task[d][0]<=ed:
            task.remove(task[d])
            d-=1
        d+=1
print(a)