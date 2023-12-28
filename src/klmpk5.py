import numpy as np


def print_menu():
    print("OLEH KELOMPOK 5 ALGEO IF III A")
    print("\nMENU")
    print("1. Penjumlahan dan Pengurangan Matriks")
    print("2. Matriks Transpose")
    print("3. Matriks Balikan")
    print("4. Determinan")
    print("5. Sistem Persamaan Linier")
    print("6. Keluar")


# pertambahan matriks
def penjumlahan_pengurangan():
    def tambah_matriks(a, b):
        result = [[0, 0], [0, 0]]
        for i in range(len(a)):
            for j in range(len(a[0])):
                result[i][j] = a[i][j] + b[i][j]
        return result

    def kurang_matriks(a, b):
        result = [[0, 0], [0, 0]]
        for i in range(len(a)):
            for j in range(len(a[0])):
                result[i][j] = a[i][j] - b[i][j]
        return result

    while True:
        print("\nSub-menu:")
        print("1. Penjumlahan matriks")
        print("2. Pengurangan matriks")
        print("3. Kembali ke Menu Utama")

        pilihan_submenu = input("Masukkan pilihan (1/2/3): ")

        if pilihan_submenu == "3":
            break
        elif pilihan_submenu == "1":
            # Input matriks A
            print("\nMasukkan matriks A:")
            matriks_A = [
                [
                    float(input(f"Masukkan nilai matriks_A[{i + 1}][{j + 1}]: "))
                    for j in range(2)
                ]
                for i in range(2)
            ]

            # Input matriks B
            print("Masukkan matriks B:")
            matriks_B = [
                [
                    float(input(f"Masukkan nilai matriks_B[{i + 1}][{j + 1}]: "))
                    for j in range(2)
                ]
                for i in range(2)
            ]

            # Operasi penjumlahan
            hasil_tambah = tambah_matriks(matriks_A, matriks_B)
            print("\nHasil penjumlahan matriks:")
            for row in hasil_tambah:
                print(row)

        elif pilihan_submenu == "2":
            # Input matriks A
            print("\nMasukkan matriks A:")
            matriks_A = [
                [
                    float(input(f"Masukkan nilai matriks_A[{i + 1}][{j + 1}]: "))
                    for j in range(2)
                ]
                for i in range(2)
            ]

            # Input matriks B
            print("Masukkan matriks B:")
            matriks_B = [
                [
                    float(input(f"Masukkan nilai matriks_B[{i + 1}][{j + 1}]: "))
                    for j in range(2)
                ]
                for i in range(2)
            ]

            # Operasi pengurangan
            hasil_kurang = kurang_matriks(matriks_A, matriks_B)
            print("\nHasil pengurangan matriks:")
            for row in hasil_kurang:
                print(row)

        else:
            print("Pilihan tidak valid. Masukkan 1, 2, atau 3.")


# matriks transpose
def matriks_transpose():
    size = int(input("Masukan ukuran matriks (2 or 3): "))
    matrix = np.array(get_matrix_from_input(size))
    transpose_matrix = np.transpose(matrix)
    print("\n matriks Transpose:")
    display_matrix(transpose_matrix)


# Function to get matrix input
def get_matrix_from_input(size):
    print(f"Masukkan elemen matriks {size}x{size}:")
    matrix = []
    for i in range(size):
        row = list(
            map(float, input(f"Masukan baris {i + 1} dipisahkan oleh spasi: ").split())
        )
        matrix.append(row)
    return matrix


# Function to display matrix
def display_matrix(matrix):
    print("Matrix:")
    for row in matrix:
        print(" ".join([str(x) for x in row]))


# Function to perform operations
def perform_operations(matrix):
    transpose_matrix = np.transpose(matrix)
    print("\nMatriks Transpose: ")
    display_matrix(transpose_matrix)

    determinant = np.linalg.det(matrix)
    print("\nMatriks Determinant: ", determinant)

    inverse_matrix = np.linalg.inv(matrix)
    print("\nMatriks Inverse: ")
    display_matrix(inverse_matrix)


def matriks_balikan():
    def inverse_matriks(matriks):
        det = matriks[0][0] * matriks[1][1] - matriks[0][1] * matriks[1][0]
        if det == 0:
            return None
        else:
            inv_det = 1 / det
            return [
                [matriks[1][1] * inv_det, -matriks[0][1] * inv_det],
                [-matriks[1][0] * inv_det, matriks[0][0] * inv_det],
            ]

    # Input matriks
    print("\nMasukkan matriks:")
    matriks = [
        [float(input(f"Masukkan nilai matriks[{i + 1}][{j + 1}]: ")) for j in range(2)]
        for i in range(2)
    ]

    # Operasi invers
    hasil_inverse = inverse_matriks(matriks)
    if hasil_inverse is not None:
        print("\nHasil invers matriks:")
        for row in hasil_inverse:
            print(row)
    else:
        print("\nMatriks tidak memiliki invers.")


# determinan
def determinant_2x2(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    result = a * d - b * c
    steps = [
        f"Determinant = ({a} * {d}) - ({b} * {c})",
        f"            = {a * d} - {b * c}",
        f"            = {result}",
    ]
    return result, steps


def determinant_3x3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    result = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

    steps = [
        f"Determinant = {a} * ({e} * {i} - {f} * {h}) - {b} * ({d} * {i} - {f} * {g}) + {c} * ({d} * {h} - {e} * {g})",
        f"            = {a * (e * i - f * h)} - {b * (d * i - f * g)} + {c * (d * h - e * g)}",
        f"            = {result}",
    ]

    return result, steps


def determinan():
    def get_matrix_from_input(size):
        print(f"Masukan elemen matriks {size}x{size}:")
        matrix = []
        for i in range(size):
            row = list(
                map(
                    float,
                    input(f"Masukan baris {i + 1} dipisahkan oleh spasi: ").split(),
                )
            )
            matrix.append(row)
        return matrix

    print("Matriks Determinan")

    while True:
        print("\nSub-menu:")
        print("1. Determinan Matriks 2x2")
        print("2. Determinan Matriks 3x3")
        print("3. Kembali ke Menu Utama")

        pilihan_submenu = input("Masukkan pilihan (1/2/3): ")

        if pilihan_submenu == "3":
            break
        elif pilihan_submenu == "1":
            matrix = get_matrix_from_input(2)
            result, steps = determinant_2x2(matrix)
        elif pilihan_submenu == "2":
            matrix = get_matrix_from_input(3)
            result, steps = determinant_3x3(matrix)
        else:
            print("Pilihan tidak valid. Masukkan 1, 2, atau 3.")
            continue

        print("\nCalculation Steps:")
        for step in steps:
            print(step)

        print(f"\nThe determinant of the matrix is: {result}")


# SPL
def sistem_persamaan_linier():
    def gauss_jordan(a):
        n = len(a)

        for k in range(n):
            if a[k, k] == 0:
                for i in range(k + 1, n):
                    if a[i, k] != 0:
                        a[[k, i]] = a[[i, k]]
                        break

            pivot = a[k, k]
            a[k] /= pivot

            for i in range(n):
                if i != k:
                    factor = a[i, k]
                    a[i] -= factor * a[k]

        x = a[:, -1]
        return x

    print("\nSistem Persamaan Linier Solver")

    # Memasukkan koefisien matriks A dan vektor hasil b dari pengguna
    a11 = float(input("Masukkan a11: "))
    a12 = float(input("Masukkan a12: "))
    a21 = float(input("Masukkan a21: "))
    a22 = float(input("Masukkan a22: "))
    b1 = float(input("Masukkan b1: "))
    b2 = float(input("Masukkan b2: "))

    # Membentuk matriks A dan vektor b sebagai augmented matrix
    A = np.array([[a11, a12, b1], [a21, a22, b2]])

    # Menyelesaikan SPL menggunakan metode Gauss-Jordan
    solution = gauss_jordan(A)

    # Menampilkan hasil
    print("\nHasil nilai matriks A setelah eliminasi Gauss-Jordan: ")
    print(A[:, :-1])
    print("Hasil nilai vektor x (solusi SPL): ")
    print(solution)


while True:
    print_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        penjumlahan_pengurangan()
    elif choice == 2:
        matriks_transpose()
    elif choice == 3:
        matriks_balikan()
    elif choice == 4:
        determinan()
    elif choice == 5:
        sistem_persamaan_linier()
    elif choice == 6:
        print("Terimakasih Semoga Bermanfaat")
        print("dibuat oleh kelompok 5 ALJABAR GEOMETRI IF III A")
        print("Ayi Muhamad N")
        print("Rizal MZ")
        print("Gina Rahmawati")
        print("Sandrina Sabilah")
        print("Widi Asih")

    else:
        print("Invalid choice, please try again.")
