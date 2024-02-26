import socket
import sys

class ExitException(Exception):
    pass

# creata a TCP/IP socket to enable connection
sock =  socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# connect socket to the file in which server is waiting
server_address = '/tmp/socket_file'
print('connecting to {}'.format(server_address))

# try connecting to the server
# if any error occurs, print the error message and exits
try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

# when the connection is established, sends messages to the server
try:
    # set message to send in byte
    print('Welocome to the lucky color generator!!')
    message = input('What mood are you in today?: ')
    if message == 'exit':
        raise ExitException()
    sock.sendall(message.encode())

    # set timeout to 2 seconds
    # if the server does not response within 2 seconds, moves forward
    sock.settimeout(2)

    # waits for server's reponse, and prints the message
    try:
        while True:
            # receives data from the server (max 32 bytes)
            data  = sock.recv(1024)

            # prints data if there's any, otherwise termintes the loop
            if data:
                print(data.decode())
                print('Are you happy with our color suggestion?')
                message = input('(Y/N) >>> ')
                if message == 'Y':
                    break
                sock.sendall(message.encode())
            else:
                break

    # timeout error
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

except ExitException:
    pass

# finally closes the socket
finally:
    print('Thank you for using our generator!!')
    sock.close()