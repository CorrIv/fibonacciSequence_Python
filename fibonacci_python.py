
# Dev: Ivan Correia Lima Coqueiro
# Data: 31/08/2022
# Ultima atualização: 31/08/22 22:49
# Programa que calcula a sequencia de fibonacci em python

#espaço para adicionar um valor inteiro de 1 ao infinito
numero = int(input('insira um numero a partir de 1 :'))

#função que calcula os numeros da sequencia de fibonacci 
def fibonacci(numero):
    segundo_digito = 1              #o primeiro digito sempre é um inteiro chamado 1
    Indices = [None]*numero         #um array vazio para ser preenchido pelo sistema
    
    #remove o caso de numero = 0
    if numero == 0:
        print('é dado o seguinte valor', 0)
        return Indices

    #remove o caso de numero = 1
    if numero == 1:
        print('é dado o seguinte valor', 1)
        return Indices

    #resolve os indices para todos os outros casos
    else:
        Indices[0] = 0                               #add o numero 0 no primeiro digito
        for i in range(numero-1):
           Indices[i+1]= Indices[i] + segundo_digito #soma o primeiro digito (0) com o segundo, e incrementa o segundo com o indice do digito anterior
           segundo_digito = Indices[i]

        print('os valores dados serão de:', Indices)    #retorna os valores do array
    return Indices

#imprime os resultados da função
print(fibonacci(numero))
