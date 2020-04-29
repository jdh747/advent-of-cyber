# Tooling
- Gobuster, for enumerating http servers pages. Installed with `apt install gobuster`
- Wordlist, DirBuster-Lists/directory-list-2.3-big.txt, from: `https://sourceforge.net/projects/dirbuster/files/DirBuster%20Lists/Current/DirBuster-Lists.tar.bz2/download?use_mirror=nchc&use_mirror=osdn`

1. Find admin page with `gobuster -w DirBuster-Lists/directory-list-2.3-big.txt`: 10.10.216.127:3000/sysadmin
2. Check sysadmin page source to find comment: `/* Admin portal created by arctic digital design - check out our github repo */`
3. Search comment and navigate to resulting github: https://github.com/ashu-savani/arctic-digital-design
4. Github contains username (admin) and password (defaultpass). Login