from parser import parser
import os


def main():
    # Exibe o diretório de trabalho atual para ajudar na verificação de onde o arquivo 'entrada.txt' está localizado
    print("Diretório de trabalho atual:", os.getcwd())
    
    try:
        with open('entrada.txt', 'r') as file:
            data = file.read() 
            
            # Verifica se o arquivo está vazio
            if data.strip() == '':
                print("O arquivo 'entrada.txt' está vazio.")
                return  # Interrompe a execução se o arquivo estiver vazio
            
            parser.parse(data)  # A função parser.parse faz a análise do conteúdo do arquivo
    except FileNotFoundError:
        print("Arquivo 'entrada.txt' não encontrado.")

if __name__ == "__main__":
    main() 
