# 🔐 Project 1: Failed Login Attempt Analyzer

This script scans a sample auth log file for suspicious IP addresses with multiple failed login attempts.# 🔐 Project 1: Failed Login Attempt Analyzer

This script scans a sample auth log file for suspicious IP addresses with multiple failed login attempts.

## 💻 How I Simulated the Log File

I used a sample file `auth.log` and simulated failed login attempts by appending entries. Then used this command to run the script:

Below is the failed login attempts executed on my own machine, hence that's why all theses failed attempts use the same 
local address (127.0.0.1 ).They show different times and and dates of the login attempots.

```bash
python3 log_analysis.py

nkugza-dasmall@Nkululeko-LM28:~/cyber_projects$ ssh wronguser@localhost
wronguser@localhost's password:
Permission denied, please try again.
wronguser@localhost's password:
Permission denied, please try again.
wronguser@localhost's password:
wronguser@localhost: Permission denied (publickey,password).
nkugza-dasmall@Nkululeko-LM28:~/cyber_projects$ sudo grep "Failed password" /var/log/auth.log
[sudo] password for nkugza-dasmall:
2025-04-17T12:37:15.561288+02:00 Nkululeko-LM28 sshd[1720]: Failed password for invalid user wronguser from 127.0.0.1 port 34932 ssh2
2025-04-17T12:37:21.313101+02:00 Nkululeko-LM28 sshd[1720]: Failed password for invalid user wronguser from 127.0.0.1 port 34932 ssh2
2025-04-17T12:37:28.115059+02:00 Nkululeko-LM28 sshd[1720]: Failed password for invalid user wronguser from 127.0.0.1 port 34932 ssh2
2025-04-17T12:39:15.216683+02:00 Nkululeko-LM28 sudo: nkugza-dasmall : TTY=pts/0 ; PWD=/home/nkugza-dasmall/bruce-force-detector ; USER=root ; COMMAND=/usr/bin/grep 'Failed password' /var/log/auth.log
2025-04-23T08:04:02.186511+02:00 Nkululeko-LM28 sshd[559]: Failed password for invalid user wronguser from 127.0.0.1 port 32898 ssh2
2025-04-23T08:04:08.024986+02:00 Nkululeko-LM28 sshd[559]: Failed password for invalid user wronguser from 127.0.0.1 port 32898 ssh2
2025-04-23T08:04:12.019377+02:00 Nkululeko-LM28 sshd[559]: Failed password for invalid user wronguser from 127.0.0.1 port 32898 ssh2
2025-04-23T08:04:56.505269+02:00 Nkululeko-LM28 sudo: nkugza-dasmall : TTY=pts/0 ; PWD=/home/nkugza-dasmall/cyber_projects ; USER=root ; COMMAND=/usr/bin/grep 'Failed password' /var/log/auth.log
nkugza-dasmall@Nkululeko-LM28:~/cyber_projects$ python3 log_analysis.py

🔥 Suspicious IPs with multiple failed login attempts:

IP: 127.0.0.1 | Attempts: 6
nkugza-dasmall@Nkululeko-LM28:~/cyber_projects$

