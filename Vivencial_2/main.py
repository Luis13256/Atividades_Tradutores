from parser import parser
import os


def main():
    print("Diretório de trabalho atual:", os.getcwd())
    try:
        with open('entrada.txt', 'r') as file:
            data = file.read()
            if data.strip() == '':
                print("O arquivo 'entrada.txt' está vazio.")
                return
            parser.parse(data)  # Chamada sem atribuição
    except FileNotFoundError:
        print("Arquivo 'entrada.txt' não encontrado.")


if __name__ == "__main__":
    main()
