# PROGRES Modul PDF Bergambar learv.online
Format baris: | tanggal | mata pelajaran | materi (judul, jumlah halaman, daftar bab) | id buku | sumber | status di situs |

## Sudah dibuat — JANGAN DIULANG
Matematika : aljabar · bilangan-bulat · pecahan-desimal · perbandingan · statistika-peluang ·
             soal-cerita-logika · aritmetika-sosial · trigonometri · limit-turunan · himpunan ·
             garis-sudut · segi-empat-segitiga · relasi-fungsi
Fisika     : gerak-gaya · listrik-dinamis · gelombang-optik
Kimia      : struktur-atom · ikatan-kimia · reaksi-redoks
Biologi    : keanekaragaman-hayati · fotosintesis · sistem-organ · genetika-evolusi
Lainnya    : sejarah-indonesia · english-grammar · mengelola-uang · literasi-digital ·
             berbicara-depan-umum

## Riwayat modul yang dibuat

| Tanggal | Mata pelajaran | Materi | id buku | Sumber | Status di situs |
|---|---|---|---|---|---|
| 2026-11-12 | Matematika (Kelas VII–VIII) | Segi Empat dan Segitiga Itu Asyik! (18 hlm, 16 bab: pengenalan; persegi; persegi panjang; jajargenjang; belah ketupat; layang-layang; trapesium; jenis segitiga; keliling; luas segitiga; bangun gabungan; satuan; jebakan; ringkasan; latihan; peta) | segi-empat-segitiga | modul-segi-empat-segitiga/modul-sumber.md (+ build.py, page.html, render.py) | PDF, sumber, dan kode tersimpan di GitHub; belum diunggah ke learv.online |
| 2026-11-13 | Matematika (Kelas VIII) | Relasi dan Fungsi Itu Jelas! (18 hlm, 16 bab: pasangan dan himpunan; perkalian Kartesius; pasangan berurutan; pengertian relasi; penyajian relasi; diagram panah; domain/kodomain/range; pengertian fungsi; uji fungsi; jenis pemetaan; notasi fungsi; penerapan; jebakan; ringkasan; latihan; peta) | relasi-fungsi | Paket_Sumber_Relasi_dan_Fungsi.zip (lampiran; folder GitHub belum terunggah) | PDF, sumber, dan kode selesai dibuat serta QA; folder belum dapat dipush karena konektor tidak menyediakan transfer berkas lokal; PDF tidak diunggah ke repository/learv.online |

## Sudah tercakup buku Aljabar — jangan dibuat ulang
Bentuk aljabar dan operasinya, sifat operasi, pangkat dan bentuk akar, pecahan aljabar,
persamaan dan pertidaksamaan linear, SPLDV, persamaan kuadrat dan parabola, polinomial,
faktorisasi, fungsi dan grafik (fungsi linear/gradien, komposisi, invers), barisan dan deret.
Catatan: modul Garis dan Sudut sudah memuat jumlah sudut segitiga, sudut luar, dan segitiga
sama kaki dari sisi sudutnya — modul Segi Empat dan Segitiga cukup fokus pada jenis bangun,
keliling, dan luas.
Catatan tambahan: modul `segi-empat-segitiga` mencakup klasifikasi segi empat dan segitiga menurut sisi,
keliling, luas bangun tunggal dan gabungan, serta satuan. Pembahasan sudut tidak diulang.
Catatan tambahan: modul `relasi-fungsi` mencakup relasi, perkalian Kartesius, pasangan berurutan,
diagram panah, domain/kodomain/range, definisi dan uji fungsi, pola satu-satu/banyak-ke-satu/into/onto,
notasi f(a), dan penerapan dasar. Fungsi linear/gradien, komposisi, serta invers tetap mengikuti buku Aljabar.

## Antrean (Matematika dulu sampai habis)
1. Teorema Pythagoras   ← berikutnya
2. Lingkaran
3. Bangun Ruang Sisi Datar
4. Transformasi Geometri
5. Kesebangunan dan Kekongruenan
6. Bangun Ruang Sisi Lengkung
Sesudah Matematika habis: Fisika, Kimia, Biologi, Sejarah, Bahasa Inggris, Keterampilan Hidup
(antrean topiknya disusun saat gilirannya tiba).

## Arahan pengguna
- Judul buku boleh berbeda dari judul materi, asalkan memakai pola "<Materi> Itu <sifat>!".
- Modul dibuat satu per hari, satu modul per percakapan.
- Hasil modul disimpan ke GitHub repository `VanQue-Dev/Book-Order` atas arahan terbaru pengguna; ketentuan ini mengesampingkan larangan unggah ke GitHub di SPEC lama untuk tugas ini.
- Jangan mengunggah ke learv.online.
- Setiap modul baru wajib memiliki folder root `modul-<id>` berisi README.md, modul-sumber.md, build.py, page.html, render.py, dan PDF final jika upload biner GitHub didukung. PROGRES.md diperbarui dalam eksekusi yang sama.

Catatan eksekusi 2026-11-13: PDF final dan paket sumber lengkap sudah disiapkan serta dilampirkan. Pembaruan PROGRES di repository dilakukan terpisah untuk mencegah modul dibuat ulang; folder `modul-relasi-fungsi` belum ada di GitHub karena jalur transfer file lokal ke konektor tidak tersedia pada runtime ini.
