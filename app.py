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

st.set_page_config(layout='wide')
st.title('Penugasan Asesor BKD')
st.header('Penugasan Asesor BKD')

sheet_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRrs605OjSBBbGchqUt35HgN2c71vrsQGkhhHW4xHMti91Z23BmlqGHv-O1G131tXAYxkcxsuRrfMqw/pub?output=csv'

df = pd.read_csv(sheet_data)

st.write('## 5 data pertama')
st.write(df.head())

st.write('## Rangkuman')

colprodi, coljabamik, colserdos = st.columns(3)
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
with colserdos:
    st.plotly_chart(
        px.pie(
            df, names='Status Serdos',
            title='Komposisi Status Sertifikasi Dosen'
        )
    )
