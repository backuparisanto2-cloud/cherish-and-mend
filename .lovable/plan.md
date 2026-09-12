# Bantuan & Mulai Ulang pada Menu WhatsApp

Menyempurnakan alur menu chatbot agar warga tetap disapa hangat tanpa nama, dapat memilih layanan dengan format yang konsisten, serta selalu memiliki jalan keluar saat bingung.

## Perubahan

- Gunakan sapaan berdasarkan waktu tanpa nama ketika username WhatsApp kosong, berupa nomor, atau tidak layak ditampilkan.
- Ringkas menu utama menjadi daftar pilihan bernomor yang jelas dan konsisten untuk diketik atau dipilih melalui kontrol WhatsApp bila tersedia.
- Tambahkan pilihan `8 — Bantuan` dan `0 — Mulai ulang` pada menu utama.
- Terima perintah teks `help`, `bantuan`, `mulai ulang`, `start over`, dan `restart` secara konsisten, selain pilihan angka.
- Balasan Bantuan menjelaskan cara memilih menu, kembali ke awal, bertanya dengan kalimat biasa, dan menghubungi operator.
- Perintah Mulai ulang selalu mengosongkan posisi menu lalu menampilkan menu utama tanpa memicu sapaan AI berulang.

## Perilaku yang dipertahankan

- Sapaan personal memakai nama WhatsApp bila tersedia.
- Sapaan dan menu tetap dikirim sebagai dua pesan berurutan.
- Navigasi submenu, eskalasi petugas, basis pengetahuan, dan efek mengetik tetap berjalan seperti sekarang.

## Verifikasi

- Uji sapaan dengan nama kosong, spasi, nomor telepon, dan nama valid.
- Uji pilihan `1–7`, `8`, `0`, serta semua kata perintah Bantuan/Mulai ulang dari menu utama maupun submenu.
- Pastikan status menu kembali ke awal setelah Mulai ulang dan aplikasi tetap lolos pemeriksaan.
