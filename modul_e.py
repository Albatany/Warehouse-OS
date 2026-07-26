from dataclasses import dataclass
import csv

@dataclass
class Barang:
    id_resi: int
    kode_barang: str
    nama_barang: str
    harga: int
    tahun_kedaluwarsa: int
    kondisi_fisik: str
    nomor_rak: int
    tanggal_masuk: str
    jumlah: int

def load_data(path: str = "data_barang.csv") -> list[Barang]:
    data: list[Barang] = []
    with open(path, newline="", encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(
                Barang(
                    id_resi=int(row["id_resi"]),
                    kode_barang=row["kode_barang"],
                    nama_barang=row["nama_barang"],
                    harga=int(row["harga"]),
                    tahun_kedaluwarsa=int(row["tahun_kedaluwarsa"]),
                    kondisi_fisik=row["kondisi_fisik"],
                    nomor_rak=int(row["nomor_rak"]),
                    tanggal_masuk=row["tanggal_masuk"],
                    jumlah=int(row["jumlah"]),
                )
            )
    return data

class HashTableLokasiRak:
    def __init__(self, size: int = 101):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, kode_barang: str) -> int:
        total = sum(ord(ch) for ch in kode_barang)
        return total % self.size

    def insert(self, kode_barang: str, nomor_rak: int) -> None:
        index = self._hash(kode_barang)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == kode_barang:
                bucket[i] = (kode_barang, nomor_rak)
                return
        bucket.append((kode_barang, nomor_rak))

    def get(self, kode_barang: str):
        index = self._hash(kode_barang)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == kode_barang:
                return v
        return None

def build_hash_table(data: list[Barang]) -> HashTableLokasiRak:
    ht = HashTableLokasiRak()
    for b in data:
        ht.insert(b.kode_barang, b.nomor_rak)
    return ht

def simpan_peta_ke_csv(path: str, data: list[Barang], ht: HashTableLokasiRak):
    with open(path, "w", newline="", encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerow(["kode_barang", "nomor_rak"])

        sudah = set()
        for b in data:
            if b.kode_barang not in sudah:
                rak = ht.get(b.kode_barang)
                writer.writerow([b.kode_barang, rak])
                sudah.add(b.kode_barang)

    print(f"\nFile mapping berhasil dibuat → {path}")

def main():
    data = load_data()
    ht = build_hash_table(data)

    print("\n==============================================")
    print("        Kode_Barang  →  Nomor_Rak")
    print("==============================================")

    sudah = set()
    for b in data:
        if b.kode_barang not in sudah:
            rak = ht.get(b.kode_barang)
            print(f"{b.kode_barang:<15} →  Rak {rak}")
            sudah.add(b.kode_barang)

    simpan_peta_ke_csv("data_peta.csv", data, ht)

    print("\nTotal kode barang unik :", len(sudah))
    print("Semua data berhasil dipetakan ke hash table.")

if __name__ == "__main__":
    main()