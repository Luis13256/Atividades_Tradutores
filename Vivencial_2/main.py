from parser import parser


def main():
    try:
        with open('entrada.txt', 'r') as file:
            data = file.read()

            # Verifica se o arquivo está vazio
            if data.strip() == '':
                print("O arquivo 'entrada.txt' está vazio.")
                return  # Interrompe a execução se o arquivo estiver vazio

            # Análise do conteúdo do arquivo
            parser.parse(data)
    except FileNotFoundError:
        print("Arquivo 'entrada.txt' não encontrado.")


if __name__ == "__main__":
    main()
