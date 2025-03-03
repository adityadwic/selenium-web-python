# Automation Testing Portfolio

## Deskripsi

Selamat datang di **Automation Testing Portfolio**! Proyek ini menampilkan berbagai skrip dan framework otomatisasi pengujian menggunakan **Selenium** dan **Python**. Di sini, Anda akan menemukan beberapa contoh pengujian otomatisasi untuk berbagai kasus uji pada aplikasi web, yang dirancang untuk mendemonstrasikan keterampilan dan pengalaman saya dalam otomatisasi pengujian perangkat lunak.

Proyek ini juga mencakup penerapan beberapa framework testing, seperti **Page Object Model (POM)**, **Data-Driven Testing**, dan pendekatan **Linear Testing** untuk pengujian otomatisasi yang terstruktur dan dapat dipelihara.

## Fitur

- **Selenium WebDriver** dengan Python untuk mengotomatisasi pengujian aplikasi web.
- **Page Object Model (POM)** untuk mengorganisir elemen halaman dan interaksi dalam aplikasi web secara terstruktur dan reusable.
- **Data-Driven Testing** dengan file eksternal (seperti CSV, Excel, atau JSON) untuk menguji berbagai input dan data.
- **Keyword-Driven Testing** dan **Behavior-Driven Testing (BDD)** (jika diterapkan di proyek tertentu).
- Berbagai jenis tes, termasuk registrasi pengguna, login pengguna, pencarian produk, dan banyak lagi.

## Teknologi yang Digunakan

- **Selenium WebDriver**: Framework utama untuk otomasi pengujian aplikasi web.
- **Python**: Bahasa pemrograman utama untuk penulisan skrip otomatisasi.
- **pytest**: Kerangka pengujian untuk menulis dan mengeksekusi pengujian.
- **webdriver-manager**: Untuk mengelola driver browser secara otomatis.
- **POM (Page Object Model)**: Pola desain yang digunakan untuk mengorganisir pengujian aplikasi web.

## Struktur Proyek

```plaintext
automation-framework/
│
├── tests/                       # Folder untuk test case
│   ├── pom_test_registration.py # Test case untuk registrasi pengguna
│   ├── pom_test_login.py        # Test case untuk login pengguna
│   ├── pom_test_search_product.py # Test case untuk mencari produk
│
├── pages/                        # Folder untuk Page Object Model
│   ├── home_page.py              # Kelas untuk halaman Home
│   ├── signup_page.py            # Kelas untuk halaman Sign Up
│   ├── login_page.py             # Kelas untuk halaman Login
│   ├── products_page.py          # Kelas untuk halaman Produk
│
├── drivers/                      # Folder untuk WebDriver (untuk Chrome, Firefox, dll.)
│   └── chromedriver.exe
│
├── utilities/                    # Folder untuk utilitas tambahan
│   └── driver_factory.py         # Untuk mengelola inisialisasi WebDriver
│
└── requirements.txt              # File untuk dependensi
```

## Instalasi

Untuk memulai proyek ini, Anda hanya perlu mengikuti beberapa langkah sederhana:

1. Clone repository ini ke komputer Anda:

```bash
git clone https://github.com/username/automation-testing-portfolio.git
cd automation-testing-portfolio
```
2. Instal dependensi yang diperlukan menggunakan pip:

```pip install -r requirements.txt```

3.	Jalankan tes menggunakan pytest:

```pytest tests/```

## Tes

Tes akan dijalankan pada seluruh file di folder `tests/`.

## Cara Menambahkan Test Baru

Untuk menambahkan tes baru ke dalam proyek, ikuti langkah-langkah berikut:

1. Buat file test baru di dalam folder `tests/` dan ikuti pola pengujian yang ada.
2. Buat kelas baru di dalam folder `pages/` untuk setiap halaman baru yang relevan.
3. Tulis test case menggunakan pendekatan **Page Object Model (POM)** untuk memastikan kode dapat dipelihara dengan baik.
4. Jalankan pytest untuk memastikan semua pengujian berjalan dengan baik.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, Anda dapat mengikuti langkah-langkah berikut:

1. Fork repository ini.
2. Buat branch baru untuk fitur atau perbaikan yang ingin Anda tambahkan.
3. Setelah selesai, buat pull request untuk mendiskusikan perubahan Anda.

Pastikan untuk mengikuti pedoman pengkodean yang ada dan menulis tes otomatis untuk setiap perubahan yang Anda buat.

## Penulis

- Nama Anda: [LinkedIn Aditya Dwi Cahyono](https://www.linkedin.com/in/adityadwicahyono/) | [GitHub](https://github.com/adityadwic)
