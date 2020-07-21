from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import Link

if __name__ == '__main__':
    
    net = Mininet()
    
    # Hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    # Routers
    r1 = net.addHost('r1')
    r2 = net.addHost('r2')
    r3 = net.addHost('r3')

    # Links
    net.addLink(h1, r1, intfName1 = 'h1-eth0', intfName2 = 'r1-eth0')
    net.addLink(r1, r2, intfName1 = 'r1-eth1', intfName2 = 'r2-eth0')
    net.addLink(r2, r3, intfName1 = 'r2-eth1', intfName2 = 'r3-eth0')
    net.addLink(r3, h2, intfName1 = 'r3-eth1', intfName2 = 'h2-eth0')

    # build the network with the devices
    net.build()

    # h1
    h1.cmd("ifconfig h1-eth0 0")
    h1.cmd("ifconfig h1-eth0 10.1.1.1 netmask 255.255.255.0")
    # h1 lo
    h1.cmd("ifconfig lo 122.1.1.4 netmask 255.255.255.255")

    #h1 routes
    h1.cmd("ip route add default via 10.1.1.2 dev h1-eth0")
    h1.cmd("ip route add to 11.1.1.0/24 via 10.1.1.2 dev h1-eth0")
    h1.cmd("ip route add to 12.1.1.0/24 via 10.1.1.2 dev h1-eth0")
    h1.cmd("ip route add to 13.1.1.0/24 via 10.1.1.2 dev h1-eth0")
    h1.cmd("ip route add to 122.1.1.1/32 via 10.1.1.2 dev h1-eth0")
    h1.cmd("ip route add to 122.1.1.2/32 via 10.1.1.2 dev h1-eth0")
    h1.cmd("ip route add to 122.1.1.3/32 via 10.1.1.2 dev h1-eth0")
    h1.cmd("ip route add to 122.1.1.5/32 via 10.1.1.2 dev h1-eth0")


    # h2
    h2.cmd("ifconfig h2-eth0 0")
    h2.cmd("ifconfig h2-eth0 13.1.1.2 netmask 255.255.255.0")
    # h2 lo
    h2.cmd("ifconfig lo 122.1.1.5 netmask 255.255.255.255")
    h2.cmd("ip route add default via 13.1.1.1 dev h2-eth0")
    # h1.cmd("ip route add 11.1.1.0 via 10.1.1.2 dev h1-eth0")
    #h2 routes
    h2.cmd("ip route add default via 13.1.1.1 dev h2-eth0")
    h2.cmd("ip route add to 11.1.1.0/24 via 13.1.1.1 dev h2-eth0")
    h2.cmd("ip route add to 12.1.1.0/24 via 13.1.1.1 dev h2-eth0")
    h2.cmd("ip route add to 10.1.1.0/24 via 13.1.1.1 dev h2-eth0")
    h2.cmd("ip route add to 122.1.1.1/32 via 13.1.1.1 dev h2-eth0")
    h2.cmd("ip route add to 122.1.1.2/32 via 13.1.1.1 dev h2-eth0")
    h2.cmd("ip route add to 122.1.1.3/32 via 13.1.1.1 dev h2-eth0")
    h2.cmd("ip route add to 122.1.1.4/32 via 13.1.1.1 dev h2-eth0")
    
    #r1
    r1.cmd("ifconfig r1-eth0 0")
    r1.cmd("ifconfig r1-eth1 0")
    r1.cmd("ifconfig r1-eth0 10.1.1.2 netmask 255.255.255.0")
    r1.cmd("ifconfig r1-eth1 11.1.1.2 netmask 255.255.255.0")
    r1.cmd("ifconfig lo 122.1.1.1 netmask 255.255.255.255")

    # r1 - IP Forwarding
    r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    #r1 routes
    r1.cmd("ip route add to 12.1.1.0/24 via 11.1.1.1 dev r1-eth1")
    r1.cmd("ip route add to 13.1.1.0/24 via 11.1.1.1 dev r1-eth1")
    r1.cmd("ip route add to 122.1.1.4/32 via 10.1.1.1 dev r1-eth0")
    r1.cmd("ip route add to 122.1.1.2/32 via 11.1.1.1 dev r1-eth1")
    r1.cmd("ip route add to 122.1.1.3/32 via 11.1.1.1 dev r1-eth1")
    r1.cmd("ip route add to 122.1.1.5/32 via 11.1.1.1 dev r1-eth1")
    
    # r2
    r2.cmd("ifconfig r2-eth0 0")
    r2.cmd("ifconfig r2-eth1 0")
    r2.cmd("ifconfig r2-eth0 11.1.1.1 netmask 255.255.255.0")
    r2.cmd("ifconfig r2-eth1 12.1.1.1 netmask 255.255.255.0")
    r2.cmd("ifconfig lo 122.1.1.2 netmask 255.255.255.255")

    # r2 IP Forwarding
    r2.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    #h1 routes
    r2.cmd("ip route add to 10.1.1.0/24 via 11.1.1.2 dev r2-eth0")
    r2.cmd("ip route add to 13.1.1.0/24 via 12.1.1.2 dev r2-eth1")
    r2.cmd("ip route add to 122.1.1.1/32 via 11.1.1.2 dev r2-eth0")
    r2.cmd("ip route add to 122.1.1.4/32 via 11.1.1.2 dev r2-eth0")
    r2.cmd("ip route add to 122.1.1.3/32 via 12.1.1.2 dev r2-eth1")
    r2.cmd("ip route add to 122.1.1.5/32 via 12.1.1.2 dev r2-eth1")

    # r3
    r3.cmd("ifconfig r3-eth0 0")
    r3.cmd("ifconfig r3-eth1 0")
    r3.cmd("ifconfig r3-eth0 12.1.1.2 netmask 255.255.255.0")
    r3.cmd("ifconfig r3-eth1 13.1.1.1 netmask 255.255.255.0")
    r3.cmd("ifconfig lo 122.1.1.3 netmask 255.255.255.255")

    # r3 IP Forwarding
    r3.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    #h1 routes
    r3.cmd("ip route add to 11.1.1.0/24 via 12.1.1.1 dev r3-eth0")
    r3.cmd("ip route add to 10.1.1.0/24 via 12.1.1.1 dev r3-eth0")
    r3.cmd("ip route add to 122.1.1.1/32 via 12.1.1.2 dev r3-eth0")
    r3.cmd("ip route add to 122.1.1.2/32 via 12.1.1.1 dev r3-eth0")
    r3.cmd("ip route add to 122.1.1.4/32 via 12.1.1.1 dev r3-eth0")
    r3.cmd("ip route add to 122.1.1.5/32 via 13.1.1.2 dev r3-eth1")

    CLI(net)

    net.stop()
