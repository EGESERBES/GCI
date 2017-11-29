#! python

# FİBONACCİ SAYILARI:
# Dizinin ardışık iki teriminin toplamı sonraki terimi verir:
a, b = 0, 1
c=int(input("kaçıncı sayıya kadar gireyim:"))

while b < c:
    print(b)
    a, b  = b, a+b
    
