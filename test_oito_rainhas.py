def test_valida_entrada():
    tabuleiro = ['00001000', '01000000', '00010000', '00000010', 
                '00100000', '00000001', '00000100']
    assert valida_entrada(tabuleiro) == -1