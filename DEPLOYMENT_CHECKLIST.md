# ✅ Checklist Deployment Railway

## Sebelum Deploy

- [ ] Pastikan bot sudah ditest di local dan berfungsi dengan baik
- [ ] Pastikan semua gambar produk ada di folder `gambar/`
- [ ] Pastikan file `.env` sudah dikonfigurasi dengan benar
- [ ] Pastikan `requirements.txt` sudah lengkap
- [ ] Backup database lokal (jika ada data penting)

## Setup GitHub

- [ ] Buat repository baru di GitHub
- [ ] Initialize git di folder project (`git init`)
- [ ] Add semua file (`git add .`)
- [ ] Commit (`git commit -m "Initial commit"`)
- [ ] Add remote repository
- [ ] Push ke GitHub (`git push -u origin main`)

## Setup Railway

- [ ] Buat akun Railway dengan GitHub
- [ ] Buat project baru di Railway
- [ ] Connect dengan GitHub repository
- [ ] Tunggu build selesai

## Environment Variables

Copy semua variables dari `.env` ke Railway:

- [ ] `TELEGRAM_BOT_TOKEN`
- [ ] `ADMIN_PASSWORD`
- [ ] `WARUNG_NAME`
- [ ] `WARUNG_ADDRESS`
- [ ] `WARUNG_DESCRIPTION`
- [ ] `BANK_NAME`
- [ ] `BANK_ACCOUNT`
- [ ] `BANK_ACCOUNT_NAME`
- [ ] `FLAT_RATE_ONGKIR`

## Testing

- [ ] Cek logs di Railway dashboard (tidak ada error)
- [ ] Test `/start` command di Telegram
- [ ] Test lihat menu (gambar muncul)
- [ ] Test pesan menu
- [ ] Test upload bukti transfer
- [ ] Test login admin (`/loginadmin`)
- [ ] Test approve payment
- [ ] Test update status pesanan
- [ ] Test konfirmasi penerimaan
- [ ] Test generate laporan

## Post-Deployment

- [ ] Setup monitoring/alerts (opsional)
- [ ] Dokumentasikan URL Railway project
- [ ] Backup database secara berkala
- [ ] Update dokumentasi jika ada perubahan

## Maintenance

- [ ] Cek logs secara berkala
- [ ] Monitor penggunaan resource di Railway
- [ ] Backup database setiap minggu
- [ ] Update dependencies jika ada security patch

---

**Catatan:**
- Railway memberikan $5 credit gratis per bulan
- Bot akan restart otomatis jika crash
- Database SQLite akan hilang jika redeploy (gunakan PostgreSQL untuk production)
