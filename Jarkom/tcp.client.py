# SOCKET = Penjumlahan, pembagian, pengurangan, perkalian
from socket import * # import all

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

# AF_INET = ipv4 | SOCK_STREAM = TCP
clientSocket.connect(
    (serverName, serverPort)
)

print("[SYSTEM] Masukan pesan")

running = True
while running:
    
    # input 
    message = input("> ")

    # mengirim ke server
    # encode = abcdef = 101010101010101010101011
    clientSocket.send(message.encode())

    # kalo exit = spocket ditutup
    if message == "exit":
        print("[SYSTEM] keluar dari program")
        running = False
        break

    # menerima pesan dari server
    # abc = 101010101011
    modifiedMessage = clientSocket.recv(2048)

    print("[SERVER] pesan : ", modifiedMessage.decode())

# menutup socket yg tidak dipakai
clientSocket.close()
print("[SYSTEM] socket ditutup")