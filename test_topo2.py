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
   
    # TODO: Move to global space
    no_host = 35
    #no_switch = 9
    #band1 = 100
    #band2 = 1000

# creating test toplogy
    def __init__(self, **opts):
	host = 35
	switch = 9
 	band1 = 100
	band2 = 1000
        
        super(test, self).__init__(**opts)
        # adding Host
        for i in range (host):
            self.addHost('h'+str(i+1))


        # Adding switches
        '''for i in range (switch):
	    mac = 'dpid=' + '"000000000000000' + str(i+1) +'"'
	    print(mac)
	    sw = 's'+str(i+1)
	    print(sw, mac)
            self.addSwitch(sw)'''
        s1 = self.addSwitch('s1', dpid="0000000000000001")
        s2 = self.addSwitch('s2', dpid="0000000000000002")
        s3 = self.addSwitch('s3', dpid="0000000000000003")
	s4 = self.addSwitch('s4', dpid="0000000000000004")
	s5 = self.addSwitch('s5', dpid="0000000000000005")
	s6 = self.addSwitch('s6', dpid="0000000000000006")
	s7 = self.addSwitch('s7', dpid="0000000000000007")
	s8 = self.addSwitch('s8', dpid="0000000000000008")
	s9 = self.addSwitch('s9', dpid="0000000000000009")
	    
 

	# adding Links
	i = 2
	j = 1
	while i <= switch-1:
		while j <= host:
			for k in range(j,j+5):
				self.addLink('h'+str(k), 's'+str(i), bw=band1)
			j = j+5
			break
		i = i+1
	self.addLink(s1, s2, bw=100)
	self.addLink(s1, s3, bw=100)
	self.addLink(s1, s4, bw=100)

        #self.addLink(s1, s9, bw=1000)
	self.addLink(s1, s5, bw=100)
	self.addLink(s1, s6, bw=100)
	self.addLink(s1, s7, bw=100)
	self.addLink(s1, s8, bw=100)
        # Links for S2
	


def run():
    cleanup()
    c = RemoteController('c', '127.0.0.1', 6653)
    net = Mininet(topo=test(), host=CPULimitedHost, controller=None, link=TCLink)
    net.addController(c)
    net.start()	 
    
    i = 1
    ip_3 = 100
    swt = 2		
    while i <= 35:
	#print("i: "+str(i))
        k = 1
	
	for j in range (i,i+5):
		#print("j "+str(j))
		hostname = 'h'+str(j)
		host = net.get(hostname)
		ip = '192.168.'
		ip = ip + str(ip_3) + '.' + str(k) + '/24'
                k = k+1
		
		host.setIP(ip)
		host.cmd('route add default '+'h'+str(j)+'-eth0')
		switch = '10.0.100.' + str(swt) + '/24' + ' 000000000000000'+ str(swt)
                host.cmd('arp -s ' + str(switch))  
	swt = swt + 1	
	i = i+5
        ip_3 = ip_3+1
	
	  #ip = '192.168.100.' + str(i+1) + '/24'
	  #host.setIP(ip)
	  #host.cmd('route add default '+'h'+str(i+1)+'-eth0')
          #host.cmd('arp -s 10.0.100.2/24 0000000000000002')
    for x in range(1,36):
        hostnm = 'h'+str(x)
        #print(hostnm)
        target = 'h'+str(5)
        #print(target)
        hostn = net.get(hostnm)
        #print(hostn)
        targethost = net.get(target)
        #print(targethost)
        if hostn != targethost:
	    print('InTO target host loop:')
            net.iperf((hostn, targethost))

    
    #CLI(net)
    	
	


  
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
	




