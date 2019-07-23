#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.util import dumpNodeConnections


class CustomTree(Topo):
	"Creating the switches and hosts, then building the tree"

	def build(self):
		#Adding Hosts - Client PC & Client Server
		h1 = self.addHost('h1',ip='10.0.0.1',cls= None,defaultRoute=None)
		h2 = self.addHost('h2',ip='10.0.0.254',cls= None,defaultRoute=None)
		#Adding Switches
		info("Adding Switches\n")
		s1 = self.addSwitch('s1',datapath=None,protocols=None)
		s2 = self.addSwitch('s2',datapath=None,protocols=None)
		s3 = self.addSwitch('s3',datapath=None,protocols=None)
		s4 = self.addSwitch('s4',datapath=None,protocols=None)
		s5 = self.addSwitch('s5',datapath=None,protocols=None)
		s6 = self.addSwitch('s6',datapath=None,protocols=None)
		s7 = self.addSwitch('s7',datapath=None,protocols=None)
		s8 = self.addSwitch('s8',datapath=None,protocols=None)
		s9 = self.addSwitch('s9',datapath=None,protocols=None)
		s10 = self.addSwitch('s10',datapath=None,protocols=None)
		s11 = self.addSwitch('s11',datapath=None,protocols=None)
		
		info("Adding Links\n")
		#Adding bandwidth attribute
		self.addLink(s1,s5,cls=TCLink,bw=10)
		self.addLink(s8,s5,cls=TCLink,bw=15)
		self.addLink(s2,s5,cls=TCLink,bw=15)
		self.addLink(s2,s6,cls=TCLink,bw=20)
		self.addLink(s9,s5,cls=TCLink,bw=15)
		self.addLink(s6,s5,cls=TCLink,bw=20)
		self.addLink(s6,s9,cls=TCLink,bw=15)
		self.addLink(s3,s6,cls=TCLink,bw=15)
		self.addLink(s10,s6,cls=TCLink,bw=10)
		self.addLink(s7,s6,cls=TCLink,bw=20)
		self.addLink(s7,s3,cls=TCLink,bw=10)
		self.addLink(s10,s7,cls=TCLink,bw=15)
		self.addLink(s4,s7,cls=TCLink,bw=15)
		self.addLink(s11,s7,cls=TCLink,bw=10)
		info("Adding Host Links\n")
		#Adding Host Links
		self.addLink(h1,s1)
		self.addLink(h2,s11)




def myProgram():
	info("Topology Python Script...\n")
	net = Mininet(topo=CustomTree(), build=False, ipBase='10.0.0.0/8',autoStaticArp=True,link=TCLink)
	info("Adding the RemoteController\n")
	c0 = net.addController('c0',ip='127.0.0.1',protocol='tcp',controller=RemoteController, port = 6633)
	info("Adding Hosts\n")
	info("Starting network")
	#net.build()
	net.start()
	info('*** Starting switches\n')



	info('Dumping Host connections')
	dumpNodeConnections(net.hosts)
	info('Check Ping Activity')
	net.pingAll()


	#info('*** Testing bandwidth between my hosts ****\n')
	#h1, h2 = net.get('h1','h2');
	#net.iperf((h1,h2))
	#info('**** Post configure switches and hosts\n')
	CLI(net)
	net.stop()	


if __name__ == '__main__':
	setLogLevel('info')
	myProgram()
