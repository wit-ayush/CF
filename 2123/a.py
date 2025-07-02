t = int(input())

def whoWins(n):
  m = n % 4
  if m == 0:
    return "Bob"
  else:
    return "Alice"
  # 0 1 2 3 
  # A B A B 
  
while t > 0:
  t-=1
  print(whoWins(int(input())))