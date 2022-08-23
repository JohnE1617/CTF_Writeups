https://tryhackme.com/room/mrrobot

**Basic enumeration**

    22/tcp  closed ssh
    80/tcp  open   http     Apache httpd
    |_http-title: Site doesn't have a title (text/html).
    |_http-server-header: Apache
    443/tcp open   ssl/http Apache httpd
    |_http-title: Site doesn't have a title (text/html).
    | ssl-cert: Subject: commonName=www.example.com
    | Not valid before: 2015-09-16T10:45:03
    |_Not valid after:  2025-09-13T10:45:03
    |_http-server-header: Apache

So it looks like we are working with a standard webserver so we should start to more enumerations

    gobuster dir -u http://10.10.237.76/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,php

    nikto -h 10.10.237.76  
    
We find a robots.txt file so we should investigate that:

    User-agent: *
    fsocity.dic
    key-1-of-3.txt
    
    └─# cat key-1-of-3.txt 
    073403c8a58a1f80d943455fb30724b9

Lets also grab that .dic file

    wget http://10.10.237.76/fsocity.dic   

That is a big file! let us take a look at some of the entries

        └─# head fsocity.dic                                                                          
    true
    false
    wikia
    from
    the
    now
    Wikia
    extensions
    scss
    window
    
    └─# wc -l fsocity.dic 
    858160 fsocity.dic
    
    └─# sort -u fsocity.dic > sorted.dic

    └─# wc -l sorted.dic
    11451 sorted.dic

Whew that is much more reasonable to workwith, My bet is that this is a password/username list

**Initial Foothold**
    
    

         
