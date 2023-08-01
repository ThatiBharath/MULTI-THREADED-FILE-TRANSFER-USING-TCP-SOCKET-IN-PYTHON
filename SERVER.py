import os
import socket
import threading
IP_ADDRESS ="localhost"
PORT_NUMBER =7898
ADDRESS = (IP_ADDRESS, PORT_NUMBER)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"
def handle_client(conn, addr):
 print(f"NEW CONNECTION of :{addr}connected.")
 conn.send("OK@WELCOME TO THE SERVER FILE.....".encode(FORMAT))
 connected=True
 while connected:
 data = conn.recv(SIZE).decode(FORMAT)
 data = data.split("@")
 command = data[0]
 if command == "LIST":
 files = os.listdir(SERVER_DATA_PATH)
 send_data ="OK@"
 if len(files) == 0:
 send_data += "The server_data folder is empty!"
 else:
 send_data += "\n".join(f for f in files)
 conn.send(send_data.encode(FORMAT))
9
 
 elif command == "UPLOAD":
 name, text = data[1], data[2]
 filepath=os.path.join(SERVER_DATA_PATH, name)
 with open(filepath, "w") as f:
 f.write(text)
 send_data = "OK@YOUR FILE uploaded successfully."
 conn.send(send_data.encode(FORMAT))
 elif command == "DELETE":
 files = os.listdir(SERVER_DATA_PATH)
 send_data = "OK@"
 filename = data[1]
 if len(files) == 0:
 send_data += "The server_data floder is empty!"
 else:
 if filename in files:
 os.system(f"rm {SERVER_DATA_PATH}/{filename}")
 send_data += "FILE deleted successfully from the server_data."
 else:
 send_data += "File does not found in the server_data folder."
 conn.send(send_data.encode(FORMAT))
 elif command == "LOGOUT":
 break
 elif command == "HELP":
 data = "OK@"
 data += "LIST: List all the files that are present in server_data folder.\n"
 data += "UPLOAD <path>: Upload a file to the server_data folder.\n"
 data += "DELETE <filename>: Delete a file from the server_data folder.\n"
 data += "LOGOUT: Disconnect from the server.\n"
 data += "HELP: List all the commands."
 conn.send(data.encode(FORMAT))
 
 print(f"DISCONNECTED... {addr} disconnected from client")
10
 conn.close()
def main():
 print("SERVER IS READY TO CONNECT WITH THE CLIENTS...")
 server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
 try:
 if(server.bind(ADDRESS)!=-1):
 server.listen()
 print(f"Server is listening on {IP_ADDRESS} : {PORT_NUMBER}.")
 except OSError:
 print("OOPS! CHECK THE IP_ADDRESS OR PORT_NUMBER YOU HAVE ENTERED !")
 
 try:
 while True:
 conn, addr = server.accept()
 thread = threading.Thread(target=handle_client, args=(conn, addr))
 thread.start()
 print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
 except OSError:
 print("CONNECTION IS REJECTED FOR NOW...")
if __name__ == "__main__":
 main()