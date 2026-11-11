# Segi Empat dan Segitiga Itu Asyik!

Folder ini berisi materi sumber lengkap dan kode untuk membangun ulang modul PDF matematika kelas VII–VIII.

## Isi folder

- `modul-sumber.md` — naskah modul lengkap, daftar bab, dan tiga blok kode sumber.
- `build.py` — pembuat ilustrasi SVG orisinal.
- `page.html` — tata letak dan isi halaman modul.
- `render.py` — penggabung SVG dan perender PDF A4.

## Membuat PDF

Gunakan Python 3. Simpan keempat berkas (`build.py`, `page.html`, `render.py`, dan bila perlu `modul-sumber.md`) dalam direktori yang sama. Pasang salah satu mesin render yang didukung:

- Playwright + Chromium (pilihan utama), atau
- WeasyPrint, atau
- xhtml2pdf.

Kemudian jalankan:

```bash
python render.py
```

Skrip akan menghasilkan `modul.html` dan `Modul_Segi_Empat_dan_Segitiga.pdf`.

## Metadata

- ID modul: `segi-empat-segitiga`
- Mata pelajaran: Matematika
- Sasaran: kelas VII–VIII
- PDF hasil final: 18 halaman (sampul, panduan/daftar isi, dan 16 bab)
- Bahasa: Indonesia
