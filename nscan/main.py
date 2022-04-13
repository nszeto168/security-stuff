#!/usr/bin/python3
# Welcome to my incredible port scanner!
import sys, getopt
import full_connect_scan

argument_list = sys.argv[1:]  # Collects the flag

options = "hfm :"

long_options = ["help", "moo", "full-connect", " "]

try:

   flag, value = getopt.getopt(argument_list, options, long_options) #

   for currentArgument, currentValue in flag:
       # we can probably use a dictionary instead of iterating multiple times...
        if currentArgument in ("-h", "--help"):
            print(
            """
            HELP:
            -h, --help
            COW:
            -m, --moo
            FULL CONNECT SCAN: 
            -f, --full-connect
            """)
        if currentArgument in ("-m", "--moo"):
            print(
            """
             _____
            < moo >
             -----
                    \   ^__^
                     \  (oo)\_______
                        (__)\       )\/\||----w |
                            ||     ||
            """)
        if currentArgument in ("-f", "--full-connect"):
            # I know this solution is kinda gross because it doesn't parse like a normal command
            # I have other things to do, so rn im just doing quick and dirty
            target = input("Enter the target hostname or IP address: ")
            fport = input("Enter the first port you want to scan (will scan in a range): ")
            lport = input("Enter the last port you want to scan (will scan in a range): ")
            print("Performing a full connect scan")
            results = full_connect_scan.scan(fport, lport, target)
            for port in results:
                # print out all the open ports
                print(f"Port {port} is open for business!")

except getopt.GetoptError:
    print("Use the -h or --help for help")