import numpy as np

# Input ukuran array 3 dimensi
batch = int(input("Masukkan jumlah batch: "))

baris_A = int(input("Masukkan jumlah baris Matrix A: "))
kolom_A = int(input("Masukkan jumlah kolom Matrix A: "))

baris_B = int(input("Masukkan jumlah baris Matrix B: "))
kolom_B = int(input("Masukkan jumlah kolom Matrix B: "))

# Mengecek syarat perkalian matriks
if kolom_A != baris_B:
    print("\nMatrix tidak dapat dikalikan!")
    print("Kolom Matrix A harus sama dengan baris Matrix B.")
    exit()

# Membuat array A dan B
A = np.zeros((batch, baris_A, kolom_A), dtype=int)
B = np.zeros((batch, baris_B, kolom_B), dtype=int)

# Input nilai Matrix A
print("\nMasukkan nilai Matrix A:")
for b in range(batch):
    print(f"\nBatch {b + 1}")
    for i in range(baris_A):
        for j in range(kolom_A):
            A[b][i][j] = int(input(f"A[{b}][{i}][{j}] = "))

# Input nilai Matrix B
print("\nMasukkan nilai Matrix B:")
for b in range(batch):
    print(f"\nBatch {b + 1}")
    for i in range(baris_B):
        for j in range(kolom_B):
            B[b][i][j] = int(input(f"B[{b}][{i}][{j}] = "))

# Perkalian matrix 3 dimensi
hasil = np.matmul(A, B)

# Menampilkan hasil
print("\n==============================")
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nHasil perkalian A x B:")
print(hasil)

print("\nBentuk A     :", A.shape)
print("Bentuk B     :", B.shape)
print("Bentuk hasil :", hasil.shape)
print("==============================")
