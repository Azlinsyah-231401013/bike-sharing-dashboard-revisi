import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("darkgrid")

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "cleaned_hour.csv")

if not os.path.exists(file_path):
    st.error("File cleaned_hour.csv tidak ditemukan!")
    st.stop()

df = pd.read_csv(file_path)

# ========================

# TITLE

# ========================

st.title("🚲 Bike Sharing Dashboard")
st.markdown("Analisis pengaruh cuaca, musim, dan waktu terhadap jumlah penyewaan sepeda (2011–2012)")

# ========================

# SIDEBAR FILTER

# ========================

st.sidebar.header("Filter")

selected_year = st.sidebar.selectbox(
"Pilih Tahun",
options=sorted(df["year"].unique())
)

selected_season = st.sidebar.selectbox(
"Pilih Musim",
options=sorted(df["season"].unique())
)

filtered_df = df[
(df["year"] == selected_year) &
(df["season"] == selected_season)
]

# ========================

# METRICS

# ========================

st.subheader("📊 Ringkasan Data")

col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", int(filtered_df["total_count"].sum()))
col2.metric("Rata-rata", int(filtered_df["total_count"].mean()))
col3.metric("Maksimum", int(filtered_df["total_count"].max()))

# ========================

# VISUALISASI 1

# ========================

st.subheader("🌤️ Pengaruh Cuaca terhadap Penyewaan")

weather_avg = filtered_df.groupby("weather_condition")["total_count"].mean().reset_index()

fig, ax = plt.subplots()
sns.barplot(
data=weather_avg,
x="weather_condition",
y="total_count",
palette="coolwarm",
ax=ax
)

plt.xticks(rotation=20)
plt.title("Rata-rata Penyewaan Berdasarkan Cuaca")

st.pyplot(fig)

# ========================

# VISUALISASI 2

# ========================

st.subheader("⏰ Pola Penyewaan Berdasarkan Jam")

hour_avg = filtered_df.groupby("hour")["total_count"].mean().reset_index()

fig2, ax2 = plt.subplots()
sns.lineplot(
data=hour_avg,
x="hour",
y="total_count",
marker="o",
color="#FF5722",
ax=ax2
)

plt.title("Rata-rata Penyewaan per Jam")
plt.xlabel("Jam")
plt.ylabel("Jumlah Penyewaan")

st.pyplot(fig2)

# ========================

# VISUALISASI 3

# ========================

st.subheader("📅 Hari Kerja vs Akhir Pekan")

df_temp = filtered_df.copy()
df_temp["workingday"] = df_temp["workingday"].map({
1: "Hari Kerja",
0: "Akhir Pekan"
})

fig3, ax3 = plt.subplots()
sns.boxplot(
x="workingday",
y="total_count",
data=df_temp,
palette="Set2",
ax=ax3
)

st.pyplot(fig3)

# ========================

# INSIGHT

# ========================

st.subheader("💡 Insight")

st.markdown("""

* Cuaca cerah menghasilkan jumlah penyewaan tertinggi.
* Penyewaan meningkat pada jam sibuk (07.00–09.00 dan 17.00–19.00).
* Hari kerja menunjukkan pola penggunaan yang lebih tinggi dibanding akhir pekan.
* Data berdasarkan periode 2011–2012.
  """)

# ========================

# FOOTER

# ========================

st.markdown("---")
st.markdown("👤 **Azlinsyah Fadhilah Meran**")
