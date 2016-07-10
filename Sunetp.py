import subprocess
from time import sleep
def spres(val):
    subprocess.Popen(['mpg123','presact.mp3'])
    sleep(3)
    if(val == 990):
        subprocess.Popen(['mpg123','990p.mp3'])
    elif(val == 991):
        subprocess.Popen(['mpg123','991p.mp3'])
    elif(val == 992):
        subprocess.Popen(['mpg123','992p.mp3'])
    elif(val == 993):
        subprocess.Popen(['mpg123','993p.mp3'])
    elif(val == 994):
        subprocess.Popen(['mpg123','994p.mp3'])
    elif(val == 995):
        subprocess.Popen(['mpg123','995p.mp3'])
    elif(val == 996):
        subprocess.Popen(['mpg123','996p.mp3'])
    elif(val == 997):
        subprocess.Popen(['mpg123','997p.mp3'])
    elif(val == 998):
        subprocess.Popen(['mpg123','998p.mp3'])
    elif(val == 999):
        subprocess.Popen(['mpg123','999p.mp3'])
    elif(val == 1000):
        subprocess.Popen(['mpg123','1000p.mp3'])
    
                          
