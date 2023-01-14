import subprocess
from multiprocessing import Process
import sys
print("python3 ama-url.py filename grepurls)
os.popen("shodan download --limit -1 "+str(sys.argv[1])+"mem.json.gz 'port:11211 org:\"Amazon\"'").read()
ips = os.popen("shodan parse --fields ip_str "+str(sys.argv[1])+"mem.json.gz").read()
def task(i):
    ip = ips.splitlines()
    this = subprocess.Popen('gau '+ip[i]+' | grep '+str(sys.argv[2])), stdout=subprocess.PIPE, shell=True).communicate()
    if this:
        with open(ip[i].strip()+".txt", 'w') as filed:
            print(this, file=filed)
            filed.close()
    else:
        print("ip : "+ip[i]+" is empty ", end="\r")

if __name__ == '__main__':
    processes=[Process(target=task, args=(n,)) for n in range(len(ips.splitlines()))]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
        
