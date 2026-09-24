expressao = input("Digite uma expressão: ")
pilha=[0]*10
topo=-1
i=0
valido = True  


while i<len(expressao):
    caractere = expressao[i]
    if caractere == "(":
        topo=topo+1
        pilha[topo]= caractere
    i=i+1
    if caractere == ")":
        if topo==-1:
            valido = False
        else:
            topo=topo-1

if topo == -1:
        valido=True
else:
        valido=False
if valido:
        print("Opção válida!")
else:
         print("Opção inválida!")



