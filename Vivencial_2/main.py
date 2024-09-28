# Importa o parser (analisador sintático) e o módulo os para lidar com operações do sistema operacional
from parser import parser
import os

# Função principal que será executada
def main():
    # Exibe o diretório de trabalho atual para ajudar na verificação de onde o arquivo 'entrada.txt' está localizado
    print("Diretório de trabalho atual:", os.getcwd())
    
    # Tenta abrir o arquivo 'entrada.txt' no modo de leitura
    try:
        # Abre o arquivo 'entrada.txt'
        with open('entrada.txt', 'r') as file:
            data = file.read()  # Lê o conteúdo do arquivo
            
            # Verifica se o arquivo está vazio
            if data.strip() == '':
                print("O arquivo 'entrada.txt' está vazio.")
                return  # Interrompe a execução se o arquivo estiver vazio
            
            # Envia os dados lidos para o parser para análise sintática
            parser.parse(data)  # A função parser.parse faz a análise do conteúdo do arquivo
    except FileNotFoundError:
        # Caso o arquivo não seja encontrado, exibe uma mensagem de erro
        print("Arquivo 'entrada.txt' não encontrado.")

# Ponto de entrada do script
if __name__ == "__main__":
    main()  # Chama a função principal
