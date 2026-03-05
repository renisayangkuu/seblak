# 📤 Cara Push ke GitHub

## Masalah: Permission Denied

Anda mendapat error 403 karena Git menggunakan credential yang salah.

## Solusi 1: Menggunakan Personal Access Token (Recommended)

### Langkah 1: Buat Personal Access Token

1. Login ke GitHub (https://github.com)
2. Klik foto profil (kanan atas) → Settings
3. Scroll ke bawah → Developer settings (paling bawah)
4. Personal access tokens → Tokens (classic)
5. Klik "Generate new token" → "Generate new token (classic)"
6. Beri nama: "Seblak Bot Deploy"
7. Pilih expiration: "No expiration" atau "90 days"
8. Centang scope: **repo** (semua)
9. Klik "Generate token"
10. **COPY TOKEN** (hanya muncul sekali!)

### Langkah 2: Push dengan Token

```bash
# Remove remote yang salah
git remote remove origin

# Add remote dengan format: https://TOKEN@github.com/username/repo.git
git remote add origin https://YOUR_TOKEN_HERE@github.com/renisayangkuu/seblak.git

# Push
git push -u origin main
```

**Ganti `YOUR_TOKEN_HERE` dengan token yang Anda copy!**

## Solusi 2: Menggunakan GitHub Desktop (Paling Mudah)

1. Download GitHub Desktop: https://desktop.github.com
2. Install dan login dengan akun GitHub Anda
3. File → Add Local Repository
4. Pilih folder: `C:\Users\kxkl_\Downloads\proyek`
5. Klik "Publish repository"
6. Pilih repository: renisayangkuu/seblak
7. Klik "Push origin"

## Solusi 3: Menggunakan SSH Key

### Setup SSH Key:

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy public key
cat ~/.ssh/id_ed25519.pub
```

### Add SSH Key ke GitHub:

1. Login ke GitHub
2. Settings → SSH and GPG keys
3. New SSH key
4. Paste public key
5. Save

### Push dengan SSH:

```bash
# Remove remote
git remote remove origin

# Add SSH remote
git remote add origin git@github.com:renisayangkuu/seblak.git

# Push
git push -u origin main
```

## Solusi 4: Login Ulang Git Credential

```bash
# Clear credential
git credential-manager-core erase

# Push (akan minta login)
git push -u origin main
```

Saat muncul login window:
- Username: renisayangkuu
- Password: **GUNAKAN TOKEN** (bukan password GitHub)

## Verifikasi Setelah Push Berhasil

1. Buka https://github.com/renisayangkuu/seblak
2. Pastikan semua file sudah ada
3. Cek folder `gambar/` ada gambar produk
4. Cek file `bot.py`, `requirements.txt`, dll

## Langkah Selanjutnya: Deploy ke Railway

Setelah berhasil push ke GitHub:

1. Login ke https://railway.app
2. New Project → Deploy from GitHub repo
3. Pilih repository: renisayangkuu/seblak
4. Set environment variables (lihat DEPLOY.md)
5. Bot akan otomatis running!

---

**Pilih salah satu solusi di atas yang paling mudah untuk Anda!**

Saya rekomendasikan **Solusi 2 (GitHub Desktop)** karena paling mudah dan tidak perlu setup token/SSH.
