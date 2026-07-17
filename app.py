import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="MindCare Dashboard", page_icon="🧠", layout="wide")

st.markdown("""
<style>
.block-container{padding-top:2rem;}
.stButton>button{width:100%;border-radius:10px;}
</style>
""", unsafe_allow_html=True)

if "hasil" not in st.session_state:
    st.session_state.hasil=[]
 
menu=st.sidebar.radio("📋 Menu",["🏠 Home","📚 Edukasi","📝 Self Check","📊 Dashboard","👨 About"])

if menu=="🏠 Home":
    st.title("🧠 MindCare Dashboard")
    st.subheader("Healthy Mind • Healthy Life")
    try:
        st.image("gamabar/_KELOMPOK 3 (Psikologi Kesehatan Mental)_page-0001.jpgs",use_container_width=True)
    except:
        st.info("Tambahkan file mental.png pada folder yang sama.")
    st.success("Selamat datang di aplikasi edukasi kesehatan mental mahasiswa.")
    c1,c2,c3=st.columns(3)
    with c1:
        st.info("😊 Self Care")
        st.write("Luangkan waktu untuk diri sendiri.")
    with c2:
        st.warning("😴 Sleep")
        st.write("Tidur 7–8 jam setiap hari.")
    with c3:
        st.success("💪 Healthy Lifestyle")
        st.write("Olahraga dan makan bergizi.")

elif menu=="📚 Edukasi":
    st.title("📚 Edukasi")
    with st.expander("😰 Apa itu Stres?"):
        st.write("Stres adalah respons tubuh terhadap tekanan.")
    with st.expander("😟 Apa itu Kecemasan?"):
        st.write("Kecemasan adalah rasa khawatir yang berlebihan.")
    with st.expander("💡 Tips Menjaga Kesehatan Mental"):
        st.markdown("""
- Tidur cukup
- Olahraga
- Kelola waktu
- Curhat dengan orang terpercaya
- Beribadah
""")

elif menu=="📝 Self Check":
    st.title("📝 Self Check")
    st.caption("Nilai 0 = Tidak Pernah, 3 = Sangat Sering")
    qs=[
        "Saya merasa mudah lelah",
        "Saya sulit tidur",
        "Saya sulit berkonsentrasi",
        "Saya mudah cemas",
        "Saya kehilangan semangat"
    ]
    total=0
    for q in qs:
        total+=st.slider(q,0,3,0)
    st.subheader(f"Skor: {total}")
    if total<=5:
        kategori="Baik 🟢"; st.success(kategori)
    elif total<=10:
        kategori="Perlu Istirahat 🟡"; st.warning(kategori)
    else:
        kategori="Perlu Konseling 🔴"; st.error(kategori)

    a,b=st.columns(2)
    with a:
        if st.button("💾 Simpan Data"):
            st.session_state.hasil.append({"Skor":total,"Kategori":kategori})
            st.success("Data disimpan.")
    with b:
        if st.button("🗑️ Clear Data"):
            st.session_state.hasil.clear()
            st.success("Semua data dihapus.")
            st.rerun()

elif menu=="📊 Dashboard":
    st.title("📊 Dashboard")
    if not st.session_state.hasil:
        st.warning("Belum ada data.")
    else:
        df=pd.DataFrame(st.session_state.hasil)
        c1,c2=st.columns(2)
        c1.metric("Jumlah Data",len(df))
        c2.metric("Rata-rata Skor",round(df["Skor"].mean(),2))
        st.plotly_chart(px.bar(df,y="Skor",color="Kategori",text="Skor"),use_container_width=True)
        st.plotly_chart(px.pie(df,names="Kategori",title="Distribusi Kategori"),use_container_width=True)
        st.dataframe(df,use_container_width=True)
        if st.button("❌ Hapus Semua Data Dashboard"):
            st.session_state.hasil.clear()
            st.rerun()

else:
    st.title("👨 About")
    st.write("""
### Dashboard Edukasi Kesehatan Mental

Proyek praktikum **Sistem Multimedia** menggunakan:
- Python
- Streamlit
- Pandas
- Plotly

**Catatan:** Self Check hanya untuk edukasi, bukan alat diagnosis medis.
""")
    st.info("©️ Universitas Nurdin Hamzah")