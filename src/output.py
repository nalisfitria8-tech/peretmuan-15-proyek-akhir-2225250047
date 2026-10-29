def tampilkan_hasil(hasil_ringkasan):
    """Menampilkan ringkasan analisis data ke terminal."""
    print("\n--- RINGKASAN ANALISIS NILAI KELAS ---")
    print(f"Total Siswa / Data  : {hasil_ringkasan['jumlah']}")
    print(f"Rata-rata Kelas     : {hasil_ringkasan['rata_rata']:.2f}")
    print(f"Nilai Minimum       : {hasil_ringkasan['minimum']}")
    print(f"Nilai Maksimum      : {hasil_ringkasan['maksimum']}")
    print(f"Jumlah Tuntas       : {hasil_ringkasan['lulus']}")
    print("--------------------------------------\n")