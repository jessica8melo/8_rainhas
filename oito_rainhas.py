"""Implementação de verificação se tabuleiro
contém a solução do problema das 8 rainhas
"""
def checa_diagonal(indices_linha, indices_coluna):
    """Função que checa se há uma ataque diagonalmente"""
    indice = 0
    while indice < len(indices_coluna)-1:
        cont = indice + 1
        while cont < len(indices_linha):
            delta_x = indices_linha[indice] - indices_linha[cont]
            delta_y = indices_coluna[indice] - indices_coluna[cont]
            if delta_x in (delta_y, -delta_y):
                return 0
            cont+=1
        indice+=1
    return 1

def checa_vertical(tabuleiro, indices_linha):
    """Função que checa se há uma ataque verticalmente"""
    for linha in tabuleiro:
        i = linha.index('1')
        if i in indices_linha:
            return 0
        indices_linha.append(i)
    return indices_linha


def checa_horizontal(tabuleiro, indices_coluna):
    """Função que checa se há uma ataque horizontamenlte"""
    i = 8
    for linha in tabuleiro:
        rainhas_linha = 0
        for caracter in linha:
            if caracter == '1':
                rainhas_linha += 1
        if rainhas_linha > 1:
            return 0
        indices_coluna.append(i)
        i -= 1
    return indices_coluna

def valida_entrada(tabuleiro):
    """Função que valida se o tabuleiro é 8x8 e
    se há exatamente 8 rainhas no tabuleiro"""
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
    """Função que recebe a entrada e chama as condições de validação"""
    tabuleiro = []
    indices_linha = []
    indices_coluna = []
    n_linha = 8
    while n_linha > 0:
        linha = input(f"Descreva a linha {n_linha} do seu tabuleiro: ")
        tabuleiro.append(linha)
        n_linha -= 1
    if valida_entrada(tabuleiro) == -1:
        return "-1 (Entrada inválida)"
    if checa_horizontal(tabuleiro, indices_coluna) == 0:
        return "0 (Não é solução)"
    if checa_vertical(tabuleiro, indices_linha) == 0:
        return "0 (Não é solução)"
    if checa_diagonal(indices_linha, indices_coluna) == 0:
        return "0 (Não é solução)"
    return "1 (É solução)"

print(main())
