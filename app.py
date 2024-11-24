import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time
import openpyxl
st.header('レッスン13: カラムとコンテナによるレイアウト')
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("列1")
    st.write("ここは1列目です。")
    st.button("ボタン1", key="button1")

with col2:
    st.subheader("列2")
    st.write("ここは2列目です。")
    st.checkbox("チェックボックス", key="checkbox1")

with col3:
    st.subheader("列3")
    st.write("ここは3列目です。")
    st.radio("ラジオボタン", ["選択肢1", "選択肢2", "選択肢3"], key="radio1")
    
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("左側（幅広）")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
    selected_column = st.selectbox("データを選択", ["A", "B", "C"], key="data_select")
    st.line_chart(chart_data[selected_column])

with col_right:
    st.subheader("右側（幅狭）")
    st.write(f"選択されたデータ: {selected_column}")
    st.write(f"平均値: {chart_data[selected_column].mean():.2f}")
    st.write(f"最大値: {chart_data[selected_column].max():.2f}")
    st.write(f"最小値: {chart_data[selected_column].min():.2f}")
    
with st.container():
    st.subheader("ネストされたレイアウト")

    col1, col2 = st.columns(2)

    with col1:
        st.write("左側のカラム")
        with st.container():
            st.write("左側のコンテナ")
            slider_value = st.slider("値を選択", 0, 100, 50, key="nested_slider")
            st.write(f"選択された値: {slider_value}")

    with col2:
        st.write("右側のカラム")
        with st.container():
            st.write("右側の上部コンテナ")
            option = st.selectbox("オプションを選択", ["オプション1", "オプション2", "オプション3"], key="nested_select")
            st.write(f"選択されたオプション: {option}")

        with st.container():
            st.write("右側の下部コンテナ")
            if st.button("クリックしてください", key="nested_button"):
                st.write("ボタンがクリックされました！")
                
                
st.header('レッスン14: エクスパンダーとサイドバーによるレイアウト')

st.subheader("エクスパンダーの使用例")

# 1年分のデータを生成
sales_data = pd.DataFrame({
    '日付': pd.date_range(start='2023-01-01', end='2023-12-31'),
    '売上': np.random.randint(1000, 5000, 365),
    '商品': np.random.choice(['A', 'B', 'C'], 365)
})

with st.expander("データセットの詳細を表示"):
    st.dataframe(sales_data)

with st.expander("グラフを表示"):
    fig = go.Figure(data=go.Scatter(x=sales_data['日付'], y=sales_data['売上'], mode='lines+markers'))
    fig.update_layout(title='日別売上推移')
    st.plotly_chart(fig)

with st.expander("統計情報"):
    st.write(f"総売上: {sales_data['売上'].sum():,}円")
    st.write(f"平均売上: {sales_data['売上'].mean():.2f}円")
    st.write(f"最高売上: {sales_data['売上'].max():,}円")
    st.write(f"最低売上: {sales_data['売上'].min():,}円")
    
st.subheader("サイドバーの使用例")

st.sidebar.title("データ分析ツール")

analysis_option = st.sidebar.radio(
    "分析オプション",
    ("データ概要", "売上分析", "商品別分析")
)

date_range = st.sidebar.date_input(
    "日付範囲",
    value=(sales_data['日付'].min().date(), sales_data['日付'].max().date())
)

filtered_data = sales_data[(sales_data['日付'].dt.date >= date_range[0]) & (sales_data['日付'].dt.date )]
                                                                          
st.subheader("高度なエクスパンダーの使用例")

with st.expander("カスタム分析"):
    selected_product = st.selectbox("分析する商品を選択", sales_data['商品'].unique())
    product_data = filtered_data[filtered_data['商品'] == selected_product]

    if product_data.empty:
        st.info("選択された日付範囲と商品の組み合わせにデータがありません。")
    else:
        st.write(f"商品 {selected_product} の分析")
        st.line_chart(product_data.set_index('日付')['売上'])

        if st.checkbox("詳細統計を表示"):
            st.write(product_data['売上'].describe())