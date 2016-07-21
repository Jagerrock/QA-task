import SocketServer
import subprocess
import logging

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.FileHandler("logs.log"))
LOG.setLevel(logging.INFO)

class MyTCPHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		self.data = self.request.recv(1024).strip()
		LOG.warn (self.data)
		print "{} wrote:".format(self.client_address[0])
		LOG.info (format(self.client_address[0]))
		output = subprocess.check_output(self.data, shell=True)
		print(output)
		self.request.sendall(output)
		LOG.info(output)

if __name__ == "__main__":
	HOST, PORT = 'localhost', 9999

server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()
