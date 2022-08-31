https://tryhackme.com/room/skynet

**Basic Enumeration**

    └─# rustscan --ulimit 5000 --batch-size 2500 -a 10.10.204.113 -- -A -oN nmap_initial

    Open 10.10.204.113:22
    Open 10.10.204.113:80
    Open 10.10.204.113:110
    Open 10.10.204.113:139
    Open 10.10.204.113:143
    Open 10.10.204.113:445

Looks like we have ssh, webserver, pop3, samba, imap running on this server so lets kick off a few enumeration tools for the webserver and the samba shares

    ┌──(root㉿kali)-[/home/kali/skynet]
    └─# enum4linux -a 10.10.204.113              
    
    ┌──(root㉿kali)-[/home/kali/skynet]
    └─# enum4linux -a 10.10.204.113    
    
 
**ENUM4LINUX**

        =======================================( Users on 10.10.204.113 )=======================================

      index: 0x1 RID: 0x3e8 acb: 0x00000010 Account: milesdyson	Name: 	Desc: 

      user:[milesdyson] rid:[0x3e8]

       =================================( Share Enumeration on 10.10.204.113 )=================================


        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        anonymous       Disk      Skynet Anonymous Share
        milesdyson      Disk      Miles Dyson Personal Share
        IPC$            IPC       IPC Service (skynet server (Samba, Ubuntu))

      //10.10.204.113/print$	Mapping: DENIED Listing: N/A Writing: N/A
      //10.10.204.113/anonymous	Mapping: OK Listing: OK Writing: N/A
      //10.10.204.113/milesdyson	Mapping: DENIED Listing: N/A Writing: N/A
 
 
 From this we can see a potential username of milesdyson which we should keep an eye on
 
 **GoBuster**
 
     /admin                (Status: 301) [Size: 314] [--> http://10.10.204.113/admin/]
    /css                  (Status: 301) [Size: 312] [--> http://10.10.204.113/css/]  
    /js                   (Status: 301) [Size: 311] [--> http://10.10.204.113/js/]   
    /config               (Status: 301) [Size: 315] [--> http://10.10.204.113/config/]
    /ai                   (Status: 301) [Size: 311] [--> http://10.10.204.113/ai/]   
    /squirrelmail         (Status: 301) [Size: 321] [--> http://10.10.204.113/squirrelmail/]


Only with our shares lets take a look at our
