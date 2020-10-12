import time 
from datetime import datetime as dt 
import sys

#
# A script created to block the sites you want at a special time.
# Do not delete the given files by the script, otherwise you may actually
# get in troble.
# Create by amirhossein at Oct 12th 2020

UPDATE_TIME = 3600 # 1 hour

# set the time limits 
STARTING_CLOCK = 8
ENDING_CLOCK = 16
allow = True
  
# change hosts path according to your OS 
hosts_path = "/etc/hosts"
# localhost's IP 
redirect = "127.0.0.1"
  
# websites That you want to block 
file_of_sites = "data.txt"
backup_file = "backup"
website_list = []


def save_backup():
    global hosts_path, backup_file
    with open(hosts_path, 'r') as file: 
        content = file.read() 
        with open(backup_file, 'w') as dest:
        	dest.write(content)
        	print(":> We backuped your data, please don't remove the file.")


def restore_data(): 
    global hosts_path, backup_file
    try:
    	with open(backup_file, 'r') as file: 
        	content = file.read() 
        	with open(hosts_path, 'w') as dest:
        		dest.write(content)
        		print(":> Data restored.") 
    except:
    	print(">? Since you removed the backup file, cannot restore your data")  
    finally:
    	sys.exit(0)	  		      	


def input_sites():
	try:
		with open(file_of_sites, 'r') as file:
			content = file.readlines()
			website_list = [line for line in content]
	except:
		print(":?> No \"data.txt\" found to get the sites.")
		sys.exit(-1)		


def time_check(): # to check if the program should still run
	global STARTING_CLOCK, ENDING_CLOCK
	cond_1=dt(dt.now().year,dt.now().month,dt.now().day,STARTING_CLOCK)<dt.now()
	cond_2=dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,ENDING_CLOCK)
	return cond_1 and cond_2


def block_sites():	
    global hosts_path, redirect, website_list
	# modifying the host file
    with open(hosts_path, 'r+') as file: 
        content = file.read() 
        for website in website_list: 
            if website in content: 
                pass
            else: 
                # mapping hostnames to your localhost IP address 
                file.write(redirect + " " + website + "\n") 


def free_sites():  
    global hosts_path, redirect, website_list
    # Reseting the host file
    with open(hosts_path, 'r+') as file: 
        content = file.readlines() 
        file.seek(0) # set the position to first line 
        for line in content: 
            if not any(website in line for website in website_list): 
                file.write(line) # write the first lines before we exe
  
        # removing hostnmes from host file 
        file.truncate() # resizing to its default 


def safe_terminate():
	free_sites()
	print(":> Program is now terminated succussfully.")
	sys.exit(0)


def exe():
    global hosts_path, redirect, website_list, UPDATE_TIME
    # program main loop
    while True: 
    	if time_check(): # time of your work 
        	print("::> At working time, the websites are now block ...") 
        	block_sites()
    	else: # out of the working time
    		print("::> At free time, the websites are now available ...") 
    		free_sites()	
  		# wait for update time to come
    	try: 
    		time.sleep(UPDATE_TIME) 
    	except:
    		try:
    			safe_terminate()	
    		except:
    			print("::?> Warning => Program may damaged your host file.")
    			sys.exit(-1)


def go(argv):
	if argv[1] == "RESET":
		restore_data()
	save_backup()	
	input_sites()
	exe()	


if __name__ == "__main__":
	go(sys.argv[0:])