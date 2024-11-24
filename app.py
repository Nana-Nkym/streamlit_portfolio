import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time
st.header('レッスン10: ボタンとチェックボックス')

if st.button('データを生成', key='generate_data'):
    random_data = pd.DataFrame(np.random.randn(20, 3), columns=['X', 'Y', 'Z'])
    st.write(random_data)

show_chart = st.checkbox('チャートを表示', key='show_chart')

if show_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['X', 'Y', 'Z'])
    fig = go.Figure()
    for column in chart_data.columns:
        fig.add_trace(go.Scatter(x=chart_data.index, y=chart_data[column], mode='lines', name=column))
    st.plotly_chart(fig)
    
if 'counter' not in st.session_state:
    st.session_state.counter = 0

col1, col2, col3 = st.columns(3)

if col1.button('カウントアップ', key='count_up'):
    st.session_state.counter += 1

if col2.button('カウントダウン', key='count_down'):
    st.session_state.counter -= 1

if col3.button('リセット', key='reset_count'):
    st.session_state.counter = 0

st.write(f"現在のカウント: {st.session_state.counter}")

column_options = st.multiselect(
    '表示する列を選択してください',
    ['X', 'Y', 'Z'],
    ['X', 'Y', 'Z'],
    key='column_selection')

sample_data = pd.DataFrame(np.random.randn(10, 3), columns=['X', 'Y', 'Z'])
st.write(sample_data[column_options])


