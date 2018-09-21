from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Echo(DatagramProtocol):

    def datagramReceived(self, data, address):
        self.transport.write(data, address)

reactor.listenUDP(8000, Echo())
reactor.run()