"""Testes da implementação"""
from oito_rainhas import valida_entrada, checa_horizontal, checa_vertical, checa_diagonal

def test_valida_entrada():
    """Faz a validação da função valida_entrada com testes de um tabuleiro
    incompleto e um tabuleiro sem 8 rainhas"""
    tabuleiro1 = ['10001000', '01000000', '00010000', '00000010',
                '00100000', '00000001', '00000100']
    tabuleiro2 = ['00001000', '01000000', '00010000', '00000010',
                '00100000', '00000001', '00000100', '00000000']
    assert valida_entrada(tabuleiro1) == -1
    assert valida_entrada(tabuleiro2) == -1

def test_checa_horizontal():
    """Faz a validação da função checa_horizontal com testes de um tabuleiro
    com ataque horizontal"""
    tabuleiro = ['00001001', '01000000', '00010000', '00000010',
                '00100000', '00000001', '00000100','00000000']
    assert checa_horizontal(tabuleiro) == 0

def test_checa_vertical():
    """Faz a validação da função checa_vertical com testes de um tabuleiro
    com ataque vertical"""
    tabuleiro = ['01000000', '01000000', '00010000', '00000010',
                '00100000', '00000001', '00000100','10000000']
    assert checa_vertical(tabuleiro) == 0

def test_checa_diagonal():
    """Faz a validação da função checa_diagonal com testes de um tabuleiro
    com ataque diagonal"""
    tabuleiro = ['00001000', '00010000', '01000000', '00000010',
                '00100000', '00000001', '00000100', '10000000']
    assert checa_diagonal(tabuleiro) == 0
