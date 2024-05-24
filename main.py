#Lista de nomes

nomes = ['Guilherme', 'Matheus', 'Douglas', 'João', 'Carlos', 'Amanda']

#Usuário informa o índice que deseja alterar 

indice = int(input('Informe o índice que deseja alterar: '))
indice -= 1 #Para corrigir o indice, pois o usuário não é obrigado a saber se que começa em 0

#Usuário informa o novo nome

nomes[indice] = input('Informe o novo nome: ')

#Exibe a lista inteira com as alterações

for nome in nomes:
    print(nome)