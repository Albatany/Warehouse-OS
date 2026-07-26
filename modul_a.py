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

def input_barang(data: list[Barang]) -> None:
    print("[WareHouse OS 2.1] Input Barang Baru")
    print("------")
    kondisi = input("Kondisi fisik barang (Baik atau Rusak): ")
    if kondisi.lower() not in ("baik", "bagus"):
        print("Barang ditolak karena kondisi tidak baik")
        return

    kode = input("Kode barang: ")
    nama = input("Nama barang: ")
    harga = int(input("Harga: "))
    tahun_kedaluwarsa = int(input("Tahun kedaluwarsa: "))
    nomor_rak = int(input("Nomor rak: "))
    tanggal_masuk = input("Tanggal masuk (YYYY MM DD): ")
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
        jumlah=jumlah,
    )
    data.append(barang_baru)
    print("Barang berhasil disimpan dengan ID resi", new_id)

def main():
    data = load_data()
    input_barang(data)

if __name__ == "__main__":
    main()