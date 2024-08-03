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

nmap Output:

╰─ nmap 192.168.56.101                                                                                     ─╯
Starting Nmap 7.95 ( https://nmap.org ) at 2024-08-03 10:04 IST
Nmap scan report for 192.168.56.101
Host is up (0.00086s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE  SERVICE
80/tcp  open   http
443/tcp closed https
