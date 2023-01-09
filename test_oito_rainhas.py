from oito_rainhas import valida_entrada, checaHorizontal

def test_valida_entrada(): 
    tabuleiro1 = ['00001000', '01000000', '00010000', '00000010',
                '00100000', '00000001', '00000100']
    tabuleiro2 = ['00001000', '01000000', '00010000', '00000010',
                '00100000', '00000001', '00000100', '00000000']
    assert valida_entrada(tabuleiro1) == -1 #Tabuleiro incompleto
    assert valida_entrada(tabuleiro2) == -1 #Tabuleiro sem 8 rainhas

def test_checaHorizontal():
    tabuleiro = ['00001001', '01000000', '00010000', '00000010',
                '00100000', '00000001', '00000000']
    assert checaHorizontal(tabuleiro) == -1