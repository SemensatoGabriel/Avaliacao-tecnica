#QUESTAO 1

def fibo(num):
    '''
        definindo a função para cálculo da sequência de Fibonacci,
        a sequência contem apenas números positivos inteiros,
        logo a primeira posição é 1 e o cálculo é feito a partir de 2
    '''
    if num <= 1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)

#SOLICITANDO O NUMERO
x = int(input("Digite um valor para cálculo de Fibonacci: "))

#EXECUTANDO A FUNCAO
result = fibo(x)

#APRESENTANDO O RESULTADO
print("O %dº valor da sequência de fibonacci é %d" % (x, result))


#QUESTAO 2
'''
    O problema ao usuário inserir 50 seria maior demanda de memória e tempo,
    uma vez que, as funções recursivas são funções que chamam a si mesma 
    até atingir o ponto inicial, no caso acima até numero = 1.
    Deste modo, quanto maior o número digitado, maior será o tempo demandado de execução.
'''