import socket
import threading

start = 1
end = 1024
address = "www.google.com"

def testPort(ip, port):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
        print(str(port) + " open")
    except:
        pass

ip = socket.gethostbyname(address)

thread_list = []

for port in range(start, end+1):
    thread = threading.Thread(target=testPort, args=(ip, port))
    thread_list.append(thread)
    thread.start()

for thread in thread_list:
    thread.join()

print("Done")
