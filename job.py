import pandas as pd

import altair as alt
import streamlit as st
import datetime

job = pd.read_csv("job.csv")


st.title('受講者数可視化')

st.sidebar.write("""## 表示年度選択""")
s_year, e_year = st.sidebar.slider(
    '範囲を指定してください。',
    2010, 2022, (2010, 2022)
)
domain_pd = pd.to_datetime(
    [str(s_year)+'-01-01', str(e_year)+'-01-01']).astype(int) / 10 ** 6


num_employee = st.multiselect(
    '業務を選択してください。',
    list(job["業務"].unique().tolist()),
    ["システム化戦略・企画・計画"]
)

class_shiken = st.selectbox(
    '見たい受講区分を選択してください。',
    list(job["区分"].unique()))

st.write(class_shiken)
st.write(type(class_shiken))
data = job[job["業務"].isin(num_employee)]
data = data[data['区分'] == class_shiken]


chart = (
    alt.Chart(data)
    .mark_line(opacity=0.8, clip=True)
    .encode(
        x=alt.X("年度:T",
                scale=alt.Scale(domain=list(domain_pd))),
        y=alt.Y("人数:Q", stack=None),
        color='業務:N'
    )
)
st.altair_chart(chart, use_container_width=True)
