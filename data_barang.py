# Muhammad Aziz Syah Dani
# F1E325063 
# (Implementasi Gabungan semua kode dari Modul A sampai Modul E menjadi OS Sederhana.)

from dataclasses import dataclass
from typing import List, Optional
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

def load_data_from_csv(path: str) -> List[Barang]:
    data: List[Barang] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(
                Barang(
                    id_resi = int(row["id_resi"]),
                    kode_barang = row["kode_barang"],
                    nama_barang = row["nama_barang"],
                    harga = int(row["harga"]),
                    tahun_kedaluwarsa = int(row["tahun_kedaluwarsa"]),
                    kondisi_fisik = row["kondisi_fisik"],
                    nomor_rak = int(row["nomor_rak"]),
                    tanggal_masuk = row["tanggal_masuk"],
                    jumlah = int(row["jumlah"]),
                )
            )
    return data

# Modul A: Input barang
def input_barang(data: List[Barang]) -> None:
    print("[Input Barang Baru]")
    kondisi = input("Kondisi fisik barang (Baik/Rusak): ")
    if kondisi.lower() not in ("baik", "bagus"):
        print("Barang ditolak karena kondisi tidak baik")
        return
    
    kode = input("Kode barang: ")
    nama = input("Nama barang: ")
    harga = int(input("Harga: "))
    tahun_kedaluwarsa = int(input("Tahun kedaluwarsa: "))
    nomor_rak = int(input("Nomor rak: "))
    tanggal_masuk = input("Tanggal masuk (YYYY-MM-DD): ")
    jumlah = int(input("Jumlah: "))
    
    if data:
        new_id = max(b.id_resi for b in data) + 1
    else:
        new_id = 1
    
    barang_baru = Barang(
        id_resi=new_id,
        kode_barang=kode,
        nama_barang=nama,
        harga=harga,
        tahun_kedaluwarsa=tahun_kedaluwarsa,
        kondisi_fisik=kondisi,
        nomor_rak=nomor_rak,
        tanggal_masuk=tanggal_masuk,
        jumlah=jumlah
    )
    data.append(barang_baru)
    print("Barang berhasil disimpan dengan ID resi", new_id)

# Modul C: Sorting
def bubble_sort_by_harga(barang_list: List[Barang]) -> List[Barang]:
    arr = barang_list[:]
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j].harga > arr[j+1].harga:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort_by_expired(barang_list: List[Barang]) -> List[Barang]:
    arr = barang_list[:]
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            if arr[j].tahun_kedaluwarsa < arr[min_index].tahun_kedaluwarsa:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def quicksort_by_id(barang_list: List[Barang]) -> List[Barang]:
    if len(barang_list) <= 1:
        return barang_list[:]
    pivot = barang_list[len(barang_list)//2].id_resi
    left = [b for b in barang_list if b.id_resi < pivot]
    middle = [b for b in barang_list if b.id_resi == pivot]
    right = [b for b in barang_list if b.id_resi > pivot]
    return quicksort_by_id(left) + middle + quicksort_by_id(right)

# Modul D: Searching
def linear_search_by_nama(barang_list: List[Barang], keyword: str) -> List[Barang]:
    result = []
    keyword_lower = keyword.lower()
    for b in barang_list:
        if keyword_lower in b.nama_barang.lower():
            result.append(b)
    return result

def binary_search_by_id(sorted_list: List[Barang], target_id: int) -> Optional[Barang]:
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_id = sorted_list[mid].id_resi
        if mid_id == target_id:
            return sorted_list[mid]
        elif mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Modul E: Hash Table
class HashTableLokasiRak:
    def __init__(self, size: int = 101):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    
    def _hash(self, kode_barang: str) -> int:
        total = 0
        for ch in kode_barang:
            total += ord(ch)
        return total % self.size
    
    def insert(self, kode_barang: str, nomor_rak: int) -> None:
        index = self._hash(kode_barang)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == kode_barang:
                bucket[i] = (kode_barang, nomor_rak)
                return
        bucket.append((kode_barang, nomor_rak))
    
    def get(self, kode_barang: str) -> Optional[int]:
        index = self._hash(kode_barang)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == kode_barang:
                return v
        return None

def build_hash_table_from_data(data: List[Barang]) -> HashTableLokasiRak:
    ht = HashTableLokasiRak()
    for b in data:
        ht.insert(b.kode_barang, b.nomor_rak)
    return ht

def tampilkan_barang_singkat(b: Barang) -> None:
    print(f"[{b.id_resi}] {b.nama_barang} | Kode {b.kode_barang} | Harga {b.harga} | Rak {b.nomor_rak}")

def main():
    data = load_data_from_csv("data_barang.csv")
    hash_table = build_hash_table_from_data(data)
    
    while True:
        print("\nWareHouse OS 2.1 by Aziz")
        print("----------------------------")
        print("1. Input barang baru")
        print("2. Tampilkan 5 barang termurah (Bubble Sort)")
        print("3. Tampilkan 5 barang tercepat kedaluwarsa (Selection Sort)")
        print("4. Cari barang berdasarkan nama (Linear Search)")
        print("5. Cari barang berdasarkan ID resi (Binary Search + Quicksort)")
        print("6. Cari nomor rak dari kode barang (Hash Table)")
        print("")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            input_barang(data)
            hash_table = build_hash_table_from_data(data)
        elif pilihan == "2":
            sorted_harga = bubble_sort_by_harga(data)
            for b in sorted_harga[:5]:
                tampilkan_barang_singkat(b)
        elif pilihan == "3":
            sorted_expired = selection_sort_by_expired(data)
            for b in sorted_expired[:5]:
                tampilkan_barang_singkat(b)
        elif pilihan == "4":
            key = input("Masukkan kata kunci nama barang: ")
            hasil = linear_search_by_nama(data, key)
            if not hasil:
                print("Barang tidak ditemukan")
            else:
                for b in hasil:
                    tampilkan_barang_singkat(b)
        elif pilihan == "5":
            sorted_id = quicksort_by_id(data)
            target = int(input("Masukkan ID resi yang dicari: "))
            b = binary_search_by_id(sorted_id, target)
            if b is None:
                print("Barang dengan ID tersebut tidak ditemukan")
            else:
                tampilkan_barang_singkat(b)
        elif pilihan == "6":
            kode = input("Masukkan kode barang: ")
            rak = hash_table.get(kode)
            if rak is None:
                print("Kode barang tidak ditemukan di hash table")
            else:
                print("Barang dengan kode", kode, "berada di rak nomor", rak)
        elif pilihan == "0":
            break
        else:
            print("Menu tidak dikenal")

if __name__ == "__main__":
    main()