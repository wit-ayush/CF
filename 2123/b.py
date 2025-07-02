t = int(input())

def sol(arr, j, k):
  jVal = arr[j-1]
  if k != 1:
    return "Yes"
  
  max_val = arr[0]
  for i in arr:
    max_val = max(i, max_val)
  
  if max_val == jVal:
    return "Yes"
  
  return "No"

while t > 0:
  t -= 1
  n, j, k = map(int, input().split())
  print(sol(list(map(int, input().split())), j, k))