t = int(input())

matrix = []
n = 0

while t > 0:
  t -= 1
  n += 1

  x = input()
  a = []
  for i in x.split(' '):
    a.append(i)
  matrix.append(a)

i, j = 0, 0
multi = matrix[i][j]

ans = ""
while i < t and j < t:
  if str(matrix[i+1][j]*multi)[-1] == '0':
    multi *= matrix[i+1][j]
    if j+1 < t:
      j += 1
      ans += 'D'
    elif i+1 < t:
      i += 1
  else:
    multi *= matrix[i][j+1]
    if i+1 < t:
      i += 1
    elif j+1 < t:
      j += 1