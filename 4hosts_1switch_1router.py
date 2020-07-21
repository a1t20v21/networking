from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import Link

if __name__ == '__main__':

    net = Mininet()
   
    # add two hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    # add an L2 switch
    s5 = net.addHost('s5')
    
    # add links
    Link(h1, s5) # h1-(h1-eth0)<------->(s5-eth0)-s5
    Link(h2, s5)
    
    net.build()

    # delete the default IP config in both h1 and h2
    h1.cmd("ifconfig h1-eth0 0")
    h2.cmd("ifconfig h2-eth0 0")

    # vlan config on L2 switch
    s5.cmd("ifconfig s5-eth0 0")
    s5.cmd("ifconfig s5-eth1 0")

    s5.cmd("brctl addbr vlan10")
    s5.cmd("ifconfig vlan10 up")

    s5.cmd("brctl addif vlan10 s5-eth0")
    s5.cmd("brctl addif vlan10 s5-eth1")

    # ip config on the hosts
    h1.cmd("ifconfig h1-eth0 10.0.10.1 netmask 255.255.255.0")
    h2.cmd("ifconfig h2-eth0 10.0.10.2 netmask 255.255.255.0")

    h1.cmd("ip route add default via 10.0.10.254 dev h1-eth0")
    h2.cmd("ip route add default via 10.0.10.254 dev h2-eth0")

    CLI(net)

    net.stop()
