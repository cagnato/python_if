print("Voce entrou na floresta, porém se deparou com uma bifurcação, deseja seguir pela esquerda ou direita?")

caminho = input("Insira seu caminho: ").lower()

# S = str
# N = str

if caminho == "esquerda":
    print("Voce encontrou um rio, deseja atravessa-lo? S/N")
    resposta = input("Escolha sua ação: ")
    if resposta == "s":
        print("Voce foi atravessar o rio, mas caiu nele e se molhou! Voce não é atlético, amigo 🤦‍♂️")
    elif resposta == "n":
        print("Voce não tentou atravessar o rio e continuou seco! Bom trabalho.👍")
    else:
        print("Insira uma resposta válida")    
elif caminho == "direita":
    print("Voce encontrou uma montanha, deseja subi-la? S/N")
    resposta = input("Escolha sua ação: ")
    if resposta == "s":
        print("Voce foi subir a montanha, mas se cansou na metade e parou. Melhore este condicionamento 🤦‍♂️")
    elif resposta == "n":
        print("Voce não tentou subir a montanha e continuou com folego.👍")
    else: 
        print("Insira uma resposta válida") 
else:
    print("Escolha um caminho válido!!!")  