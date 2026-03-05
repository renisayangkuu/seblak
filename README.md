# 🍜 Bot UMKM Seblak Sami

Bot Telegram untuk UMKM makanan dengan fitur pemesanan, pembayaran, dan laporan harian.

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python bot.py
```

Database dan menu sample otomatis dibuat!

## ✨ Fitur

### Customer:
- Lihat menu lengkap dalam 1 chat (populer di atas)
- Pemesanan dengan pilihan pickup/delivery
- Upload bukti transfer
- Cek status pesanan dan riwayat pembelian
- Notifikasi status pesanan

### Admin:
- Login dengan password
- Konfirmasi/tolak pembayaran
- Lihat bukti transfer
- Generate laporan harian PDF

## 📋 Command Bot

### Customer:
- `/start` - Mulai bot dan lihat menu
- `/pesanan` - Cek status pesanan Anda

### Admin:
- `/loginadmin` - Login admin (password default: admin123)
- `/admin` - Menu admin (setelah login)

## ⚙️ Konfigurasi (.env)

```env
# Bot Token
TELEGRAM_BOT_TOKEN=your_bot_token_here

# Admin
ADMIN_PASSWORD=admin123

# Informasi Warung
WARUNG_NAME=Seblak Sami
WARUNG_ADDRESS=Jl. Contoh No. 123, Jakarta Selatan
WARUNG_DESCRIPTION=🌶️🔥 SEBLAK SAMI – Pedasnya Bikin Nagih! 🔥🌶️\n\nSeblak Sami hadir dengan rasa gurih, pedas, dan kaya rempah yang siap memanjakan lidah kamu! Dibuat fresh setiap ada pesanan, jadi selalu hangat dan nikmat saat sampai di tanganmu.\n\nKami menyediakan 3 pilihan ukuran porsi:\n🍜 Porsi Kecil – pas buat ngemil\n🍜 Porsi Sedang – bikin kenyang & puas\n🍜 Porsi Besar – cocok buat yang lapar banget atau makan rame-rame\n\n✨ Keunggulan Seblak Sami:\n🌶️ Level pedas bisa pilih sendiri\n🍢 Topping lengkap & melimpah\n🚚 Tersedia layanan antar langsung ke tempatmu\n💸 Harga ramah di kantong\n\nMau makan enak tanpa ribet keluar rumah? Tinggal pesan, tunggu sebentar, dan seblak hangat siap dinikmati!

# Pembayaran
BANK_NAME=BCA
BANK_ACCOUNT=1234567890
BANK_ACCOUNT_NAME=Seblak Sami

# Ongkir
FLAT_RATE_ONGKIR=10000
```

Sesuaikan nilai-nilai di atas dengan informasi warung Anda.

## 📖 Dokumentasi Lengkap

Lihat `PANDUAN_LENGKAP.md` untuk dokumentasi detail.

## 📁 Struktur File

```
├── bot.py              # Main bot (all-in-one)
├── seed_menu.py        # Sample menu data
├── test_setup.py       # Setup validator
├── .env                # Configuration
├── requirements.txt    # Dependencies
├── gambar/             # Folder gambar produk
└── umkm_bot.db         # SQLite database (auto-created)
```

## 🖼️ Cara Mengganti Gambar Produk

### Langkah 1: Siapkan Gambar
- Siapkan 3 gambar produk seblak Anda
- Format yang didukung: `.jpg`, `.png`, `.jpeg`, `.avif`, `.webp`
- Rekomendasi: gunakan format `.jpg` atau `.png` untuk kompatibilitas terbaik
- Ukuran maksimal: 5MB per gambar
- Resolusi yang disarankan: 800x600 atau 1024x768 pixels

### Langkah 2: Masukkan ke Folder
1. Buka folder: `gambar/`
2. Hapus atau pindahkan gambar lama
3. Copy 3 gambar baru Anda ke folder `gambar`
4. Beri nama yang jelas dan berurutan (alfabetis), contoh:
   - `1-seblak-kecil.jpg`
   - `2-seblak-sedang.jpg`
   - `3-seblak-besar.jpg`

### Langkah 3: Update Database
Jalankan perintah ini di terminal:

```bash
python seed_menu.py
```

Script akan otomatis:
- Mendeteksi gambar di folder `gambar`
- Mengurutkan berdasarkan nama file (alfabetis)
- Mengassign gambar ke 3 ukuran menu (Kecil, Sedang, Besar)

### Langkah 4: Restart Bot
1. Stop bot yang sedang berjalan (Ctrl+C)
2. Jalankan ulang bot:

```bash
python bot.py
```

Selesai! Gambar baru akan muncul saat customer klik "🍽️ Lihat Menu"

## 💡 Tips

- Ganti password default di `.env` untuk keamanan
- Gunakan `/admin` untuk akses cepat menu admin
- Customer bisa cek pesanan dengan `/pesanan`
- Generate laporan setiap akhir hari
- Backup file `umkm_bot.db` secara berkala

## 🚀 Deploy ke Railway

### Persiapan

1. **Buat akun Railway**
   - Kunjungi [railway.app](https://railway.app)
   - Sign up dengan GitHub

2. **Install Railway CLI (opsional)**
   ```bash
   npm install -g @railway/cli
   ```

### Deploy via GitHub

1. **Push project ke GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/username/repo-name.git
   git push -u origin main
   ```

2. **Deploy di Railway**
   - Login ke Railway dashboard
   - Klik "New Project"
   - Pilih "Deploy from GitHub repo"
   - Pilih repository Anda
   - Railway akan otomatis detect dan deploy

3. **Set Environment Variables**
   
   Di Railway dashboard, masuk ke tab "Variables" dan tambahkan:
   
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ADMIN_PASSWORD=your_secure_password
   WARUNG_NAME=Seblak Sami
   WARUNG_ADDRESS=Jl. Contoh No. 123, Jakarta Selatan
   WARUNG_DESCRIPTION=Deskripsi warung Anda...
   BANK_NAME=BCA
   BANK_ACCOUNT=1234567890
   BANK_ACCOUNT_NAME=Seblak Sami
   FLAT_RATE_ONGKIR=10000
   ```

4. **Deploy ulang**
   - Railway akan otomatis redeploy setelah environment variables ditambahkan
   - Bot akan running 24/7 di Railway

### Deploy via Railway CLI

```bash
# Login
railway login

# Link project
railway link

# Deploy
railway up

# Set environment variables
railway variables set TELEGRAM_BOT_TOKEN=your_token_here
railway variables set ADMIN_PASSWORD=your_password
# ... set semua variables lainnya

# Check logs
railway logs
```

### Catatan Penting

- Database SQLite akan tersimpan di Railway volume
- Gambar produk di folder `gambar/` akan ikut ter-deploy
- Bot akan restart otomatis jika crash
- Cek logs di Railway dashboard untuk monitoring

### Troubleshooting

**Bot tidak merespon:**
- Cek logs di Railway dashboard
- Pastikan semua environment variables sudah diset
- Pastikan bot token valid

**Database hilang setelah redeploy:**
- Railway menggunakan ephemeral storage untuk SQLite
- Database akan reset setiap redeploy
- Untuk data persistent, backup database secara berkala
- Atau gunakan Railway Volume untuk persistent storage

**Gambar tidak muncul:**
- Pastikan folder `gambar/` ada di repository
- Pastikan path gambar di database benar
- Jalankan `python seed_menu.py` setelah deploy pertama kali
