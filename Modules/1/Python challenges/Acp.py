a=1
b=2
c=3
print(f"Before: a={a}, b={b}, c={c}")
d=a
a=c
c=b
b=d
print(f"After: a={a}, b={b}, c={c}")
