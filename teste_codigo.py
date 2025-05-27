import codigo_aluno

def test_soma():
    assert codigo_aluno.soma(2, 3) == 5
    assert codigo_aluno.soma(-1, 1) == 0

def test_subtrai():
    assert codigo_aluno.subtrai(5, 3) == 2
    assert codigo_aluno.subtrai(0, 3) == -3

def test_multiplica():
    assert codigo_aluno.multiplica(4, 3) == 12
    assert codigo_aluno.multiplica(-1, 5) == -5

def test_divide():
    assert codigo_aluno.divide(10, 2) == 5
    assert codigo_aluno.divide(5, 0) == "Erro: divisão por zero"
    assert codigo_aluno.divide(9, 3) == 3
