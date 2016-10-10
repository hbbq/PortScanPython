import socket
import threading

start = 1
end = 1024
address = "one.dev.parttrap.com"

def testPort(add, prt):
    try:
        sock = socket.socket()
        ip = socket.gethostbyname(add)
        sock.connect((ip, prt))
        print(str(prt) + " open")
    except:
        pass

thread_list = []

for port in range(start, end+1):
    thread = threading.Thread(target=testPort, args=(address, port))
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Done")