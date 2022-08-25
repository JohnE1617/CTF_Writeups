https://tryhackme.com/room/overpass

BoxIP = 10.10.121.50

**Basic Enumeration**

    ┌──(root㉿kali)-[/home/kali/overpass]
    └─# rustscan --ulimit 5000 -b 2500 -a 10.10.121.50 -- -A

    22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 37:96:85:98:d1:00:9c:14:63:d9:b0:34:75:b1:f9:57 (RSA)
    | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLYC7Hj7oNzKiSsLVMdxw3VZFyoPeS/qKWID8x9IWY71z3FfPijiU7h9IPC+9C+kkHPiled/u3cVUVHHe7NS68fdN1+LipJxVRJ4o3IgiT8mZ7RPar6wpKVey6kubr8JAvZWLxIH6JNB16t66gjUt3AHVf2kmjn0y8cljJuWRCJRo9xpOjGtUtNJqSjJ8T0vGIxWTV/sWwAOZ0/TYQAqiBESX+GrLkXokkcBXlxj0NV+r5t+Oeu/QdKxh3x99T9VYnbgNPJdHX4YxCvaEwNQBwy46515eBYCE05TKA2rQP8VTZjrZAXh7aE0aICEnp6pow6KQUAZr/6vJtfsX+Amn3
    |   256 53:75:fa:c0:65:da:dd:b1:e8:dd:40:b8:f6:82:39:24 (ECDSA)
    | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMyyGnzRvzTYZnN1N4EflyLfWvtDU0MN/L+O4GvqKqkwShe5DFEWeIMuzxjhE0AW+LH4uJUVdoC0985Gy3z9zQU=
    |   256 1c:4a:da:1f:36:54:6d:a6:c6:17:00:27:2e:67:75:9c (ED25519)
    |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINwiYH+1GSirMK5KY0d3m7Zfgsr/ff1CP6p14fPa7JOR
    80/tcp open  http   syn-ack ttl 63 Golang net/http server (Go-IPFS json-rpc or InfluxDB API)


Next we can start a gobuster and Nikto Scans to start our automated enumeration while we go visit the webpage


    ──(root㉿kali)-[/home/kali/overpass]
    └─# gobuster dir -u http://10.10.121.50/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,php 

    ┌──(root㉿kali)-[/home/kali/overpass]
    └─# nikto -h 10.10.121.50 


for CTF it is good practice to look at the page source and CSS so lets investigate there first


     <p>Overpass allows you to securely store different
                    passwords for every service, protected using military grade
                    <!--Yeah right, just because the Romans used it doesn't make it military grade, change this?-->
                    cryptography to keep you safe.


We get a clue on what kind of cryptography they are using since it is a Roman reference I am betting this is a Caesar Cypher

Next we navigate to the aboutus page and we can see some potential user names

    Our Staff

    Ninja - Lead Developer

    Pars - Shibe Enthusiast and Emotional Support Animal Manager

    Szymex - Head Of Security

    Bee - Chief Drinking Water Coordinator

    MuirlandOracle - Cryptography Consultant

 Next we go to the downloads page and it may look like we have the source code to look at...

    <li><a href="src/overpass.go" download>Source Code</li>

investigating the sourcecode we can see that they are using the rotate 47 caesar-cipher. Additionally, there is another potential username leaked.

      //A linear search is the best I can do, Steve says it's Oh Log N whatever that means

In the meantime our gobuster has found an admin panel. Let's start a hydra attack using the username 'steve'

    ┌──(root㉿kali)-[/home/kali/overpass]
    └─# hydra -l steve -P /usr/share/wordlists/rockyou.txt 10.10.121.50 http-post-form "/admin:username=^USER^&password=^PASS^:F=Incorrect Credentials"

Well after trying for awhile I gave upon they hydra approach. lets look at the post form a little more closely


