from socket import *

def contar_vogais(frase):
    """
    --> Esta função, recebe ums string e conta o número de ocorrências das vogais na mesma.
    """
    cont_a = frase.count('a')
    cont_e = frase.count('e')
    cont_i = frase.count('i')
    cont_o = frase.count('o')
    cont_u = frase.count('u')

    return f'a={cont_a} e={cont_e} i={cont_i} o={cont_o} u={cont_u}'


# Declarando o endereço do servidor e a porta que serão utilizadas
serverPort = 12000  # utilizar a mesma porta que o cliente, ou vice-versa

# instanciando um INET, STREAMing socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# associando o número de porta do servidor, serverPort , ao socket
serverSocket.bind(('', serverPort))

# escutando até que chegue algum dado, serverSocket é a porta de entrada
serverSocket.listen(1)

# escrevendo, no terminal, que o servidor está pronto para receber os pacotes
print('O servidor está pronto para receber')

while True:
    # chamando o método accept() para serverSocket, que cria um novo socket no servidor (connectionSocket) dedicado a esse cliente  specífico
    connectionSocket, addr = serverSocket.accept()
    
    """
        Cliente e servidor, então, completam a apresentação, criando uma conexão TCP entre o clientSocket do cliente e o connection-Socket do servidor. Após estabelecer a conexão TCP, cliente e servidor podem enviar bytes um para o outro por ela. Com TCP, todos os bytes enviados de um lado têm garantias não apenas de que chegarão ao outro lado, mas também na ordem.
    """

    sentence = connectionSocket.recv(1024)

    # decodificando a frase recebida pela servidor para uma string
    modifiedSentence = str(sentence.decode(encoding='utf-8', errors='strict'))

    # chamando a função que irá contar o número de vogais
    processed_sentence = str(contar_vogais(modifiedSentence))

    # codificando o a frase que contém a contagem das vogais
    processed_sentence = bytes(processed_sentence.encode(encoding='utf-8', errors='strict'))

    # enviando o resultado para o cliente
    connectionSocket.send(processed_sentence)

    # fechando o socket da conexão
    connectionSocket.close()

    # lembrando que serverSocket permanece aberto, outro cliente agora pode bater à porta e enviar uma sentença ao servidor, para que seja modificada.