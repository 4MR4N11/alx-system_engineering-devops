# 0x07. Networking basics #0

This project is about networking basics. We will learn about OSI model, LAN, WAN, IP address, TCP/UDP, and more.

## Files

- [0-OSI_model](./0-OSI_model): Text file answering the following questions:
  - What is the OSI model?
	- Set of specifications that network hardware manufacturers must respect
	- The OSI model is a conceptual model that characterizes the communication
	  functions of a telecommunication system without regard to their underlying
	  internal structure and technology
	- The OSI model is a model that characterizes the communication functions of
	  a telecommunication system with a strong regard for their underlying
	  internal structure and technology
  - How is the OSI model organized?
	- Alphabetically
	- From the lowest to the highest level
	- Randomly

- [1-types_of_network](./1-types_of_network): Text file answering the following questions:
  - What type of network a computer in local is connected to?
	- Internet
	- WAN
	- LAN
  - What type of network could connect an office in one building to another
	office in a building a few streets away?
	- Internet
	- WAN
	- LAN
  - What network do you use when you browse www.google.com from your
	smartphone (not connected to the Wifi)?
	- Internet
	- WAN
	- LAN

- [2-MAC_and_IP_address](./2-MAC_and_IP_address): Text file answering the following questions:
  - What is a MAC address?
	- The name of a network interface
	- The unique identifier of a network interface
	- A network interface
  - What is an IP address?
	- Is to devices connected to a network what postal address is to houses
	- The unique identifier of a network interface
	- Is a number that network devices use to connect to networks

- [3-UDP_and_TCP](./3-UDP_and_TCP): Text file answering the following questions:
  - Which statement is correct for the TCP box:
	- It is a protocol that is transferring data in a slow way but surely
	- It is a protocol that is transferring data in a fast way and might loss
	  data along in the process
  - Which statement is correct for the UDP box:
	- It is a protocol that is transferring data in a slow way but surely
	- It is a protocol that is transferring data in a fast way and might loss
	  data along in the process
  - Which statement is correct for the TCP worker:
	- Have you received boxes x, y, z?
	- May I increase the rate at which I am sending you boxes?

- [4-TCP_and_UDP_ports](./4-TCP_and_UDP_ports): Bash script that displays listening ports:
  - That only shows listening sockets
  - That shows the PID and name of the program to which each socket belongs

- [5-is_the_host_on_the_network](./5-is_the_host_on_the_network): Bash script that pings an IP address passed as an argument:
  - Accepts a string as an argument
  - Displays `Usage: 5-is_the_host_on_the_network {IP_ADDRESS}` if no argument
	is passed
  - Ping the IP 5 times
