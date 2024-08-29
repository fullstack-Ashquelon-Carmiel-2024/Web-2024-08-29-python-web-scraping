a = b = c = 45

print(f'a = {a}, b = {b}, c = {c}')

b += 6

print(f'Again: a = {a}, b = {b}, c = {c}')

d = 'lalala'

b,d = d,b

# In JS we would use or [b,d] = [d,b]
# or would use temp variable

print(f'Again: a = {a}, b = {b}, c = {c}, d = {d}')
# Again: a = 45, b = lalala, c = 45, d = 51

print(f'Type of b is {type(b)} and type of d is {type(d)}')
print(f'Type of False is {type(False)}')
print(f'Type of a = {a} was {type(a)} and the type of str(a) is {type(str(a))}')

a = float(input('Enter number a: '))
b = int(input('Enter number b: '))
print(f'a + b = {a + b}')