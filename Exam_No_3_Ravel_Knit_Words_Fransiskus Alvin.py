# Akses P = 0
# Akses P U = 1 ==> Katanya diakses sampai range perulangan
# Akses P U R = 2


# print(kata.extend())
# print(kata_baru.append(kata))
# for rows in range(len(kata)):
#     # hasil = kata_baru.append(kata[0:rows+1])
#     print(kata[0:rows+1], end = "")

# kata = "Digital"

def ravel(kata):
    kata_baru = ""
    for rows in range(len(kata)): #Looping Sampai Dengan Seluruh Panjang Kata
        kata_baru += kata[0 : (rows + 1)] # menambahkan kata yang sudah ada dengan kata + rows 
    return kata_baru

print(ravel("Purwadhika"))
print(ravel("Digital"))
print(ravel("Coding"))
print(ravel("School"))

# def ravel(kata):
#     kata_baru = []
#     for rows in range(len(kata)):
#         hasil = kata_baru.append(kata[0:rows+1])
#         return hasil
    # for column in kata[0 : (rows + 1) ]:
    #     print(column, end=" ")

# print(ravel("makan"))

## knit function 
# kata = "DDiDigDigiDigitDigitaDigital"
# kata = kata[5]
# print(kata)
# print(len(kata))
# kata_baru = kata_baru + kata[0]
# kata_baru = kata_baru + kata[2] + 2
# kata_baru = kata_baru + kata[5] + 3
# kata_baru = kata_baru + kata[9] + 4
# kata_baru = kata_baru + kata[14] + 5
# print(kata_baru)
# for row in range(len(kata)):

def knit(kata):
    kata_baru = ""
    angka_tambah = 0
    angka_index = 0
    while angka_index < len(kata):
        # print(kata[0])
        # angka +=1
        if angka_tambah == 0:
            kata_baru += kata[0]
            angka_tambah = 2
        else: 
            angka_index += angka_tambah #0 + 2 + 3
            if angka_index > len(kata):
                break
            else:
                # print(angka_index)
                kata_baru += kata[angka_index]
                angka_tambah += 1 # jadi 3
                # print(angka_tambah)
    return kata_baru

print(knit('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
print(knit('DDiDigDigiDigitDigitaDigital'))
print(knit('CCoCodCodiCodinCoding'))
print(knit('SScSchSchoSchooSchool'))





