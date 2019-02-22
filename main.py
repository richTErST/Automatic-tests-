#Check is IPv4 Address is correct

import subprocess
from subprocess import PIPE, Popen

def checkIP(myIP):
    print("Test: inconfig001")
    Status_test = "FAILED"

    cmd = "ipconfig"

    process = Popen(args=cmd, stdout=PIPE, stderr=subprocess.STDOUT, shell=False)
    process.wait()

    output = process.communicate()[0].decode('iso-8859-2')
    rc = process.returncode

    output = output.splitlines()

    for line in output:
        if "IPv4 Address" in line:
            #print(line)
            line = line.split(":")[1].strip()
            #print(line)
            if line == myIP :
                Status_test = "PASS"

#checking vaulue of return code
    #print("return code", rc)

    print("Test result: ", Status_test)
    return 0

print("Check the ip compatibility with the system: ", end='')
myIP = input()
#Egzample myIP = "192.168.0.164"
checkIP(myIP)