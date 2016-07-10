import subprocess
from time import sleep
def stemp(val):
    subprocess.Popen(['mpg123','tempact.mp3'])
    sleep(3)
    if(val == 15):
        subprocess.Popen(['mpg123','15c.mp3'])
    elif(val == 20):
        subprocess.Popen(['mpg123','20c.mp3'])
    elif(val == 26):
        subprocess.Popen(['mpg123','26c.mp3'])
    elif(val == 27):
        subprocess.Popen(['mpg123','27c.mp3'])
    elif(val == 28):
        subprocess.Popen(['mpg123','28c.mp3'])
    elif(val == 29):
        subprocess.Popen(['mpg123','29c.mp3'])
    elif(val == 30):
        subprocess.Popen(['mpg123','30c.mp3'])
    elif(val == 31):
        subprocess.Popen(['mpg123','31c.mp3'])
    elif(val == 32):
        subprocess.Popen(['mpg123','32c.mp3'])
    elif(val == 33):
        subprocess.Popen(['mpg123','33c.mp3'])
    elif(val == 34):
        subprocess.Popen(['mpg123','34c.mp3'])
    elif(val == 35):
        subprocess.Popen(['mpg123','35c.mp3'])
    elif(val == 40):
        subprocess.Popen(['mpg123','40c.mp3'])
    
                          
