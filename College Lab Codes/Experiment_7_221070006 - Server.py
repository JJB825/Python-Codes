import socket

try:
    s = socket.socket()
    print('Socket created successfully...')

except socket.error as error:
    print('Socket creation failed with error %s' %(error))

s.bind(('localhost',8080))

s.listen(1)
print('Waiting to connect with client...')

c, address = s.accept()
print('Socket connected successfully with client',address)

while True:
    c.send(bytes('Welcome to PackYourBags...','utf-8'))

    with open('Client.txt','w') as handle:
        lines = c.recv(1024).decode()
        handle.write(lines)
    handle.close()

    with open('Client.txt','r') as handle:
        for line in handle:
            print(line,end = '')
    handle.close()

    c.close()

    break