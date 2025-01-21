def area(larg,compr):
    print(f"A área de um terreno {larg}X{compr} é de {(larg*compr)}m²")
print(f"{"Controle de Terrenos":^20}")
print("-"*20)
b=float(input("LARGURA (m):"))
c=float(input("COMPRIMENTO (m):"))
area(b,c)