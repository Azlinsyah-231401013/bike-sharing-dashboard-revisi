# 🚲 Bike Sharing Dashboard

Dashboard interaktif berbasis **Streamlit** untuk menganalisis pengaruh **cuaca, musim, dan waktu** terhadap jumlah penyewaan sepeda pada periode **2011–2012**.

---

## 🌐 Demo Dashboard

👉 https://bike-sharing-dashboard-revisi-azlin.streamlit.app/

---

## 📊 Fitur Utama

* Analisis pengaruh kondisi cuaca terhadap penyewaan sepeda
* Pola penyewaan berdasarkan jam
* Perbandingan hari kerja vs akhir pekan
* Filter berdasarkan tahun dan musim

---

## 📁 Struktur Proyek

```
Submission Proyek Analisis Data/
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   ├── day.csv
│   ├── hour.csv
│   └── cleaned_hour.csv
│
├── notebook.ipynb
├── requirements.txt
├── url.txt
└── README.md
```

---

## ⚙️ Cara Menjalankan Secara Lokal

### 1. Clone Repository

```bash
git clone https://github.com/Azlinsyah-231401013/bike-sharing-dashboard-revisi.git
cd bike-sharing-dashboard-revisi
```

---

### 2. Setup Virtual Environment

Buat virtual environment:

```bash
python -m venv venv
```

Aktifkan virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Jalankan Dashboard

```bash
cd dashboard
streamlit run dashboard.py
```

---

### 5. Buka di Browser

```
http://localhost:8501
```

---

## 📈 Insight Singkat

* Penyewaan sepeda tertinggi terjadi saat **cuaca cerah**
* Puncak penggunaan pada jam sibuk:

  * 07.00–09.00
  * 17.00–19.00
* Hari kerja memiliki jumlah penyewaan lebih tinggi dibanding akhir pekan

---

## 👤 Author

**Azlinsyah Fadhilah Meran**
