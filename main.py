from helpers import gerar_palavra_secreta, jogo

if __name__ == '__main__':
    palavra_secreta = gerar_palavra_secreta()

    # Forloop que imprima a palavra escondida com estrelas
    print("\n »»»»» JOGO DA FORCA «««««")
    print("\nA palavra é: ")
    for letra in palavra_secreta:
        print("*", end=" ")

    #Calculando o tamanho da palavra
    tamanho_palavra = len(palavra_secreta)
    print(f"\n - A palavra tem {tamanho_palavra} letras.")

    jogo(palavra_secreta)
