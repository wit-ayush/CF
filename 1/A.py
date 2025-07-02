n, m, a = map(int, input().split())
k, l, r1, r2 = max(n,m), min(n,m), 0, 0
if k%a:
  r1 = 1
if l%a:
  r2 = 1
print((r1 + k//a)*(r2 + l//a))