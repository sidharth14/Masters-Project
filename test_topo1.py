#!/Desktop

from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.clean import cleanup
from threading import Thread

class test(Topo):
   # creating test toplogy
    def __init__(self, **opts):
        

        super(test, self).__init__(**opts)
        # adding Host

       	h1 = self.addHost('h1')               
	h2 = self.addHost('h2')
	h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
	h6 = self.addHost('h6')
	h7 = self.addHost('h7')
	h8 = self.addHost('h8')
	h9 = self.addHost('h9')
	h10 = self.addHost('h10')
	h11 = self.addHost('h11')
	h12 = self.addHost('h12')
	h13 = self.addHost('h13')
	h14 = self.addHost('h14')
	h15 = self.addHost('h15')
	h16 = self.addHost('h16')
	h17 = self.addHost('h17')
	h18 = self.addHost('h18')
	h19 = self.addHost('h19')
	h20 = self.addHost('h20')
	h21 = self.addHost('h21')
	h22 = self.addHost('h22')
	h23 = self.addHost('h23')
	h24 = self.addHost('h24')
	h25 = self.addHost('h25')
	h26 = self.addHost('h26')
	h27 = self.addHost('h27')
	h28 = self.addHost('h28')
	h29 = self.addHost('h29')
	h30 = self.addHost('h30')
	h31 = self.addHost('h31')
	h32 = self.addHost('h32')
	h33 = self.addHost('h33')
	h34 = self.addHost('h34')
	h35 = self.addHost('h35')
	#h36 = self.addHost('h36')
	#h37 = self.addHost('h37')
	#h38 = self.addHost('h38')
	#h39 = self.addHost('h39')
	#h40 = self.addHost('h40')
	

        # Adding switches
	
        s1 = self.addSwitch('s1', dpid="0000000000000001")
        s2 = self.addSwitch('s2', dpid="0000000000000002")
        s3 = self.addSwitch('s3', dpid="0000000000000003")
	s4 = self.addSwitch('s4', dpid="0000000000000004")
	s5 = self.addSwitch('s5', dpid="0000000000000005")
	s6 = self.addSwitch('s6', dpid="0000000000000006")
	s7 = self.addSwitch('s7', dpid="0000000000000007")
	s8 = self.addSwitch('s8', dpid="0000000000000008")
	s9 = self.addSwitch('s9', dpid="0000000000000009")
	#s1 = self.addSwitch('s1', dpid="0000000000000001")
	#s1 = self.addSwitch('s1', dpid="0000000000000001")
	
        

	# adding Links
 
        # Links for S2
	self.addLink(h1, s2, bw=100)
        print("h1 to s2 link is added")
	self.addLink(h2, s2, bw=100)
	self.addLink(h3, s2, bw=100)
	self.addLink(h4, s2, bw=100)
	self.addLink(h5, s2, bw=100)

	 # Links for S3
	self.addLink(h6, s3, bw=100)
	self.addLink(h7, s3, bw=100)
	self.addLink(h8, s3, bw=100)
	self.addLink(h9, s3, bw=100)
	self.addLink(h10, s3, bw=100)
	
	 # Links for S4
	self.addLink(h11, s4, bw=100)
	self.addLink(h12, s4, bw=100)
	self.addLink(h13, s4, bw=100)
	self.addLink(h14, s4, bw=100)
	self.addLink(h15, s4, bw=100)

	# Links for S5
	self.addLink(h16, s5, bw=100)
	self.addLink(h17, s5, bw=100)
	self.addLink(h18, s5, bw=100)
	self.addLink(h19, s5, bw=100)
	self.addLink(h20, s5, bw=100)

	# Links for S6
	self.addLink(h21, s6, bw=100)
	self.addLink(h22, s6, bw=100)
	self.addLink(h23, s6, bw=100)
	self.addLink(h24, s6, bw=100)
	self.addLink(h25, s6, bw=100)

	# Links for S7
	self.addLink(h26, s7, bw=100)
	self.addLink(h27, s7, bw=100)
	self.addLink(h28, s7, bw=100)
	self.addLink(h29, s7, bw=100)
	self.addLink(h30, s7, bw=100)

	# Links for S8
	self.addLink(h31, s8, bw=100)
	self.addLink(h32, s8, bw=100)
	self.addLink(h33, s8, bw=100)
	self.addLink(h34, s8, bw=100)
	self.addLink(h35, s8, bw=100)

	# Links for S9
	#self.addLink(h36, s9, bw=100)
	#self.addLink(h36, s9, bw=100)
	#self.addLink(h38, s9, bw=100)
	#self.addLink(h39, s9, bw=100)
	#self.addLink(h40, s9, bw=100)


	self.addLink(s1, s2, bw=100)
	self.addLink(s1, s3, bw=100)
	self.addLink(s1, s4, bw=100)

        self.addLink(s1, s9, bw=1000)
	self.addLink(s9, s5, bw=100)
	self.addLink(s9, s6, bw=100)
	self.addLink(s9, s7, bw=100)
	self.addLink(s9, s8, bw=100)
	#self.addLink(s1, s9, bw=100)
	#self.addLink(s1, s10, bw=100)

def run():
    cleanup()
    c = RemoteController('c', '127.0.0.1', 6653)
    net = Mininet(topo=test(), host=CPULimitedHost, controller=None, link=TCLink)
    net.addController(c)
    net.start()


   # Config for 1st subnet
    h1 = net.get('h1')
    h1.setIP("192.168.100.1/24")
    h1.cmd('route add default h1-eth0')
    h1.cmd('arp -s 10.0.100.2/24 0000000000000002')
    
    h2 = net.get('h2')
    h2.setIP("192.168.100.2/24")
    h2.cmd('route add default h2-eth0')
    h2.cmd('arp -s 10.0.100.2/24 0000000000000002')

    h3 = net.get('h3')
    h3.setIP("192.168.100.3/24")
    h3.cmd('route add default h3-eth0')
    h3.cmd('arp -s 10.0.100.2/24 0000000000000002')

    h4 = net.get('h4')
    h4.setIP("192.168.100.4/24")
    h4.cmd('route add default h4-eth0')
    h4.cmd('arp -s 10.0.100.2/24 0000000000000002')  
    
    h5 = net.get('h5')
    h5.setIP("192.168.100.5/24")
    h5.cmd('route add default h5-eth0')
    h5.cmd('arp -s 10.0.100.2/24 0000000000000002')

    # config subnet 2
    h6 = net.get('h6')
    h6.setIP("192.168.101.1/24")
    h6.cmd('route add default h6-eth0')
    h6.cmd('arp -s 10.0.100.3/24 0000000000000003')

    h7 = net.get('h7')
    h7.setIP("192.168.101.2/24")
    h7.cmd('route add default h7-eth0')
    h7.cmd('arp -s 10.0.100.3/24 0000000000000003')

    h8 = net.get('h8')
    h8.setIP("192.168.101.3/24")
    h8.cmd('route add default h8-eth0')
    h8.cmd('arp -s 10.0.100.3/24 0000000000000003')

    h9 = net.get('h9')
    h9.setIP("192.168.101.4/24")
    h9.cmd('route add default h9-eth0')
    h9.cmd('arp -s 10.0.100.3/24 0000000000000003')

    h10 = net.get('h10')
    h10.setIP("192.168.101.5/24")
    h10.cmd('route add default h10-eth0')
    h10.cmd('arp -s 10.0.100.3/24 0000000000000003')

	 # config subnet 3
    
  
    h11 = net.get('h11')
    h11.setIP("192.168.102.1/24")
    h11.cmd('route add default h11-eth0')
    h11.cmd('arp -s 10.0.100.4/24 0000000000000004')

    h12 = net.get('h12')
    h12.setIP("192.168.102.2/24")
    h12.cmd('route add default h12-eth0')
    h12.cmd('arp -s 10.0.100.4/24 0000000000000004')

    h13 = net.get('h13')
    h13.setIP("192.168.102.3/24")
    h13.cmd('route add default h13-eth0')
    h13.cmd('arp -s 10.0.100.4/24 0000000000000004')

    h14 = net.get('h14')
    h14.setIP("192.168.102.4/24")
    h14.cmd('route add default h14-eth0')
    h14.cmd('arp -s 10.0.100.4/24 0000000000000004')

    h15 = net.get('h15')
    h15.setIP("192.168.102.5/24")
    h15.cmd('route add default h15-eth0')
    h15.cmd('arp -s 10.0.100.4/24 0000000000000004')

       # config subnet 4

    h16 = net.get('h16')
    h16.setIP("192.168.103.1/24")
    h16.cmd('route add default h16-eth0')
    h16.cmd('arp -s 10.0.200.2/24 0000000000000005')

    h17 = net.get('h17')
    h17.setIP("192.168.103.2/24")
    h17.cmd('route add default h17-eth0')
    h17.cmd('arp -s 10.0.200.2/24 0000000000000005')

    h18 = net.get('h18')
    h18.setIP("192.168.103.3/24")
    h18.cmd('route add default h18-eth0')
    h18.cmd('arp -s 10.0.200.2/24 0000000000000005')

    h19 = net.get('h19')
    h19.setIP("192.168.103.4/24")
    h19.cmd('route add default h19-eth0')
    h19.cmd('arp -s 10.0.200.2/24 0000000000000005')

    h20 = net.get('h20')
    h20.setIP("192.168.103.5/24")
    h20.cmd('route add default h20-eth0')
    h20.cmd('arp -s 10.0.200.2/24 0000000000000005')

     #  config subnet 5

    h21 = net.get('h21')
    h21.setIP("192.168.104.1/24")
    h21.cmd('route add default h21-eth0')
    h21.cmd('arp -s 10.0.200.3/24 0000000000000006')

    h22 = net.get('h22')
    h22.setIP("192.168.104.2/24")
    h22.cmd('route add default h22-eth0')
    h22.cmd('arp -s 10.0.200.3/24 0000000000000006')

    h23 = net.get('h23')
    h23.setIP("192.168.104.3/24")
    h23.cmd('route add default h23-eth0')
    h23.cmd('arp -s 10.0.200.3/24 0000000000000006')

    h24 = net.get('h24')
    h24.setIP("192.168.104.4/24")
    h24.cmd('route add default h24-eth0')
    h24.cmd('arp -s 10.0.200.3/24 0000000000000006')

    h25 = net.get('h25')
    h25.setIP("192.168.104.5/24")
    h25.cmd('route add default h25-eth0')
    h25.cmd('arp -s 10.0.200.3/24 0000000000000006')

    #  config subnet 6

    h26 = net.get('h26')
    h26.setIP("192.168.105.1/24")
    h26.cmd('route add default h26-eth0')
    h26.cmd('arp -s 10.0.200.4/24 0000000000000007')

    h27 = net.get('h27')
    h27.setIP("192.168.105.2/24")
    h27.cmd('route add default h27-eth0')
    h27.cmd('arp -s 10.0.200.4/24 0000000000000007')

    h28 = net.get('h28')
    h28.setIP("192.168.105.3/24")
    h28.cmd('route add default h28-eth0')
    h28.cmd('arp -s 10.0.200.4/24 0000000000000007')

    h29 = net.get('h29')
    h29.setIP("192.168.105.4/24")
    h29.cmd('route add default h29-eth0')
    h29.cmd('arp -s 10.0.200.4/24 0000000000000007')

    h30 = net.get('h30')
    h30.setIP("192.168.105.5/24")
    h30.cmd('route add default h30-eth0')
    h30.cmd('arp -s 10.0.200.4/24 0000000000000007')

    #  config subnet 7

    h31 = net.get('h31')
    h31.setIP("192.168.106.1/24")
    h31.cmd('route add default h31-eth0')
    h31.cmd('arp -s 10.0.200.5/24 0000000000000008')

    
    h32 = net.get('h32')
    h32.setIP("192.168.106.2/24")
    h32.cmd('route add default h32-eth0')
    h32.cmd('arp -s 10.0.200.5/24 0000000000000008')

    h33 = net.get('h33')
    h33.setIP("192.168.106.3/24")
    h33.cmd('route add default h33-eth0')
    h33.cmd('arp -s 10.0.100.8/24 0000000000000008')

    h34 = net.get('h34')
    h34.setIP("192.168.106.4/24")
    h34.cmd('route add default h34-eth0')
    h34.cmd('arp -s 10.0.200.5/24 0000000000000008')

    h35 = net.get('h35')
    h35.setIP("192.168.106.5/24")
    h35.cmd('route add default h35-eth0')
    h35.cmd('arp -s 10.0.200.5/24 0000000000000008')


    #  config subnet 7

    #h36 = net.get('h36')
    #h36.setIP("192.168.107.1/24")
    #h36.cmd('route add default h36-eth0')
    #h36.cmd('arp -s 10.0.100.9/24 0000000000000009')

    #h37 = net.get('h37')
    #h37.setIP("192.168.107.2/24")
    #h37.cmd('route add default h37-eth1')
    #h37.cmd('arp -s 10.0.100.9/24 0000000000000009')

    #h38 = net.get('h38')
    #h38.setIP("192.168.107.3/24")
    #h38.cmd('route add default h38-eth1')
    #h38.cmd('arp -s 10.0.100.9/24 0000000000000009')

    #h39 = net.get('h39')
    #h39.setIP("192.168.107.4/24")
    #h39.cmd('route add default h39-eth1')
    #h39.cmd('arp -s 10.0.100.9/24 0000000000000009')

    #h40 = net.get('h40')
    #h40.setIP("192.168.107.5/24")
    #h40.cmd('route add default h40-eth1')
    #h40.cmd('arp -s 10.0.100.9/24 0000000000000009')



    #s1 = net.get('s1')
    #s1.setIP('10.0.100.1/24')

    #s2 = net.get('s2')
    #s2.setIP('10.0.100.2/24')
    
    #s3 = net.get('s3')
    #s3.setIP('10.0.100.3/24')
    
    #s4 = net.get('s4')
    #s4.setIP('10.0.100.4/24')
    
    #s5 = net.get('s5')
    #s5.setIP('10.0.200.2/24')
    
    #s6 = net.get('s6')
    #s6.setIP('10.0.200.3/24')
    
    #s7 = net.get('s7')
    #s7.setIP('10.0.200.4/24')
    
    #s8 = net.get('s8')
    #s8.setIP('10.0.200.5/24')
    
    #s9 = net.get('s9')
    #s9.setIP('10.0.200.1/24')
  
    #net.pingAll()


    CLI(net)
    
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
	




