from mininet.topo import Topo
from mininet.net import Mininet

class Anillo( Topo ):

    def __init__( self, n=2):

        # Initialize topology
        Topo.__init__( self )
        
        # Constant values for sw-sw links
        bw_1 = 1000
        delay_1 = '3ms'

        # Constant values for sw-host links
        bw_2 = 100
        delay_2 = '2ms'

        # Creating big ring
	switchList = []
	for swnum in range(n):
            switchList.append(self.addSwitch('sw%s' % (swnum+1)))
	    # host = self.addHost('h%s' % (swnum+1))
	    # self.addLink(host, switchList[swnum], bw=50, delay='1ms')
            if swnum > 0:
	       self.addLink(switchList[swnum], switchList[swnum-1], bw=1000, delay='5ms')

        self.addLink(switchList[0],switchList[n-1], bw=1000, delay='5ms')
        
        # Creating first small ring switches
        self.addSwitch('sw14')
        self.addSwitch('sw15')
        self.addSwitch('sw16')
        self.addSwitch('sw17')
        self.addSwitch('sw18')

        # Connecting first small ring switches
        self.addLink('sw13', 'sw14', bw=bw_1, delay=delay_1)         
        self.addLink('sw14', 'sw15', bw=bw_1, delay=delay_1)         
        self.addLink('sw15', 'sw16', bw=bw_1, delay=delay_1)         
        self.addLink('sw16', 'sw17', bw=bw_1, delay=delay_1)         
        self.addLink('sw17', 'sw18', bw=bw_1, delay=delay_1)         
        self.addLink('sw18', 'sw11', bw=bw_1, delay=delay_1)         

        # Creating second small ring switches
        for switch in range (19,25):
            self.addSwitch('sw%s' % switch)
        #self.addSwitch('sw19')
        #self.addSwitch('sw20')
        #self.addSwitch('sw21')
        #self.addSwitch('sw22')
        #self.addSwitch('sw23')
        #self.addSwitch('sw24')

        # Connecting second small ring switches
        self.addLink('sw5', 'sw19', bw=bw_1, delay=delay_1)         
        self.addLink('sw19', 'sw20', bw=bw_1, delay=delay_1)         
        self.addLink('sw20', 'sw21', bw=bw_1, delay=delay_1)         
        self.addLink('sw21', 'sw22', bw=bw_1, delay=delay_1)         
        self.addLink('sw22', 'sw23', bw=bw_1, delay=delay_1)         
        self.addLink('sw23', 'sw24', bw=bw_1, delay=delay_1)         
        self.addLink('sw24', 'sw4', bw=bw_1, delay=delay_1)         

        # Creating not ringed switches  
#       self.addSwitch('sw25')
#       self.addSwitch('sw26')
#       self.addSwitch('sw27')
#       self.addSwitch('sw28')
#       self.addSwitch('sw29')
#       self.addSwitch('sw30')
#       self.addSwitch('sw31')
#       self.addSwitch('sw32')
#       self.addSwitch('sw33')
#       self.addSwitch('sw34')
#       self.addSwitch('sw35')
#       self.addSwitch('sw36')
        for switch in range (25, 37):
            self.addSwitch('sw%s' % switch)

        # Connecting not ringed switches
        self.addLink('sw25', 'sw18', bw=bw_1, delay=delay_1)
        self.addLink('sw26', 'sw16', bw=bw_1, delay=delay_1)
        self.addLink('sw27', 'sw13', bw=bw_1, delay=delay_1)
        self.addLink('sw28', 'sw1', bw=bw_1, delay=delay_1)
        self.addLink('sw29', 'sw20', bw=bw_1, delay=delay_1)
        self.addLink('sw30', 'sw20', bw=bw_1, delay=delay_1)
        self.addLink('sw31', 'sw21', bw=bw_1, delay=delay_1)
        self.addLink('sw32', 'sw22', bw=bw_1, delay=delay_1)
        self.addLink('sw33', 'sw23', bw=bw_1, delay=delay_1)
        self.addLink('sw34', 'sw6', bw=bw_1, delay=delay_1)
        self.addLink('sw35', 'sw7', bw=bw_1, delay=delay_1)
        self.addLink('sw36', 'sw9', bw=bw_1, delay=delay_1)

        # Adding hosts
        n_host=37
        for host in range (1, n_host):
            self.addHost('h%s' % host)
        
        # Connecting each host with their corresponding switch
        self.addLink('h1', 'sw27', bw=bw_2, delay=delay_2)
        self.addLink('h2', 'sw27', bw=bw_2, delay=delay_2)
        self.addLink('h3', 'sw28', bw=bw_2, delay=delay_2)
        self.addLink('h4', 'sw28', bw=bw_2, delay=delay_2)
        self.addLink('h5', 'sw28', bw=bw_2, delay=delay_2)
        self.addLink('h6', 'sw2', bw=bw_2, delay=delay_2)
        self.addLink('h7', 'sw2', bw=bw_2, delay=delay_2)
        self.addLink('h8', 'sw29', bw=bw_2, delay=delay_2)
        self.addLink('h9', 'sw30', bw=bw_2, delay=delay_2)
        self.addLink('h10', 'sw30', bw=bw_2, delay=delay_2)
        self.addLink('h11', 'sw31', bw=bw_2, delay=delay_2)
        self.addLink('h12', 'sw31', bw=bw_2, delay=delay_2)
        self.addLink('h13', 'sw32', bw=bw_2, delay=delay_2)
        self.addLink('h14', 'sw22', bw=bw_2, delay=delay_2)
        self.addLink('h15', 'sw33', bw=bw_2, delay=delay_2)
        self.addLink('h16', 'sw23', bw=bw_2, delay=delay_2)
        self.addLink('h17', 'sw24', bw=bw_2, delay=delay_2)
        self.addLink('h18', 'sw5', bw=bw_2, delay=delay_2)
        self.addLink('h19', 'sw34', bw=bw_2, delay=delay_2)
        self.addLink('h20', 'sw34', bw=bw_2, delay=delay_2)
        self.addLink('h21', 'sw6', bw=bw_2, delay=delay_2)
        self.addLink('h22', 'sw35', bw=bw_2, delay=delay_2)
        self.addLink('h23', 'sw35', bw=bw_2, delay=delay_2)
        self.addLink('h24', 'sw8', bw=bw_2, delay=delay_2)
        self.addLink('h25', 'sw8', bw=bw_2, delay=delay_2)
        self.addLink('h26', 'sw9', bw=bw_2, delay=delay_2)
        self.addLink('h27', 'sw36', bw=bw_2, delay=delay_2)
        self.addLink('h28', 'sw36', bw=bw_2, delay=delay_2)
        self.addLink('h29', 'sw36', bw=bw_2, delay=delay_2)
        self.addLink('h30', 'sw11', bw=bw_2, delay=delay_2)
        self.addLink('h31', 'sw25', bw=bw_2, delay=delay_2)
        self.addLink('h32', 'sw25', bw=bw_2, delay=delay_2)
        self.addLink('h33', 'sw17', bw=bw_2, delay=delay_2)
        self.addLink('h34', 'sw26', bw=bw_2, delay=delay_2)
        self.addLink('h35', 'sw26', bw=bw_2, delay=delay_2)
        self.addLink('h36', 'sw15', bw=bw_2, delay=delay_2)

topos = { 'anillo': ( lambda: Anillo(n=13) ) }
