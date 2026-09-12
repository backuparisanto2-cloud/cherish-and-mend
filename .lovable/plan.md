# Sapaan Natural, Sapaan Personal & Efek Mengetik

Membuat pembuka percakapan chatbot Purworejo terasa manusiawi: menyapa warga dengan namanya, ditulis oleh AI (bukan template), lalu menu layanan muncul menyusul dengan jeda singkat seperti orang mengetik.

## Yang akan dirasakan warga

Saat warga mengirim "halo":

1. Muncul jeda singkat, lalu pesan pertama: sapaan personal, mis. "Halo Bu Rina, selamat sore. Ada yang bisa saya bantu hari ini?"
2. Beberapa saat kemudian pesan kedua: daftar menu layanan.

Kalau nama warga tidak diketahui, sapaan tetap hangat tanpa nama ("Halo, selamat sore.").

## Karakter chatbot (soul)

Ditanamkan sebagai aturan tetap untuk semua jawaban AI:

- **Humble** — rendah hati, tidak menggurui, tidak sok tahu.
- **Jelas** — akurat, ringkas, terstruktur, tidak bertele-tele.
- **Melayani** — responsif, sabar, solutif, fokus pada kebutuhan warga.

Gaya bahasa: sederhana, ramah, sopan, Bahasa Indonesia sehari-hari, tanpa kalimat kaku/berulang. Jawaban pendek untuk pertanyaan pendek, dan selalu ditutup dengan satu kalimat ajakan lanjut supaya percakapan tidak menggantung.

## Kecepatan & efek mengetik

- Jeda mengetik dihitung dari panjang pesan, dengan batas atas ~2,5 detik. Tidak ada jeda dibuat-buat untuk "kesan berpikir".
- Sapaan dan menu dikirim sebagai dua pesan berurutan; jeda di antaranya singkat dan proporsional.
- Kalau AI belum menjawab dalam ~3 detik, warga lebih dulu menerima "Sebentar, saya cek informasinya dulu." lalu jawabannya menyusul.
- Batas tunggu AI diperketat dari 10 detik ke ~7 detik; kalau lewat, jawaban kata kunci dari basis pengetahuan langsung dipakai supaya warga tidak menunggu.
- Indikator "sedang mengetik..." asli di WhatsApp hanya bisa muncul kalau Chatera menyediakan endpoint presence/typing. Saya akan cek dokumentasi/endpoint-nya; kalau tidak tersedia, efeknya diwujudkan lewat jeda + pesan berurutan seperti di atas.

## Cakupan yang tidak berubah

Navigasi menu angka, isi naskah resmi, alur eskalasi ke petugas, dan survei penutup tetap seperti sekarang. Fokus tahap ini hanya alur pembuka dan gaya bicara.

## Rincian teknis

- `src/lib/chatera-bot.server.ts`
  - Tambah `AI_PERSONA` (humble/jelas/melayani + aturan gaya, panjang, penutup) dan pakai di `AI_SYSTEM_PROMPT` untuk semua jawaban AI.
  - Tambah `resolveGreetingReply(name)`: AI menyusun satu kalimat sapaan personal berdasarkan nama + waktu lokal (Asia/Jakarta) dengan timeout ~4 detik; gagal/timeout jatuh ke sapaan sopan siap-pakai berbasis waktu. Hasil: `{ greeting, menu }` dua pesan.
  - `resolveReply` mengembalikan daftar pesan (`messages: string[]`) sebagai ganti satu `reply`, plus `typingDelayMs` per pesan; jalur menu/KB/eskalasi mengisi satu pesan saja agar perilaku lama tetap.
  - Tambah `sendBotMessages(ctx, messages)` yang mengirim berurutan dengan jeda `typingDelayFor(text)` (≈35 ms/karakter, min 500 ms, maks 2.500 ms) dan, bila endpoint typing Chatera tersedia, mengirim sinyal typing sebelum tiap pesan.
  - `AI_TIMEOUT_MS` 10.000 → 7.000; tambah pesan tunggu "Sebentar, saya cek informasinya dulu." bila AI belum selesai dalam 3.000 ms.
- `src/lib/chatera-webhook.server.ts`
  - Ambil nama pengirim (`payload.data.sender.name`, fallback ke `contacts.name`) dan teruskan ke `resolveReply`.
  - Ganti pemanggilan `sendBotReply` tunggal dengan `sendBotMessages`; status percakapan, `current_menu_path`, dan `awaiting_operator_confirmation` diperbarui setelah pesan terakhir terkirim, seperti sekarang.
  - Sapaan personal hanya untuk pesan pembuka (greeting saat `current_menu_path` kosong), bukan setiap pesan.
- Verifikasi: unit-cek `resolveReply` untuk input sapaan/angka/pertanyaan bebas, lalu simulasi webhook (payload bertanda tangan) untuk memastikan dua pesan terkirim berurutan dan status percakapan tetap benar.
