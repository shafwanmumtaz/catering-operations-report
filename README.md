# Sistem Rekapitulasi Distribusi Porsi Katering B2B & Pelaporan Inventaris

👤 **Penyusun:** Shafwan Mumtaz (Staf Operasional & Inventaris — PT Mumtaz Catering)  
📊 **Tools:** Microsoft Excel & Python (`pandas`)

---

## 1. Latar Belakang Operasional

Dalam operasional katering korporat (B2B) di **PT Mumtaz Catering**, pengiriman makanan karyawan dilakukan setiap hari terbagi ke dalam tiga jadwal shift utama:
- **Lunch** (Makan Siang)
- **Dinner** (Makan Malam)
- **Supper** (Makan Larut Malam)

Pencatatan yang presisi sangat krusial agar jumlah porsi yang dikirim sesuai dengan surat jalan harian, meminimalkan selisih bahan baku (*food waste*), serta memastikan tagihan periode (*billing cycle*) untuk klien korporat seperti **Pakons Prime Hotel** (516 porsi per periode rekap) tervalidasi 100% akurat.

---

## 2. Alur Rekapitulasi & Pengendalian Inventaris

1. **Pencatatan Harian per Shift:** Mencatat jumlah porsi pesanan dan realisasi pengiriman pada shift *Lunch*, *Dinner*, dan *Supper*.
2. **Rekonsiliasi Siklus Tagihan (*Billing Reconciliation*):** Mengagregasi total porsi per periode menggunakan Microsoft Excel untuk diverifikasi bersama pihak administrasi klien sebelum penerbitan *invoice*.
3. **Pemantauan Stok Bahan Baku:** Membandingkan volume porsi keluar dengan penggunaan bahan baku utama di dapur produksi guna menjaga efisiensi operasional (*cost control*).

---

## 3. Struktur File Repositori

```text
├── data/
│   └── rekap_distribusi_porsi_b2b_sample.csv   # Contoh tabel rekapitulasi distribusi 516 porsi (Lunch, Dinner, Supper)
├── rekap_distribusi.py                         # Skrip Python untuk memvalidasi total porsi per shift & periode
└── README.md                                   # Dokumentasi sistem pelaporan operasional
```
