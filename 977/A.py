x, y = map(int, input().split())
for i in range(y):
  if x % 10 == 0:
    x = x // 10
  else:
    x -= 1
print(x)
