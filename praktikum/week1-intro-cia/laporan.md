# Laporan Praktikum Kriptografi
Minggu ke-: 1
Topik: CIA_intro
Nama: Dimas Aditya Nugroho
NIM: 230202744 
Kelas: 5 IKRB

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menjelaskan **sejarah dan evolusi kriptografi** dari masa klasik hingga modern.  
2. Menyebutkan **prinsip Confidentiality, Integrity, Availability (CIA)** dengan benar.  
3. Menyimpulkan **peran kriptografi** dalam sistem keamanan informasi modern.  
4. Menyiapkan repositori GitHub sebagai media kerja praktikum.  

---
## 2. Ringkasan Sejarah Kriptografi
1. Era Kriptografi Klasik
Pada era klasik, teknik enkripsi sederhana digunakan untuk menjaga rahasia pesan. Contohnya, Caesar Cipher yang menggantikan setiap huruf dengan huruf lain pada posisi tertentu dalam alfabet, dan Vigenere Cipher yang menggunakan kunci berupa kata untuk menggeser huruf secara bergantian. Meskipun cukup efektif pada masanya, metode ini rentan terhadap analisis frekuensi dan teknik kriptoanalisis sederhana.
2. Kriptografi Modern
Perkembangan teknologi digital mendorong munculnya kriptografi modern yang berbasis matematis dan algoritma komputer. Algoritma simetris seperti AES (Advanced Encryption Standard) memungkinkan enkripsi data yang cepat dan aman dengan satu kunci rahasia. Sementara itu, algoritma asimetris seperti RSA menggunakan pasangan kunci publik dan privat, memungkinkan komunikasi aman tanpa pertukaran kunci secara langsung. Era ini menekankan keamanan berbasis kompleksitas matematika dan kekuatan komputasi.
3. Kriptografi Kontemporer
Di era kontemporer, kriptografi tidak hanya melindungi komunikasi, tetapi juga mendukung sistem terdesentralisasi. Teknologi seperti blockchain menggunakan kriptografi untuk memverifikasi transaksi secara transparan dan aman. Cryptocurrency memanfaatkan prinsip ini untuk membangun jaringan keuangan digital yang tidak bergantung pada otoritas pusat. Selain itu, konsep smart contract dan tokenisasi menunjukkan bagaimana kriptografi modern dapat memperluas fungsi keamanan ke berbagai aplikasi digital.
---

## 3. Prinsip CIA
1. Confidentiality (Kerahasiaan)
Confidentiality memastikan bahwa informasi hanya bisa diakses oleh pihak yang berwenang. Tujuannya mencegah pihak yang tidak berhak membaca atau menggunakan data.
Contoh:
a.Password dan autentikasi dua faktor (2FA) pada akun email atau media sosial.
b.Enkripsi pesan di aplikasi Telegram atau WhatsApp, sehingga hanya penerima yang bisa membaca isi pesan.
c.Akses berbasis peran (Role-Based Access Control) di sistem perusahaan, agar karyawan hanya bisa melihat data sesuai jabatan.
2. Integrity (Integritas)
Integrity menjaga agar informasi tetap akurat dan tidak berubah tanpa izin. Hal ini penting agar data dapat dipercaya.
Contoh:
a.Checksum atau hash file untuk memastikan file yang diunduh tidak rusak atau diubah.
b.Tanda tangan digital pada dokumen resmi, seperti kontrak elektronik.
c.Version control (misalnya Git) untuk melacak perubahan kode program, sehingga setiap perubahan tercatat dan bisa diverifikasi.
3. Availability (Ketersediaan)
Availability menjamin informasi dan sistem bisa diakses saat dibutuhkan. Tanpa aspek ini, data yang aman dan akurat menjadi tidak berguna.
Contoh:
a. Backup rutin dan cloud storage, sehingga data bisa dipulihkan jika terjadi kerusakan.
b. Server dengan redundansi dan load balancing, agar layanan tetap berjalan meski ada gangguan.
c. Perlindungan dari serangan DoS/DDoS, agar website atau aplikasi tetap bisa diakses oleh pengguna sah.
Hubungan ketiganya:
Ketiganya saling terkait: menjaga kerahasiaan tanpa integritas membuat data tidak dapat dipercaya; menjaga integritas tanpa availability membuat data tidak bisa digunakan; sementara availability tanpa confidentiality dapat menyebabkan kebocoran informasi. Semua elemen harus diterapkan secara seimbang untuk keamanan informasi yang efektif.
## 4. Dokumentasi
Ringkasan materi = laporan.md
![Setup GitHub](screenshots/github.png)
![comit GitHub](screenshots/comit.png)
## 5. Quiz
1. Tokoh yang dianggap sebagai bapak kriptografi modern
Whitfield Diffie dan Martin Hellman sering disebut sebagai bapak kriptografi modern karena mereka memperkenalkan konsep kriptografi kunci publik pada tahun 1976. Kontribusi mereka membuka jalan bagi metode enkripsi yang lebih aman dan fleksibel dibandingkan kriptografi klasik.
2. Algoritma kunci publik populer saat ini
Beberapa algoritma kunci publik yang banyak digunakan meliputi:
RSA (Rivest Shamir Adleman) digunakan untuk enkripsi dan tanda tangan digital.
ECC (Elliptic Curve Cryptography) enkripsi yang lebih efisien dengan ukuran kunci lebih kecil.
Diffie Hellman (DH) digunakan untuk pertukaran kunci secara aman.
DSA (Digital Signature Algorithm) digunakan untuk tanda tangan digital.
3. Perbedaan utama antara kriptografi klasik dan modern terletak pada cara pengelolaan kunci dan tingkat keamanannya. Kriptografi klasik umumnya menggunakan satu kunci yang sama untuk enkripsi dan dekripsi, sehingga lebih mudah dipecahkan melalui analisis frekuensi atau metode manual. Sementara itu, kriptografi modern menggunakan sistem kunci publik dan privat, sehingga kunci yang digunakan untuk mengenkripsi berbeda dengan kunci untuk mendekripsi. Keamanan kriptografi modern juga jauh lebih tinggi karena bergantung pada perhitungan matematis yang kompleks, seperti faktorisasi bilangan besar atau logaritma diskret. Contoh kriptografi klasik antara lain Caesar cipher dan Vigenère cipher, sedangkan contoh modern termasuk RSA, ECC, dan AES.