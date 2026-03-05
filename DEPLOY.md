# 🚀 Panduan Deploy Bot ke Railway

## Langkah 1: Persiapan

### 1.1 Buat Akun Railway
1. Kunjungi [railway.app](https://railway.app)
2. Klik "Login" atau "Start a New Project"
3. Sign up menggunakan akun GitHub Anda

### 1.2 Persiapkan Repository GitHub
1. Buat repository baru di GitHub
2. Jangan centang "Initialize with README" (karena sudah ada)

## Langkah 2: Push ke GitHub

Buka terminal di folder project dan jalankan:

```bash
# Initialize git (jika belum)
git init

# Add semua file
git add .

# Commit
git commit -m "Initial commit - Seblak Sami Bot"

# Set branch ke main
git branch -M main

# Add remote (ganti dengan URL repository Anda)
git remote add origin https://github.com/username/seblak-sami-bot.git

# Push ke GitHub
git push -u origin main
```

## Langkah 3: Deploy di Railway

### 3.1 Buat Project Baru
1. Login ke [Railway Dashboard](https://railway.app/dashboard)
2. Klik tombol "New Project"
3. Pilih "Deploy from GitHub repo"
4. Pilih repository yang baru Anda push
5. Railway akan otomatis detect Python project dan mulai build

### 3.2 Set Environment Variables

Setelah project dibuat, klik tab "Variables" dan tambahkan satu per satu:

**Required Variables:**
```
TELEGRAM_BOT_TOKEN=8465113216:AAHhGoVwDDRkYhxKjXNLcghR7x8W61wafhw
ADMIN_PASSWORD=reni1445
```

**Warung Information:**
```
WARUNG_NAME=Seblak Sami
WARUNG_ADDRESS=Jl. Contoh No. 123, Jakarta Selatan
WARUNG_DESCRIPTION=🌶️🔥 SEBLAK SAMI – Pedasnya Bikin Nagih! 🔥🌶️\n\nSeblak Sami hadir dengan rasa gurih, pedas, dan kaya rempah yang siap memanjakan lidah kamu! Dibuat fresh setiap ada pesanan, jadi selalu hangat dan nikmat saat sampai di tanganmu.\n\nKami menyediakan 3 pilihan ukuran porsi:\n🍜 Porsi Kecil – pas buat ngemil\n🍜 Porsi Sedang – bikin kenyang & puas\n🍜 Porsi Besar – cocok buat yang lapar banget atau makan rame-rame\n\n✨ Keunggulan Seblak Sami:\n🌶️ Level pedas bisa pilih sendiri\n🍢 Topping lengkap & melimpah\n🚚 Tersedia layanan antar langsung ke tempatmu\n💸 Harga ramah di kantong\n\nMau makan enak tanpa ribet keluar rumah? Tinggal pesan, tunggu sebentar, dan seblak hangat siap dinikmati!
```

**Payment Configuration:**
```
BANK_NAME=BCA
BANK_ACCOUNT=1234567890
BANK_ACCOUNT_NAME=Seblak Sami
```

**Delivery Configuration:**
```
FLAT_RATE_ONGKIR=10000
```

**Optional (untuk PostgreSQL, jika tidak diset akan pakai SQLite):**
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=umkm_bot
DB_USER=postgres
DB_PASSWORD=
```

### 3.3 Deploy
1. Setelah semua variables diset, Railway akan otomatis redeploy
2. Tunggu hingga status berubah menjadi "Active" (hijau)
3. Bot Anda sudah running 24/7!

## Langkah 4: Setup Database & Menu

### 4.1 Akses Railway Shell (Opsional)

Jika ingin menjalankan seed_menu.py di Railway:

1. Install Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```

2. Login dan link project:
   ```bash
   railway login
   railway link
   ```

3. Jalankan shell:
   ```bash
   railway run python seed_menu.py
   ```

### 4.2 Atau Manual via Bot

Alternatif: Database akan otomatis dibuat saat bot pertama kali dijalankan. Anda bisa menambahkan menu via bot atau edit database secara manual.

## Langkah 5: Monitoring

### 5.1 Cek Logs
1. Di Railway dashboard, klik tab "Deployments"
2. Klik deployment yang aktif
3. Scroll ke bawah untuk melihat logs
4. Pastikan tidak ada error

### 5.2 Test Bot
1. Buka Telegram
2. Cari bot Anda
3. Kirim `/start`
4. Test semua fitur

## Troubleshooting

### Bot tidak merespon
**Solusi:**
- Cek logs di Railway dashboard
- Pastikan TELEGRAM_BOT_TOKEN benar
- Pastikan bot tidak running di tempat lain (local)

### Database kosong / menu tidak ada
**Solusi:**
- Jalankan `railway run python seed_menu.py`
- Atau tambahkan menu manual via admin panel

### Gambar tidak muncul
**Solusi:**
- Pastikan folder `gambar/` ada di repository
- Pastikan file gambar sudah di-commit dan push
- Jalankan seed_menu.py lagi untuk update path gambar

### Bot crash terus
**Solusi:**
- Cek logs untuk error message
- Pastikan semua dependencies di requirements.txt
- Pastikan Python version compatible (3.11)

### Environment variables tidak terbaca
**Solusi:**
- Pastikan tidak ada typo di nama variable
- Redeploy setelah menambahkan variables
- Cek dengan `railway logs` apakah variables ter-load

## Update Bot

Setiap kali Anda update code:

```bash
git add .
git commit -m "Update: deskripsi perubahan"
git push
```

Railway akan otomatis detect perubahan dan redeploy!

## Backup Database

**Penting:** Railway menggunakan ephemeral storage. Database bisa hilang saat redeploy.

**Solusi:**
1. Backup database secara berkala
2. Download file `umkm_bot.db` via Railway CLI:
   ```bash
   railway run cat umkm_bot.db > backup.db
   ```
3. Atau gunakan Railway PostgreSQL untuk production

## Biaya

- Railway memberikan $5 credit gratis per bulan
- Bot Telegram biasanya menggunakan resource minimal
- Cukup untuk running 24/7 dengan traffic normal

## Support

Jika ada masalah:
1. Cek dokumentasi Railway: https://docs.railway.app
2. Cek logs di Railway dashboard
3. Join Railway Discord untuk bantuan

---

**Selamat! Bot Anda sudah running di cloud! 🎉**
