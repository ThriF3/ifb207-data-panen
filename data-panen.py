global data_panen
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500,
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 900,
            'kedelai': 450,
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600,
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550,
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480,
        }
    },
}

# Soal Nomor 1
def tampilkan(data):
    for i, values in data.items():
        print(f"> { i }")
        print(f"  >> Nama Lokasi :{ values['nama_lokasi'] }")
        print("  >> Hasil Panen :");
        for j, panen in values['hasil_panen'].items():
            print(f"    >>> { i } :{ panen }")
        
        print("-------------------------------------------")
    
# Soal Nomor 2
def tampilkan_jagung(data):
    print("> Hasil Panen Jagung")
    for i, values in data.items():
        print(f"  > { values['nama_lokasi'] } : { values['hasil_panen']['jagung'] }")
        
# Soal Nomor 3
def tampilkan_lokasi3(data):
    print(data['lokasi3']['nama_lokasi'])


def main():
    # tampilkan(data_panen)
    # tampilkan_jagung(data_panen)
    tampilkan_lokasi3(data_panen)
    
main()