
import sys
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver
from twisted.python import log
from twisted.internet import reactor


class CmdProtocol(LineReceiver):
    delimiter = '\n'

    def conenectMade(self):
        self.client_ip = self.transport.getPeer()[1]
        log.msg("Client connection from %s" % self.client_ip)

        if len(self.factory.clients) >= self.factory.clients_max:
            log.msg("Too many connections. bye!")

            self.client_ip = None
            self.transport.loseConnection()
        else:
            self.factory.clients.append(self.client_ip)

    def connectionLost(self, reason):
        log.msg("Lost client connection. Reason: %s" % reason)
        if self.client_ip:
            self.factory.clients.remove(self.client_ip)

    def lineReceived(self, line):
        log.msg("Cmd receviced from %s:%s" % (self.client_ip, line))


class MyFacotry(ServerFactory):
    protocol = CmdProtocol

    def __init__(self, client_max=10):
        self.clients_max = client_max
        self.clients = []


log.startLogging(sys.stdout)
reactor.listenTCP(9999, MyFacotry(2))
reactor.run()
