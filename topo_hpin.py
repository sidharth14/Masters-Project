from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.clean import cleanup
from threading import Thread
from time import sleep
"""
Instructions to run the topo:
    1. Go to directory where this file is.
    2. run: sudo -E python Simple_Pkt_Topo.py.py

The topo has 4 switches and 4 hosts. They are connected in a star shape.
"""


class SimplePktSwitch(Topo):
    """Simple topology example."""

    def __init__(self, **opts):
        """Create custom topo."""

        # Initialize topology
        # It uses the constructor for the Topo cloass
        super(SimplePktSwitch, self).__init__(**opts)

        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
	h5 = self.addHost('h5')
	h6 = self.addHost('h6')
	h7 = self.addHost('h7')
	h8 = self.addHost('h8')

        # Adding switches
	
        s1 = self.addSwitch('s1', dpid="0000000000000001")
        s2 = self.addSwitch('s2', dpid="0000000000000002")
        s3 = self.addSwitch('s3', dpid="0000000000000003")
        #s4 = self.addSwitch('s4', dpid="0000000000000004")

        # Add links
        self.addLink(h1, s1, bw=100)
        self.addLink(h2, s1, bw=100)
        self.addLink(h3, s1, bw=100)
        self.addLink(h4, s1, bw=100)
	self.addLink(h5, s2, bw=100)
	self.addLink(h6, s2, bw=100)
	self.addLink(h7, s2, bw=100)
	self.addLink(h8, s2, bw=100)

        self.addLink(s1, s3, bw=1000)
        self.addLink(s2, s3, bw=1000)
        #self.addLink(s1, s4, bw=1000)


def run():
    cleanup()
    c = RemoteController('c', '127.0.0.1', 6653)
    net = Mininet(topo=SimplePktSwitch(), host=CPULimitedHost, controller=None, link=TCLink)
    net.addController(c)
    net.start()
    
    h1, h5 = net.get('h1','h5')
    #net.iperf((h1, h5))
    h2 = net.get('h2')
    print('Type of h2: ')
    print(type(h2))
    h3, h4, h6, h7, h8 = net.get('h3','h4','h6','h7','h8')	
    #print "Testing network connectivity"
    #net.pingAll()
    #result = h5.cmd('ifconfig')
    #print(result)
    #result3 = h2.cmd('ping 10.0.0.5 -c 4')
    #print(result3)
    #print "Starting xtrem here"
    #t1 = threading.Thread(target = h4.cmd('xterm h4')) 
    #t2 = threading.Thread(target = h1.cmd('sudo hping3 10.0.0.4 --flood')) 
    #t1.start()
    #t2.start()
    #t1.join()
    #t2.join()
    #print (result2)
    
    #CLI(net)
    target = h1
    #print('target host is: ',target)
    #seconds = 10
    popens = {}
    
    hosts = (h1, h2, h3, h4, h5, h6, h7, h8)
    for h in hosts:
        #print('hosts are:', h)	
	if h == target:
	    popens[h] = h.popen('tcpdump -w hpin39.pcap')
	    print('Starting tcpdump here:')
        #popens[h]=h.popen('hping3', target.IP(), '-u')
	
	else:
            #popens[h]=h.popen('ping',target.IP())
	    #popens[h]=h.popen('hping3',target.IP(),' --udp',' --file hpin_testing.txt',' --data 100')
	    popens[h]=h.popen('hping3 ' + target.IP() + ' -c 20 --file hpin_testing.txt --data 100')
	    print(target.IP())
	    #print('hping3', target.IP(),' --file hpin_testing.txt --data 100')
	    #print('started pinging the target (h1)',h)



        #print"Monitoring output for",seconds,'seconds'
	#endTime = time()+seconds
	#for h, line in pmonitor(popens, timeoutms= 500):
	    #if h:
                #print '%s: %s' % ( h.name, line ),
                #if time() >= endTime:
                    #for p in popens.values():
                        #p.send_signal( SIGINT )
        
    CLI(net)
    net.stop()

# if the script is run directly (sudo custom/optical.py):
if __name__ == '__main__':
    setLogLevel('info')
    run()
