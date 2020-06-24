"""
***** [0.04 pontos]: Testando usuario_escolhe_jogada com jogada inválida: valor <= 0 (n = 5, m = 3, respostas 0, 2) - Falhou *****
Timeout

***** [0.05 pontos]: Testando usuario_escolhe_jogada com múltiplas jogadas inválidas (n = 5, m = 3, respostas 5, 0, -1, 2) - Falhou *****
Timeout
"""
from JogoNiMAuto import usuario_escolhe_jogada

def test_usuario_escolhe_jogadan5m3():
    assert usuario_escolhe_jogada(5,3) == 0
