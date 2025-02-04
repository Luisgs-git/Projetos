try:
    a=int(input("Num:"))
    b= int(input("Den:"))
    r =a/b
except (ValueError,TypeError):
    print("Tivemos um problema com os tipos de dados!")
except ZeroDivisionError:
    print("Não da pra dividir por 0")
except KeyboardInterrupt:
    print("O usuario não escreveu dados!")
except Exception as erro:
    print(f"Tivemos um erro!{erro.__class__} e {erro.__cause__}")
else:
    print(f"O resultado é {r}")
finally:
    print("Volte sempre! Muito obrigado!")