import streamlit as st
import random

# Layout tempat duduk: 4 baris × 12 kolom, dengan 35 kursi aktif
layout_mask = [[1]*5 + [0] + [1]*3 + [1]*4 for _ in range(4)]

def get_empty_layout():
    return [[None if seat == 1 else -1 for seat in row] for row in layout_mask]

def get_all_positions():
    return [(r, c) for r in range(4) for c in range(12) if layout_mask[r][c] == 1]

def generate_layout(numbers):
    positions = get_all_positions()
    random.shuffle(positions)
    layout = get_empty_layout()
    for i, num in enumerate(numbers):
        r, c = positions[i]
        layout[r][c] = num
    return layout

def get_position(layout, number):
    for r in range(4):
        for c in range(12):
            if layout[r][c] == number:
                return (r, c)
    return None

def are_adjacent(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    return abs(r1 - r2) + abs(c1 - c2) == 1

def is_valid(new_layout, prev_layout):
    for num in range(1, 36):
        pos_new = get_position(new_layout, num)
        pos_prev = get_position(prev_layout, num)
        if pos_new and pos_prev and are_adjacent(pos_new, pos_prev):
            return False
    return True

# Streamlit App
st.title("🎲 Acak Tempat Duduk Kelas")
st.markdown("Setiap kali diacak, posisi siswa tidak akan berdampingan dengan posisi sebelumnya.")

if 'prev_layout' not in st.session_state:
    st.session_state.prev_layout = generate_layout(list(range(1, 36)))

if st.button("🔄 Acak Tempat Duduk"):
    for _ in range(1000):
        new_layout = generate_layout(list(range(1, 36)))
        if is_valid(new_layout, st.session_state.prev_layout):
            st.session_state.prev_layout = new_layout
            break

layout = st.session_state.prev_layout

# Tampilkan visualisasi layout
for row in layout:
    cols = st.columns(12)
    for idx, seat in enumerate(row):
        if seat == -1:
            cols[idx].markdown(" ")
        else:
            cols[idx].button(str(seat), disabled=True)
