text = ""
while text != "#":
  text = input() 
  a = text[0] 
  s = text[2:]
  s = s.lower()
  n = 0
  for i in range(len(s)):
    if s[i] == a:
      n+=1
  if text != "#":
    print(a,n)
