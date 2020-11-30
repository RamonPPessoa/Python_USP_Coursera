decrescente = True
anterior = int(input("Digite o primeiro número da sequencia"))

valor = 1
 
while valor !=0 and decrescente:
     valor = int(input("Proximo numero da sequencia"))
     if valor > anterior:
        decrescente = False
     anterior = valor
     
     
if decrescente:
    print("Decrescente")
else:
    print("Crescente")