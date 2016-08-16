#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Packet sniffer in python3 by Engine'''

__author__ = 'Engine'

import sys
import socket
from struct import unpack

# convert a string of 6 characters of ethernet address in a format hex string
def eth_addr(s):
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (s[0], s[1], s[2], s[3], s[4], s[5])
    return b


# 0                   1                   2                   3
# 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |       Ethernet destination address (first 32 bits)            |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# | Ethernet dest (last 16 bits)  |Ethernet source (first 16 bits)|
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |       Ethernet source address (last 32 bits)                  |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |        Type code              |                               |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
def eth_parser(raw_eth):
    '''parse ethernet frame header'''
    # s is for bytes, 6s means 6 bytes
    # h is for integer, whose standard size is 2 bytes
    eth = unpack("!6s6sh", raw_eth)  # eth is a tuple of d_mac, s_mac, type_code
    eth_fields = {}  # create a dict to store ethernet frame header information
    eth_fields["Destination MAC"] = eth_addr(eth[0])  # use eth_addr function for formatting
    eth_fields["Source MAC"] = eth_addr(eth[1])
    # socket.ntohs - convert a 16-bit integer from network to host byte order
    # I dont't really know this, it just convert 2048 to 8
    # 8 represents the data part is a ip package
    eth_fields["Protocol"] = "Internet Protocol" if socket.ntohs(eth[2]) == 8 else None
    return eth_fields

# 0                   1                   2                   3
# 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |Version|  IHL  |Type of Service|          Total Length         |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |         Identification        |Flags|      Fragment Offset    |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |  Time to Live |    Protocol   |         Header Checksum       |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |                       Source Address                          |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |                    Destination Address                        |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |                    Options                    |    Padding    |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
def iph_parser(raw_iph):
    '''parse IP datagram header'''
    # B is for integer, whose standard size is 1 bytes
    # H is for integer, whose standard size is 2 bytes. In python type
    # format "H" & "h" are same in python type, but diffrent in c type
    iph = unpack("!BBHHHBBH4s4s", raw_iph)  # so iph is a 10-elements tuple
    iph_fields = {}

    version_ihl = iph[0]  # Version and IHL share the 1st bytes
    iph_fields["Version"] = version_ihl >> 4  # right shift 4 bits to get the Version
    iph_fields["IHL"] = (version_ihl & 0x0F) * 4    # get the ip header length

    # we don't care about type of service, and identification
    iph_fields["Total Length"] = iph[2]  # totcal length is the length of ip header and data part
    flags = iph[4] >> 13  # flags & fragment offset share the 2 bytes, we just get flags by shifting
    iph_fields["MF"] = 1 if flags & 1 else 0  # test the 1st bit
    iph_fields["DF"] = 1 if flags & 2 else 0  # test the 2nd bit
    iph_fields["Fragment Offset"] = iph[4] & 0x1FFF  # get the fragment offset part from iph[4]
    iph_fields["Time to Live"] = iph[5]
    iph_fields["Protocol"] = iph[6]
    iph_fields["Header Checksum"] = iph[7]
    # socket.inet_ntoa - convert an ip address from 32-bit packed binary format to string format
    iph_fields["Source Address"] = socket.inet_ntoa(iph[8])
    iph_fields["Desination Address"] = socket.inet_ntoa(iph[9])

    return iph_fields


# 0                   1                   2                   3
# 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |          Source Port          |       Destination Port        |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |                        Sequence Number                        |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |                    Acknowledgment Number                      |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |  Data |           |U|A|P|R|S|F|                               |
# | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
# |       |           |G|K|H|T|N|N|                               |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |           Checksum            |         Urgent Pointer        |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |                    Options                    |    Padding    |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |                             data                              |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
def tcph_parser(raw_tcph):
    '''parse tcp package header'''
    # L is for integer,whose standard size is 4 bytes
    tcph = unpack("!HHLLBBHHH", raw_tcph)  #tcph has 9 elements
    tcph_fields = {}

    tcph_fields["Source Port"] = tcph[0]
    tcph_fields["Destination Port"] = tcph[1]
    tcph_fields["Sequence Number"] = tcph[2]
    tcph_fields["Acknowledgement Number"] = tcph[3]
    tcph_fields["Data Offset"] = tcph[4] >> 4  # data offset & reserved share tcph[4]
    flags = tcph[5]
    tcph_fields["FIN"] = 1 if flags & 1 else 0  # test n bit
    tcph_fields["SYN"] = 1 if flags & 2 else 0
    tcph_fields["RST"] = 1 if flags & 4 else 0
    tcph_fields["PSH"] = 1 if flags & 8 else 0
    tcph_fields["ACK"] = 1 if flags & 16 else 0
    tcph_fields["URG"] = 1 if flags & 32 else 0
    tcph_fields["Window"] = tcph[6]
    tcph_fields["Checksum"] = tcph[7]
    tcph_fields["Urgent Pointer"] = tcph[8]

    return tcph_fields



# 0      7 8     15 16    23 24    31
# +--------+--------+--------+--------+
# |     Source      |   Destination   |
# |      Port       |      Port       |
# +--------+--------+--------+--------+
# |                 |                 |
# |     Length      |    Checksum     |
# +--------+--------+--------+--------+
def udph_parser(raw_udph):
    '''parse udp package header'''
    udph = unpack("!HHHH", raw_udph)
    udph_fields = {}

    udph_fields["Source Port"] = udph[0]
    udph_fields["Destination Port"] = udph[1]
    udph_fields["Length"] = udph[2]
    udph_fields["Checksum"] = udph[3]

    return udph_fields

# 0                   1                   2                   3
# 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |     Type      |     Code      |          Checksum             |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |                             unused                            |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |      Internet Header + 64 bits of Original Data Datagram      |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
def icmph_parser(raw_icmph):
    '''parse icmp package header'''
    icmph = unpack("!BBH", raw_icmph)
    icmph_fields = {}

    icmph_fields["Type"] = icmph[0]
    icmph_fields["Code"] = icmph[1]
    icmph_fields["Checksum"] = icmph[2]

    return icmph_fields

# define my print function to make the output more beautiful
def myprint(t, d):
    print("=" * 64)
    print('|', t, ' ' * (59 - len(t)), '|')
    print("*" * 64)
    for k, v in d.items():
        print('|', k, ' ' * (25 - len(k)) , ':', str(v), ' ' * (30 - len(str(v))), "|")
    print("=" * 64)
    print("")

def main():
    try:
        # socket.ntohs: convert a 16-bit integer from network to host byte order
        # create a socket AF_PACKET type raw socket
        # raw socket will bypassed the transport layer, so we can get the ethernet frame
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    except socket.error as msg:
        print("Socket could not be created. Error Code: " + str(msg[0]) + "Message " + msg[1])
        sys.exit(0)

    eth_length = 14  # ethernet frame header is 14 bytes long

    while True:
        # receive a packet, set buffersize the max value
        # recvfrom(buffersize [, flags]) -> (data, address info)
        raw_packet = s.recvfrom(65565)

        # the return value of recvfrom is a tuple, we just need the data
        packet = raw_packet[0]

        # packet[0:14] is the ethernet frame header of the packet
        eth_fields = eth_parser(packet[0:eth_length])
        myprint("Ethernet Frame Header", eth_fields)  # print the ethernet frame header

        if eth_fields["Protocol"] == "Internet Protocol":
            # here we just think about the fixed part
            iph_fields = iph_parser(packet[eth_length:eth_length + 20])

            # t is the total length of ip header and ethernet frame header
            t = iph_fields["IHL"] + eth_length
            if iph_fields["Protocol"] == 6:
                iph_fields["Protocol"] = "Transmission Control Protocol"
                # also we just think about the fixed part
                tcph_fields = tcph_parser(packet[t:t + 20])
                myprint("IP Package Header", iph_fields)
                myprint("TCP Package Header", tcph_fields)
            elif iph_fields["Protocol"] == 17:
                iph_fields["Protocol"] = "User Datagram Protocol"
                udph_fields = udph_parser(packet[t:t + 8])
                myprint("IP Package Header", iph_fields)
                myprint("UDP Package Header", udph_fields)
            elif iph_fields["Protocol"] == 1:
                iph_fields["Protocol"] = "Internet Control Message Protocol"
                icmph_fields = icmph_parser(packet[t:t + 4])
                myprint("IP Package Header", iph_fields)
                myprint("ICMP Package Header", icmph_fields)
            else:
                print("Protocols other than TCP/UDP/ICMP")


if __name__ == '__main__':
    main()
