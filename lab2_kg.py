import matplotlib.pyplot as plt
from functools import reduce


picture = plt.figure(figsize=(9.6, 5.4))
with open('/Users/andro/Downloads/DS6.txt', 'r') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
a= [x,y]
i=0
for el in a[i:]:
      for j in a[i+1:]:
          s = [list(b) for b in zip(el,j)]
      i+=1

def convex_hull(points):

    left, right, none = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def rotate(a, b, c):
        return cmp((b[0] - a[0])*(c[1] - b[1]) - (b[1] - a[1])*(c[0] - b[0]), 0)

    def _left(shell, r):
        while len(shell) > 1 and rotate(shell[-2], shell[-1], r) == right:
            shell.pop()
        if not len(shell) or shell[-1] != r:
            shell.append(r)
        return shell

    points = sorted(points)
    ln = reduce(_left, points, [])
    u = reduce(_left, reversed(points), [])
    return ln.extend(u[i] for i in range(1, len(u) - 1)) or ln


lis1 = convex_hull(s)


result = []
for sublist in lis1:
    for item in sublist:
        result.append(item)

k = result[1::2]
h = result[::2]
plt.plot(k,h)
plt.scatter(y,x,color = "black")
plt.show()
picture.savefig('/Users/andro/OneDrive/Рабочий стол/lab3_kg/lab3_kg.jpg')
