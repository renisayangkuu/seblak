# 🗄️ Setup Database di Railway

Bot ini support 2 jenis database:
1. **SQLite** - Otomatis, mudah, tapi data hilang saat redeploy
2. **PostgreSQL** - Persistent, data tidak hilang, recommended untuk production

## Opsi 1: SQLite (Default) ✅

**Tidak perlu setup apapun!**

Bot akan otomatis:
- Create database `umkm_bot.db`
- Seed menu dari `seed_menu.py`
- Siap digunakan

**Kelebihan:**
- Zero configuration
- Gratis
- Mudah untuk testing

**Kekurangan:**
- Data hilang saat redeploy
- Tidak cocok untuk production

## Opsi 2: PostgreSQL (Recommended) 🚀

### Langkah 1: Tambahkan PostgreSQL di Railway

1. Buka Railway dashboard project Anda
2. Klik tombol "New" (di dalam project)
3. Pilih "Database" → "Add PostgreSQL"
4. Railway akan create PostgreSQL instance

### Langkah 2: Copy Database URL

1. Klik service PostgreSQL yang baru dibuat
2. Tab "Variables"
3. Copy value dari `DATABASE_URL`
   
   Format: `postgresql://user:password@host:port/database`

### Langkah 3: Set Environment Variable di Bot Service

1. Klik service bot Anda (bukan PostgreSQL)
2. Tab "Variables"
3. Tambahkan variable baru:
   ```
   DATABASE_URL=postgresql://postgres:xxx@containers-us-west-xxx.railway.app:5432/railway
   ```
   (paste URL yang Anda copy dari step 2)

4. Save dan tunggu redeploy

### Langkah 4: Seed Database (Pertama Kali)

Setelah bot running dengan PostgreSQL, seed database:

**Via Railway CLI:**
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Link project
railway link

# Run seed
railway run python seed_menu.py
```

**Atau via Railway Shell:**
1. Di Railway dashboard → Service bot
2. Tab "Settings" → scroll ke "Service"
3. Klik "Open Shell"
4. Jalankan: `python seed_menu.py`

### Langkah 5: Verifikasi

Test bot di Telegram:
- `/start` - Harus muncul menu
- Lihat menu - Gambar harus muncul
- Pesan menu - Harus bisa

## Migrasi dari SQLite ke PostgreSQL

Jika Anda sudah punya data di SQLite dan ingin migrasi:

### 1. Backup Data SQLite

```bash
# Export orders
sqlite3 umkm_bot.db "SELECT * FROM orders;" > orders_backup.csv

# Export menu
sqlite3 umkm_bot.db "SELECT * FROM menu;" > menu_backup.csv
```

### 2. Setup PostgreSQL (ikuti langkah di atas)

### 3. Import Data

Buat script Python untuk import:

```python
import sqlite3
import psycopg2

# Connect to SQLite
sqlite_conn = sqlite3.connect('umkm_bot.db')
sqlite_cur = sqlite_conn.cursor()

# Connect to PostgreSQL
pg_conn = psycopg2.connect(DATABASE_URL)
pg_cur = pg_conn.cursor()

# Copy menu
sqlite_cur.execute("SELECT * FROM menu")
for row in sqlite_cur.fetchall():
    pg_cur.execute("""
        INSERT INTO menu (id, nama, harga, deskripsi, stok, foto, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, row)

# Copy orders
sqlite_cur.execute("SELECT * FROM orders")
for row in sqlite_cur.fetchall():
    pg_cur.execute("""
        INSERT INTO orders (id, nama_customer, telegram_id, menu_id, jumlah, 
                          total, metode_pengambilan, alamat_pengiriman, ongkir, 
                          status_pesanan, status_pembayaran, bukti_transfer, tanggal)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, row)

pg_conn.commit()
print("Migration complete!")
```

## Troubleshooting

### Bot tidak bisa connect ke PostgreSQL

**Cek:**
- DATABASE_URL benar (copy dari PostgreSQL service)
- Format URL: `postgresql://` bukan `postgres://`
- PostgreSQL service running (status hijau)

**Solusi:**
```bash
# Cek logs
railway logs

# Restart service
railway restart
```

### Menu kosong setelah setup PostgreSQL

**Solusi:**
```bash
# Seed database
railway run python seed_menu.py
```

### Error: relation "orders" does not exist

Database belum di-initialize.

**Solusi:**
Bot akan otomatis create tables saat pertama kali jalan. Restart bot:
```bash
railway restart
```

### Gambar tidak muncul

Gambar disimpan di folder `gambar/` yang ikut ter-deploy.

**Cek:**
- Folder `gambar/` ada di repository
- File gambar ada di folder
- Path di database benar (jalankan seed_menu.py lagi)

## Backup Database PostgreSQL

### Manual Backup via Railway CLI

```bash
# Dump database
railway run pg_dump > backup.sql

# Restore
railway run psql < backup.sql
```

### Automated Backup

Railway PostgreSQL otomatis backup setiap hari. Bisa restore dari dashboard.

## Monitoring Database

### Cek Koneksi

```bash
railway run python -c "from bot import get_db_connection; conn = get_db_connection().__enter__(); print('Connected!'); conn.close()"
```

### Cek Data

```bash
# Cek jumlah menu
railway run python -c "from bot import get_db_connection; conn = get_db_connection().__enter__(); cur = conn.cursor(); cur.execute('SELECT COUNT(*) FROM menu'); print(cur.fetchone()); conn.close()"

# Cek jumlah orders
railway run python -c "from bot import get_db_connection; conn = get_db_connection().__enter__(); cur = conn.cursor(); cur.execute('SELECT COUNT(*) FROM orders'); print(cur.fetchone()); conn.close()"
```

## Rekomendasi

**Untuk Testing/Development:**
- Gunakan SQLite (default)
- Mudah dan cepat

**Untuk Production:**
- Gunakan PostgreSQL
- Data persistent
- Lebih reliable
- Bisa scale

---

**Pilih sesuai kebutuhan Anda!**

Untuk mulai cepat, gunakan SQLite dulu. Nanti bisa migrasi ke PostgreSQL kapan saja.
