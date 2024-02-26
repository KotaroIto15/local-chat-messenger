import socket
import os
from faker import Faker

fake = Faker()

# create the UNIX socket with stream mode
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# set the relative path to the file from which the server waits for connection
server_address = '/tmp/socket_file'

# if the connection was already established, unlink the server address
try:
    os.unlink(server_address)
# if the server address does not exist, ignore the exception
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

# bind socket to the server address
sock.bind(server_address)

# set the socket ready for connection request
# max 1 client
sock.listen(1)

# accepts the connection
connection, client_address = sock.accept()
print('Connection achieved')
try:
    # waits on new data from the client
    while True:
        # reads data from the connection
        # reads data of maximum 16 bytes each time 
        data = connection.recv(1024)

        # if data is not blank (= client sends any message)
        if data:
            # converts binary data to string
            data_str = data.decode()
            color = fake.color().replace('#', '')
            print(color)
            if data_str == 'N':
                response = 'Sorry to hear that you are not happy with our suggestion. \n'
                response += 'Here is another color suggestion from us!! \n'
            else:
                response = 'Here is your lucky color for today!! \n'
            
            response += f'https://www.computerhope.com/cgi-bin/htmlcolor.pl?c={color}'
            # sends the processed message back to the client
            connection.sendall(response.encode())
        
        # if data is blank, terminates the loop
        else:
            print('Client closed the socket')
            break
                
finally:
    print('Closing current connection')
    connection.close()
    sock.close()