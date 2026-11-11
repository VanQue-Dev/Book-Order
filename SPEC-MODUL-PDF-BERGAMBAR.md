# SPEC: Pembuatan Modul PDF Bergambar learv.online

> **File ini adalah instruksi kerja, bukan bahan bacaan.**
> Jika kamu (asisten AI) membaca file ini dari Google Drive sebagai bagian dari tugas terjadwal,
> kerjakan seluruh langkah di Bagian 3 secara berurutan, patuhi semua aturan di Bagian 2,
> dan jangan menyelesaikan tugas sebelum seluruh checklist di Bagian 9 terpenuhi.
> Bahasa modul dan bahasa balasan: **Bahasa Indonesia** (santai tapi baku).

Versi spec: 1.0 · Disusun 11 November 2026 · Pemilik: project WebLearv (learv.online)

---

## 1. Tujuan dan konteks

learv.online adalah situs materi sekolah. Setiap materi dibuat dulu sebagai **modul PDF bergambar**
(satu bab satu halaman, penuh ilustrasi SVG orisinal), lalu nanti diubah menjadi buku interaktif di situs.

Peran kamu saat menjalankan tugas ini: **desainer sekaligus guru**.
Tugasnya mengubah materi sekolah yang kaku menjadi modul yang mudah dipahami siswa SMP/SMA Indonesia.
Isi materi tidak boleh dipangkas — tugas ini memperjelas, bukan meringkas.

**Satu kali jalan = satu modul baru.** Jangan membuat dua modul dalam satu sesi.

### Berkas yang kamu pakai dan hasilkan (di Google Drive)

| Berkas | Peran |
|---|---|
| `SPEC-MODUL-PDF-BERGAMBAR.md` | file ini, dibaca setiap kali tugas berjalan |
| `progres-materi-bergambar.md` | catatan progres: modul yang sudah dibuat, antrean, arahan pengguna. **Dibaca di awal, ditulis ulang di akhir.** |
| `modul-sumber/<id>.md` | sumber kode satu modul (build.py + page.html + render.py di dalam blok kode) |
| `Modul_<Nama>.pdf` | hasil akhir yang dibaca pengguna |

---

## 2. Aturan mutlak (melanggar satu saja = modul ditolak)

1. **Satu bab = satu halaman PDF.** Kalau tidak muat, ringkas kalimatnya, jangan buang isinya.
2. **Setiap bab dibuka dengan analogi kehidupan sehari-hari Indonesia** (jajan di kantin, ojek online, uang jajan, tabungan, martabak, grup WA, rel kereta, jam dinding, kue). Analogi harus **menjelaskan**, bukan tempelan.
3. **Angka dalam analogi harus cocok dengan rumusnya.** Contoh: tarif ojek 3.000/km + 5.000 = 20.000 → 3x + 5 = 20 → x = 5.
4. **Semua ilustrasi digambar sendiri dengan SVG inline.** Dilarang mengambil gambar dari web, dilarang memakai karakter, maskot, atau merek milik orang lain.
5. **Setiap contoh dan kunci jawaban wajib dihitung ulang** sebelum ditulis. Sertakan baris "Cek:" pada contoh yang bisa dicek.
6. **Gambar harus akurat secara matematis.** Sudut 60° di gambar harus benar-benar 60°; titik pada grafik harus benar-benar di koordinatnya. Hitung koordinat, jangan menebak.
7. **QA visual wajib dijalankan** (Bagian 8). Modul tidak boleh dikirim sebelum thumbnail diperiksa dengan mata.
8. **Jangan mengunggah apa pun ke learv.online atau GitHub** dalam tugas ini. Tugas ini hanya membuat modul + menyimpan sumber.
9. **Perbarui `progres-materi-bergambar.md`** di akhir, dengan menulis ulang seluruh isinya (pertahankan semua bagian lama, tambahkan baris baru).
10. **Jangan membuat materi yang sudah ada di tabel progres.** Kalau seluruh antrean habis, jangan mengarang materi baru: laporkan ke pengguna dan berhenti.
11. **Setiap halaman bab harus terisi penuh**, minimal 85% tinggi kertas. Halaman yang separuh bawahnya kosong dianggap gagal. Patokan angkanya ada di Bagian 5B, dan cara menghitungnya di Bagian 8.
12. **Dilarang memakai emoji sebagai label kotak.** Pakai sprite ikon SVG di Lampiran B. Emoji sering tercetak sebagai kotak kosong (□) dan merusak seluruh halaman — apalagi di WeasyPrint.
13. **Pecahan ditulis bertumpuk**, bukan miring: `<span class="frac">` di HTML dan helper `frac_svg()` di dalam gambar. Dilarang menulis `3/4` sebagai teks biasa.
14. **Setiap gambar harus berbeda jenisnya dari gambar bab sebelumnya.** Dilarang memakai motif yang sama (misalnya deretan kotak batang) di lebih dari tiga bab. Katalog jenis gambar ada di Bagian 6B.
15. **Jumlah bab minimal 14.** Jangan menggabungkan dua konsep besar menjadi satu bab hanya agar cepat selesai.

---

## 2B. Rapor mutu: delapan kegagalan nyata yang harus dihindari

Modul "Pecahan & Desimal" pernah dibuat dengan spec versi awal dan hasilnya jauh di bawah standar.
Berikut yang terjadi — jangan ulangi satu pun.

| # | Yang terjadi | Akibatnya | Aturan pencegahnya |
|---|---|---|---|
| 1 | Isi tiap bab hanya 4 kotak pendek | Separuh bawah setiap halaman kosong melompong | Bagian 5B: anggaran isi |
| 2 | Label kotak memakai emoji | Semua judul kotak tercetak sebagai kotak kosong □ | Lampiran B: sprite ikon |
| 3 | Semua gambar berupa deretan kotak batang | 9 bab tampak identik, gambar berhenti menjelaskan | Bagian 6B: katalog gambar |
| 4 | Pecahan ditulis `3/4` sebagai teks biasa | Terlihat seperti pembagian, bukan pecahan | `.frac` dan `frac_svg()` |
| 5 | Gambar hanya berisi 3–5 bentuk tanpa angka | Gambar jadi hiasan, bukan penjelas | Bagian 6B: syarat minimum |
| 6 | Hanya 13 bab, operasi desimal digabung | Materi kurikulum ada yang hilang | Aturan 15 |
| 7 | Daftar isi tanpa subjudul analogi | Pembaca tidak tahu isi tiap bab | Bagian 4 |
| 8 | Sampul: maskot kecil, separuh halaman kosong | Sampul terasa belum jadi | Bagian 4B |

**Perbandingan satu bab yang sama:**

```
BURUK (yang terjadi)                      BAIK (yang diminta)
─────────────────────────────────         ─────────────────────────────────
Bayangkan   2 kalimat                     Bayangkan   3–4 kalimat bercerita
Konsepnya   3 kalimat                     Konsepnya   3 kalimat + 3 butir daftar
Rumus                                     Rumus
Contoh      3 langkah                     Contoh      4 langkah + baris Cek
Ingat!      1 kalimat                     Contoh 2    kasus berbeda ATAU tabel 4 baris
Coba Sendiri 1 kalimat                    Ingat!      2 kalimat + trik hafalan
                                          Awas Jebakan 2 kalimat
→ halaman terisi 55%                      Coba Sendiri 2 soal + jawaban
                                          → halaman terisi 90%
```

---

## 3. Langkah kerja (urut, jangan dilompati)

### Langkah 0 — Baca catatan progres
Buka `progres-materi-bergambar.md` di Drive. Catat:
- daftar materi yang **sudah** dibuat (kolom "Materi" dan "id buku"),
- **antrean berikutnya**,
- bagian **"Arahan pengguna"** — arahan pengguna selalu mengalahkan antrean,
- bagian **"Topik yang sudah tercakup buku lain"** — jangan membuat ulang topik di situ.

Kalau catatan progres berisi perintah berhenti/menunggu, **berhenti** dan laporkan.

### Langkah 1 — Pilih SATU materi
Ambil materi teratas dari antrean yang belum punya modul.
Prioritas mata pelajaran: **Matematika sampai habis, baru mata pelajaran lain.**
Tulis di awal balasan: materi apa yang dipilih dan alasannya satu kalimat.

### Langkah 2 — Susun isi materi secara lengkap
Kumpulkan seluruh isi materi itu sesuai kurikulum Indonesia untuk jenjangnya:
definisi, semua rumus, jenis/klasifikasi, langkah prosedur, kesalahan umum, dan tipe soal yang biasa keluar.
Target: **16 bab** (boleh 13–17 kalau materinya lebih kecil/besar).

Pola bab yang selalu dipakai:
- Bab 1 sampai n−4: materi inti, satu konsep per bab, berurutan dari yang paling dasar.
- Bab n−3: **Awas Jebakan!** — 10 pasang "✗ Salah" vs "✓ Benar", ditambah 3 "Jurus" pemeriksaan.
- Bab n−2: **Kartu Ringkasan** — semua rumus dalam kartu berwarna, satu halaman, cocok ditempel di meja belajar.
- Bab n−1: **Latihan Soal** — 10 soal bercerita + kunci jawaban di bawah garis putus-putus.
- Bab n: **Peta Belajar** — jalur berliku berisi semua pos + tabel centang "Aku sudah bisa…".

### Langkah 3 — Rencanakan tiap bab sebelum menulis kode
Untuk setiap bab tulis dulu (di kepalamu atau di catatan kerja):
- satu analogi sehari-hari,
- satu ilustrasi yang **menjelaskan konsep** (model luas, timbangan, garis bilangan, diagram alur, grafik) — bukan hiasan,
- satu contoh berlangkah dengan pengecekan,
- satu "Coba Sendiri" + jawabannya.

### Langkah 4 — Periksa kebenaran
Hitung ulang semua contoh, semua kunci jawaban, dan semua angka yang muncul di gambar.
Kalau ada yang salah di materi sumber, perbaiki dan sebutkan di balasan akhir.

### Langkah 5 — Tulis tiga berkas kode
Selalu tiga berkas terpisah di folder kerja:

| Berkas | Isi |
|---|---|
| `build.py` | fungsi-fungsi pembuat SVG + `FIG = dict(...)` berisi semua gambar |
| `page.html` | seluruh teks modul dengan placeholder `{{nama}}` untuk tiap gambar |
| `render.py` | mengganti placeholder lalu merender PDF |

Template ketiganya ada di Lampiran A, B, C. **Mulai dari template, jangan menulis dari nol.**

### Langkah 6 — Render
Jalankan `python render.py`. Baca Bagian 7 untuk urutan mesin render dan cara menanganinya kalau gagal.

### Langkah 7 — QA visual dan kepadatan
Jalankan prosedur Bagian 8 **seluruhnya**, termasuk `cek_kepadatan.py`. Bab yang berstatus
KURANG PADAT wajib ditambah isinya lalu dirender ulang. Ulangi sampai semua bab materi berstatus OK
dan lembar thumbnail bersih.

### Langkah 8 — Simpan sumber ke Drive
Simpan `modul-sumber/<id>.md` dengan susunan:
1. judul modul, id buku, jumlah halaman,
2. satu paragraf "Cara render ulang",
3. daftar bab,
4. "Catatan teknis" (hal khusus di modul ini: id unik, trik penulisan, viewBox tidak lazim),
5. isi **lengkap** `build.py`, `page.html`, `render.py` dalam tiga blok kode.

### Langkah 9 — Kirim hasil dan perbarui progres
- Kirim PDF ke pengguna.
- Tulis pesan singkat: materi apa yang dibuat, materi berikutnya dalam antrean, dan apa yang perlu pengguna lakukan.
- Tulis ulang `progres-materi-bergambar.md`: tambah satu baris tabel (tanggal, mata pelajaran, materi + daftar bab singkat, id buku, path sumber, status `belum diunggah`), lalu perbarui antrean (coret materi yang baru dibuat, geser nomor).

---

## 4. Struktur halaman modul

| Urutan | Halaman | Isi |
|---|---|---|
| 1 | **Sampul** | latar gradasi penuh, judul mengajak ("Himpunan Itu Rapi!", "Garis & Sudut Itu Tajam!"), satu paragraf pengantar, chip daftar topik, maskot SVG orisinal, footer `learv.online` |
| 2 | **Cara Pakai + Daftar Isi** | legenda 6 kotak warna, daftar isi dua kolom (judul bab + subjudul analogi), tabel kamus simbol |
| 3.. | **Satu bab per halaman** | lihat pola di Langkah 2 |

Judul modul: **nama materi + kata sifat positif + "Itu"**. Contoh: "Pecahan & Desimal Itu Gampang!", "Aritmetika Sosial Itu Cuan!".

### 4B. Syarat sampul

Sampul memakai seluruh tinggi kertas, tanpa jalur kosong besar. Yang wajib ada, urut dari atas:

1. chip mata pelajaran dan jenjang,
2. judul 2 baris, ukuran 44pt,
3. satu paragraf pengantar yang menyebut **tiga sampai lima analogi** dari isi modul,
4. **minimal 10 chip topik** (satu per bab inti),
5. **maskot SVG setinggi minimal 260 satuan viewBox** — benda nyata yang berkaitan dengan materi dan
   diberi wajah sederhana (kotak misteri bertuliskan x, busur derajat bermata, martabak berwajah),
   bukan sekadar kotak berisi tulisan,
6. footer: `learv.online` di kiri, satu kalimat ajakan dari maskot di kanan.

---

## 5. Sistem desain

### Palet (jangan diubah)

| Nama | Hex | Latar pucat |
|---|---|---|
| navy | `#1b2559` | — |
| biru | `#3b6ef5` | `#e9f0ff` |
| oranye | `#ff8a3d` | `#fff1e6` |
| hijau | `#16a37b` | `#e3f6ef` |
| kuning | `#ffc93c` | `#fff8e1` |
| ungu | `#7b5cf0` | `#efeafe` |
| merah | `#ef4b5a` | `#fde8ea` |
| abu teks | `#5d6788` | latar lembut `#f7f9fd` |

Warna lencana nomor bab **bergilir**: biru → oranye → hijau → ungu → merah → biru → …

### Font
Judul & label **Poppins**, isi **Inter**.
Cek ketersediaan dulu (lihat Bagian 7, preflight). Kalau tidak ada, pakai rantai fallback
`'Poppins','DejaVu Sans',sans-serif` dan tetap lanjut — jangan mencoba memasang font atau mengunduh dari internet.

### Enam kotak warna (konsisten di semua bab, jangan menambah jenis baru)

| Kotak | Kelas | Isi |
|---|---|---|
| **Bayangkan…** `#ic-bay` | `.bay` (peach) | cerita pembuka bab, 3 kalimat |
| **Konsepnya** `#ic-kon` | `.kon` (biru muda) | inti materi + 3 butir `<ul class="dot">` |
| **Contoh** `#ic-con` | `.con` (mint) | 4 langkah bernomor + baris "Cek:" |
| **Ingat!** `#ic-ing` | `.ing` (krem, garis putus-putus) | trik, jembatan keledai |
| **Awas Jebakan** `#ic-awas` | `.awas` (pink) | kesalahan umum |
| 🎯 **Coba Sendiri** | `.coba` (lavender) | soal mini + jawaban |

Rumus penting ditaruh di `.formula`: kotak berbingkai navy, rata tengah.
### 5B. Anggaran isi per halaman bab (patokan wajib)

Satu halaman A4 dengan margin 14 mm memuat kira-kira **2.400–2.900 karakter teks** ditambah satu gambar
setinggi 150–320 satuan viewBox. Pakai patokan ini:

| Unsur | Jumlah minimum per bab | Catatan |
|---|---|---|
| Kotak warna | **5** | Bayangkan, Konsepnya, Contoh, Ingat!, Coba Sendiri — wajib ada semua |
| Kotak tambahan | 1 | Awas Jebakan **atau** Contoh kedua **atau** `<table class="d">` berisi 3–5 baris |
| Gambar SVG | 1 (boleh 2) | tinggi viewBox 150–320 |
| `.formula` | 1 | kecuali bab yang memang tidak berumus |
| Kalimat di kotak Bayangkan | 3 kalimat | harus bercerita, bukan definisi |
| Butir daftar di Konsepnya | 3 | pakai `<ul class="dot">` |
| Langkah di kotak Contoh | 4 langkah + 1 baris "Cek:" | |
| Soal di Coba Sendiri | 2 soal | jawaban di `.ans` |
| Total teks satu bab | **2.300–2.900 karakter** | di luar tag HTML |

**Kalau sebuah bab kurang dari 2.300 karakter**, tambahkan dengan urutan ini:
(a) contoh kedua dengan kasus berbeda, (b) tabel ringkas, (c) kotak Awas Jebakan khusus bab itu,
(d) satu soal lagi di Coba Sendiri. **Jangan** menambal dengan memperbesar font atau memberi jarak kosong.

**Kalau lebih dari 2.900 karakter**, padatkan kalimatnya — jangan menghapus kotak.

### Aturan CSS yang WAJIB dipatuhi (subset aman)

Mesin render non-Chrome (WeasyPrint dll.) tidak mendukung semua CSS modern.
Supaya hasilnya sama di mesin mana pun:

- ✅ Pakai `@page{size:A4;margin:14mm 14mm 16mm}` dan `@page:first{margin:0}`.
- ✅ Pakai `print-color-adjust:exact` agar warna latar ikut tercetak.
- ✅ Pemisah halaman: `page-break-before:always` (bukan `break-before`).
- ✅ Tata letak dua kolom (teks | gambar): pakai **`<table class="two">`** dengan `<td class="t">` dan `<td class="g" width="40%">`. Jangan pakai CSS Grid untuk ini.
- ✅ Kisi kartu/legenda: pakai `<table>` juga, atau `display:inline-block` dengan lebar persen.
- ❌ **Jangan** pakai `display:grid`, `grid-template-columns`, `gap`, `flex`, `aspect-ratio`, variabel CSS (`var()`), `clamp()`, `:has()`.
- ❌ Jangan pakai `text-transform:uppercase` pada label kotak (rumus `f(x) = mx + c` akan berubah jadi `F(X) = MX + C`).
- ❌ Jangan memuat font/gambar/CSS dari internet. Semuanya inline.

Ukuran teks acuan: isi 10,6pt, judul bab 19pt, judul kotak 10,5pt, catatan kecil 9,5pt.

---

## 6. Aturan ilustrasi SVG

Setiap aturan di bawah ini lahir dari bug yang pernah terjadi. Patuhi semuanya.

1. **Satu fungsi Python per gambar**, mengembalikan string `<svg viewBox="0 0 W H" class="fig">…</svg>`.
   Lebar viewBox standar **300** (gambar kolom kanan) atau **640** (peta belajar selebar halaman).
   Tinggi bebas, sesuaikan isi — **jangan menyisakan ruang kosong besar di bawah**.
2. **Hitung koordinat dengan Python, jangan ditebak.** Sediakan helper:
   `P(cx,cy,r,deg)` untuk titik pada sudut, `T(x,y,teks,…)` untuk teks, `L(...)` untuk garis.
   Sudut memakai konvensi matematika (berlawanan arah jarum jam); ingat sumbu y SVG menghadap ke bawah,
   jadi `y = cy − r·sin(θ)`.
3. **Elemen yang dipakai ulang dengan `<use>` harus berada di dalam `<defs>`.**
   Kalau tidak, `<g id>` aslinya ikut tergambar di titik (0,0) dan muncul sebagai potongan nyasar di pojok.
4. **`<mask>` sering tidak didukung mesin render non-Chrome.** Untuk daerah arsir seperti diagram Venn,
   pakai `<clipPath>` atau gambar poligon/juring yang sudah dihitung. Kalau terpaksa memakai `<mask>`,
   wajib periksa hasilnya di PDF dan sebutkan di "Catatan teknis".
5. **Semua `id` di dalam SVG harus unik se-modul** (beri prefix modul, misalnya `gsah1`, `hmcov`).
   Beberapa SVG bisa tampil di satu halaman; id kembar membuat gambar saling merusak.
6. **Anotasi garis penunjuk pada rumus** (misalnya menunjuk koefisien pada 5x² − 3x + 8):
   letakkan setiap angka, huruf, dan tanda sebagai `<text>` terpisah dengan `x` eksplisit dan
   `text-anchor="middle"`. Pangkat dibuat sebagai `<text>` kecil yang dinaikkan. Garis penunjuk memakai
   koordinat x yang sama persis. **Jangan** menulis rumus dalam satu `<text>` berisi `<tspan>` lalu menebak posisi garisnya.
7. **Label di dekat tepi viewBox gampang terpotong.** Pakai `text-anchor="end"` atau geser ke dalam.
8. **Teks jangan ditimpa garis.** Kalau angka harus berada di atas garis/arsiran, beri halo:
   `stroke="<warna latar>" stroke-width="3.5" paint-order="stroke"`.
9. **Garis lengkung dan panah jangan melintasi teks.** Taruh kurvanya di bawah atau di samping teks.
10. **Semua angka di gambar harus sama dengan angka di teks bab itu.** Periksa ulang setelah revisi teks.
11. **Maskot sampul**: bentuk sederhana orisinal yang berhubungan dengan materi (kotak misteri bertuliskan x,
    busur derajat bermata, dua lingkaran Venn berwajah). Dilarang meniru karakter atau logo yang sudah ada.

---

### 6B. Katalog jenis ilustrasi (wajib bergilir)

Gambar yang baik **membuat konsep terlihat**, bukan mengulang angka yang sudah ada di teks.
Putar jenisnya supaya tidak ada dua bab berturut-turut yang mirip:

| Jenis | Dipakai untuk | Contoh |
|---|---|---|
| **Benda nyata dipotong** | bagian dari keseluruhan | martabak 8 potong, pizza, kue lapis |
| **Batang/pita sebanding** | membandingkan dua nilai | dua pita panjang berbeda bertumpuk |
| **Garis bilangan** | urutan, letak, jarak | pecahan dan desimal di satu garis |
| **Timbangan** | kesetaraan, persamaan | dua sisi seimbang |
| **Diagram alur / tangga** | prosedur berlangkah | langkah mengubah pecahan ke persen |
| **Uang dan harga** | persen, diskon, untung-rugi | label harga dicoret, pecahan uang |
| **Wadah terisi** | bagian, persen, kapasitas | gelas, botol, tangki |
| **Dua lajur salah vs benar** | kesalahan umum | kolom merah dan kolom hijau |
| **Peta/jalur** | ringkasan perjalanan belajar | peta belajar di bab terakhir |
| **Objek bergeometri** | sudut, bangun, ruang | balok, jam dinding, busur derajat |

**Syarat minimum satu gambar:**
- minimal **12 elemen** SVG (bentuk + teks), bukan 3 kotak polos;
- minimal **3 label teks berangka** yang nilainya sama dengan teks bab;
- minimal **satu bentuk yang menyerupai benda nyata** (bukan hanya persegi panjang) pada sekurang-kurangnya
  separuh jumlah bab;
- punya judul kecil di atas atau keterangan kecil di bawah.

**Tanda gambar yang gagal:** hanya deretan kotak berwarna; tidak ada angka; bentuknya sama persis dengan
gambar bab sebelumnya; atau isinya cuma tulisan di dalam kotak (itu teks, bukan gambar).

---

## 7. Pipeline render

### Preflight (jalankan sekali di awal sesi, sebelum menulis kode)

```python
# preflight.py — cek lingkungan, cetak laporan singkat
import importlib, shutil, sys
def has(m):
    try: importlib.import_module(m); return True
    except Exception: return False
print("playwright   :", has("playwright"))
print("weasyprint   :", has("weasyprint"))
print("xhtml2pdf    :", has("xhtml2pdf"))
print("reportlab    :", has("reportlab"))
print("fitz (PyMuPDF):", has("fitz"))
print("pdf2image    :", has("pdf2image"))
print("PIL          :", has("PIL"))
print("chrome bin   :", shutil.which("google-chrome") or shutil.which("chromium"))
print("pdftoppm     :", shutil.which("pdftoppm"))
# font
try:
    from matplotlib import font_manager as fm
    names = {f.name for f in fm.fontManager.ttflist}
    print("Poppins ada  :", "Poppins" in names)
    print("Inter ada    :", "Inter" in names)
except Exception as e:
    print("cek font gagal:", e)
```

Catat hasilnya. Mesin render dipilih dengan urutan berikut (pakai yang pertama tersedia):

1. **Chrome headless lewat Playwright** — hasil paling akurat. Pakai kalau ada.
2. **WeasyPrint** — pure Python, hasil bagus untuk subset CSS di Bagian 5.
3. **xhtml2pdf (pisa)** — darurat; dukungan CSS-nya terbatas, hasil akan lebih sederhana.

Kalau tidak satu pun tersedia: **berhenti dan laporkan ke pengguna**, jangan memaksakan hasil dengan
mesin yang tidak bisa menggambar SVG. Jangan mencoba memasang paket lewat internet.

### Hal-hal yang berbeda di WeasyPrint (wajib diperhatikan)

- SVG inline **harus** punya `viewBox`; beri juga `width:100%;height:auto` lewat CSS kelas `.fig`.
- `<mask>` tidak didukung → lihat aturan SVG no. 4.
- Emoji mungkin tampil hitam-putih atau sebagai kotak. Kalau kotak kosong muncul di QA,
  ganti emoji judul kotak dengan simbol teks (`▸`, `★`, `!`) dan sebutkan di catatan teknis.
- Header/footer nomor halaman dibuat lewat CSS `@page{@bottom-center{content:counter(page)}}`,
  bukan lewat `footer_template` seperti di Chrome. Template di Lampiran C sudah menanganinya.

---

## 8. QA visual (wajib, tidak boleh dilewati)

1. **Hitung halaman.** Harus = 1 sampul + 1 cara pakai + jumlah bab. Kalau lebih, ada bab yang meluber.
2. **Render thumbnail semua halaman** dan **lihat gambarnya sendiri** (tampilkan di sesi, jangan hanya diproses):

```python
# qa.py — thumbnail 10 halaman per lembar
import fitz                      # kalau tak ada, pakai pdf2image / pdftoppm
from PIL import Image
doc = fitz.open("Modul_Nama.pdf")
ims = []
for p in doc:
    pix = p.get_pixmap(dpi=45)
    ims.append(Image.frombytes("RGB",[pix.width,pix.height],pix.samples))
for k in range(0, len(ims), 10):
    g = ims[k:k+10]; w,h = g[0].size
    sh = Image.new("RGB",(w*5,h*2),"white")
    for i,im in enumerate(g): sh.paste(im,((i%5)*w,(i//5)*h))
    sh.save(f"qa_sheet{k//10}.png")
print("halaman:", len(ims))
```

3. **Hitung kepadatan tiap bab** dan tampilkan tabelnya. Bab yang belum lolos WAJIB ditambah isinya
   (Bagian 5B) sebelum lanjut:

```python
# cek_kepadatan.py
import re
h = open("modul.html", encoding="utf-8").read()
bab = re.findall(r'<section class="page">(.*?)</section>', h, re.S)
print("halaman 1 = Cara Pakai; bab materi mulai halaman 2. Status hanya berlaku untuk bab materi.")
print(f"{'hlm':>4} {'judul':<34} {'karakter':>9} {'kotak':>6} {'svg':>4}  status")
for i, b in enumerate(bab, 1):
    judul = re.search(r'<h2>(.*?)</h2>', b)
    judul = re.sub(r'<.*?>', '', judul.group(1)) if judul else '-'
    teks  = re.sub(r'<svg.*?</svg>', '', b, flags=re.S)
    teks  = re.sub(r'<.*?>', ' ', teks)
    n     = len(re.sub(r'\s+', ' ', teks).strip())
    kotak = len(re.findall(r'class="box ', b))
    nsvg  = len(re.findall(r'<svg[^>]*viewBox', b))      # hanya gambar; ikon label tidak dihitung
    ok    = "OK" if (2300 <= n <= 2900 and kotak >= 6) else ("KURANG PADAT" if n < 2300 else "TERLALU PADAT")
    print(f"{i:>4} {judul[:34]:<34} {n:>9} {kotak:>6} {nsvg:>4}  {ok}")
```

   Halaman Cara Pakai dan bab khusus (Jebakan, Ringkasan, Latihan, Peta) boleh di luar rentang itu;
   bab materi biasa tidak boleh.

4. **Periksa variasi gambar**: tulis jenis gambar tiap bab dalam satu baris, merujuk katalog Bagian 6B.
   Kalau ada jenis yang muncul lebih dari tiga kali, ganti salah satunya.

5. **Yang dicari pada lembar thumbnail:**
   - halaman yang isinya meluber ke halaman berikutnya,
   - ruang kosong besar yang aneh di bawah halaman,
   - potongan gambar nyasar di pojok kiri atas (gejala aturan SVG no. 3),
   - kotak warna yang terpotong di tepi halaman.
6. **Perbesar setiap halaman yang padat gambar** (dpi 80–110) dan periksa:
   label bertabrakan, teks tertimpa garis, angka terpotong di tepi viewBox, panah menembus teks.
7. **Periksa semua gambar sekaligus** dengan merender `FIG` ke satu halaman HTML berisi semua SVG
   berdampingan, lalu lihat. Ini cara tercepat menemukan gambar yang rusak.
6. **Cek ulang angka** di gambar vs teks bab.
7. Perbaiki **akar masalahnya**, bukan menggeser posisi secara coba-coba, lalu render ulang dan periksa lagi.

Cara memperbaiki yang aman: edit dengan `str.replace` disertai `assert old in s`, supaya kalau polanya
tidak ketemu, prosesnya berhenti dan kamu tahu ada yang salah.

Kalau halaman meluber, perbaiki dengan urutan ini: (a) gabungkan dua kotak yang isinya mirip,
(b) pindahkan satu kalimat "Ingat!" menjadi `<p class="mini">` di dalam kotak Contoh,
(c) persingkat kalimat. **Jangan** mengecilkan font seluruh halaman.

---

## 9. Checklist sebelum menyelesaikan tugas

- [ ] Hanya **satu** modul baru dibuat
- [ ] Materi sesuai antrean dan belum pernah dibuat
- [ ] Jumlah halaman = 1 + 1 + jumlah bab (tidak ada yang meluber)
- [ ] Setiap bab punya analogi sehari-hari + ilustrasi yang menjelaskan
- [ ] Semua contoh dan kunci jawaban sudah dihitung ulang
- [ ] Semua angka di gambar cocok dengan teksnya
- [ ] Tidak ada gambar dari internet; tidak ada karakter/merek orang lain
- [ ] Semua `id` SVG unik; tidak ada potongan nyasar di pojok
- [ ] Tabel kepadatan sudah dijalankan: tiap bab materi 2.300–2.900 karakter dan minimal 6 kotak
- [ ] Tidak ada emoji sebagai label; semua memakai sprite ikon SVG
- [ ] Semua pecahan bertumpuk, di teks maupun di gambar
- [ ] Tidak ada jenis gambar yang dipakai lebih dari tiga kali
- [ ] Jumlah bab minimal 14
- [ ] Lembar thumbnail sudah **dilihat**, bukan hanya dibuat
- [ ] Bab Awas Jebakan, Kartu Ringkasan, Latihan + kunci, dan Peta Belajar ada
- [ ] `modul-sumber/<id>.md` tersimpan lengkap (tiga blok kode utuh)
- [ ] `progres-materi-bergambar.md` ditulis ulang: baris baru + antrean diperbarui
- [ ] PDF dikirim ke pengguna + pesan singkat
- [ ] Tidak ada yang diunggah ke situs/GitHub

---

## 10. Penamaan

- id modul: huruf kecil, pakai tanda hubung, tanpa singkatan — `garis-sudut`, `aritmetika-sosial`, `pecahan-desimal`
- berkas PDF: `Modul_Garis_Sudut.pdf` (Kapital Tiap Kata, pemisah garis bawah)
- sumber: `modul-sumber/garis-sudut.md`

---

## Lampiran A — Template `build.py`

```python
# -*- coding: utf-8 -*-
# <Nama Materi> — fungsi SVG orisinal. FIG menggantikan placeholder {{nama}} di page.html.
import math

NAVY="#1b2559"; BLUE="#3b6ef5"; ORG="#ff8a3d"; GRN="#16a37b"
YEL="#ffc93c"; PUR="#7b5cf0"; RED="#ef4b5a"; GREY="#5d6788"
PBLUE="#e9f0ff"; PORG="#fff1e6"; PGRN="#e3f6ef"; PPUR="#efeafe"
PRED="#fde8ea"; PYEL="#fff8e1"; SBG="#f7f9fd"

# ---------- helper dasar ----------
def T(x, y, t, size=12, fill=NAVY, w="700", fam="Poppins", anchor="middle"):
    """Teks. y adalah garis alas (baseline), jadi untuk teks rata tengah vertikal
    di titik (cx,cy) pakai y = cy + size*0.36."""
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="{fam}" '
            f'font-size="{size}" font-weight="{w}" fill="{fill}">{t}</text>')

def Thalo(x, y, t, size=12, fill=NAVY, bg="#ffffff", anchor="middle"):
    """Teks dengan halo, dipakai kalau teks berada di atas garis atau arsiran."""
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Poppins" '
            f'font-size="{size}" font-weight="700" fill="{fill}" stroke="{bg}" '
            f'stroke-width="3.5" paint-order="stroke">{t}</text>')

def svg(w, h, body, cls="fig"):
    return (f'<svg viewBox="0 0 {w} {h}" class="{cls}" xmlns="http://www.w3.org/2000/svg">'
            + "".join(body) + '</svg>')

def P(cx, cy, r, deg):
    """Titik pada sudut deg (berlawanan arah jarum jam dari sumbu x+, sumbu y SVG ke bawah)."""
    return cx + r*math.cos(math.radians(deg)), cy - r*math.sin(math.radians(deg))

def L(x1, y1, x2, y2, col=NAVY, w=2, extra=""):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" '
            f'stroke-width="{w}" stroke-linecap="round" {extra}/>')

def ray(cx, cy, deg, r, col=NAVY, w=2.2, extra=""):
    x, y = P(cx, cy, r, deg); return L(cx, cy, x, y, col, w, extra)

def arc(cx, cy, r, a1, a2, col=ORG, w=2, fill="none", op=1):
    """Busur a1→a2 berlawanan jarum jam. fill != none menghasilkan juring."""
    x1, y1 = P(cx, cy, r, a1); x2, y2 = P(cx, cy, r, a2)
    large = 1 if (a2 - a1) % 360 > 180 else 0
    if fill != "none":
        return (f'<path d="M{cx:.1f},{cy:.1f} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 0 '
                f'{x2:.1f},{y2:.1f} Z" fill="{fill}" fill-opacity="{op}" stroke="{col}" stroke-width="{w}"/>')
    return (f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 0 {x2:.1f},{y2:.1f}" '
            f'fill="none" stroke="{col}" stroke-width="{w}"/>')

def dot(x, y, r=4, col=NAVY):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>'

def frac_svg(x, y, atas, bawah, size=13, col=NAVY, lebar=None):
    """Pecahan bertumpuk di dalam SVG (aturan 13). (x, y) = titik tengah garis pembatas."""
    w = lebar or max(len(str(atas)), len(str(bawah))) * size * 0.62 + 6
    return (T(x, y - size*0.28, str(atas), size, col) +
            f'<line x1="{x-w/2:.1f}" y1="{y:.1f}" x2="{x+w/2:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="1.6"/>' +
            T(x, y + size*0.95, str(bawah), size, col))

def marker(i, col, pre="mk"):
    """Panah. pre harus unik per modul agar id tidak bentrok."""
    return (f'<marker id="{pre}{i}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" '
            f'markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>')

# ---------- Bab 1: <judul> ----------
def fig_contoh():
    s = [f'<defs>{marker(1, BLUE, "xx")}</defs>']
    s.append(f'<rect x="8" y="10" width="284" height="80" rx="12" fill="{PBLUE}"/>')
    s.append(T(150, 56, "ganti dengan gambar sungguhan", 12, BLUE))
    return svg(300, 100, s)

# ---------- Peta belajar (selalu ada, lebar 640) ----------
def fig_map(stops, berikutnya):
    pts = [(55,70),(160,55),(265,80),(370,55),(475,80),(585,110),
           (535,220),(430,240),(325,215),(220,240),(115,215),(40,175)]
    cols = [BLUE,ORG,GRN,PUR,RED,BLUE,ORG,GRN,PUR,RED,BLUE,ORG]
    n = min(len(stops), len(pts))
    s = ['<svg viewBox="0 0 640 330" class="fig" xmlns="http://www.w3.org/2000/svg">']
    d = "M" + " L".join(f"{x},{y}" for x, y in pts[:n])
    s.append(f'<path d="{d}" fill="none" stroke="#dfe6fb" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>')
    s.append(f'<path d="{d}" fill="none" stroke="{YEL}" stroke-width="3" stroke-dasharray="8 7" stroke-linejoin="round"/>')
    for i in range(n):
        x, y = pts[i]; c = cols[i % len(cols)]
        s.append(f'<circle cx="{x}" cy="{y}" r="19" fill="{c}" stroke="#fff" stroke-width="4"/>')
        s.append(T(x, y+5, str(i+1), 13, "#fff"))
        ty = y-28 if i < 6 else y+38
        tx, anchor = x, "middle"
        if i == 0: tx, anchor = 36, "start"
        if i == 5: tx, anchor = 604, "end"
        if i == 11: tx, anchor = 22, "start"
        s.append(T(tx, ty, stops[i], 12, NAVY, "600", "Poppins", anchor))
    s.append(f'<rect x="40" y="290" width="560" height="32" rx="16" fill="{NAVY}"/>')
    s.append(T(320, 311, berikutnya, 12.5, "#fff", "600"))
    s.append('</svg>')
    return "".join(s)

FIG = dict(
    cover=fig_contoh(),          # ganti: maskot sampul, viewBox 440x300
    contoh=fig_contoh(),
    map=fig_map(["Pos 1","Pos 2"], "Berikutnya: <materi>. <ajakan singkat>"),
)
```

## Lampiran B — Template `page.html`

CSS di bawah ini sudah memakai subset aman Bagian 5. **Salin apa adanya**, ganti hanya warna sampul,
judul, dan isinya.

```html
<!DOCTYPE html><html lang="id"><head><meta charset="utf-8"><title>JUDUL MODUL</title>
<style>
@page{size:A4;margin:14mm 14mm 16mm; @bottom-left{content:"JUDUL MODUL · learv.online";font-family:Inter,sans-serif;font-size:8pt;color:#8a93ad} @bottom-right{content:counter(page);font-family:Inter,sans-serif;font-size:8pt;color:#8a93ad}}
@page:first{margin:0; @bottom-left{content:""} @bottom-right{content:""}}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font-family:Inter,'DejaVu Sans',sans-serif;font-size:10.6pt;line-height:1.5;color:#1b2559}
h1,h2,h3,.lbl,.chip,.badge{font-family:Poppins,'DejaVu Sans',sans-serif}
.cover{width:210mm;height:297mm;background:linear-gradient(150deg,#7b5cf0 0%,#3b6ef5 55%,#16a37b 100%);color:#fff;padding:26mm 20mm;position:relative;overflow:hidden}
.cover .kls{display:inline-block;background:rgba(255,255,255,.2);padding:5px 14px;border-radius:20px;font-weight:600;font-size:11pt}
.cover h1{font-size:44pt;line-height:1.05;margin:14px 0 10px}
.cover p.sub{font-size:13pt;max-width:150mm}
.chip{display:inline-block;background:#fff;color:#1b2559;border-radius:20px;padding:5px 13px;font-size:9.5pt;font-weight:600;margin:0 6px 6px 0}
.chips{margin:14px 0 20px}
.cover .mascot{text-align:center;margin-top:6mm}
.cover .foot{position:absolute;bottom:16mm;left:20mm;right:20mm;font-size:10pt}
.cover .foot .kanan{float:right}
.page{page-break-before:always}
.head{border-bottom:2px solid #eef1f8;padding-bottom:8px;margin-bottom:10px}
.head table{width:100%;border:0;margin:0}
.head td{border:0;padding:0;vertical-align:middle}
.badge{width:46px;height:46px;border-radius:14px;color:#fff;font-weight:700;font-size:20pt;text-align:center;line-height:46px}
.head h2{margin:0 0 0 14px;font-size:19pt;line-height:1.15}
.head .an{font-size:10pt;color:#5d6788;margin:2px 0 0 14px}
.box{border-radius:12px;padding:9px 13px;margin:8px 0}
.box .lbl{font-weight:700;font-size:10.5pt;margin-bottom:3px}
.box p{margin:3px 0}
.bay{background:#fff1e6}.bay .lbl{color:#d2661d}
.kon{background:#e9f0ff}.kon .lbl{color:#3b6ef5}
.con{background:#e3f6ef}.con .lbl{color:#0f8a66}
.ing{background:#fff8e1;border:2px dashed #ffc93c}.ing .lbl{color:#a87800}
.awas{background:#fde8ea}.awas .lbl{color:#c9303f}
.coba{background:#efeafe}.coba .lbl{color:#5c3ed6}
.formula{border:2.5px solid #1b2559;border-radius:12px;text-align:center;font-family:Poppins,'DejaVu Sans',sans-serif;font-weight:600;font-size:12.5pt;padding:7px 10px;margin:8px auto;max-width:165mm;background:#fff}
table.two{width:100%;border-collapse:collapse;margin:0}
table.two td{border:0;padding:0;vertical-align:middle}
table.two td.g{width:40%;padding-left:14px}
.fig{width:100%;height:auto;display:block}
ol.st{margin:4px 0;padding-left:20px}ol.st li{margin:2px 0}
ul.dot{margin:3px 0;padding-left:18px}
table.d{border-collapse:collapse;width:100%;margin:6px 0;font-size:10pt}
table.d th{background:#1b2559;color:#fff;font-family:Poppins,'DejaVu Sans',sans-serif;font-weight:600;padding:5px 8px;text-align:left}
table.d td{padding:5px 8px;border-bottom:1px solid #e4e8f2}
table.d tr:nth-child(even) td{background:#f5f7fc}
.ans{font-size:9.6pt;color:#5c3ed6;border-top:1px dashed #b9a9f5;margin-top:5px;padding-top:4px}
.toc td{width:50%;vertical-align:top;padding:3px 8px 3px 0}
.leg{width:100%;border-collapse:separate;border-spacing:6px 0;margin:0 -6px}
.leg td{width:33.33%;vertical-align:top;padding:0}
.leg .box{margin:0 0 8px;font-size:9.4pt;height:100%}
.toc .it{background:#f5f7fc;border-radius:10px;padding:6px 11px}
.toc b{font-family:Poppins,'DejaVu Sans',sans-serif}
.toc span{display:block;font-size:9pt;color:#5d6788}
.card{border-radius:12px;padding:10px 13px;color:#1b2559}
.card h3{margin:0 0 4px;font-size:11.5pt}
.card .f{font-family:Poppins,'DejaVu Sans',sans-serif;font-weight:600;font-size:10.5pt;background:#fff;border-radius:8px;padding:4px 8px;margin:3px 0;display:inline-block}
.card p{margin:3px 0;font-size:9.8pt}
.x,.v{border-radius:10px;padding:6px 10px;font-size:10pt}
.x{background:#fde8ea}.v{background:#e3f6ef}
.x b{color:#c9303f}.v b{color:#0f8a66}
.kunci{border-top:2px dashed #8a93ad;margin-top:12px;padding-top:8px;font-size:9.8pt}
.mini{font-size:9.5pt;color:#5d6788}
/* ikon label kotak — pengganti emoji (aturan 12) */
.ic{width:13px;height:13px;vertical-align:-1.5px;margin-right:5px}
/* pecahan bertumpuk (aturan 13) */
.frac{display:inline-block;vertical-align:-0.42em;text-align:center;font-family:Poppins,'DejaVu Sans',sans-serif;line-height:1.08;margin:0 2px}
.frac .n{display:block;padding:0 3px;border-bottom:1.6px solid currentColor}
.frac .d{display:block;padding:0 3px}
.frac.s{font-size:.9em}
</style></head><body>

<!-- SPRITE IKON — letakkan sekali saja, tepat sesudah <body>. Ikon memakai currentColor,
     jadi warnanya otomatis mengikuti warna judul kotaknya. -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="ic-bay" viewBox="0 0 16 16"><path d="M1.6 4.6h12.8l-1.5 8.4a1 1 0 0 1-1 .8H4.1a1 1 0 0 1-1-.8z" fill="currentColor"/><path d="M5.2 4.6V3.2a2.8 2.8 0 0 1 5.6 0v1.4" fill="none" stroke="currentColor" stroke-width="1.5"/></symbol>
<symbol id="ic-kon" viewBox="0 0 16 16"><circle cx="8" cy="6.4" r="4.4" fill="currentColor"/><rect x="6" y="11" width="4" height="1.5" rx=".7" fill="currentColor"/><rect x="6.4" y="13.2" width="3.2" height="1.5" rx=".7" fill="currentColor"/></symbol>(c) persingkat kalimat. **Jangan** mengecilkan font seluruh halaman.

---

## 9. Checklist sebelum menyelesaikan tugas

- [ ] Hanya **satu** modul baru dibuat
- [ ] Materi sesuai antrean dan belum pernah dibuat
- [ ] Jumlah halaman = 1 + 1 + jumlah bab (tidak ada yang meluber)
- [ ] Setiap bab punya analogi sehari-hari + ilustrasi yang menjelaskan
- [ ] Semua contoh dan kunci jawaban sudah dihitung ulang
- [ ] Semua angka di gambar cocok dengan teksnya
- [ ] Tidak ada gambar dari internet; tidak ada karakter/merek orang lain
- [ ] Semua `id` SVG unik; tidak ada potongan nyasar di pojok
- [ ] Tabel kepadatan sudah dijalankan: tiap bab materi 2.300–2.900 karakter dan minimal 6 kotak
- [ ] Tidak ada emoji sebagai label; semua memakai sprite ikon SVG
- [ ] Semua pecahan bertumpuk, di teks maupun di gambar
- [ ] Tidak ada jenis gambar yang dipakai lebih dari tiga kali
- [ ] Jumlah bab minimal 14
- [ ] Lembar thumbnail sudah **dilihat**, bukan hanya dibuat
- [ ] Bab Awas Jebakan, Kartu Ringkasan, Latihan + kunci, dan Peta Belajar ada
- [ ] `modul-sumber/<id>.md` tersimpan lengkap (tiga blok kode utuh)
- [ ] `progres-materi-bergambar.md` ditulis ulang: baris baru + antrean diperbarui
- [ ] PDF dikirim ke pengguna + pesan singkat
- [ ] Tidak ada yang diunggah ke situs/GitHub

---

## 10. Penamaan

- id modul: huruf kecil, pakai tanda hubung, tanpa singkatan — `garis-sudut`, `aritmetika-sosial`, `pecahan-desimal`
- berkas PDF: `Modul_Garis_Sudut.pdf` (Kapital Tiap Kata, pemisah garis bawah)
- sumber: `modul-sumber/garis-sudut.md`

---

## Lampiran A — Template `build.py`

```python
# -*- coding: utf-8 -*-
# <Nama Materi> — fungsi SVG orisinal. FIG menggantikan placeholder {{nama}} di page.html.
import math

NAVY="#1b2559"; BLUE="#3b6ef5"; ORG="#ff8a3d"; GRN="#16a37b"
YEL="#ffc93c"; PUR="#7b5cf0"; RED="#ef4b5a"; GREY="#5d6788"
PBLUE="#e9f0ff"; PORG="#fff1e6"; PGRN="#e3f6ef"; PPUR="#efeafe"
PRED="#fde8ea"; PYEL="#fff8e1"; SBG="#f7f9fd"

# ---------- helper dasar ----------
def T(x, y, t, size=12, fill=NAVY, w="700", fam="Poppins", anchor="middle"):
    """Teks. y adalah garis alas (baseline), jadi untuk teks rata tengah vertikal
    di titik (cx,cy) pakai y = cy + size*0.36."""
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="{fam}" '
            f'font-size="{size}" font-weight="{w}" fill="{fill}">{t}</text>')

def Thalo(x, y, t, size=12, fill=NAVY, bg="#ffffff", anchor="middle"):
    """Teks dengan halo, dipakai kalau teks berada di atas garis atau arsiran."""
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Poppins" '
            f'font-size="{size}" font-weight="700" fill="{fill}" stroke="{bg}" '
            f'stroke-width="3.5" paint-order="stroke">{t}</text>')

def svg(w, h, body, cls="fig"):
    return (f'<svg viewBox="0 0 {w} {h}" class="{cls}" xmlns="http://www.w3.org/2000/svg">'
            + "".join(body) + '</svg>')

def P(cx, cy, r, deg):
    """Titik pada sudut deg (berlawanan arah jarum jam dari sumbu x+, sumbu y SVG ke bawah)."""
    return cx + r*math.cos(math.radians(deg)), cy - r*math.sin(math.radians(deg))

def L(x1, y1, x2, y2, col=NAVY, w=2, extra=""):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" '
            f'stroke-width="{w}" stroke-linecap="round" {extra}/>')

def ray(cx, cy, deg, r, col=NAVY, w=2.2, extra=""):
    x, y = P(cx, cy, r, deg); return L(cx, cy, x, y, col, w, extra)

def arc(cx, cy, r, a1, a2, col=ORG, w=2, fill="none", op=1):
    """Busur a1→a2 berlawanan jarum jam. fill != none menghasilkan juring."""
    x1, y1 = P(cx, cy, r, a1); x2, y2 = P(cx, cy, r, a2)
    large = 1 if (a2 - a1) % 360 > 180 else 0
    if fill != "none":
        return (f'<path d="M{cx:.1f},{cy:.1f} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 0 '
                f'{x2:.1f},{y2:.1f} Z" fill="{fill}" fill-opacity="{op}" stroke="{col}" stroke-width="{w}"/>')
    return (f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 0 {x2:.1f},{y2:.1f}" '
            f'fill="none" stroke="{col}" stroke-width="{w}"/>')

def dot(x, y, r=4, col=NAVY):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>'

def frac_svg(x, y, atas, bawah, size=13, col=NAVY, lebar=None):
    """Pecahan bertumpuk di dalam SVG (aturan 13). (x, y) = titik tengah garis pembatas."""
    w = lebar or max(len(str(atas)), len(str(bawah))) * size * 0.62 + 6
    return (T(x, y - size*0.28, str(atas), size, col) +
            f'<line x1="{x-w/2:.1f}" y1="{y:.1f}" x2="{x+w/2:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="1.6"/>' +
            T(x, y + size*0.95, str(bawah), size, col))

def marker(i, col, pre="mk"):
    """Panah. pre harus unik per modul agar id tidak bentrok."""
    return (f'<marker id="{pre}{i}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" '
            f'markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>')

# ---------- Bab 1: <judul> ----------
def fig_contoh():
    s = [f'<defs>{marker(1, BLUE, "xx")}</defs>']
    s.append(f'<rect x="8" y="10" width="284" height="80" rx="12" fill="{PBLUE}"/>')
    s.append(T(150, 56, "ganti dengan gambar sungguhan", 12, BLUE))
    return svg(300, 100, s)

# ---------- Peta belajar (selalu ada, lebar 640) ----------
def fig_map(stops, berikutnya):
    pts = [(55,70),(160,55),(265,80),(370,55),(475,80),(585,110),
           (535,220),(430,240),(325,215),(220,240),(115,215),(40,175)]
    cols = [BLUE,ORG,GRN,PUR,RED,BLUE,ORG,GRN,PUR,RED,BLUE,ORG]
    n = min(len(stops), len(pts))
    s = ['<svg viewBox="0 0 640 330" class="fig" xmlns="http://www.w3.org/2000/svg">']
    d = "M" + " L".join(f"{x},{y}" for x, y in pts[:n])
    s.append(f'<path d="{d}" fill="none" stroke="#dfe6fb" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>')
    s.append(f'<path d="{d}" fill="none" stroke="{YEL}" stroke-width="3" stroke-dasharray="8 7" stroke-linejoin="round"/>')
    for i in range(n):
        x, y = pts[i]; c = cols[i % len(cols)]
        s.append(f'<circle cx="{x}" cy="{y}" r="19" fill="{c}" stroke="#fff" stroke-width="4"/>')
        s.append(T(x, y+5, str(i+1), 13, "#fff"))
        ty = y-28 if i < 6 else y+38
        tx, anchor = x, "middle"
        if i == 0: tx, anchor = 36, "start"
        if i == 5: tx, anchor = 604, "end"
        if i == 11: tx, anchor = 22, "start"
        s.append(T(tx, ty, stops[i], 12, NAVY, "600", "Poppins", anchor))
    s.append(f'<rect x="40" y="290" width="560" height="32" rx="16" fill="{NAVY}"/>')
    s.append(T(320, 311, berikutnya, 12.5, "#fff", "600"))
    s.append('</svg>')
    return "".join(s)

FIG = dict(
    cover=fig_contoh(),          # ganti: maskot sampul, viewBox 440x300
    contoh=fig_contoh(),
    map=fig_map(["Pos 1","Pos 2"], "Berikutnya: <materi>. <ajakan singkat>"),
)
```

## Lampiran B — Template `page.html`

CSS di bawah ini sudah memakai subset aman Bagian 5. **Salin apa adanya**, ganti hanya warna sampul,
judul, dan isinya.

```html
<!DOCTYPE html><html lang="id"><head><meta charset="utf-8"><title>JUDUL MODUL</title>
<style>
@page{size:A4;margin:14mm 14mm 16mm; @bottom-left{content:"JUDUL MODUL · learv.online";font-family:Inter,sans-serif;font-size:8pt;color:#8a93ad} @bottom-right{content:counter(page);font-family:Inter,sans-serif;font-size:8pt;color:#8a93ad}}
@page:first{margin:0; @bottom-left{content:""} @bottom-right{content:""}}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font-family:Inter,'DejaVu Sans',sans-serif;font-size:10.6pt;line-height:1.5;color:#1b2559}
h1,h2,h3,.lbl,.chip,.badge{font-family:Poppins,'DejaVu Sans',sans-serif}
.cover{width:210mm;height:297mm;background:linear-gradient(150deg,#7b5cf0 0%,#3b6ef5 55%,#16a37b 100%);color:#fff;padding:26mm 20mm;position:relative;overflow:hidden}
.cover .kls{display:inline-block;background:rgba(255,255,255,.2);padding:5px 14px;border-radius:20px;font-weight:600;font-size:11pt}
.cover h1{font-size:44pt;line-height:1.05;margin:14px 0 10px}
.cover p.sub{font-size:13pt;max-width:150mm}
.chip{display:inline-block;background:#fff;color:#1b2559;border-radius:20px;padding:5px 13px;font-size:9.5pt;font-weight:600;margin:0 6px 6px 0}
.chips{margin:14px 0 20px}
.cover .mascot{text-align:center;margin-top:6mm}
.cover .foot{position:absolute;bottom:16mm;left:20mm;right:20mm;font-size:10pt}
.cover .foot .kanan{float:right}
.page{page-break-before:always}
.head{border-bottom:2px solid #eef1f8;padding-bottom:8px;margin-bottom:10px}
.head table{width:100%;border:0;margin:0}
.head td{border:0;padding:0;vertical-align:middle}
.badge{width:46px;height:46px;border-radius:14px;color:#fff;font-weight:700;font-size:20pt;text-align:center;line-height:46px}
.head h2{margin:0 0 0 14px;font-size:19pt;line-height:1.15}
.head .an{font-size:10pt;color:#5d6788;margin:2px 0 0 14px}
.box{border-radius:12px;padding:9px 13px;margin:8px 0}
.box .lbl{font-weight:700;font-size:10.5pt;margin-bottom:3px}
.box p{margin:3px 0}
.bay{background:#fff1e6}.bay .lbl{color:#d2661d}
.kon{background:#e9f0ff}.kon .lbl{color:#3b6ef5}
.con{background:#e3f6ef}.con .lbl{color:#0f8a66}
.ing{background:#fff8e1;border:2px dashed #ffc93c}.ing .lbl{color:#a87800}
.awas{background:#fde8ea}.awas .lbl{color:#c9303f}
.coba{background:#efeafe}.coba .lbl{color:#5c3ed6}
.formula{border:2.5px solid #1b2559;border-radius:12px;text-align:center;font-family:Poppins,'DejaVu Sans',sans-serif;font-weight:600;font-size:12.5pt;padding:7px 10px;margin:8px auto;max-width:165mm;background:#fff}
table.two{width:100%;border-collapse:collapse;margin:0}
table.two td{border:0;padding:0;vertical-align:middle}
table.two td.g{width:40%;padding-left:14px}
.fig{width:100%;height:auto;display:block}
ol.st{margin:4px 0;padding-left:20px}ol.st li{margin:2px 0}
ul.dot{margin:3px 0;padding-left:18px}
table.d{border-collapse:collapse;width:100%;margin:6px 0;font-size:10pt}
table.d th{background:#1b2559;color:#fff;font-family:Poppins,'DejaVu Sans',sans-serif;font-weight:600;padding:5px 8px;text-align:left}
table.d td{padding:5px 8px;border-bottom:1px solid #e4e8f2}
table.d tr:nth-child(even) td{background:#f5f7fc}
.ans{font-size:9.6pt;color:#5c3ed6;border-top:1px dashed #b9a9f5;margin-top:5px;padding-top:4px}
.toc td{width:50%;vertical-align:top;padding:3px 8px 3px 0}
.leg{width:100%;border-collapse:separate;border-spacing:6px 0;margin:0 -6px}
.leg td{width:33.33%;vertical-align:top;padding:0}
.leg .box{margin:0 0 8px;font-size:9.4pt;height:100%}
.toc .it{background:#f5f7fc;border-radius:10px;padding:6px 11px}
.toc b{font-family:Poppins,'DejaVu Sans',sans-serif}
.toc span{display:block;font-size:9pt;color:#5d6788}
.card{border-radius:12px;padding:10px 13px;color:#1b2559}
.card h3{margin:0 0 4px;font-size:11.5pt}
.card .f{font-family:Poppins,'DejaVu Sans',sans-serif;font-weight:600;font-size:10.5pt;background:#fff;border-radius:8px;padding:4px 8px;margin:3px 0;display:inline-block}
.card p{margin:3px 0;font-size:9.8pt}
.x,.v{border-radius:10px;padding:6px 10px;font-size:10pt}
.x{background:#fde8ea}.v{background:#e3f6ef}
.x b{color:#c9303f}.v b{color:#0f8a66}
.kunci{border-top:2px dashed #8a93ad;margin-top:12px;padding-top:8px;font-size:9.8pt}
.mini{font-size:9.5pt;color:#5d6788}
/* ikon label kotak — pengganti emoji (aturan 12) */
.ic{width:13px;height:13px;vertical-align:-1.5px;margin-right:5px}
/* pecahan bertumpuk (aturan 13) */
.frac{display:inline-block;vertical-align:-0.42em;text-align:center;font-family:Poppins,'DejaVu Sans',sans-serif;line-height:1.08;margin:0 2px}
.frac .n{display:block;padding:0 3px;border-bottom:1.6px solid currentColor}
.frac .d{display:block;padding:0 3px}
.frac.s{font-size:.9em}
</style></head><body>

<!-- SPRITE IKON — letakkan sekali saja, tepat sesudah <body>. Ikon memakai currentColor,
     jadi warnanya otomatis mengikuti warna judul kotaknya. -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="ic-bay" viewBox="0 0 16 16"><path d="M1.6 4.6h12.8l-1.5 8.4a1 1 0 0 1-1 .8H4.1a1 1 0 0 1-1-.8z" fill="currentColor"/><path d="M5.2 4.6V3.2a2.8 2.8 0 0 1 5.6 0v1.4" fill="none" stroke="currentColor" stroke-width="1.5"/></symbol>
<symbol id="ic-kon" viewBox="0 0 16 16"><circle cx="8" cy="6.4" r="4.4" fill="currentColor"/><rect x="6" y="11" width="4" height="1.5" rx=".7" fill="currentColor"/><rect x="6.4" y="13.2" width="3.2" height="1.5" rx=".7" fill="currentColor"/></symbol>
<symbol id="ic-con" viewBox="0 0 16 16"><path d="M11.4 1.8l2.8 2.8-7.6 7.6-3.5.7.7-3.5z" fill="currentColor"/><path d="M2 14.4h12" stroke="currentColor" stroke-width="1.5"/></symbol>
<symbol id="ic-ing" viewBox="0 0 16 16"><circle cx="8" cy="5.2" r="3.6" fill="currentColor"/><path d="M8 8.8v5.6" stroke="currentColor" stroke-width="1.6"/></symbol>
<symbol id="ic-awas" viewBox="0 0 16 16"><path d="M8 1.6l6.8 12H1.2z" fill="currentColor"/><path d="M8 6v3.6" stroke="#fff" stroke-width="1.5"/><circle cx="8" cy="11.6" r=".9" fill="#fff"/></symbol>
<symbol id="ic-coba" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6.6" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="8" cy="8" r="3.4" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="8" cy="8" r="1.3" fill="currentColor"/></symbol>
</defs></svg>

<!-- CATATAN xhtml2pdf: mesin darurat ini tidak mengenal <use>. Kalau terpaksa memakainya,
     tempelkan isi <symbol> langsung di setiap label. Di Chrome dan WeasyPrint, <use> aman. -->

<!-- SAMPUL -->
<section class="cover">
<span class="kls">MATA PELAJARAN · Kelas X · Modul Bergambar</span>
<h1>JUDUL<br>MODUL</h1>
<p class="sub">Satu paragraf pengantar yang menyebut tiga sampai lima analogi sehari-hari dari modul ini.</p>
<div class="chips"><span class="chip">Topik 1</span><span class="chip">Topik 2</span></div>
<div class="mascot">{{cover}}</div>
<div class="foot">learv.online<span class="kanan">Kalimat maskot yang mengajak</span></div>
</section>

<!-- CARA PAKAI + DAFTAR ISI -->
<section class="page">
<div class="head"><table><tr><td width="46"><div class="badge" style="background:#1b2559">★</div></td>
<td><h2>Cara Pakai Modul Ini</h2><div class="an">Setiap kotak warna punya tugasnya sendiri</div></td></tr></table></div>
<table class="leg"><tr>
<td><div class="box bay"><div class="lbl"><svg class="ic"><use href="#ic-bay"/></svg>Bayangkan…</div>Cerita sehari-hari pembuka bab.</div></td>
<td><div class="box kon"><div class="lbl"><svg class="ic"><use href="#ic-kon"/></svg>Konsepnya</div>Inti materi dan rumusnya.</div></td>
<td><div class="box con"><div class="lbl"><svg class="ic"><use href="#ic-con"/></svg>Contoh</div>Langkah demi langkah dengan cek.</div></td>
</tr><tr>
<td><div class="box ing"><div class="lbl"><svg class="ic"><use href="#ic-ing"/></svg>Ingat!</div>Trik dan jembatan keledai.</div></td>
<td><div class="box awas"><div class="lbl"><svg class="ic"><use href="#ic-awas"/></svg>Awas Jebakan</div>Kesalahan yang sering terjadi.</div></td>
<td><div class="box coba"><div class="lbl"><svg class="ic"><use href="#ic-coba"/></svg>Coba Sendiri</div>Soal mini dan jawabannya.</div></td>
</tr></table>
<h3 style="margin:16px 0 8px;font-size:14pt">Daftar Isi</h3>
<table class="toc">
<tr><td><div class="it"><b>1. Judul Bab</b><span>subjudul analogi</span></div></td>
    <td><div class="it"><b>2. Judul Bab</b><span>subjudul analogi</span></div></td></tr>
</table>
</section>

<!-- BAB 1 -->
<section class="page">
<div class="head"><table><tr><td width="46"><div class="badge" style="background:#3b6ef5">1</div></td>
<td><h2>Judul Bab</h2><div class="an">subjudul analogi</div></td></tr></table></div>
<table class="two"><tr><td class="t">
<div class="box bay"><div class="lbl"><svg class="ic"><use href="#ic-bay"/></svg>Bayangkan…</div><p>Cerita pembuka.</p></div>
<div class="box kon"><div class="lbl"><svg class="ic"><use href="#ic-kon"/></svg>Konsepnya</div><p>Inti materi.</p></div>
</td><td class="g">{{contoh}}</td></tr></table>
<div class="formula">rumus penting</div>
<div class="box con"><div class="lbl"><svg class="ic"><use href="#ic-con"/></svg>Contoh</div>
<ol class="st"><li>Langkah satu.</li><li>Langkah dua. <span class="mini">Cek: … ✓</span></li></ol></div>
<div class="box ing"><div class="lbl"><svg class="ic"><use href="#ic-ing"/></svg>Ingat!</div><p>Trik, dua kalimat.</p></div>
<div class="box awas"><div class="lbl"><svg class="ic"><use href="#ic-awas"/></svg>Awas Jebakan</div><p>Kesalahan khas bab ini.</p></div>
<div class="box coba"><div class="lbl"><svg class="ic"><use href="#ic-coba"/></svg>Coba Sendiri</div><p>Soal mini.</p>
<div class="ans">Jawaban: …</div></div>
</section>

<!-- BAB PETA BELAJAR (terakhir) -->
<section class="page">
<div class="head"><table><tr><td width="46"><div class="badge" style="background:#1b2559">16</div></td>
<td><h2>Peta Belajar</h2><div class="an">Centang setiap pos yang sudah kamu kuasai</div></td></tr></table></div>
{{map}}
<table class="d"><tr><th>Pos</th><th>Aku sudah bisa…</th><th>✓</th></tr>
<tr><td>1. …</td><td>…</td><td>☐</td></tr></table>
<div class="box bay"><div class="lbl">🛒 Tantangan penutup</div><p>Kegiatan nyata di rumah atau di kelas.</p></div>
</section>
</body></html>
```

## Lampiran C — Template `render.py`

Mencoba Chrome → WeasyPrint → xhtml2pdf, memakai mesin pertama yang tersedia.

```python
# render.py — ganti NAMA sesuai modul
import os, sys, importlib
BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "Modul_Nama.pdf")
HTML = os.path.join(BASE, "modul.html")

# 1) gabungkan FIG ke page.html
ns = {}
exec(open(os.path.join(BASE, "build.py"), encoding="utf-8").read(), ns)
h = open(os.path.join(BASE, "page.html"), encoding="utf-8").read()
for k, v in ns["FIG"].items():
    h = h.replace("{{" + k + "}}", v)
assert "{{" not in h, "masih ada placeholder yang belum diganti: " + h[h.index("{{"):h.index("{{")+30]
open(HTML, "w", encoding="utf-8").write(h)

def ada(m):
    try: importlib.import_module(m); return True
    except Exception: return False

# 2) pilih mesin render
if ada("playwright"):
    import asyncio
    from playwright.async_api import async_playwright
    async def main():
        async with async_playwright() as p:
            b = await p.chromium.launch(args=["--no-sandbox"])
            pg = await b.new_page()
            await pg.goto("file://" + HTML); await pg.wait_for_timeout(800)
            await pg.pdf(path=OUT, format="A4", print_background=True, prefer_css_page_size=True)
            await b.close()
    asyncio.run(main()); mesin = "chrome/playwright"

elif ada("weasyprint"):
    from weasyprint import HTML as WH
    WH(filename=HTML).write_pdf(OUT); mesin = "weasyprint"

elif ada("xhtml2pdf"):
    from xhtml2pdf import pisa
    with open(OUT, "wb") as f:
        pisa.CreatePDF(open(HTML, encoding="utf-8").read(), dest=f)
    mesin = "xhtml2pdf (darurat, periksa hasilnya ekstra teliti)"

else:
    sys.exit("TIDAK ADA MESIN RENDER. Laporkan ke pengguna, jangan memaksakan hasil.")

# 3) laporan singkat
try:
    import fitz; n = fitz.open(OUT).page_count
except Exception:
    n = "?"
print(f"selesai: {OUT} · mesin: {mesin} · halaman: {n}")
```

## Lampiran D — Aturan memperbarui catatan progres

Tabel di `progres-materi-bergambar.md` memakai kolom persis ini:

```
| Tanggal | Mata pelajaran | Materi | id buku | Sumber | Status di situs |
```

Baris baru ditulis seperti ini (kolom Materi memuat judul buku, jumlah halaman, dan daftar bab singkat):

```
| 2026-11-11 | Matematika (Kelas 7) | Garis dan Sudut ("Garis & Sudut Itu Tajam!", 18 hlm, 16 bab: titik/garis/sinar/ruas, kedudukan dua garis, satuan sudut, busur derajat, jenis sudut, sudut jarum jam, penyiku & pelurus, bertolak belakang, garis sejajar & transversal, F/Z/C + kail, sudut segitiga, melukis dengan jangka, jebakan, ringkasan, latihan, peta) | garis-sudut | modul-sumber/garis-sudut.md | belum diunggah |
```

Lalu di bagian **Antrean**: hapus materi yang baru dibuat, geser nomornya, dan beri tanda `← berikutnya`
pada nomor 1. Tambahkan juga satu kalimat di bagian "Topik yang sudah tercakup" kalau modul baru ini
sudah memuat sebagian materi dari antrean berikutnya (supaya tidak dibuat dua kali).

Semua bagian lain (**Arahan pengguna**, **Catatan teknis**, daftar buku yang sudah ada di situs)
**disalin utuh**, jangan dipotong atau diringkas.<symbol id="ic-con" viewBox="0 0 16 16"><path d="M11.4 1.8l2.8 2.8-7.6 7.6-3.5.7.7-3.5z" fill="currentColor"/><path d="M2 14.4h12" stroke="currentColor" stroke-width="1.5"/></symbol>
<symbol id="ic-ing" viewBox="0 0 16 16"><circle cx="8" cy="5.2" r="3.6" fill="currentColor"/><path d="M8 8.8v5.6" stroke="currentColor" stroke-width="1.6"/></symbol>
<symbol id="ic-awas" viewBox="0 0 16 16"><path d="M8 1.6l6.8 12H1.2z" fill="currentColor"/><path d="M8 6v3.6" stroke="#fff" stroke-width="1.5"/><circle cx="8" cy="11.6" r=".9" fill="#fff"/></symbol>
<symbol id="ic-coba" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6.6" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="8" cy="8" r="3.4" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="8" cy="8" r="1.3" fill="currentColor"/></symbol>
</defs></svg>

<!-- CATATAN xhtml2pdf: mesin darurat ini tidak mengenal <use>. Kalau terpaksa memakainya,
     tempelkan isi <symbol> langsung di setiap label. Di Chrome dan WeasyPrint, <use> aman. -->

<!-- SAMPUL -->
<section class="cover">
<span class="kls">MATA PELAJARAN · Kelas X · Modul Bergambar</span>
<h1>JUDUL<br>MODUL</h1>
<p class="sub">Satu paragraf pengantar yang menyebut tiga sampai lima analogi sehari-hari dari modul ini.</p>
<div class="chips"><span class="chip">Topik 1</span><span class="chip">Topik 2</span></div>
<div class="mascot">{{cover}}</div>
<div class="foot">learv.online<span class="kanan">Kalimat maskot yang mengajak</span></div>
</section>

<!-- CARA PAKAI + DAFTAR ISI -->
<section class="page">
<div class="head"><table><tr><td width="46"><div class="badge" style="background:#1b2559">★</div></td>
<td><h2>Cara Pakai Modul Ini</h2><div class="an">Setiap kotak warna punya tugasnya sendiri</div></td></tr></table></div>
<table class="leg"><tr>
<td><div class="box bay"><div class="lbl"><svg class="ic"><use href="#ic-bay"/></svg>Bayangkan…</div>Cerita sehari-hari pembuka bab.</div></td>
<td><div class="box kon"><div class="lbl"><svg class="ic"><use href="#ic-kon"/></svg>Konsepnya</div>Inti materi dan rumusnya.</div></td>
<td><div class="box con"><div class="lbl"><svg class="ic"><use href="#ic-con"/></svg>Contoh</div>Langkah demi langkah dengan cek.</div></td>
</tr><tr>
<td><div class="box ing"><div class="lbl"><svg class="ic"><use href="#ic-ing"/></svg>Ingat!</div>Trik dan jembatan keledai.</div></td>
<td><div class="box awas"><div class="lbl"><svg class="ic"><use href="#ic-awas"/></svg>Awas Jebakan</div>Kesalahan yang sering terjadi.</div></td>
<td><div class="box coba"><div class="lbl"><svg class="ic"><use href="#ic-coba"/></svg>Coba Sendiri</div>Soal mini dan jawabannya.</div></td>
</tr></table>
<h3 style="margin:16px 0 8px;font-size:14pt">Daftar Isi</h3>
<table class="toc">
<tr><td><div class="it"><b>1. Judul Bab</b><span>subjudul analogi</span></div></td>
    <td><div class="it"><b>2. Judul Bab</b><span>subjudul analogi</span></div></td></tr>
</table>
</section>

<!-- BAB 1 -->
<section class="page">
<div class="head"><table><tr><td width="46"><div class="badge" style="background:#3b6ef5">1</div></td>
<td><h2>Judul Bab</h2><div class="an">subjudul analogi</div></td></tr></table></div>
<table class="two"><tr><td class="t">
<div class="box bay"><div class="lbl"><svg class="ic"><use href="#ic-bay"/></svg>Bayangkan…</div><p>Cerita pembuka.</p></div>
<div class="box kon"><div class="lbl"><svg class="ic"><use href="#ic-kon"/></svg>Konsepnya</div><p>Inti materi.</p></div>
</td><td class="g">{{contoh}}</td></tr></table>
<div class="formula">rumus penting</div>
<div class="box con"><div class="lbl"><svg class="ic"><use href="#ic-con"/></svg>Contoh</div>
<ol class="st"><li>Langkah satu.</li><li>Langkah dua. <span class="mini">Cek: … ✓</span></li></ol></div>
<div class="box ing"><div class="lbl"><svg class="ic"><use href="#ic-ing"/></svg>Ingat!</div><p>Trik, dua kalimat.</p></div>
<div class="box awas"><div class="lbl"><svg class="ic"><use href="#ic-awas"/></svg>Awas Jebakan</div><p>Kesalahan khas bab ini.</p></div>
<div class="box coba"><div class="lbl"><svg class="ic"><use href="#ic-coba"/></svg>Coba Sendiri</div><p>Soal mini.</p>
<div class="ans">Jawaban: …</div></div>
</section>

<!-- BAB PETA BELAJAR (terakhir) -->
<section class="page">
<div class="head"><table><tr><td width="46"><div class="badge" style="background:#1b2559">16</div></td>
<td><h2>Peta Belajar</h2><div class="an">Centang setiap pos yang sudah kamu kuasai</div></td></tr></table></div>
{{map}}
<table class="d"><tr><th>Pos</th><th>Aku sudah bisa…</th><th>✓</th></tr>
<tr><td>1. …</td><td>…</td><td>☐</td></tr></table>
<div class="box bay"><div class="lbl">🛒 Tantangan penutup</div><p>Kegiatan nyata di rumah atau di kelas.</p></div>
</section>
</body></html>
```

## Lampiran C — Template `render.py`

Mencoba Chrome → WeasyPrint → xhtml2pdf, memakai mesin pertama yang tersedia.

```python
# render.py — ganti NAMA sesuai modul
import os, sys, importlib
BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "Modul_Nama.pdf")
HTML = os.path.join(BASE, "modul.html")

# 1) gabungkan FIG ke page.html
ns = {}
exec(open(os.path.join(BASE, "build.py"), encoding="utf-8").read(), ns)
h = open(os.path.join(BASE, "page.html"), encoding="utf-8").read()
for k, v in ns["FIG"].items():
    h = h.replace("{{" + k + "}}", v)
assert "{{" not in h, "masih ada placeholder yang belum diganti: " + h[h.index("{{"):h.index("{{")+30]
open(HTML, "w", encoding="utf-8").write(h)

def ada(m):
    try: importlib.import_module(m); return True
    except Exception: return False

# 2) pilih mesin render
if ada("playwright"):
    import asyncio
    from playwright.async_api import async_playwright
    async def main():
        async with async_playwright() as p:
            b = await p.chromium.launch(args=["--no-sandbox"])
            pg = await b.new_page()
            await pg.goto("file://" + HTML); await pg.wait_for_timeout(800)
            await pg.pdf(path=OUT, format="A4", print_background=True, prefer_css_page_size=True)
            await b.close()
    asyncio.run(main()); mesin = "chrome/playwright"

elif ada("weasyprint"):
    from weasyprint import HTML as WH
    WH(filename=HTML).write_pdf(OUT); mesin = "weasyprint"

elif ada("xhtml2pdf"):
    from xhtml2pdf import pisa
    with open(OUT, "wb") as f:
        pisa.CreatePDF(open(HTML, encoding="utf-8").read(), dest=f)
    mesin = "xhtml2pdf (darurat, periksa hasilnya ekstra teliti)"

else:
    sys.exit("TIDAK ADA MESIN RENDER. Laporkan ke pengguna, jangan memaksakan hasil.")

# 3) laporan singkat
try:
    import fitz; n = fitz.open(OUT).page_count
except Exception:
    n = "?"
print(f"selesai: {OUT} · mesin: {mesin} · halaman: {n}")
```

## Lampiran D — Aturan memperbarui catatan progres

Tabel di `progres-materi-bergambar.md` memakai kolom persis ini:

```
| Tanggal | Mata pelajaran | Materi | id buku | Sumber | Status di situs |
```

Baris baru ditulis seperti ini (kolom Materi memuat judul buku, jumlah halaman, dan daftar bab singkat):

```
| 2026-11-11 | Matematika (Kelas 7) | Garis dan Sudut ("Garis & Sudut Itu Tajam!", 18 hlm, 16 bab: titik/garis/sinar/ruas, kedudukan dua garis, satuan sudut, busur derajat, jenis sudut, sudut jarum jam, penyiku & pelurus, bertolak belakang, garis sejajar & transversal, F/Z/C + kail, sudut segitiga, melukis dengan jangka, jebakan, ringkasan, latihan, peta) | garis-sudut | modul-sumber/garis-sudut.md | belum diunggah |
```

Lalu di bagian **Antrean**: hapus materi yang baru dibuat, geser nomornya, dan beri tanda `← berikutnya`
pada nomor 1. Tambahkan juga satu kalimat di bagian "Topik yang sudah tercakup" kalau modul baru ini
sudah memuat sebagian materi dari antrean berikutnya (supaya tidak dibuat dua kali).

Semua bagian lain (**Arahan pengguna**, **Catatan teknis**, daftar buku yang sudah ada di situs)
**disalin utuh**, jangan dipotong atau diringkas.