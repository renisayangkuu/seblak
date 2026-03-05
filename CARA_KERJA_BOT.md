# 📖 Cara Kerja Bot Seblak Sami

## 🎯 Gambaran Umum

Bot ini adalah sistem pemesanan makanan otomatis melalui Telegram. Customer bisa pesan, bayar, dan track pesanan. Admin bisa kelola pesanan dan generate laporan.

---

## 👥 Untuk Customer (Pembeli)

### 1. Mulai Bot
```
Customer: /start
Bot: Menampilkan sambutan + tombol menu
```

### 2. Lihat Menu
```
Customer: Klik "🍽️ Lihat Menu"
Bot: Kirim 3 gambar seblak (Kecil, Sedang, Besar)
     + Tampilkan detail harga & deskripsi
     + Tombol pilih ukuran
```

### 3. Pesan Menu
```
Customer: Klik "🛒 Ukuran Sedang - Rp 15,000"
Bot: "Berapa porsi yang ingin dipesan?"

Customer: Ketik "2"
Bot: "Bagaimana pesanan ingin diterima?"
     [🏪 Ambil Sendiri] [🚚 Dikirim]
```

### 4a. Jika Pilih PICKUP (Ambil Sendiri)
```
Customer: Klik "🏪 Ambil Sendiri"
Bot: Langsung tampilkan detail pesanan + instruksi transfer
     Total: Rp 30,000 (tanpa ongkir)
```

### 4b. Jika Pilih DELIVERY (Dikirim)
```
Customer: Klik "🚚 Dikirim"
Bot: "Silakan kirim alamat lengkap pengiriman"

Customer: Ketik alamat lengkap
Bot: Tampilkan detail pesanan + instruksi transfer
     Total: Rp 40,000 (termasuk ongkir Rp 10,000)
```

### 5. Upload Bukti Transfer
```
Bot: "💳 Silakan transfer ke: BCA 1234567890"
     [📸 Saya Sudah Bayar]

Customer: Klik "📸 Saya Sudah Bayar"
Bot: "Silakan upload foto bukti transfer"

Customer: Kirim foto bukti transfer
Bot: "✅ Bukti transfer berhasil dikirim!"
     "Pesanan sedang menunggu konfirmasi admin"
```

### 6. Cek Status Pesanan
```
Customer: /pesanan
Bot: Tampilkan daftar pesanan dengan status:
     - ⏳ Menunggu konfirmasi
     - 🔄 Sedang diproses
     - 👨‍🍳 Sedang dibuat
     - 🚚 Sedang diantar / ✅ Siap diambil
     - ✅ Selesai
```

### 7. Konfirmasi Penerimaan
```
Bot: "🚚 Pesanan sedang diantar"
     [✅ Konfirmasi Sudah Diterima]

Customer: Klik "✅ Konfirmasi Sudah Diterima"
Bot: "✅ Pesanan selesai! Terima kasih!"
```

---

## 👨‍💼 Untuk Admin (Penjual)

### 1. Login Admin
```
Admin: /loginadmin
Bot: "Masukkan password admin"

Admin: Ketik password (default: reni1445)
Bot: "✅ Login berhasil!"
```

### 2. Akses Menu Admin
```
Admin: /admin
Bot: Tampilkan menu admin:
     [📋 Pesanan Menunggu (3)]
     [📊 Generate Laporan]
```

### 3. Lihat Pesanan Baru
```
Admin: Klik "📋 Pesanan Menunggu"
Bot: Tampilkan daftar pesanan yang perlu dikonfirmasi:
     
     🆔 #7
     👤 Rere
     🍴 Seblak - Ukuran Sedang x2
     💰 Rp 40,000
     
     [📸 Lihat #7] [✅ #7] [❌ #7]
```

### 4. Lihat Bukti Transfer
```
Admin: Klik "📸 Lihat #7"
Bot: Kirim foto bukti transfer + detail pesanan
     [✅ Konfirmasi] [❌ Tolak]
```

### 5. Approve Pembayaran
```
Admin: Klik "✅ Konfirmasi"
Bot: "✅ Pembayaran pesanan #7 dikonfirmasi"
     [👨‍🍳 Sedang Dibuat]

Customer dapat notifikasi:
     "✅ Pembayaran dikonfirmasi! Status: Sedang diproses"
```

### 6. Update Status: Sedang Dibuat
```
Admin: Klik "👨‍🍳 Sedang Dibuat"
Bot: "✅ Status diupdate: Sedang Dibuat"
     [🚚 Sedang Diantar] atau [✅ Siap Diambil]

Customer dapat notifikasi:
     "👨‍🍳 Pesanan sedang dibuat oleh chef kami!"
```

### 7a. Update Status: Sedang Diantar (untuk Delivery)
```
Admin: Klik "🚚 Sedang Diantar"
Bot: "✅ Status diupdate: Sedang Diantar"

Customer dapat notifikasi:
     "🚚 Pesanan sedang dalam perjalanan!"
     [✅ Konfirmasi Sudah Diterima]
```

### 7b. Update Status: Siap Diambil (untuk Pickup)
```
Admin: Klik "✅ Siap Diambil"
Bot: "✅ Status diupdate: Siap Diambil"

Customer dapat notifikasi:
     "✅ Pesanan siap diambil di Seblak Sami!"
     [✅ Konfirmasi Sudah Diambil]
```

### 8. Generate Laporan
```
Admin: Klik "📊 Generate Laporan"
Bot: Generate PDF laporan harian
     - Total pesanan
     - Total omzet
     - Detail semua pesanan hari ini
     
     Kirim file PDF ke admin
```

---

## 🔄 Alur Lengkap (Flow Chart)

```
CUSTOMER                          BOT                           ADMIN
   |                               |                              |
   |------ /start ---------------->|                              |
   |<----- Sambutan + Menu --------|                              |
   |                               |                              |
   |------ Lihat Menu ------------>|                              |
   |<----- 3 Gambar + Pilihan -----|                              |
   |                               |                              |
   |------ Pilih Ukuran ---------->|                              |
   |<----- Minta Jumlah -----------|                              |
   |                               |                              |
   |------ Ketik "2" ------------->|                              |
   |<----- Pilih Metode -----------|                              |
   |                               |                              |
   |------ Pilih Delivery -------->|                              |
   |<----- Minta Alamat -----------|                              |
   |                               |                              |
   |------ Kirim Alamat ---------->|                              |
   |<----- Instruksi Transfer -----|                              |
   |                               |                              |
   |------ Upload Bukti ---------->|                              |
   |<----- Konfirmasi Terkirim ----|                              |
   |                               |                              |
   |                               |------ Notif Pesanan Baru --->|
   |                               |                              |
   |                               |<----- Lihat Bukti -----------|
   |                               |------ Kirim Foto Bukti ----->|
   |                               |                              |
   |                               |<----- Approve Pembayaran ----|
   |<----- Notif Dikonfirmasi -----|                              |
   |                               |                              |
   |                               |<----- Update: Sedang Dibuat -|
   |<----- Notif Sedang Dibuat ----|                              |
   |                               |                              |
   |                               |<----- Update: Sedang Diantar |
   |<----- Notif Sedang Diantar ---|                              |
   |                               |                              |
   |------ Konfirmasi Diterima --->|                              |
   |<----- Pesanan Selesai --------|                              |
   |                               |------ Notif ke Admin ------->|
```

---

## 💾 Database

Bot menyimpan data di database SQLite (`umkm_bot.db`):

### Tabel `menu`
```
- id: ID menu
- nama: Nama menu (contoh: "Seblak - Ukuran Sedang")
- harga: Harga (contoh: 15000)
- deskripsi: Deskripsi menu
- stok: Jumlah stok
- foto: Path gambar
- status: tersedia/habis
```

### Tabel `orders`
```
- id: ID pesanan
- nama_customer: Nama customer
- telegram_id: Telegram ID customer
- menu_id: ID menu yang dipesan
- jumlah: Jumlah porsi
- total: Total harga
- metode_pengambilan: pickup/delivery
- alamat_pengiriman: Alamat (jika delivery)
- ongkir: Ongkos kirim
- status_pesanan: menunggu/diproses/sedang_dibuat/sedang_diantar/siap_diambil/selesai
- status_pembayaran: menunggu/menunggu_konfirmasi/lunas/ditolak
- bukti_transfer: File ID foto bukti
- tanggal: Waktu pesanan
```

---

## 🎨 Fitur-Fitur

### ✅ Untuk Customer:
1. Lihat menu dengan gambar
2. Pesan dengan pilihan ukuran
3. Pilih pickup atau delivery
4. Input alamat (jika delivery)
5. Upload bukti transfer
6. Cek status pesanan real-time
7. Konfirmasi penerimaan pesanan
8. Notifikasi setiap perubahan status

### ✅ Untuk Admin:
1. Login dengan password
2. Lihat pesanan baru
3. Lihat bukti transfer
4. Approve/reject pembayaran
5. Update status pesanan (sedang dibuat, sedang diantar, siap diambil)
6. Generate laporan harian PDF
7. Notifikasi pesanan baru
8. Notifikasi konfirmasi penerimaan

---

## 🚀 Teknologi

- **Python** - Bahasa pemrograman
- **python-telegram-bot** - Library untuk Telegram Bot API
- **SQLite/PostgreSQL** - Database
- **ReportLab** - Generate PDF laporan
- **Railway** - Hosting (cloud platform)

---

## 📱 Command Bot

### Customer:
- `/start` - Mulai bot
- `/pesanan` - Cek status pesanan

### Admin:
- `/loginadmin` - Login admin
- `/admin` - Menu admin

---

## 🔐 Keamanan

1. **Admin Password** - Hanya admin yang bisa approve pesanan
2. **Telegram ID** - Setiap user punya ID unik
3. **Environment Variables** - Token & password disimpan aman
4. **Validation** - Input user divalidasi

---

## 💡 Tips Penggunaan

### Untuk Customer:
- Pastikan foto bukti transfer jelas
- Cek status pesanan dengan `/pesanan`
- Konfirmasi penerimaan setelah pesanan sampai

### Untuk Admin:
- Cek pesanan baru secara berkala
- Update status pesanan tepat waktu
- Generate laporan setiap akhir hari
- Backup database secara berkala

---

**Bot ini berjalan 24/7 di Railway dan siap melayani customer kapan saja!** 🎉
