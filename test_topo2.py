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
	host = 35         # total number of hosts in network
	switch = 9        #total number of switches in the network
 	band1 = 100       #Bandwidth of the link in Mbps
	band2 = 1000
	queue_size = 32   #Defines the length of queue size 
        
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
				self.addLink('h'+str(k), 's'+str(i), bw=band1, max_queue_size=queue_size)
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
    hosts = list()
    popens = {}
    #target = h5
    #target = 'h'+str(5)
    for x in range(1,36):
        hostnm = 'h'+str(x)
        #hosts.append(hostnm)
        #print(hostnm)
        
        #print(target)
        hostn = net.get(hostnm)
	hosts.append(hostn)        
	#print(type()hostn)
        #print(hostn)
        #targethost = net.get(target)
        #print(targethost)
        #if hostn != targethost:
	    #print('InTO target host loop:')
            #net.iperf((hostn, targethost))
    #hosts = (h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23, h24, h25, h26, h27, h28, h29, h30, h31, h32, h33, h34, h35)
    target = net.get('h'+str(5))
    
    #print(hosts)
    for h in hosts:
        #print('hosts are:', h)	
	if h == target:
            print('got the target host tobe h5',target)
	    popens[h] = h.popen('tcpdump -w hpin_test.pcap')
	    #print('Starting tcpdump here:')
        else:
            popens[h]=h.popen('hping3 ' + target.IP() + ' -c 20 --file hpin_testing.txt --data 100')
	    #print(target.IP())
        #popens[h]=h.popen('sudo','hping3',' -c',' 500',' --udp',' -p',' 100',target.IP())

    
    CLI(net)
    	  
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
	




