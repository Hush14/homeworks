def fac(n):
     if n == 0:
          return 1
     return fac(n-1) * n

x=int(input())
print(fac(x))