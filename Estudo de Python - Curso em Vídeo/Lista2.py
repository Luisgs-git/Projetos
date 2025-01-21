a=[2,3,4,5]
#b=a#a=b e b=a
b = a[:]
b[2]=8
print(f'Lista A:{a}')
print(f'Lista B:{b}')