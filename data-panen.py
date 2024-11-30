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
    
# Soal Nomor 4
padi_lokasi1 = {
    'panen': data_panen['lokasi1']['hasil_panen']['padi'],
    'kedelai': data_panen['lokasi1']['hasil_panen']['kedelai'],
}

padi_lokasi2 = {
    'panen': data_panen['lokasi2']['hasil_panen']['padi'],
    'kedelai': data_panen['lokasi2']['hasil_panen']['kedelai'],
}

padi_lokasi3 = {
    'panen': data_panen['lokasi3']['hasil_panen']['padi'],
    'kedelai': data_panen['lokasi3']['hasil_panen']['kedelai'],
}

padi_lokasi4 = {
    'panen': data_panen['lokasi4']['hasil_panen']['padi'],
    'kedelai': data_panen['lokasi4']['hasil_panen']['kedelai'],
}

padi_lokasi5 = {
    'panen': data_panen['lokasi5']['hasil_panen']['padi'],
    'kedelai': data_panen['lokasi5']['hasil_panen']['kedelai'],
}

# Soal No. 5
hasil_panen = {}
hasil_panen['lokasi1'] = padi_lokasi1
hasil_panen['lokasi2'] = padi_lokasi2
hasil_panen['lokasi3'] = padi_lokasi3
hasil_panen['lokasi4'] = padi_lokasi4
hasil_panen['lokasi5'] = padi_lokasi5

# Soal No. 6
def cek_panen(data):
    for i, values in data.items():
        if values['hasil_panen']['padi'] > 1300 or values['hasil_panen']['jagung'] > 800:
            print(f"{ values['nama_lokasi'] } memerlukan perhatian khusus.")
        else:
            print(f"{ values['nama_lokasi'] } dalam komdisi baik.")


def main():
    # tampilkan(data_panen)
    # tampilkan_jagung(data_panen)
    tampilkan_lokasi3(data_panen)
    print(hasil_panen)
    cek_panen(data_panen)
    
main()