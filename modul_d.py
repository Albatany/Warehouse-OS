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

def load_data(path: str = "data_barang_c.csv") -> list[Barang]:
    data: list[Barang] = []
    with open(path, newline="", encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get("id_resi"):
                continue
            try:
                id_resi = int(row["id_resi"])
            except ValueError:
                continue

            data.append(
                Barang(
                    id_resi=id_resi,
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

def quicksortaziz(data: list[Barang]) -> list[Barang]:
    if len(data) <= 1:
        return data[:]
    pivot = data[len(data) // 2].id_resi
    left = [b for b in data if b.id_resi < pivot]
    middle = [b for b in data if b.id_resi == pivot]
    right = [b for b in data if b.id_resi > pivot]
    return quicksortaziz(left) + middle + quicksortaziz(right)

def linearsearch(data: list[Barang], keyword: str) -> list[Barang]:
    hasil: list[Barang] = []
    key = keyword.lower()
    for b in data:
        if key in b.nama_barang.lower():
            hasil.append(b)
    return hasil

def binarysearch(sorted_data: list[Barang], target: int) -> Barang | None:
    low = 0
    high = len(sorted_data) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_id = sorted_data[mid].id_resi
        if mid_id == target:
            return sorted_data[mid]
        elif mid_id < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

def tampilkan(b: Barang) -> None:
    print(f"[{b.id_resi}] {b.nama_barang} | Rak {b.nomor_rak}")

def main():
    data = load_data()
    print("[WareHouse OS 2.1] Pencarian Barang")
    print("------")
    print("1. Cari berdasarkan nama (Linear Search)")
    print("2. Cari berdasarkan id resi (Binary Search)")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        key = input("Masukkan kata kunci nama barang: ")
        hasil = linearsearch(data, key)
        if not hasil:
            print("Tidak ada barang dengan nama tersebut")
        else:
            for b in hasil:
                tampilkan(b)

    elif pilihan == "2":
        sorted_data = quicksortaziz(data)
        target = int(input("Masukkan id resi: "))
        b = binarysearch(sorted_data, target)
        if b is None:
            print("Barang dengan id tersebut tidak ditemukan")
        else:
            tampilkan(b)

if __name__ == "__main__":
    main()