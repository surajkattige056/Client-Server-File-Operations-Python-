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

class client():
    def questions(self, s):
        choice = input("So, do you want to save a new file or load an existing one?(save/load)")
        choice = choice.lower()
        s.send(choice.encode('utf-8'))
        filename = input("What is the name of the file? ")
        s.send(filename.encode('utf-8'))
        return choice

    def client_operation(self):
        HOST = '127.0.0.1'
        PORT = 50003
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((HOST,PORT))
        while True:
            choice = self.questions(s)
            if choice =='save':
                fileData = input('Type the data you want to input into the file: ')
                s.send(fileData.encode('utf-8'))

            elif choice == 'load':
                fileData = s.recv(1024)
                fileData = str(fileData)
                fileData = fileData[2:len(fileData)-1]
                print(fileData)
            ques = input('Do you want to save/load another file?(yes/no) ')
            ques = ques.lower()
            s.send(ques.encode('utf-8'))
            if ques == 'no':
                break

        s.close()

def main():
    c = client()
    c.client_operation()


if __name__ == "__main__":
    main()