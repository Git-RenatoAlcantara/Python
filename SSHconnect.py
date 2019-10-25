import paramiko
import socket
 
def http_proxy(proxy, target, timeout=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    sock.connect( (proxy) )
 
    cmd_connect = "CONNECT %s:%d HTTP/1.1\r\n\r\n"%target
    sock.sendall(cmd_connect)
    sock.settimeout(2)
    try:
        while True:
            dados = sock.recv( 8192 )
            if not dados: break
            print(dados)
    except socket.error, ex:
        print("Error: {}".format(ex))
       
sock = http_proxy(proxy=("127.0.0.1",8088),
        target=("34.95.212.133", 80),
        timeout=50)
 
       
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname="34.95.212.133", sock=sock, username="teste", password="teste123")