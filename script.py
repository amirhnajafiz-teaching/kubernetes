import time 
from datetime import datetime as dt 

UPDATE_TIME = 3600 # 1 hour

# set the time limits 
STARTING_CLOCK = 8
ENDING_CLOCK = 16
  
# change hosts path according to your OS 
hosts_path = "/etc/hosts"
# localhost's IP 
redirect = "127.0.0.1"
  
# websites That you want to block 
website_list = ["www.facebook.com","facebook.com","dub119.mail.live.com"] 


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
    	time.sleep(UPDATE_TIME) 