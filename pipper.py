import os
import sys
import urllib
import subprocess

def download(file_url,local_filename):
	web_file = urllib.urlopen(file_url)
	local_file = open(local_filename, 'w')
	local_file.write(web_file.read())
	web_file.close()
	local_file.close()

def get_windows_pip3_path():
	python_dir = sys.executable
	split = python_dir.split("\\")
	pip3_path = ""
	for i in range(0,len(split)-1):
		pip3_path = "%s/%s" %(pip3_path,split[i])
	pip3_path = "%s/Scripts/pip3" %pip3_path[1:]

	return pip3_path

def pip3_install_module(module_name):
	pip3_path = "pip3"
	DEVNULL = open(os.devnull,'wb')
	new_installation = True

	try:
		subprocess.call(["pip3"], stdout=DEVNULL) # verify if pip3 is already installed
	except OSError as e:
		if(sys.platform[:3] == "win"):
			pip3_path = get_windows_pip3_path()
			try:
				subprocess.call([pip3_path],stdout=DEVNULL)
				new_installation = False
				print "[+] Found Windows pip3 executable at '%s'" %pip3_path
			except:
				pass

		if(new_installation):
			print "[!] pip3 is not currently installed."

			if(os.path.isfile("get-pip3.py") is False):
				print "[*] Downloading get-pip3.py.."
				download("https://bootstrap.pypa.io/get-pip3.py","get-pip3.py")
			else:
				print "[+] get-pip3-py found in the current directory."

	    	os.system("python get-pip3.py")

	    	try:
	    		subprocess.call(["pip3"],stdout=DEVNULL)
	    	except:
	    		if(sys.platform[:3] == "win"):
		    		python_dir = sys.executable # "C:\\Python27\\python.exe"
		    		split = python_dir.split("\\")
		    		pip3_path = ""
		    		for i in range(0,len(split)-1): # let's avoid python.exe
		    			pip3_path = "%s/%s" %(pip3_path,split[i])

		    		pip3_path = "%s/Scripts/pip3" %pip3_path[1:]

	if(new_installation):
		try:
			os.remove("get-pip3.py")
		except:
			pass

	os.system("%s install --upgrade pip3" %pip3_path)
	print "\n[*] Installing module '%s'" %module_name
	os.system("%s install %s" %(pip3_path,module_name))

