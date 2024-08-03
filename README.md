    # Assignment-on-Networking-and-Servers
Assignment on Networking and Servers


1. Created a new directory using command :
    mkdir /etc/httpd/conf/vhosts
2. Created new virtual host conf file :
    nano /etc/httpd/conf/vhosts/awesomeweb.com
3. added following code in conf file.

    <VirtualHost *:80>
        ServerAdmin mandarphadke1434@gmail.com
        DocumentRoot "/srv/awesomeweb.com"
        ServerName awesomeweb.com
        <Directory "/srv/awesomeweb.com">
            Require all granted
        </Directory>
    </VirtualHost>

4. Created new folder :
    mkdir /srv/awesomeweb.com
5. moved the html project template to /srv/awesomeweb.com folder.
6. Changed the ownership of website using :
    chown -R root:http /srv/awesomeweb.com
7. added new line apache in conf file "Include conf/vhosts/awesomeweb.com" using command :
     "nano /etc/httpd/conf/httpd.conf"
8. Restarted the apache server using command
    systemctl restart httpd

--------------------------------------------------------------------------------------
installing nginx on virtualbox
1. Installed virtualbox
2. Booted linux-mint in virtualbox
3. Installed nginix in virtualbox
4. Started the nginx service
5. On localhost nginx basic html file is visible.
6. Similarly Installed nginx on host and started the service.
7. Used Host-Only Adapter in virtual box.
8. And scanned the IP of virtualbox using nmap.
nmap -p 1-65535 -T4 -A -v 192.168.56.101
nmap Output:

╭─    ~ ▓▒░────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────░▒▓ ✔  took 3s   at 01:10:35 PM  ─╮
╰─ nmap -p 1-65535 -T4 -A -v 192.168.56.101                                                                                                                                              ─╯
Starting Nmap 7.95 ( https://nmap.org ) at 2024-08-03 13:15 IST
NSE: Loaded 157 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 13:15
Completed NSE at 13:15, 0.00s elapsed
Initiating NSE at 13:15
Completed NSE at 13:15, 0.00s elapsed
Initiating NSE at 13:15
Completed NSE at 13:15, 0.00s elapsed
Initiating Ping Scan at 13:15
Scanning 192.168.56.101 [2 ports]
Completed Ping Scan at 13:15, 0.00s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:15
Completed Parallel DNS resolution of 1 host. at 13:15, 0.00s elapsed
Initiating Connect Scan at 13:15
Scanning 192.168.56.101 [65535 ports]
Discovered open port 80/tcp on 192.168.56.101
Connect Scan Timing: About 23.31% done; ETC: 13:18 (0:01:42 remaining)
Connect Scan Timing: About 59.61% done; ETC: 13:17 (0:00:41 remaining)
Completed Connect Scan at 13:17, 87.65s elapsed (65535 total ports)
Initiating Service scan at 13:17
Scanning 1 service on 192.168.56.101
Completed Service scan at 13:17, 6.03s elapsed (1 service on 1 host)
NSE: Script scanning 192.168.56.101.
Initiating NSE at 13:17
Completed NSE at 13:17, 5.02s elapsed
Initiating NSE at 13:17
Completed NSE at 13:17, 0.02s elapsed
Initiating NSE at 13:17
Completed NSE at 13:17, 0.00s elapsed
Nmap scan report for 192.168.56.101
Host is up (0.00048s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT    STATE  SERVICE VERSION
80/tcp  open   http    Apache httpd 2.4.58 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.58 (Ubuntu)
443/tcp closed https

NSE: Script Post-scanning.
Initiating NSE at 13:17
Completed NSE at 13:17, 0.00s elapsed
Initiating NSE at 13:17
Completed NSE at 13:17, 0.00s elapsed
Initiating NSE at 13:17
Completed NSE at 13:17, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 99.12 seconds

