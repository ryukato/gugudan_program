i = 1
j = 1
while i < 10:
  print(f'================= {i} 단 시작 =================')
  while j < 10:
    r = i * j
    print(f'{i} * {j} = {r}')
    j = j + 1
  i = i + 1
  j = 1
