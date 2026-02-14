a, b = map(int, raw_input().split())
 
years = 0
 
while a <= b:
    a *= 3      # Limak triples
    b *= 2      # Bob doubles
    years += 1  # One full year passes
 
 
print years
