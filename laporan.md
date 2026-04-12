# Modul 6 TCP

# Menangkap Tansfer TCP dalam Jumlah Besar dari Komputer Pribadi ke Remote Server
## Langkah-langkah :

1. Buka file yg ada di Modul Jarkom (http://gaia.cs.umass.edu/wireshark-labs/alice.txt) lalu download file tersebut.

![Gambar](../assets/image/Modul6Gambar1.png)

2. lalu buka halaman (http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html), masukan file yg sudah di download

![Gambar](../assets/image/Modul6Gambar2.png)

3. Jalankan wireshark, lalu start capture dan kembali ke browser untuk upload file alice.txt. Setelah itu stop capture jika sudah selesai upload.

![Gambar](../assets/image/Modul6Gambar3.png)

4. Lalu ketik di wireshark bagian filter (tcp contains "POST"). untuk menemukan paket upload.

![Gambar](../assets/image/Modul6Gambar4.png)

## Pertanyaan

1. Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien (sumber) untuk mentransfer file ke gaia cs.umass.edu?

![Gambar](../assets/image/Modul6Gambar5.png)

Berdasarkan hasil analisis paket HTTP POST pada Wireshark, komputer klien menggunakan alamat IP 192.168.1.53 dan nomor port 58898 untuk mentransfer file ke server.

2. Apa alamat IP dari gaia.cs.umass.edu? Pada nomor port berapa ia mengirim dan menerima segmen TCP untuk koneksi ini? 

![Gambar](../assets/image/Modul6Gambar6.png)
![Gambar](../assets/image/Modul6Gambar7.png)

Server gaia.cs.umass.edu memiliki alamat IP 128.119.245.12 dan menggunakan port 80 untuk komunikasi TCP karena menggunakan protokol HTTP.

3. Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien Anda (sumber) untuk mentransfer  ke gaia.cs.umass.edu? 

![Gambar](../assets/image/Modul6Gambar8.png)

Dari hasil capture yg didapatkan pada Wireshark, alamat IP tujuan (gaia.cs.umass.edu) adalah 128.119.245.12. Hasil ini didapat dari nslookup gaia.cs.umass.edu 8.8.8.8, yang menunjukkan alamat IP yang sama. Dengan demikian, alamat IP pada Wireshark sesuai dengan hasil resolusi DNS.

# Uji Coba Dasar TCP

## Langkah-langkah :

1. Download dan extrak file http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip

2. Buka file tcp-ethereal-trace-1 dengan wireshark

![Gambar](../assets/image/Modul6Gambar9.png)

## Pertanyaan

1. Berapa nomor urut segmen TCP SYN yang digunakan untuk memulai sambungan TCP antara komputer klien dan gaia.cs.umass.edu? Apa yang dimiliki segmen tersebut sehingga teridentifikasi sebagai segmen SYN? 

![Gambar](../assets/image/Modul6Gambar10.png)

Berdasarkan hasil filter menggunakan tcp.flags.syn == 1 && tcp.flags.ack == 0, diperoleh segmen TCP SYN dengan Sequence Number sebesar 0. Segmen ini diidentifikasi sebagai SYN karena memiliki flag SYN = 1 dan ACK = 0, yang menunjukkan bahwa segmen tersebut merupakan awal dari proses pembentukan koneksi TCP (three-way handshake).

2. Berapa nomor urut segmen SYNACK yang dikirim oleh gaia.cs.umass.edu ke komputer klien sebagai balasan dari SYN? Berapa nilai dari field Acknowledgement pada segmen SYNACK? Bagaimana gaia.cs.umass.edu menentukan nilai tersebut? Apa yang dimiliki oleh segmen sehingga teridentifikasi sebagai segmen SYNACK?.

![Gambar](../assets/image/Modul6Gambar11.png)

Berdasarkan hasil filter menggunakan tcp.flags.syn == 1 && tcp.flags.ack == 1, diperoleh segmen TCP SYN-ACK dengan Sequence Number sebesar 0 dan Acknowledgement Number sebesar 1. Nilai ACK diperoleh dari Sequence Number segmen SYN sebelumnya yang bernilai 0, kemudian ditambahkan 1. Segmen ini diidentifikasi sebagai SYN-ACK karena memiliki flag SYN = 1 dan ACK = 1, yang menunjukkan bahwa server merespons permintaan koneksi dari klien dalam proses three-way handshake.

3. Berapa nomor urut segmen TCP yang berisi perintah HTTP POST?

![Gambar](../assets/image/Modul6Gambar12.png)

Berdasarkan hasil filter menggunakan tcp.port == 1161 && tcp contains "POST", diperoleh segmen TCP yang berisi perintah HTTP POST dengan Sequence Number sebesar 1. Segmen ini merupakan awal pengiriman data dari klien ke server setelah proses three-way handshake selesai.

4. Hitung RTT, waktu kirim, waktu ACK, dan Estimated RTT

![Gambar](../assets/image/Modul6Gambar13.png)

Berdasarkan hasil analisis menggunakan filter tcp.port == 1161 dan fitur Statistics → TCP Stream Graph → Round Trip Time, diperoleh bahwa nilai RTT (Round Trip Time) berkisar antara sekitar 50 ms hingga 270 ms. Nilai RTT diperoleh dari selisih waktu antara pengiriman segmen TCP oleh klien dan penerimaan acknowledgement (ACK) dari server. Variasi nilai RTT dipengaruhi oleh kondisi jaringan selama proses transmisi data.

5. Berapa panjang setiap enam segmen TCP pertama?

![Gambar](../assets/image/Modul6Gambar14.png)

Berdasarkan hasil analisis menggunakan filter tcp.port == 1161, panjang enam segmen TCP pertama diperoleh dari bagian Reassembled TCP Segments, yaitu sebesar 565 byte, 1460 byte, 1460 byte, 1460 byte, 1460 byte, dan 1460 byte. Jika dijumlahkan, total panjang keenam segmen tersebut adalah 7865 byte.

6. Berapa jumlah minimum ruang buffer tersedia yang disarankan kepada penerima dan diterima untuk seluruh trace? Apakah kurangnya ruang buffer penerima pernah menghambat pengiriman?

![Gambar](../assets/image/Modul6Gambar15.png)

Berdasarkan hasil analisis menggunakan filter tcp.port == 1161, nilai minimum ruang buffer (window size) yang diterima adalah sebesar 5840 byte. Nilai ini menunjukkan kapasitas buffer yang tersedia pada sisi penerima. Selama proses transmisi, tidak ditemukan indikasi bahwa kekurangan ruang buffer menghambat pengiriman data, karena tidak terlihat adanya penundaan atau retransmission akibat window yang penuh.

7. Apakah ada segmen yang ditransmisikan ulang dalam file trace?

![Gambar](../assets/image/Modul6Gambar16.png)

Segmen retransmission dicek menggunakan filter tcp.analysis.retransmission pada Wireshark. Berdasarkan hasil filter, tidak ditemukan adanya segmen yang ditransmisikan ulang dalam trace, sehingga dapat disimpulkan bahwa tidak terjadi retransmission selama proses komunikasi TCP.

8. Berapa banyak data yang biasanya diakui oleh penerima dalam ACK? Dapatkah anda mengidentifikasi kasus-kasus di mana penerima melakukan ACK untuk setiap segmen yang diterima?

![Gambar](../assets/image/Modul6Gambar17.png)

Berdasarkan hasil analisis menggunakan filter tcp.port == 1161 && tcp.flags.ack == 1, terlihat bahwa nilai acknowledgment number meningkat dalam jumlah besar setiap kali ACK dikirim, sehingga menunjukkan bahwa penerima mengakui beberapa segmen sekaligus. Dengan demikian, penerima tidak selalu mengirim ACK untuk setiap segmen, melainkan menggunakan cumulative ACK untuk mengakui data dalam jumlah lebih besar.

9. Berapa throughput (byte yang ditransfer per satuan waktu) untuk sambungan TCP?

![Gambar](../assets/image/Modul6Gambar18.png)

Throughput koneksi TCP diperoleh menggunakan fitur Statistics → TCP Stream Graph → Throughput pada Wireshark dengan filter tcp.port == 1161. Berdasarkan grafik yang ditampilkan, nilai throughput berada pada kisaran sekitar 200 kbps hingga 260 kbps. Nilai ini menunjukkan jumlah data yang berhasil ditransmisikan per satuan waktu selama proses komunikasi berlangsung.

# Congestion Control Pada TCP

## Langkah-langkah :

1. Identifikasi Slow Start & Congestion Avoidance (file tcp-ethereal-trace-1)
  - Buka file tcp-ethereal-trace-1 dengan wireshark lalu setelah membuka file dalam wireshark filter "TCP"
  - Klik Statistics -> TCP Stream Graph -> Time-Sequence Graph (Stevens)

![Gambar](../assets/image/Modul6Gambar19.png)

  - Di awal (0–±1 detik) grafik naik cepat, itu fase slow start. Setelah itu berubah jadi naik lebih pelan dan stabil (linear), tandanya masuk congestion avoidance. Grafiknya juga tidak terlalu stabil, kemungkinan karena delay/ACK, tapi secara keseluruhan masih stabil karena tidak ada penurunan tajam.

2. Identifikasi Slow Start & Congestion Avoidance (alice.txt)
  - Buka Wireshark lalu pilih opsi wifi dan start
  - Pada bagian ini sama seperti step yang sudah pernah di lakukan yaitu upload file "alice.txt" ke web http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html
  - Buka wireshark lalu filter "TCP"

![Gambar](../assets/image/Modul6Gambar20.png)

  - Pada grafik kedua, kenaikan sequence number di awal tidak menunjukkan pola yang signifikan dan cenderung datar dalam beberapa waktu. Setelah itu, terjadi peningkatan secara tiba-tiba, sehingga fase slow start tidak terlihat jelas seperti pada grafik sebelumnya.

Perubahan berikutnya juga tidak menunjukkan pola linear yang stabil, melainkan berupa lonjakan-lonjakan. Hal ini mengindikasikan bahwa proses pengiriman data kurang konsisten kemungkinan dipengaruhi oleh variasi delay pada jaringan Wi-Fi. Meskipun demikian, koneksi masih tergolong stabil karena tidak terdapat penurunan drastis pada sequence number yang menandakan packet loss besar atau timeout.