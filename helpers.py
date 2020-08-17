import random
from config import TENTATIVAS_ADICIONAIS, ARQUIVO_PALAVRAS_SECRETAS


def gerar_palavra_secreta():
    """
    Função para selecionar aleatoriamente do arquivo texto
    :return: uma palavra aleatória
    """
    with open(ARQUIVO_PALAVRAS_SECRETAS, 'r') as f_obj:
        palavra = f_obj.read().splitlines()

    return random.choice(palavra)