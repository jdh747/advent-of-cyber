# Tools
	- Wireshark: exporting HTTP objects (.zip, .jpeg): file->export objects->http->christmas.zip and TryHackMe.jpg
	- Wireshark: checking DNS requests to holidaythief.com, with subdomain encoding 43616e64792043616e652053657269616c204e756d6265722038343931
	- CyberChef: playing around with encoded strings - https://gchq.github.io/CyberChef/
	- Steghide: extracting data embedded in jpeg
	- fcrackzip: crack encrypted zip file

# DNS
	- DNS requests to holidaythief.com exported 43616e64792043616e652053657269616c204e756d6265722038343931 in the subdomain
	- Using CyberChef, adding a 'from hex' filter, gives: Candy Cane Serial Number 8491

# Steghide
	- Pulling TryHackMe.jpg from Wireshark
	- `steghide extract -sf TryHackMe.jpg` (empty passphrase), generates christmasmonstor.txt, RFC527 lyrics

# Zip
	- Pulling christmas.zip from Wireshark
	- `fcrackzip -b --method 2 -D -p rockyou.txt -v christmaslists.zip` gives "december"
	- `unzip christmas.zip`, enter "december" for password prompt
	- Read christmaslisttimmy.txt -> PenTester
