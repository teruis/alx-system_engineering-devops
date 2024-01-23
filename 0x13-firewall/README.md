Background Context
The project involves working with firewalls, specifically configuring Uncomplicated Firewall (UFW) on web servers. The goal is to block all incoming traffic except for specific TCP ports. Additionally, the project requires setting up port forwarding using UFW.

Requirements
Install UFW on web-01 and configure it to block all incoming traffic, except for the following TCP ports:

22 (SSH)
443 (HTTPS SSL)
80 (HTTP)
Share the UFW commands used in the answer file.
Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP. Modify the UFW configuration file accordingly.

Resources
Web stack debugging guide concept page
Telnet command usage for checking socket connectivity
Tasks
Block all incoming traffic: Complete the task on web-01.
Port forwarding: Complete the advanced task on web-01.
