import pytest
from pytest import mark

from codigo.bytebank import Funcionario
class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_24 (self):
        # Given-Contexto
        entrada = "13/03/2000"
        esperado = 24

        funcionario_teste = Funcionario('teste',entrada,1111)

        #When-Ação
        resultado = funcionario_teste.idade()

        #Then-Desfecho
        assert  resultado == esperado


    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        #Given
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'

        teste_sobrenome = Funcionario(entrada,'12/10/2005',1500 )

        #when
        resultado = teste_sobrenome.sobrenome()

        #then
        assert  resultado == esperado


    def test_quando_decrecimo_salario_recebe_100000_deve_retornar_90000(self):
        #given
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_test = Funcionario(entrada_nome,'11/11/2000', entrada_salario)
        #when
        funcionario_test.decrecimo_salario()

        resultado = funcionario_test.salario

        #then
        assert resultado == esperado


    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_test = Funcionario('Ana', '17/03/1997',entrada)

        resultado = funcionario_test.calcular_bonus()

        assert esperado == resultado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):

            entrada = 100000


            funcionario_test = Funcionario('Ana', '17/03/1997', entrada)

            resultado = funcionario_test.calcular_bonus()

            assert resultado

