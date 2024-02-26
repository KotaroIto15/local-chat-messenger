# Local Chat Messenger

## Overview of the project
- Leverage the knowledge in **socket programming** to create a simple data transaction between a server and a client.
- Utilize Python **faker module** to generate randomized data used in server responses.

## `server.py`
1. Create the UNIX socket with STREAM mode.
    * Choose `AF_UNIX` as a socket domain to achieve the interaction between processes running on the same machine.
    * `SOCK_STREAM` mode ensures the credible and ordered data transportation. It is also compatible with TCP protocol.
2. Set the path to the location in which the server waits for connections from clients.
3. If the location already exists (= previous connection remains), unlink the server address by `os.unlink()` function.
4. Listen to the connection from the client. For this project maximum connection allowed is 1.
5. When the connection is established, receive the message from the client and generate random color code.
6. Embed the genearate color code in the URL of [Comptuer Hope](https://www.computerhope.com/) as a parameter. Clicking on the link will navigate to the detailed information page of the color.
7. Sends back the response to the client through `sock.sendall()`.
8. When the client closes the socket, close the connection and shut down the server.

## `client.py`
1. Create the UNIX socket with STREAM mode.
2. Connect to the server socket.
    * If any error occurs, print out the error message and terminate the execution of the program by `sys.exit(1)`
3. Define the message to send. Is asks what mood the user is in, and the user types in the response in the command line.
4. Take the user response from the command line and send it to the server via `sock.sendall()`.
5. Receive the server response and display the message. Then ask for the user feedback(i.e. if they are happy with the color suggestion). Allowed answer is either 'Y' or 'N'.
6. If the user answers 'N', ask the server for another color suggestion.
7. Repeat 5-6 until user is happy with the result.
8. When the user answers 'Y', it closes the socket and terminates the program execution.