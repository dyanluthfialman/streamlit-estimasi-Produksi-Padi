import pickle
import streamlit as st

model = pickle.load(open('estimasi_Produksipadi.sav', 'rb'))

st.title('Estimasi')
st.subheader('Jumlah Produksi Padi Di Pulau Sumatra')
st.write('---')

Tahun = st.number_input('Input Tahun(Masehi)')
Luas_Panen = st.number_input('Input Luas Panen(m²)')
Curah_hujan = st.number_input('Input Curah hujan (mm)')
Kelembapan = st.number_input('Input Total Kelembaban(gr)')
Suhu_ratarata = st.number_input('Input Suhu(°C )')

predict = ''

if st.button('Estimasi Produksi'):
    predict = model.predict(
        [[Tahun, Luas_Panen, Curah_hujan,Kelembapan,Suhu_ratarata]]    )
    st.write ('Estimasi jumlah Produksi Padi di Pulau Sumatra (TON) : ', predict)
