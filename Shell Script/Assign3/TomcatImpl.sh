#!/bin/bash

# Install Tomcat
sudo yum install tomcat7

# To start Tomcat:
sudo service tomcat7 start

# To stop Tomcat:
sudo service tomcat7 stop

# Change the default port 8080 to 8090.
sudo /sbin/iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
