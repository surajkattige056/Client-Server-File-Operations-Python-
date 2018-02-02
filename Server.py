#!/usr/bin/env python
__author__ = "Suraj S Kattige"
__version__ = "1.0.0"
__email__ = "suraj.kattige056@gmail.com"
__maintainer__ = "Suraj S Kattige"
'''
problem: Write a python server that receives a connection from the client,
stores the received data in a file, then adds the file to a list
returns the data from the file when requested
deals with errors and missing files
'''
import socket

class server:
    def server_operation(self):
        file_list=[]

        #Server Configuration
        HOST = ''
        PORT = 50003
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((HOST,PORT))
        s.listen(1) #Listens to one connection at a time
        conn, addr = s.accept()

        #Operation to send or recieve file
        while True:
            save_load = str(conn.recv(1024))
            save_load = save_load[2:len(save_load)-1]

            #If file needs to be saved
            if save_load == ('save'):
                filename = conn.recv(1024)
                data = conn.recv(1024)
                filename = str(filename)[2:len(str(filename))-1] + '.txt'
                f = open(filename,'w')
                str_data = str(data)
                str_data = str_data[2:len(str_data) - 1]
                f.write(str_data)
                file_list.append(filename)

            #If a file needs to be retrieved from the server
            elif save_load == ('load'):
                filename = conn.recv(1024)
                filename = str(filename)[2:len(str(filename)) - 1] + '.txt'
                if filename not in file_list:
                    print("This file does not exist!")
                else:
                    print('So, the file exists afterall')
                    f = open(filename,'r')
                    conn.send((f.read()).encode('utf-8'))

            choice = str(conn.recv(1024))
            choice = choice[2:len(choice)-1]
            if (choice == '') or (choice == 'no'):
                break

        conn.close()


def main():
    s = server()
    s.server_operation()

if __name__ == "__main__":
    main()