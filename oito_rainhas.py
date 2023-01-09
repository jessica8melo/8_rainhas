"""Implementação de verificação se tabuleiro
contém a solução do problema das 8 rainhas
"""
def checaHorizontal(tabuleiro):
    for linha in tabuleiro:
        rainhas_linha = 0
        for caracter in linha:
            if caracter == '1':
                rainhas_linha += 1
        if rainhas_linha > 1:
            return 0
    return 1

def valida_entrada(tabuleiro):
    rainhas = 0
    for linha in tabuleiro: 
        if len(linha) != 8: #Verifica se é um tabuleiro 8x8
            return -1
        for caracter in linha: #Conta as rainhas no tabuleiro
            if caracter == '1':
                rainhas += 1
    if rainhas != 8: #Verifica se não há 8 rainhas no tabuleiro
        return -1


def main():
    tabuleiro = []
    n_linha = 8
    while n_linha > 0:
        linha = input(f"Descreva a linha {n_linha} do seu tabuleiro: ")
        tabuleiro.append(linha)
        n_linha -= 1
    if valida_entrada(tabuleiro) == -1:
        return "-1 (Entrada inválida)"
    if checaHorizontal(tabuleiro) == 0:
        return "0 (Não é solução)"
    else:
        return "Por enquanto, dando certo"

print(main())
