t = int(input())

def name_score(x) :
  name = ""
  score = ""

  for i in x:
    if i.isdigit():
      score += i
    elif i == '-':
      score += i
    elif i == ' ':
      pass
    else:
      name += i
  return name, int(score)

arr = []
scores = {}

while t > 0:
  t -= 1

  x = input()
  name, score = name_score(x)
  scores[name] = scores.get(name, 0) + score
  k = [name, scores[name]]
  arr.append(k)

maxScore = 0
for key in scores.keys():
  maxScore = max(maxScore, scores[key])

winner = ""

for i in arr:
  if i[1] >= maxScore and scores[i[0]] == maxScore:
    print(i[0])
    break



