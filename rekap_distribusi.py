import csv

def verifikasi_rekap(csv_path: str):
    total_lunch = 0
    total_dinner = 0
    total_supper = 0
    total_keseluruhan = 0
    jumlah_hari = 0

    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            l = int(row["Shift_Lunch"])
            d = int(row["Shift_Dinner"])
            s = int(row["Shift_Supper"])
            t = int(row["Total_Porsi_Harian"])
            assert l + d + s == t, f"Selisih hitung pada tanggal {row['Tanggal']}"
            total_lunch += l
            total_dinner += d
            total_supper += s
            total_keseluruhan += t
            jumlah_hari += 1

    print("=== Rekapitulasi Distribusi Porsi Katering B2B (Pakons Prime Hotel) ===")
    print(f"Jumlah Hari Periode : {jumlah_hari} hari")
    print(f"Total Shift Lunch   : {total_lunch} porsi")
    print(f"Total Shift Dinner  : {total_dinner} porsi")
    print(f"Total Shift Supper  : {total_supper} porsi")
    print(f"Total Keseluruhan   : {total_keseluruhan} porsi (100% Tervalidasi)")

if __name__ == "__main__":
    verifikasi_rekap("data/rekap_distribusi_porsi_b2b_sample.csv")
