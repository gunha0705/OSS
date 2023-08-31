task = []
n = int(input())
for i in range(n):
    b,c=map(int, input().split())
    task.append([b,c])
task.sort(key=lambda x:x[1])

d = 1
a = 1
ed = task[0][1]
while len(task)>d:
    if ed<task[d][0]:
        ed = task[d][1]
        a += 1
    d += 1
print(a)