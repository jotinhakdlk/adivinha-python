print("Seja bem vindo ao adivinha python!")

n_secreto = 50
entrada = int(input("digite um valor aleatório: "))
acerto = entrada == n_secreto
chutemaior = entrada > n_secreto
chutemenor = entrada < n_secreto

print(f"Você digitou o número: {entrada}")

if(acerto):
    print("pabens, asserto")
else:
    if(chutemaior):
        print("o número secreto é menor que seu chute")
    if(chutemenor):
        print("o número secreto é maior que seu chute")

print("It's over, sobrou nada pro beta")