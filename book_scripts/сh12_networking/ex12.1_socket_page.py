"""

    Exercise 12.1

        Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
        You can use split(’/’) to break the URL into its component parts so you can extract the host name for the
        socket connect call. Add error checking using try and except to handle the condition where the user enters
        an improperly formatted or non-existent URL.

"""

import re
import socket


def parse_http_address():
    while True:
        try:
#            input_address = input("Please, enter HTTP address:\t")

            input_address = "http://www.py4inf.com/code/romeo.txt"
            # input_address = "py4inf.com"
            http_address = re.search(r"(http[s]?\://)?(.*?)(/.*)?$", input_address)

            if len(input_address) == 0:
                raise ValueError()

            if http_address.group(2):
                print(http_address.groups())
            else:
                raise ValueError()

            break
        except ValueError:
            print("HTTP address is not valid or unreachable! Please, correct it or try once more!")

    return http_address.groups()


http_prefix, http_domain, http_page = parse_http_address()

print(f"[{http_domain}]; [{http_prefix}]; [{http_page}];")

http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
http_socket.connect((http_domain, 80))
http_socket.send(b'GET / HTTP/1.1\r\nHost: www.py4inf.com/code/romeo.txt\r\n\r\n')

print(1)
while True:
    http_data = http_socket.recv(2000)
    if len(http_data) < 1:
        break
    print(http_data)

http_socket.close()

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.py4inf.com', 80))
# mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
#
# while True:
#     data = mysock.recv(512)
#     if ( len(data) < 1 ) :
#         break
#     print data;
#
# mysock.close()
