import subprocess
import socket
import threading
import re 
patten = r"cat ([a-z.]+)|ls| -[a|l]"
# class Shell_server_log:
#     def __init__(self,conn.add):
#         print("") write a server log in feture 
class Shell_server_client_handle(threading.Thread):
    def __init__(self,conn,add):
        threading.Thread.__init__(self)
        self.conn = conn
        self.add = add
    def run(self):
        #add --help (in feture)
        self.conn.sendall("shell server ( 2024: version 0.1 reverse shell Monitor ) \nrs# --help to show user Manual \nDisclaimer : don't abuse it ( only for student system Monitoring )\nrs#:".encode())
        while True:
            try:
                data = self.conn.recv(1024)
                if not data:
                    break
                comment = data.decode().strip()
                match = re.search(patten,comment)
                if match: 
                    # if(comment =="--help" or "-h"):if feture user manual  
                    cmd = subprocess.run(comment,shell=True,capture_output=True,text=True)
                    self.conn.sendall(cmd.stdout.encode())
                    self.conn.send("rs#:".encode())
                else:
                    self.conn.sendall("[*] Invalide systax ....\nrs#:".encode())
            except:
                pass
HOST = ""
PORT = 7878
shell_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
shell_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
shell_server.bind((HOST,PORT))
shell_server.listen()
while True:
    conn, add =shell_server.accept()
    rs = Shell_server_client_handle(conn,add)
    rs.start()
shell_server.close()


    
