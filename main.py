sequencia= (10,20,30,40,50)
pilha =[0]*10
topo=-1

topo=topo+1
pilha[topo]=sequencia[0]
i=0
while i<5:
    topo=topo+1
    pilha[topo]=sequencia[i]
    i=i+1

while topo>=0:
    print(pilha[topo])
    topo=topo-1
