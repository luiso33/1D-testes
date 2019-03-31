from random import randint # biblioteca para gerar número aleatório
N = [] # sitio
Traj = [] # Tem de ser um vetor vazio de tamanho (N/2+1) para guardar a trajetória do indivíduo 
Np = 0 # contador do número de passos 
prob = randint(0,10) #sorteia um número aleatório

#--------GERAR VETOR--------------
x = 51 #Decide o numero de sítios 
for i in range(x): #Gerar vetor, se vc substituir um valor direto no X nao precisa de usuario 
    N.append(i-(x//2)) # divisao inteira
#----------------------------------

for i in range(1, (x//2)+1): #x//+1 pq x//2 vai dar 25, porem sao 25 sitios e ele anda um a menos 
    if(prob<5):
        Traj.append(N[(x//2)-i]) #x//2 da no 0
        Np += 1
    else:
        Traj.append(N[(x//2)+i])
        Np += 1

print('Os sitios são: \n{}'.format(N))
print('O número de passos dados foram: {} '.format(Np))
print('A trajetória foi: \n{}'.format(Traj)