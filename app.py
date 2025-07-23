import streamlit as st
import random

st.set_page_config(page_title="Acak Tempat Duduk", layout="wide")
st.title("Acak Tempat Duduk 5×8 (35 kursi)")

rows = 5
cols = 8
total_slots = rows * cols  # 40 slot
active_seats = 35          # kursi aktif

# Buat daftar indeks aktif (yang digunakan)
# Ini berdasarkan urutan baris→kolom
used_indices = [i for i in range(total_slots)]
empty_indices = [35, 36, 37, 38, 39]  # posisi kosong (baris 5 kolom 4–8)
for i in empty_indices:
    used_indices.remove(i)

# Simpan shuffle seats di session
if "seats" not in st.session_state:
    st.session_state.seats = list(range(1, active_seats + 1))
    random.shuffle(st.session_state.seats)

# Tombol acak ulang
if st.button("Acak"):
    random.shuffle(st.session_state.seats)

# Tombol reset urutan
if st.button("Reset"):
    st.session_state.seats = list(range(1, active_seats + 1))

# Layout
cols_widgets = st.columns(cols)

# Isi grid 5×8
seat_idx = 0
for row in range(rows):
    for col in range(cols):
        slot_number = row * cols + col
        with cols_widgets[col]:
            if slot_number in used_indices:
                seat_number = st.session_state.seats[seat_idx]
                st.button(str(seat_number), disabled=True, key=f"{row}-{col}")
                seat_idx += 1
            else:
                st.markdown(" ")  # posisi kosong
