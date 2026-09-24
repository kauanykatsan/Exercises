#Polindromo com Pilha

palavra= "ARARA"
pilha=[0]*10
topo=-1

i=0
j=4
polindromo=True
while i<5:
    topo=topo+1
    pilha[topo]=palavra[i]
    i=i+1

while topo>=0:
    letra=pilha[topo]
    print(pilha[topo])
    
    topo=topo-1
    if letra != palavra[j]:
        polindromo=False
    
    j=j-1
        
if polindromo :
    print("False: A palavra é um polindromo")
else:
    print("True: A palavra nãe é um polindromo")