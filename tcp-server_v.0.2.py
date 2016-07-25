import SocketServer
import logging
from datetime import date

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.FileHandler("logging.log"))
LOG.setLevel(logging.INFO)

class MyTCPHandler(SocketServer.BaseRequestHandler):

    commands = ["help", "date", "myip"]


    def handle(self):
        data = self.request.recv(1024).strip()
	      LOG.info (data)
        if data == self.commands[0]:
            my_replay = "help, date, myip"
        elif data == self.commands[1]:
            td = date.today()
            my_replay = td.strftime('%m/%d/%Y')
        elif data == self.commands[2]:
            my_replay = self.client_address[0]
        else:
            my_replay = "Error!"
      	LOG.info (my_replay)
        self.request.sendall(my_replay)

if __name__ == "__main__":
    HOST, PORT = 'localhost', 10101

server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()
