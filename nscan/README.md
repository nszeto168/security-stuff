Welcome to my port scanner
With the power of multithreading, you can scan many, many ports at once!
Be careful though because if you scan too quickly, you might bring down a host or cause a ton of alerts!
As with all tools, this tool is only for use in legal and ethical activities. As Google would say
when they were less evil, "Don't be evil".
Run this tool by running main.py:

Full connect scan:
python main.py <host> -f

SYN scan:
sudo python main.py <host> -s

X-mas scan:
sudo python main.py <host> -x

The SYN scan and X-mas scan need root permissions because you are crafting packets.
By default, this program will scan TCP ports 1-1000 w/ 10 threads, the scan will take approximately 25 seconds.

If you need help, you can always use the -h or --help options.

Happy Scanning!
