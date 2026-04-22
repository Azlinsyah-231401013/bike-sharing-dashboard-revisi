# 🚲 Bike Sharing Dashboard

Dashboard interaktif berbasis **Streamlit** untuk menganalisis pengaruh **cuaca, musim, dan waktu** terhadap jumlah penyewaan sepeda pada periode **2011–2012**.

---

## 🌐 Live Demo

🔗 https://bike-sharing-dashboard-baru-azlin.streamlit.app/

---

## 📌 Deskripsi Proyek

Proyek ini merupakan bagian dari submission **Proyek Analisis Data - Dicoding**.
Tujuan utama proyek ini adalah memahami pola penyewaan sepeda berdasarkan faktor lingkungan dan waktu melalui proses analisis data.

Tahapan analisis meliputi:

* Data Wrangling
* Data Cleaning
* Exploratory Data Analysis (EDA)
* Data Visualization
* Dashboard Development menggunakan Streamlit

---

## ❓ Pertanyaan Bisnis

1. Seberapa besar pengaruh kondisi cuaca dan musim terhadap jumlah penyewaan sepeda dalam periode tahun 2011–2012?
2. Pada jam berapa tingkat penyewaan sepeda paling tinggi terjadi pada hari kerja dan akhir pekan dalam periode tahun 2011–2012?

---

## 📊 Insight Utama

* Cuaca cerah dan berawan ringan menghasilkan jumlah penyewaan tertinggi
* Cuaca buruk (hujan/salju) menurunkan jumlah penyewaan secara signifikan
* Musim panas dan gugur memiliki tingkat penyewaan lebih tinggi
* Puncak penyewaan terjadi pada:

  * 07.00 – 09.00 (pagi)
  * 17.00 – 19.00 (sore)
* Penyewaan sepeda didominasi untuk aktivitas harian (commuter)

---

## 🖥️ Fitur Dashboard

* Filter interaktif:

  * Tahun
  * Musim
* Ringkasan data:

  * Total penyewaan
  * Rata-rata penyewaan
  * Nilai maksimum
* Visualisasi:

  * Pengaruh cuaca terhadap penyewaan
  * Pola penyewaan berdasarkan jam
  * Perbandingan hari kerja dan akhir pekan

---

## 🛠️ Teknologi yang Digunakan

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit

---

## 📁 Struktur Proyek

```bash id="m62r1m"
Submission Proyek Analisis Data/
│
├── dashboard/
│   ├── dashboard.py
│   └── cleaned_hour.csv
│
├── requirements.txt
├── url.txt
├── README.md
└── Proyek_Analisis_Data_Azlinsyah_Baru.ipynb
```

---

## ▶️ Cara Menjalankan Secara Lokal

1. Install dependencies:

```bash id="s6vwgd"
pip install -r requirements.txt
```

2. Masuk ke folder dashboard:

```bash id="iqr4qn"
cd dashboard
```

3. Jalankan aplikasi:

```bash id="njsaf6"
streamlit run dashboard.py
```

4. Buka di browser:

```bash id="7l9t6l"
http://localhost:8501
```

---

## ☁️ Deployment

Dashboard ini telah dideploy menggunakan **Streamlit Cloud** dan dapat diakses melalui:

👉 https://bike-sharing-dashboard-baru-azlin.streamlit.app/

---

## 👤 Author

**Azlinsyah Fadhilah Meran**
📧 [azlinsyah4@gmail.com](mailto:azlinsyah4@gmail.com)

---

## 📎 Catatan

Proyek ini dibuat untuk memenuhi submission pada kelas
**Belajar Analisis Data dengan Python - Dicoding**.

---
