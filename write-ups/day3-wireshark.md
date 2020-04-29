# Tooling
	- Wireshark: `apt install wireshark`

# Steps
	1. Search Telnet protocol
	2. Right click -> Follow -> TCP Stream to get client-server back-and-forth
	3. Telnet is being used to pass shell commands to the server
	4. Grab packet with christmas list addition: `echo 'ps4' > christmas_list.txt`
	5. Crack password in last Telnet packet after echo'ing /etc/shadow:
		-> `cat /etc/shadow`
		-> `... buddy:$6$3GvJsNPG$ZrSFprHS13divBhlaKg1rYrYLJ7m1xsYRKxlLh0A1sUc/6SUd7UvekBOtSnSyBwk3vCDqBhrgxQpkdsNN6aYP1:18233:0:99999:7:::`
	6. Crack buddy's password with hashcat: `apt install hashcat`
	7. Use https://hashcat.net/wiki/doku.php?id=example_hashes to find example matches and match $6 to sha512crypt i.e. mode 1800
	8. Grab hashed password wordlist: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
	9. Crack: `hashcat -m 1800 hash-file rockyou.txt` --> rainbow
