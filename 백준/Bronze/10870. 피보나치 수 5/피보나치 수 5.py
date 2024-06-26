def f(n):
  if n < 1 :
    return abs(n)
  else:
    return f(n-1)+f(n-2)
    
print(f(int(input())))