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

def bubblesort(data: list[Barang]) -> list[Barang]:
    arr = data[:]
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j].harga > arr[j + 1].harga:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selectionsort(data: list[Barang]) -> list[Barang]:
    arr = data[:]
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j].tahun_kedaluwarsa < arr[min_index].tahun_kedaluwarsa:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def quicksort(data: list[Barang]) -> list[Barang]:
    if len(data) <= 1:
        return data[:]
    pivot = data[len(data) // 2].id_resi
    left = [b for b in data if b.id_resi < pivot]
    middle = [b for b in data if b.id_resi == pivot]
    right = [b for b in data if b.id_resi > pivot]
    return quicksort(left) + middle + quicksort(right)

def tampilkan(b: Barang) -> None:
    print(f"[{b.id_resi}] {b.nama_barang} | Harga {b.harga} | Exp {b.tahun_kedaluwarsa}")

def simpan_data_barang_c(
    path: str,
    data_bubble: list[Barang],
    data_selection: list[Barang],
    data_quick: list[Barang],
    n_preview: int = 10,
) -> None:
    """
    Membuat file data_barang_c.csv berisi
    10 data pertama dari masing masing hasil sorting
    """
    with open(path, "w", newline="", encoding="utf8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "id_resi", "kode_barang", "nama_barang", "harga",
            "tahun_kedaluwarsa", "kondisi_fisik",
            "nomor_rak", "tanggal_masuk", "jumlah"
        ])
        for b in data_bubble[:n_preview]:
            writer.writerow([
                b.id_resi, b.kode_barang, b.nama_barang, b.harga,
                b.tahun_kedaluwarsa, b.kondisi_fisik,
                b.nomor_rak, b.tanggal_masuk, b.jumlah
            ])

        writer.writerow([])
        writer.writerow([
            "id_resi", "kode_barang", "nama_barang", "harga",
            "tahun_kedaluwarsa", "kondisi_fisik",
            "nomor_rak", "tanggal_masuk", "jumlah"
        ])
        for b in data_selection[:n_preview]:
            writer.writerow([
                b.id_resi, b.kode_barang, b.nama_barang, b.harga,
                b.tahun_kedaluwarsa, b.kondisi_fisik,
                b.nomor_rak, b.tanggal_masuk, b.jumlah
            ])

        writer.writerow([])
        writer.writerow([
            "id_resi", "kode_barang", "nama_barang", "harga",
            "tahun_kedaluwarsa", "kondisi_fisik",
            "nomor_rak", "tanggal_masuk", "jumlah"
        ])
        for b in data_quick[:n_preview]:
            writer.writerow([
                b.id_resi, b.kode_barang, b.nama_barang, b.harga,
                b.tahun_kedaluwarsa, b.kondisi_fisik,
                b.nomor_rak, b.tanggal_masuk, b.jumlah
            ])

def main():
    data = load_data()

    data_bubble = bubblesort(data)
    data_selection = selectionsort(data)
    data_quick = quicksort(data)

    print("[WareHouse OS 2.1] Sepuluh barang termurah (Bubble Sort):")
    for b in data_bubble[:10]:
        tampilkan(b)

    print("\n[WareHouse OS 2.1] Sepuluh barang tercepat kedaluwarsa (Selection Sort):")
    for b in data_selection[:10]:
        tampilkan(b)

    print("\n[WareHouse OS 2.1] Sepuluh barang dengan id resi terkecil (Quick Sort):")
    for b in data_quick[:10]:
        tampilkan(b)

    simpan_data_barang_c(
        "data_barang_c.csv",
        data_bubble,
        data_selection,
        data_quick,
        n_preview=10,
    )

    print("\n[WareHouse OS 2.1] File data_barang_c.csv sudah dibuat dari output Modul C.")

if __name__ == "__main__":
    main()