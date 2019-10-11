from mininet.topo import Topo
from mininet.net import Mininet

class Anillo( Topo ):

    def __init__( self, n=2):

        # Initialize topology
        Topo.__init__( self )

	switchList = []
	for swnum in range(n):
            switchList.append(self.addSwitch('sw%s' % (swnum+1)))
	    host = self.addHost('h%s' % (swnum+1))
	    self.addLink(host, switchList[swnum], bw=50, delay='1ms')
            if swnum > 0:
	       self.addLink(switchList[swnum], switchList[swnum-1], bw=1000, delay='5ms')

        self.addLink(switchList[0],switchList[n-1], bw=1000, delay='5ms')


topos = { 'anillo': ( lambda: Anillo(n=5) ) }
