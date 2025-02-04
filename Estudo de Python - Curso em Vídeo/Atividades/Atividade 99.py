import random
def maior(*num):
    print("Analisando os valores passados...")
    cont=max=0
    for i in num:
        print(i,end=" ")
        if cont==0:
            max=i
        else:
            if i>max:
                max=i
        cont+=1
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior valor informado foi o {max}.")


maior(1,2,3,4,5,6,7,8,9,10)
maior(7,2,5,6,7,3,5)
maior()