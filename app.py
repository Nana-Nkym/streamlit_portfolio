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


st.header('レッスン11: スライダーとセレクトボックス')

sample_size = st.slider('サンプルサイズを選択', min_value=10, max_value=1000, value=100, step=10, key='sample_slider')

data_sample1 = pd.DataFrame(np.random.randn(sample_size, 2), columns=['X', 'Y'])

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=data_sample1['X'], y=data_sample1['Y'], mode='markers'))
st.plotly_chart(fig1)

data_sample2 = pd.DataFrame(np.random.uniform(0, 100, size=(1000, 2)), columns=['P', 'Q'])

range_values = st.slider('値の範囲を選択', min_value=0.0, max_value=100.0, value=(25.0, 75.0), key='range_slider')

filtered_data = data_sample2[(data_sample2['P'] >= range_values[0]) & (data_sample2['P'] )]
                                                                       
data_sample3 = pd.DataFrame(np.random.randn(200, 2), columns=['M', 'N'])

color_option = st.selectbox('マーカーの色を選択', ['blue', 'red', 'green', 'purple'], key='color_select')

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=data_sample3['M'], y=data_sample3['N'], mode='markers', marker=dict(color=color_option)))
st.plotly_chart(fig3)

columns_to_plot = st.multiselect('プロットする列を選択', ['A', 'B', 'C', 'D'], default=['A', 'B'], key='column_multiselect')

num_points = st.slider('データポイント数', min_value=50, max_value=1000, value=200, step=50, key='points_slider')

data_sample4 = pd.DataFrame(np.random.randn(num_points, 4), columns=['A', 'B', 'C', 'D'])

fig4 = go.Figure()
for col in columns_to_plot:
    fig4.add_trace(go.Scatter(x=data_sample4.index, y=data_sample4[col], mode='lines+markers', name=col))

st.plotly_chart(fig4)

