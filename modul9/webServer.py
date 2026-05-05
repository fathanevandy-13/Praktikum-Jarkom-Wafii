from socket import *

# mengimpor modul sys untuk menghentikan program
import sys  # In order to terminate the program

# membuat socket server menggunakan IPv4 dan protokol TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# menentukan port server
serverPort = 6789

# menghubungkan socket ke port yang digunakan
serverSocket.bind(('', serverPort))

# server siap menerima 1 koneksi client dalam antrian
serverSocket.listen(1)

# perulangan agar server terus berjalan
while True:

    # Establish the connection
    # menampilkan status server siap menerima koneksi
    print("Ready to serve...")

    # menerima koneksi dari client beserta alamatnya
    connectionSocket, addr = serverSocket.accept()

    try:
        # menerima request dari browser/client maksimal 1024 byte
        message = connectionSocket.recv(1024).decode()

        # mengambil nama file dari request HTTP
        filename = message.split()[1]

        # membuka file yang diminta client
        f = open(filename[1:])

        # membaca isi file
        outputdata = f.read()

        # menutup file setelah dibaca
        f.close()

        # Send one HTTP header line into socket
        # mengirim header HTTP jika file berhasil ditemukan
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the client
        # mengirim isi file ke browser per karakter
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        # mengirim baris akhir respon
        connectionSocket.send("\r\n".encode())

        # menutup koneksi client
        connectionSocket.close()

    except IOError:

        # Send response message for file not found
        # mengirim header HTTP jika file tidak ditemukan
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())

        # mengirim halaman error 404 ke browser
        connectionSocket.send(
            "<html><body><h1>404 Not Found</h1></body></html>".encode()
        )

        # Close client socket
        # menutup koneksi client
        connectionSocket.close()

# menutup socket server
serverSocket.close()

# menghentikan program
sys.exit()