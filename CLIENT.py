import socket
IP_ADDRESS="localhost"
PORT_NUMBER=7898
ADDRESS=(IP_ADDRESS,PORT_NUMBER)
FORMAT="utf-8"
SIZE=1024
def main():
 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 client.connect(ADDRESS)
 connected=True
 while connected:
 data = client.recv(SIZE).decode(FORMAT)
 command,msg=data.split("@")
 if command == "DISCONNECTED":
 print(f"[SERVER]: {msg}")
 break
 elif command == "OK":
 print(f"{msg}")
 data = input(">ENTER COMMAND: ")
 data = data.split(" ")
 command = data[0]
 if command == "HELP":
 client.send(command.encode(FORMAT))
 elif command == "LOGOUT":
 client.send(command.encode(FORMAT))
 break
 elif command == "LIST":
 client.send(command.encode(FORMAT))
 elif command == "DELETE":
 client.send(f"{command}@{data[1]}".encode(FORMAT))
 elif command == "UPLOAD":
 path = data[1]
 try:
 with open(f"{path}","r") as f:
 text = f.read()
 filename = path.split("/")[-1]
 send_data = f"{command}@{filename}@{text}"
 client.send(send_data.encode(FORMAT))
 except FileNotFoundError:
 
 print("SUCH FILE DOESNT EXIST" )
 else:
 print("Enter Suitable Command")
 print("Disconnected from the server.")
 client.close()
if __name__ == "__main__":
 main()
