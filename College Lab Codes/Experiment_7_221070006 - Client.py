import socket

try:
    c = socket.socket()
    print('Socket created successfully...')

except socket.error as error:
    print('Socket creation failed with error %s' %(error))

c.connect(('localhost',8080))

print(c.recv(1024).decode())

filename = input('Enter name of file : ')

text = ''

with open(filename,'r') as handle:
    for line in handle:
        text += line
    text = text.rstrip()
    c.send(bytes(text,'utf-8'))
handle.close() 

c.close()