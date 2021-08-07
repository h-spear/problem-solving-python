string = 'abacdabacaabacaaba';
pattern = 'abacaaba';

def make_table(s):
  table = [0] * len(s)

  j = 0
  for i in range(1,len(s)):
    while j > 0 and s[i] != s[j]:
      j = table[j-1]

    if s[i] == s[j]:
      j += 1
      table[i] = j
      
  return table

def KMP(s, p):
  table = make_table(s)
  
  j = 0
  for i in range(len(s)):
    while j > 0 and s[i] != p[j]:
      j = table[j-1]
    
    if s[i] == p[j]:
      if j == len(p)-1:
        print("find ", end='')
        print(i - len(p) + 2)
        j = table[j]
      else:
        j += 1
        
KMP(string,pattern)