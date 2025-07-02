t = int(input())

while t > 0:
  t -= 1

  n = int(input())
  final_total = n*(2*n+1)

  arr = []

  for i in range(n):
    arr.append(list(map(int, input().split())))
  
  ans = [0]*(2*n)
  
  i, j = 0, 0

  while i < (n - 1) or j < (n - 1):
    ans[i+j+1] = arr[i][j]
    final_total -= arr[i][j]
    if j < n - 1:
      j += 1
    elif i < n - 1:
      i += 1
  ans[i+j+1] = arr[i][j]    
  final_total -= arr[i][j]
  ans[0] = final_total
  
  print(*ans)
