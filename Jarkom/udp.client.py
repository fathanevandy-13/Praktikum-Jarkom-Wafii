from socket import *

serverName = "localhost"
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("[SYSTEM] Masukkan pesan")

while True:
    message = input("> ")

    if not message:
        continue

    clientSocket.send(message.encode())

    if message.lower() == "exit":
        print("Perintah exit dikirim. Menutup koneksi...")
        break
    elif message.lower() == "keluar":
        print("Menutup klien...")
        break

    try:
        modifiedMessage = clientSocket.recv(2048)
        print(f"[SERVER] {modifiedMessage.decode()}\n")
    except timeout:
        print("Kesalahan: Server tidak merespons (Timeout)\n")

clientSocket.close()
print("[SYSTEM] socket ditutup")