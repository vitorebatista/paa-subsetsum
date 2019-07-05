'''
Questão 04. Implemente uma solução de força bruta para o SUBSET-SUM.
            Use a instância criada na questão anterior como entrada.
'''

import time

start = time.time()


def subsetSum(v: list, k: int, n: int, t: int, res: list) -> list:
    '''
        Solução de forca bruta para o problema SUBSET-SUM.

        Parameters:
            v - vetor com as combinações possíveis
            k e n - numero de elementos do vetor (k sera decrescido em cada chamada recursiva
            t - valor do somatório
            res - vetor para acumular instâncias válidas
    '''
    aux, s, i = 0, 0, 0

    print(
        f'Executando... {round(time.time()-start,1)} segundos', end='\r')

    if (k > 0):
        res = subsetSum(v, k-1, n, t, res)
        aux = v[n-k]
        v[n-k] = 0
        res = subsetSum(v, k-1, n, t, res)
        v[n-k] = aux

    else:
        s = 0
        current = []
        for i in range(n):
            s += v[i]
            # Garante que se o valor for menor, termina com a somatória
            if (s > t):
                return res
            elif (v[i] != 0):
                current.append(v[i])

        if (s == t):
            res.append(current)

    return res


def main():

    print("# # Força bruta para SUBSET-SUM")

    v = [10000001111, 10011110000, 1000110011, 1011001100, 101010101, 110101010,
         10000000, 20000000, 1000000, 2000000, 100000, 200000, 10000, 20000,
         1000, 2000, 100, 200, 10, 20, 1, 2]

    # resultado de t esperado para a redução
    t = 11144444444

    # executa a verificacao por força bruta
    res = subsetSum(v, len(v), len(v), t, [])

    # resultado
    if len(res) > 0:
        print("\nInstâncias que atendem ao SUBSET-SUM:")
        for i in range(len(res)):
            print(f"{i+1}: {res[i]}")
    else:
        print("\nNenhuma instância atende SUBSET-SUM")


main()
