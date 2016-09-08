import socket

host = ''
port = 2000

s = socket.socket()
s.bind((host, port))

while True:
    s.listen(5)
    connection, address = s.accept()

    request = connection.recv(1024)
    
    request = request.decode('utf-8')
    if len(request) == 0:
        continue
    print('log ip and request, {}\n{}'.format(address, request))
    line = request.split('\n')[0]
    print('line', line)
    path = line.split()[1]
    print('path: ', path)
   
    r = b'Hello World!'

    connection.sendall(r)

    connection.close()

