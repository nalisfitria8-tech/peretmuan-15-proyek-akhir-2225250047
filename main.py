from src.input_data import baca_data_dari_file
from src.proses import ringkasan
from src.output import tampilkan_hasil

def main():
    print("=== PROGRAM ANALISIS NILAI SISWA ===")
    path_file = "data/contoh_data.txt"
    
    # 1. Membaca data
    data_nilai = baca_data_dari_file(path_file)
    
    if not data_nilai:
        print("Tidak ada data yang dapat diproses.")
        return
        
    # 2. Proses perhitungan dan analisis
    hasil = ringkasan(data_nilai)
    
    # 3. Tampilkan output
    tampilkan_hasil(hasil)

if __name__ == "__main__":
    main()