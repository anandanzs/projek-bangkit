import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

customer_df = pd.read_csv("customers_dataset.csv", delimiter=",")
review_df = pd.read_csv("order_reviews_dataset.csv", delimiter=",")
order_df = pd.read_csv("orders_dataset.csv", delimiter=",")

st.markdown("<h1 style='text-align: center;'>Proyek Analisis Data: E-Commerce Public Dataset</h1>", unsafe_allow_html=True)
st.write("")

st.subheader('Penjelasan Mengenai Data yang Digunakan')
teks = """
Data pelanggan e-commerce memberikan wawasan tentang interaksi dan perilaku pelanggan dalam platform. Identifikasi pelanggan memberikan landasan untuk memahami hubungan pelanggan dengan platform. Selain itu, terdapat informasi alamat pelanggan memberikan gambaran tentang geografi penyebaran pelanggan dan mempengaruhi pola pembelian atau preferensi produk berdasarkan lokasi geografis.

Data tentang ulasan pelanggan menggambarkan tingkat kepuasan dan umpan balik pelanggan terhadap pengalaman mereka dengan produk atau layanan yang dibeli. Sehingga dapat membantu untuk mengidentifikasi area yang memerlukan perhatian lebih lanjut atau perbaikan.

Informasi pesanan menciptakan jejak perjalanan pesanan pelanggan. Dengan memahami proses ini, platform dapat mengoptimalkan rantai pasokan, pengiriman, dan pelayanan pelanggan untuk meningkatkan pengalaman secara keseluruhan. Sebagai contoh, data dapat digunakan untuk mengevaluasi waktu pemenuhan pesanan, mendeteksi potensi masalah logistik, atau merencanakan promosi penjualan berdasarkan pola pembelian.

Secara keseluruhan, data pelanggan e-commerce menyediakan dasar untuk analisis mendalam mengenai perilaku pelanggan, peningkatan layanan, dan pengambilan keputusan strategis di tingkat operasional dan pemasaran.
"""
st.markdown(f'<div style="text-align: justify">{teks}</div>', unsafe_allow_html=True)

st.subheader('Data Yang Akan Digunakan')
st.write("**Tabel Customer**")
st.write(customer_df)
st.write("**Tabel Review**")
st.write(review_df)
st.write("**Tabel Order**")
st.write(order_df)
st.write("**Tabel Gabungan Antara Tabel Customer, Review, dan Order**")
merged_df = pd.merge(left=order_df, right=customer_df, how="left", on="customer_id")
all_df = pd.merge(left=merged_df, right=review_df, how="left", on="order_id")
st.table(all_df.head())

st.subheader('Pertanyaan Bisnis')
st.write("1. State mana yang paling banyak dan paling sedikit melakukan pembelian produk?")
st.write("2. Bagaimana tingkat kepuasan pelanggan tercermin dari skor ulasan?")
st.write("3. Apakah terdapat pengaruh bulan dan tertentu terhadap pembelian?")

st.subheader("Pembelian Produk Berdasarkan State")
st.write("**Analisis Data**")
purchase_frequency_by_state = customer_df.groupby('customer_state').size().reset_index(name='purchase_frequency')
purchase_frequency_by_state = purchase_frequency_by_state.sort_values(by='purchase_frequency')
st.write(purchase_frequency_by_state)

st.write("**Visualisasi Data**")
purchase_frequency_by_state = customer_df.groupby('customer_state').size().reset_index(name='purchase_frequency')
purchase_frequency_by_state = purchase_frequency_by_state.sort_values(by='purchase_frequency')

purchase_frequency_by_state = purchase_frequency_by_state.sort_values(by='purchase_frequency')
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(35, 15))
sns.barplot(x=purchase_frequency_by_state['customer_state'], y=purchase_frequency_by_state['purchase_frequency'], color='pink', ax=ax)
ax.set_ylabel("Frekuensi Pembelian", fontsize=30)
ax.set_xlabel("Kota Pembeli", fontsize=30)
ax.set_title('Pembelian Produk Berdasarkan State', loc='center', fontsize=45)
ax.tick_params(axis='y', labelsize=35)
ax.tick_params(axis='x', labelsize=30)
st.pyplot(fig)

top_states = purchase_frequency_by_state.head(5)
bottom_states = purchase_frequency_by_state.tail(5)

fig, axs = plt.subplots(1, 2, figsize=(20, 6))
axs[0].barh(top_states['customer_state'], top_states['purchase_frequency'], color='pink')
axs[0].set_title('Frekuensi Pembelian 5 State Terendah', loc='center', fontsize=20)
axs[0].set_xlabel('Frekuensi Pembelian')
axs[0].set_ylabel('Kota Pelanggan')

axs[1].barh(bottom_states['customer_state'], bottom_states['purchase_frequency'], color='pink')
axs[1].set_title('Frekuensi Pembelian 5 State Tertinggi', loc='center', fontsize=20)
axs[1].set_xlabel('Frekuensi Pembelian')
axs[1].set_ylabel('Kota Pelanggan')
st.pyplot(fig)

st.subheader("Kesimpulan")
st.write("Berdasarkan data frekuensi pembelian pada setiap negara bagian, terlihat bahwa São Paulo (SP) menjadi kontributor utama dengan jumlah pembelian yang sangat tinggi, mencerminkan potensi pasar yang signifikan di wilayah tersebut. Di sisi lain, negara bagian dengan frekuensi pembelian yang lebih rendah, seperti Roraima (RR) atau Acre (AC), mungkin memerlukan perhatian khusus dalam pengembangan strategi pemasaran dan distribusi untuk meningkatkan penetrasi pasar. Analisis ini dapat menjadi landasan bagi perusahaan untuk mengoptimalkan strategi pemasaran, logistik, dan pertumbuhan bisnis, dengan fokus pada negara bagian yang memiliki potensi tinggi atau memerlukan upaya lebih lanjut.")
st.subheader("Saran")
teks_dashboard = """
<style>
    p {
        text-align: justify;
    }
</style>

1. Dengan jumlah pembelian yang sangat tinggi di São Paulo, perusahaan sebaiknya mempertahankan fokus dan meningkatkan investasi pemasaran di wilayah ini. Upaya tambahan dapat termasuk kampanye pemasaran yang lebih spesifik dan adaptasi strategi penjualan untuk mencapai potensi pasar yang lebih besar.

2. Negara bagian seperti Roraima (RR) atau Acre (AC) yang menunjukkan frekuensi pembelian yang rendah mungkin memerlukan analisis lebih lanjut. Perusahaan perlu menyelidiki penyebab rendahnya aktivitas pembelian di wilayah-wilayah ini dan mengadaptasi strategi pemasaran, termasuk penyesuaian harga, promosi, atau inovasi produk untuk menarik pelanggan.

3. Penting untuk terus memantau kinerja strategi yang diterapkan dan secara berkala mengevaluasi data pembelian untuk mengidentifikasi perubahan tren atau perluasan peluang pasar di wilayah-wilayah tertentu.
"""

st.markdown(teks_dashboard, unsafe_allow_html=True)

st.subheader("Tingkat Kepuasan Pelanggan Berdasarkan Skor")
st.write("**Analisis Data**")
st.write("Ringkasan Analisis Statistika")
mean_score = review_df['review_score'].mean()
mean_score = round(mean_score, 2)
std_dev = review_df['review_score'].std()
std_dev = round(std_dev, 2)
min_score = review_df['review_score'].min()
max_score = review_df['review_score'].max()
data = {
    'Metric': ['Mean', 'Standard Deviation', 'Minimum', 'Maximum'],
    'Value': [mean_score, std_dev, min_score, max_score]
}
st.table(data)

st.write("Jumlah Pembeli Yang Memberikan Nilai")
count_score = review_df['review_score'].value_counts()
st.write(count_score.sort_index(ascending=True))

st.write("**Visualisasi Data**")
count_score = review_df['review_score'].value_counts()
fig, ax = plt.subplots(figsize=(8, 5))
colors = ['#FF69B4', '#FFB6C1', '#FFE4E1', '#FFC0CB', '#FF1493']
ax.pie(review_df['review_score'].value_counts(), labels=review_df['review_score'].value_counts().index, autopct='%1.1f%%', startangle=90, colors=colors)
ax.set_title('Distribusi Skor Kepuasan Pelanggan', fontsize=10)
st.pyplot(fig)

st.write("**Kesimpulan**")
st.write("Mayoritas pelanggan cenderung memberikan skor tinggi, terutama skor 5 yang mencapai jumlah 57,328, menunjukkan bahwa sebagian besar pelanggan memberikan penilaian positif terhadap layanan atau produk yang mereka terima. Meskipun skor 5 mendominasi, variasi skor ulasan terlihat dengan skor 4 yang cukup tinggi (19,142) dan skor 3 yang memiliki jumlah yang lebih rendah (8,179). Meski demikian, jumlah pelanggan yang memberikan skor 4 dan 5 secara bersama-sama mencapai 76,470, mengindikasikan tingkat kepuasan pelanggan secara umum yang tinggi. Pentingnya memahami komentar atau feedback dari pelanggan juga ditekankan, karena komentar dapat memberikan wawasan lebih mendalam tentang aspek-aspek spesifik yang memengaruhi tingkat kepuasan pelanggan. Untuk pemahaman yang lebih baik, analisis lebih lanjut dapat dilakukan dengan mempertimbangkan faktor-faktor lain seperti jenis produk atau layanan, waktu pengiriman, dan kebijakan pelayanan pelanggan.")
st.write("**Saran**")
teks_dashboard = """
<style>
    p {
        text-align: justify;
</style>

1. Meskipun mayoritas pelanggan memberikan skor tinggi, penting untuk melibatkan analisis lebih lanjut dengan mempertimbangkan faktor-faktor tambahan seperti jenis produk atau layanan, waktu pengiriman, dan kebijakan pelayanan pelanggan. Ini dapat membantu mengidentifikasi area tertentu yang mungkin memerlukan perhatian lebih lanjut untuk meningkatkan pengalaman pelanggan.

2. Komentar pelanggan dapat menjadi sumber inspirasi untuk inovasi produk atau layanan baru. Perusahaan dapat mempertimbangkan feedback pelanggan untuk mengembangkan peningkatan atau penyesuaian yang dapat meningkatkan daya tarik produk atau layanan.

3. Pemantauan secara teratur terhadap skor dan komentar pelanggan penting untuk menangkap tren atau perubahan persepsi pelanggan. Perusahaan dapat mengimplementasikan tindak lanjut yang sistematis berdasarkan temuan dari analisis, seperti perbaikan operasional atau peningkatan pelatihan karyawan.
"""
st.markdown(teks_dashboard, unsafe_allow_html=True)

st.subheader('Hubungan Antara Bulan dan Tahun Dengan Pembelian')
st.write("**Analisis Data**")
order_df['order_purchase_timestamp'] = pd.to_datetime(order_df['order_purchase_timestamp'])
order_df['purchase_month'] = order_df['order_purchase_timestamp'].dt.month
order_df['purchase_year'] = order_df['order_purchase_timestamp'].dt.year
monthly_yearly_purchase_counts = order_df.pivot_table(index='purchase_year', columns='purchase_month', aggfunc='size')
st.write(monthly_yearly_purchase_counts)

order_df["purchase_year"] = order_df["order_purchase_timestamp"].dt.year
purchase_2016 = order_df[order_df["purchase_year"] == 2016]
purchase_2017 = order_df[order_df["purchase_year"] == 2017]
purchase_2018 = order_df[order_df["purchase_year"] == 2018]
analysis_2016 = purchase_2016.groupby("purchase_month").size()
analysis_2017 = purchase_2017.groupby("purchase_month").size()
analysis_2018 = purchase_2018.groupby("purchase_month").size()
st.write("**Analisis Pada Tahun 2016**")
st.write(analysis_2016)
st.write("**Analisis Pada Tahun 2017**")
st.write(analysis_2017)
st.write("**Analisis Pada Tahun 2018**")
st.write(analysis_2018)

st.write("**Visualisasi Data**")
st.write("Menggunakan Heatmap")
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(monthly_yearly_purchase_counts, cmap='pink', annot=True, linewidths=.5, cbar_kws={'label': 'Jumlah Pembelian'})
plt.title('Pengaruh Bulan dan Tahun terhadap Pembelian', fontsize=20)
st.pyplot(fig)

st.write("Menggunakan Line Chart")
fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#FF69B4', '#FFB6C1', '#FFE4E1']
monthly_yearly_purchase_counts.T.plot(kind='line', marker='o', color=colors, linewidth=2, ax=ax)
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Pembelian')
ax.set_title('Jumlah Pembelian Setiap Bulan Pada Tahun 2016 Sampai 2018', fontsize=20)
ax.legend(title='Tahun', loc='upper right', bbox_to_anchor=(1.15, 1))
st.pyplot(fig)

fig, axs = plt.subplots(1, 3, figsize=(20, 6))
analysis_2016.plot(ax=axs[0], label='2016', marker='o', linestyle='-', color='pink')
axs[0].set_xlabel('Bulan')
axs[0].set_ylabel('Jumlah Pembelian')
axs[0].set_title('Analisis Tahun 2016 Jumlah Pembelian')
axs[0].legend(title='Tahun', loc='upper right')

analysis_2017.plot(ax=axs[1], label='2017', marker='o', linestyle='-', color='pink')
axs[1].set_xlabel('Bulan')
axs[1].set_ylabel('Jumlah Pembelian')
axs[1].set_title('Analisis Tahun 2017 Jumlah Pembelian')
axs[1].legend(title='Tahun', loc='upper right')

analysis_2018.plot(ax=axs[2], label='2018', marker='o', linestyle='-', color='pink')
axs[2].set_xlabel('Bulan')
axs[2].set_ylabel('Jumlah Pembelian')
axs[2].set_title('Analisis Tahun 2018 Jumlah Pembelian')
axs[2].legend(title='Tahun', loc='upper right')
st.pyplot(fig)

st.write("**Kesimpulan**")
st.write("Berdasarkan data jumlah pembelian per bulan dan tahun, dapat disimpulkan bahwa terdapat pengaruh bulan dan tahun tertentu terhadap aktivitas pembelian. Terjadi peningkatan jumlah pembelian dari tahun 2016 hingga 2018, dengan tren peningkatan yang lebih jelas pada tahun 2017, terutama di bulan-bulan seperti Maret, Mei, Juli, dan November. Puncak pembelian tercapai pada bulan November 2017. Namun, pada tahun 2018, pola pembelian menjadi lebih bervariasi, dengan penurunan yang signifikan di bulan Agustus dan peningkatan di bulan Oktober. Perlu dicatat bahwa terdapat data yang tidak tersedia pada tahun 2016 dan pada beberapa bulan tertentu. Kesimpulan ini memberikan wawasan tentang faktor-faktor yang dapat memengaruhi kegiatan pembelian, namun analisis lebih lanjut dengan mempertimbangkan konteks eksternal dapat memberikan pemahaman yang lebih mendalam.")
st.write("**Saran**")
teks_dashboard = """
<style>
    p {
        text-align: justify;
    }
</style>

1. Perusahaan dapat melakukan analisis yang lebih mendalam terhadap tren pembelian per tahun. Fokuskan pada tahun-tahun yang menunjukkan peningkatan signifikan, seperti 2017, untuk memahami apa yang mendorong kenaikan tersebut. Hal ini dapat membantu dalam perencanaan strategis dan pemasaran untuk tahun-tahun mendatang.

2. Selain memeriksa tren setiap tahun, perbandingan antar tahun dapat membuka wawasan tambahan. Memahami perbedaan dapat membantu perusahaan menyesuaikan strategi mereka sesuai dengan dinamika pasar yang berubah.
"""
st.markdown(teks_dashboard, unsafe_allow_html=True)