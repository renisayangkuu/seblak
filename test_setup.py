"""Test script to validate setup"""
import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("VALIDASI SETUP BOT UMKM")
print("=" * 50)

# Check token
token = os.getenv('TELEGRAM_BOT_TOKEN')
if token and token != 'YOUR_BOT_TOKEN_HERE':
    print("✅ Token bot: Sudah diset")
    print(f"   Token: {token[:10]}...{token[-5:]}")
else:
    print("❌ Token bot: BELUM DISET!")
    print("   Silakan edit file .env dan ganti YOUR_BOT_TOKEN_HERE")
    print("   Cara dapat token: chat @BotFather di Telegram")

# Check admin ID
admin_ids = os.getenv('ADMIN_TELEGRAM_IDS', '')
admin_password = os.getenv('ADMIN_PASSWORD', 'admin123')

print(f"✅ Admin Password: {admin_password}")
print("   (Ganti di file .env jika perlu)")

if admin_ids:
    print(f"✅ Pre-authorized Admin IDs: {admin_ids}")
    print("   (Opsional - admin bisa login dengan password)")
else:
    print("ℹ️  Pre-authorized Admin IDs: Tidak ada")
    print("   Admin akan login menggunakan password")

# Check database
try:
    import sqlite3
    conn = sqlite3.connect('umkm_bot.db')
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM menu")
    menu_count = cur.fetchone()[0]
    conn.close()
    print(f"✅ Database: OK ({menu_count} menu tersedia)")
except Exception as e:
    print(f"ℹ️  Database: Belum ada (akan dibuat otomatis saat bot jalan)")

# Check dependencies
try:
    import telegram
    print(f"✅ python-telegram-bot: v{telegram.__version__}")
except ImportError:
    print("❌ python-telegram-bot: Belum terinstall")

try:
    from reportlab.lib.pagesizes import A4
    print("✅ reportlab: Terinstall")
except ImportError:
    print("❌ reportlab: Belum terinstall")

print("=" * 50)

if token == 'YOUR_BOT_TOKEN_HERE':
    print("\n⚠️  SETUP BELUM LENGKAP!")
    print("\nLangkah selanjutnya:")
    print("1. Buka Telegram, cari @BotFather")
    print("2. Kirim /newbot dan ikuti instruksi")
    print("3. Copy token yang diberikan")
    print("4. Edit file .env, ganti YOUR_BOT_TOKEN_HERE dengan token Anda")
    print("5. (Opsional) Ganti ADMIN_PASSWORD di .env")
    print("6. Jalankan: python bot.py")
else:
    print("\n✅ SETUP LENGKAP! Bot siap dijalankan.")
    print("\nJalankan bot dengan: python bot.py")
    print(f"\nAdmin login: Kirim /loginadmin ke bot, masukkan password: {admin_password}")
