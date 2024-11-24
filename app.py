import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time
import openpyxl

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

st.header('レッスン12: ファイルアップローダー')

uploaded_csv = st.file_uploader("CSVファイルをアップロードしてください", type="csv", key="csv_uploader")

if uploaded_csv is not None:
    df_csv = pd.read_csv(uploaded_csv)
    st.write("アップロードされたCSVファイルの内容:")
    st.write(df_csv)

    st.write("データの基本統計:")
    st.write(df_csv.describe())

    # 数値列の選択
    numeric_columns = df_csv.select_dtypes(include=[np.number]).columns.tolist()
    selected_column = st.selectbox("グラフ化する列を選択してください", numeric_columns, key="csv_column_select")

    # ヒストグラムの作成
    fig = go.Figure(data=[go.Histogram(x=df_csv[selected_column])])
    fig.update_layout(title=f"{selected_column}のヒストグラム")
    st.plotly_chart(fig)
    
    uploaded_excel = st.file_uploader("Excelファイルをアップロードしてください", type=["xlsx", "xls"], key="excel_uploader")

if uploaded_excel is not None:
    df_excel = pd.read_excel(uploaded_excel)
    st.write("アップロードされたExcelファイルの内容:")
    st.write(df_excel)

    st.write("シート名:")
    excel_file = openpyxl.load_workbook(uploaded_excel)
    st.write(excel_file.sheetnames)

    # 列の選択
    selected_columns = st.multiselect("表示する列を選択してください", df_excel.columns.tolist(), key="excel_column_select")

    if selected_columns:
        st.write("選択された列のデータ:")
        st.write(df_excel[selected_columns])

        # 散布図の作成（2つの列が選択された場合）
        if len(selected_columns) == 2:
            fig = go.Figure(data=go.Scatter(x=df_excel[selected_columns[0]],
                                            y=df_excel[selected_columns[1]],
                                            mode='markers'))
            fig.update_layout(title=f"{selected_columns[0]} vs {selected_columns[1]}の散布図")
            st.plotly_chart(fig)