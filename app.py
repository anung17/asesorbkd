#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyleft © 2026 Anung <anung@trisakti.ac.id>
# 2026-01-07 13:14
# Distributed under terms of the MIT license.

"""
Asesor BKD
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Local class
import dosen as dsn

st.set_page_config(layout='wide')
st.title('Penugasan Asesor BKD')
st.write('# Data Dosen')

sheet_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRrs605OjSBBbGchqUt35HgN2c71vrsQGkhhHW4xHMti91Z23BmlqGHv-O1G131tXAYxkcxsuRrfMqw/pub?output=csv'

df = pd.read_csv(sheet_data)

st.write('## 5 data pertama')
st.write(df.head())

#iter_test = 5
#iter_count = 1
list_dosen = []
for row in df.itertuples(index=False):
    dosen = dsn.Dosen(row[2], row[5], row[6])
    #st.write(dosen)
    list_dosen.append(dosen)

st.write(f"{len(list_dosen)} `Dosen` objects were created.")

st.write('## Rangkuman')

colprodi, coljabamik, colpendidikan, colserdos = st.columns(4)
with colprodi:
    st.plotly_chart(
        px.pie(
            df,
            names='Program Studi',
            title='Komposisi Dosen per Program Studi'
        )
    )
with coljabamik:
    st.plotly_chart(
        px.pie(
            df, names='Jabamik',
            title='Komposisi Jabatan Akademik'
        )
    )
with colpendidikan:
    st.plotly_chart(
        px.pie(
            df, names='Pendidikan',
            title='Komposisi Pendidikan Terakhir'
        )
    )
with colserdos:
    st.plotly_chart(
        px.pie(
            df, names='Status Serdos',
            title='Komposisi Status Sertifikasi Dosen'
        )
    )
