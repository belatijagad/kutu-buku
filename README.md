# Kutu Buku
## Anggota kelompok
- Alden Luthfi Arrahman
- Ammara Pranahiza Widaryati
- Belati Jagad Bintang Syuhada
- Indira Arifia Rahmah
- Rif'At Fauzan
- Thifaalinno Fawwaz Abdi

## Deskripsi aplikasi
Literasi adalah keterampilan dasar esensial bagi setiap individu di era informasi saat ini. Lebih dari sekadar kemampuan membaca dan menulis, literasi memampukan seseorang untuk memahami, menganalisa, dan menafsirkan informasi dengan kritis. Dengan keterampilan literasi yang baik, individu dapat membuat keputusan yang lebih tepat, membedakan fakta dari opini, serta menyaring informasi yang tidak relevan atau menyesatkan. Di tengah derasnya arus informasi, literasi menjadi benteng pertahanan terhadap kesesatan informasi dan memberikan fondasi untuk pembelajaran sepanjang hayat. Tanpa literasi, seseorang akan kesulitan menghadapi tantangan di dunia modern dan berpotensi terpinggirkan dalam masyarakat yang semakin dinamis. Untuk mendukung kegiatan literasi, kami membuat sebuah aplikasi katalog buku. Aplikasi ini memuat fitur untuk menambahkan buku, menampilkan berbagai jenis buku, mengulas buku, dan menandakan buku yang sudah ada untuk masuk ke dalam *to-read list*. 

## Daftar modul yang akan diimplementasikan
Berikut adalah modul-modul yang diimplementasikan serta kontribusi setiap anggota terhadap modul yang diimplementasikan.
- Halaman utama:
  - Alden Luthfi Arrahman (100%)
- Halaman autentikasi (registrasi dan *login*)
  - Ammara Pranahiza Widaryati (80%)
  - Belati Jagad Bintang Syuhada (20%)
- Halaman melihat daftar buku
  - Rif'At Fauzan (95%)
  - Alden Luthfi Arrahman (5%)
- Halaman buku individu
  - Indira Arifia Rahmah (80%)
  - Alden Luthfi Arrahman (20%)
- Halaman menambahkan buku
  - Thifaalinno Fawwaz Abdi (50%)
  - Belati Jagad Bintang Syuhada (50%)
- Bookmark buku
  - Belati Jagad Bintang Syuhada (100%)

## Sumber dataset katalog buku
Kami menggunakan sumber data dari hasil scraping, yaitu [WuxiaWorld](https://wuxiaworld.com)

## User Persona
Berikut adalah hal yang dapat dilakukan oleh jenis pengguna
### Non logged in users
- Membuka halaman utama
- Melihat daftar buku
- Membuka halaman buku individu (tidak bisa menambahkan ulasan)
### Logged in users
- Membuka halaman utama
- Melihat daftar buku
- Membuka halaman buku individu (bisa menambahkan ulasan)
- Menambahkan buku ke katalog
### Moderators
- Semua yang dapat dilakukan `Logged in users`
- Menghapus ulasan
- Menghapus buku dari katalog
- Merestriksi akses suatu user (tidak bisa menambahkan ulasan, buku)
