import multiprocessing
import socket
def start_game():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    with open("file/atile.json","r") as f:
        reg_options=f.read()
    s.connect(("80.77.36.110",2024))
    #print(text)
    s.sendall(reg_options.encode("utf-8"))
    #date=s.recv(1024)
    s.close()
def go():
    for i in range(100000):
        print(i)
t1=multiprocessing.Process(target=start_game)
t2=multiprocessing.Process(target=go)
if __name__=="__main__":
    t1.start()
    t2.start()