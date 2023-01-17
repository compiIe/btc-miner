import subprocess
import os 
import urllib.request
import platform

current_os = platform.system()
cgminer_url = "https://github.com/ckolivas/cgminer/archive/master.zip"
username, password, pool = 'username', 'password', 'stratum+tcp://btc.slushpool.com:3333'
miner_command = f"./cgminer --url={pool} --user={username} --pass={password} -o {pool} -u {username} -p {password} --scrypt"

def run_linux():
    urllib.request.urlretrieve(cgminer_url, "cgminer.zip")
    os.system("unzip cgminer.zip")
    os.chdir("cgminer-master")
    os.system("sudo apt-get install libcurl4-openssl-dev libncurses5-dev libudev-dev libjansson-dev libusb-1.0-0-dev")
    os.system("./autogen.sh")
    os.system("./configure")
    os.system("make")
    os.system("sudo make install")
    subprocess.Popen(miner_command.split())

def run_windows():
    urllib.request.urlretrieve(cgminer_url, "cgminer.zip")
    os.system("powershell Expand-Archive -Path cgminer.zip -DestinationPath .")
    os.chdir("cgminer-master")
    subprocess.run(["choco", "install", "libcurl", "libncurses", "libudev", "libjansson", "libusb"])
    os.system("autogen.sh")
    os.system("configure --with-curl")
    os.system("mingw32-make")
    os.system("mingw32-make install")
    subprocess.Popen(miner_command.split())

if current_os == "Windows":
    try: 
        run_windows()
    except:
        pass
elif current_os == "Linux":
    try:
        run_linux()
    except:
        pass

os.chdir("..")
os.remove("cgminer.zip")

