import pandas as pd

def limpar_valores(dados):

    resultado = {}

    for chave, valor in dados.items():

        if pd.isna(valor):

            valor = ""

        elif isinstance(valor, float):

            if valor.is_integer():

                valor = int(valor)

        resultado[chave] = valor

    return resultado
