a, b, c = map(int, input().split())
print([a, b, c] if a>=b and a>=c and b>=c else [b, a, c] if b>=a and b>=c and a>=c else [a, c, b] if a>=c and a>=b and c>=b else [c, a, b] if c>=a and a>=b else [c, b, a] if c>=b and b>=a else [b, c, a] )
