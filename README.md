# Implementasi Himpunan Matematika Diskrit

Proyek ini bertujuan untuk mengimplementasikan konsep dasar **himpunan** dalam bahasa pemrograman Python. Modul ini mendukung berbagai operasi dan fungsi himpunan yang sering digunakan dalam matematika diskrit.

## **Fitur Utama**

### **Magic Methods**

1. **`__len__(self)`**  
   Mengembalikan jumlah elemen dalam himpunan (ukuran himpunan).

2. **`__contains__(self, item)`**  
   Mengecek apakah suatu elemen terdapat dalam himpunan (`True` atau `False`).

3. **`__eq__(self, other)`**  
   Mengecek apakah dua himpunan memiliki elemen yang sama (ekuivalensi).

4. **`__le__(self, other)`**  
   Mengecek apakah suatu himpunan merupakan subset dari himpunan lain.

5. **`__lt__(self, other)`**  
   Mengecek apakah suatu himpunan merupakan proper subset dari himpunan lain.

6. **`__ge__(self, other)`**  
   Mengecek apakah suatu himpunan merupakan superset dari himpunan lain.

7. **`__floordiv__(self, other)`**  
   Mengecek apakah dua himpunan setara (memiliki elemen yang sama tanpa memperhatikan urutan).

8. **`__add__(self, other)`**  
   Melakukan operasi gabungan (_union_) antara dua himpunan.

9. **`__iadd__(self, item)`**  
   Menambah elemen baru ke dalam himpunan menggunakan operator `+=`.

10. **`__sub__(self, other)`**  
    Melakukan operasi selisih (_difference_) antara dua himpunan.

11. **`__truediv__(self, other)`**  
    Menghitung irisan (_intersection_) antara dua himpunan.

12. **`__mul__(self, other)`**  
    Menghitung selisih simetris (_symmetric difference_) antara dua himpunan.

13. **`__pow__(self, other)`**  
    Menghitung hasil kali kartesian (_Cartesian Product_) antara dua himpunan.

14. **`__abs__(self)`**  
    Mengembalikan jumlah semua subset (_power set_) yang mungkin dari himpunan tersebut.

### **Operasi dan Fungsi Tambahan**

1. **Menambah Elemen**  
   Gunakan `tambah(item)` untuk menambahkan elemen baru ke dalam himpunan.

2. **Menghapus Elemen**  
   Gunakan `hapus(item)` untuk menghapus elemen dari himpunan.

3. **Komplemen**  
   Gunakan `complement(universal)` untuk menghitung komplemen dari suatu himpunan berdasarkan himpunan semesta.

4. **Himpunan Kuasa (Power Set)**  
   Gunakan `ListKuasa()` untuk mendapatkan daftar semua subset yang mungkin dari himpunan.

---

## **Cara Instalasi**

Library ini tersedia di PyPI dan dapat diinstal menggunakan perintah berikut:

```bash
pip install himpunan_tim5
```

Setelah instalasi, Anda dapat langsung mengimpor modul dan menggunakannya:

```python
from himpunan_tim5 import *
```

---

## **Contoh Penggunaan**

### **Operasi Dasar**

```python
# Membuat himpunan
h1 = Himpunan(1, 2, 3)
h2 = Himpunan(3, 4, 5)

# Gabungan
print(h1 + h2)  # Output: (1, 2, 3, 4, 5)

# Irisan
print(h1 / h2)  # Output: (3)

# Selisih
print(h1 - h2)  # Output: (1, 2)

# Menambah elemen
h1 += 4
print(h1)  # Output: (1, 2, 3, 4)
```

### **Hasil Kali Cartesian**

```python
h3 = Himpunan(1, 2)
h4 = Himpunan('A', 'B')
print(h3 ** h4)
# Output: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```

### **Komplemen**

```python
S = Himpunan(1, 2, 3, 4, 5)
h5 = Himpunan(1, 2)
print(h5.complement(S))  # Output: (3, 4, 5)
```

### **Himpunan Kuasa**

```python
h6 = Himpunan(1, 2)
print(h6.ListKuasa())
# Output: [(), (1,), (2,), (1, 2)]
```

---

## **Kontributor**

Library ini dikembangkan oleh **Team 5 IMT UCM 2023**:

- **Deny Wahyudi Asaloei**
- **Levin Dawson Wisan**
- **Muhammad Aditya Ridwan**

---

## **Link PyPI**

Anda dapat menemukan library ini di PyPI melalui tautan berikut:  
[himpunan-tim5](https://pypi.org/project/himpunan-tim5/)
