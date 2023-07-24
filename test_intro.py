import pytest
from unittest.mock import patch, call
from io import StringIO
from unittest.mock import patch
import sys
import intro

@patch('builtins.input', side_effect=['usuario', 'senha123'])
def test_autenticacao_de_usuario(mock_input):
    assert intro.autenticacao_de_usuario() == "Login bem-sucedido!" or "Login incorreto. Verifique seu login e senha."


def simulate_input(inputs):
    return StringIO("\n".join(str(i) for i in inputs))

def test_calcula_preco_do_lanche():
    test_cases = [
        # Provide test cases with user input in the format: [codigo_input, quantidade_input, expected_output]
        [100, 3, "3.60\n"],
        [101, 2, "2.60\n"],
        [102, 4, "6.00\n"],
        [103, 1, "1.20\n"],
        [104, 5, "8.50\n"],
        [105, 2, "4.40\n"],
        [106, 10, "10.00\n"],
        [999, 2, "0.00\n"],  # Invalid code, should print 0
    ]

    for codigo, quantidade, expected_output in test_cases:
        with patch("sys.stdin", simulate_input([codigo, quantidade])):
            with patch("sys.stdout", new=StringIO()) as output:
                intro.calcula_preco_do_lanche()
                assert output.getvalue() == f"Digite o código do produto: Digite a quantidade: O valor a ser pago é: {expected_output}"
