import socket

ports = [21,23,80,443,8080]

for port in ports:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.1)
    codigo = cliente.connect_ex(('IP DESEJADO', port))
    if codigo == 0:
        print port, "OPEN"
