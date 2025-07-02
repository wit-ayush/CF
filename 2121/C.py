t = int(input())

while t > 0:
  t -= 1
  r, c = map(int, input().split())

  arr = []
  max_v = 0
  for i in range(r):
    x = list(map(int, input().split()))
    max_v = max(max_v, max(x))
    arr.append(x)
  
  mx_count = 0
  r_arr = []

  for i in arr:
    c = 0
    for j in i:
      if j == max_v:
        mx_count += 1
        c += 1
    r_arr.append(c)

  c_arr = []

  for i in range(len(arr[0])):
    c = 0
    for j in range(len(arr)):
      if arr[j][i] == max_v:
        c += 1
    c_arr.append(c)
  
  returned = False
  for r_l in r_arr:
    for c_l in c_arr:
      if r_l + c_l - 1 == mx_count:
        print("ans",max_v - 1)
        returned = True
        break
  if not returned:
    print(r_arr)
    print(c_arr)
    print("ans<><>",max_v)
    



  
