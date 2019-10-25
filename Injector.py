# coding: utf-8
import socket, threading,select
 
 
def conecta(cliente, endereco):
   
    print('Cliente {} Recebido'.format(endereco))
    servidor = socket.socket()
    servidor.connect( ( '34.95.212.133', 443) )
    cliente.recv( 8192 )
    servidor.send( b'CONNECT 34.95.212.133:80 HTTP/1.0\r\n\r\n')
    servidor.recv( 8192 )
    cliente.send(b'HTTP/1.1 200 SSHPLUS\r\n\r\n')
 
    try:
        while True:
            leitura, escrita, erro = select.select( [ servidor, cliente ], [], [servidor, cliente ], 3)
            if erro: raise
            for i in leitura:
                dados = i.recv( 8192 )
                if not dados: raise
                print(dados)
                if i is servidor:
                    # Download
                    cliente.send( dados )
                else:
                    # Upload
                    servidor.send( dados )
    except:
        print('Cliente Desconectado')
 
def conn_client():
    listen = socket.socket()
    listen.bind( ( '127.0.0.1', 8088) )
    listen.listen( 0 )
    print('Esperando o Cliente no IP e Porta: 127.0.0.1:8088')
    while True:
        cliente, endereco = listen.accept()
        threading.Thread(target = conecta, args = ( cliente, endereco) ).start()
 
 
if __name__=="__main__":
    conn_client()
