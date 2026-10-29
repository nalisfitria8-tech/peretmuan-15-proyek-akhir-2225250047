def baca_data_dari_file(filepath):
    """Membaca data angka dari file teks eksternal."""
    data = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for baris in f:
                baris_bersih = baris.strip()
                if baris_bersih:
                    # Validasi sederhana mengubah ke float/integer
                    nilai = float(baris_bersih)
                    data.append(nilai)
    except FileNotFoundError:
        print(f"Peringatan: File {filepath} tidak ditemukan.")
    except ValueError:
        print("Peringatan: Terdapat format angka yang tidak valid di dalam file.")
    return data