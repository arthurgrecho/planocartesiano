def conjuntos(conj1, conj2, operacao):
    operacoes = {
        'U': (conj1 | conj2, 'União'),
        'I': (conj1 & conj2, 'Interseção'),
        'D': (conj1 - conj2, 'Diferença'),
        'C': ({(a, b) for a in conj1 for b in conj2}, 'Produto Cartesiano')
    }

    resultado, nome_operacao = operacoes.get(operacao, (set(), 'Operação desconhecida'))
    print(f'{nome_operacao}:')
    print(f' Conjunto 1: {conj1}')
    print(f' Conjunto 2: {conj2}')
    print(f' Resultado: {resultado}')

with open('entrada1.txt', 'r') as arquivo:
    linhas = [linha.strip() for linha in arquivo]

for i in range(1, len(linhas), 3):
    operacao = linhas[i]
    conj1 = set(linhas[i + 1].split(','))
    conj2 = set(linhas[i + 2].split(','))
    conjuntos(conj1, conj2, operacao)