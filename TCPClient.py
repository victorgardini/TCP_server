from socket import *

# Declarando o endereço do servidor e a porta que serão utilizadas
serverName = '127.0.0.1' # nome do servidor -> localhost
serverPort = 12000 # Portas não privilegiadas > 1023

# create an INET, STREAMing socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# now connect to the server on serverPort
clientSocket.connect((serverName, serverPort))

# salvando a frase que será enviada, por padrão, o tipo de variável é string
sentence = input('O que deseja enviar para o servidor: ')

# codificando o objeto string para um objeto bytes (sequencia se bytes)
sentence = bytes(sentence.encode(encoding='utf-8', errors='strict'))

# enviando a frase para o servidor
clientSocket.send(sentence)

# recebendo a frase do servidor
modifiedSentence = clientSocket.recv(1024)

# Decodificando a frase para string novamente
modifiedSentence = str(modifiedSentence.decode(encoding='utf-8', errors='strict'))

# exibindo a mensagem modificada na tela
print('\nMensagem do servidor:')


for sentence in modifiedSentence.split(' '):
    print(f'    A letra {sentence[0]} ocorreu {sentence[2]} vez(es)')

# fechando a conexão com o servidor
clientSocket.close()