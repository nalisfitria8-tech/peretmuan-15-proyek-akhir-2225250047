BATAS_LULUS = 60

def hitung_rata_rata(nilai):
    """Menghitung rata-rata dari list numerik[cite: 13, 17]."""
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)

def status_lulus(nilai, batas=BATAS_LULUS):
    """Menyaring nilai yang memenuhi batas kelulusan."""
    return [x for x in nilai if x >= batas]

def ringkasan(nilai):
    """Menghasilkan dictionary ringkasan statistik kelas."""
    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None,
        "lulus": len(status_lulus(nilai))
    }