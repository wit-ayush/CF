t, k = map(int, input().split())
a = input().split()

for i in range(len(a)):
  a[i] = int(a[i])
a.sort()

def main(arr):
  if t <= k:
    print(max(arr))
    return
  
  if k == 0 and min(arr) > 1:
    print(min(arr)-1)
    return
  
  if k == 0 and min(arr) == 1:
    print(-1)
    return
  
  
  if arr[k] == arr[k-1] and t > k:
    print(-1)
  else:
    print(arr[k - 1])

main(a)
