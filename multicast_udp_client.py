from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class MulticastHelloClient(DatagramProtocol):

    def startProtocol(self):
        # Join the multicast address, so we can receive replies:
        self.transport.joinGroup("228.0.0.5")
        # Send to 228.0.0.5:8005 - all listeners on the multicast address
        # (including us) will receive this message.
        self.transport.write(b'Hello World', ("228.0.0.5", 8005))

    def datagramReceived(self, datagram, address):
        print("Datagram %s received from %s" % (repr(datagram), repr(address)))
        reactor.stop()

reactor.listenMulticast(8005, MulticastHelloClient(), listenMultiple=True)
reactor.run()

# What happened when you send message from client in Multicast UDP when server is not available?
#
# The client will receive the message it sent out since there is no server available.