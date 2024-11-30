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
for i, values in data_panen.items():
    print(f"> { i }")
    print(f"  >> Nama Lokast :{ values['nama_lokasi'] }")
    print("  >> Hasil Panen :");
    for j, panen in values['hasil_panen'].items():
        print(f"    >>> { i } :{ panen }")
    
    print("-------------------------------------------")