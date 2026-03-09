detak_jantung = {70, 110, 65, 120, 80, 140,75 }

def analisa_kondisi(nilai):
    if nilai > 100:
        return "Peringatan : Takikardia(Detak Tinggi)"
    else : 
        return "Kondisi : Normal"
x = 1
x += 1
for data in detak_jantung:
    status = analisa_kondisi(data)
    print(f"data ke  {data}bpm -> {status}")