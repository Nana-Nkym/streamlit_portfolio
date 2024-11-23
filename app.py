import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
st.header('レッスン5: 折れ線グラフの作成')

# サンプルデータの作成
data = {
    '月': ['1月', '2月', '3月', '4月', '5月', '6月'],
    '売上': [100, 120, 140, 180, 200, 210],
    '利益': [20, 25, 30, 40, 50, 55]
}
df = pd.DataFrame(data)

st.write('サンプルデータ:')
st.dataframe(df)

# 基本的な折れ線グラフの作成
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['月'], y=df['売上'], mode='lines+markers', name='売上'))
fig.add_trace(go.Scatter(x=df['月'], y=df['利益'], mode='lines+markers', name='利益'))

fig.update_layout(title='月別売上と利益',
                  xaxis_title='月',
                  yaxis_title='金額（万円）')

st.plotly_chart(fig)

# カスタマイズされた折れ線グラフの作成
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['月'], y=df['売上'], mode='lines+markers', name='売上', line=dict(color='blue', width=2)))
fig.add_trace(go.Scatter(x=df['月'], y=df['利益'], mode='lines+markers', name='利益', line=dict(color='red', width=2)))

fig.update_layout(
    title='月別売上と利益の推移',
    xaxis_title='月',
    yaxis_title='金額（万円）',
    font=dict(family="Meiryo", size=12),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    hovermode="x unified"
)

fig.update_xaxes(tickangle=45)
fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='lightgrey')

st.plotly_chart(fig)

st.header('レッスン6: 棒グラフ(plotly,go)の作成')

# サンプルデータの作成
data = {
    '製品': ['A', 'B', 'C', 'D', 'E'],
    '売上': [300, 400, 200, 600, 500],
    '利益': [30, 60, 20, 100, 80]
}
df = pd.DataFrame(data)

st.write('サンプルデータ:')
st.dataframe(df)

# 基本的な棒グラフの作成
fig = go.Figure()
fig.add_trace(go.Bar(x=df['製品'], y=df['売上'], name='売上'))
fig.add_trace(go.Bar(x=df['製品'], y=df['利益'], name='利益'))

fig.update_layout(title='製品別の売上と利益',
                  xaxis_title='製品',
                  yaxis_title='金額（万円）',
                  barmode='group')

st.plotly_chart(fig)

# カスタマイズされた棒グラフの作成
fig = go.Figure()
fig.add_trace(go.Bar(x=df['製品'], y=df['売上'], name='売上', marker_color='blue'))
fig.add_trace(go.Bar(x=df['製品'], y=df['利益'], name='利益', marker_color='red'))
fig.update_layout(
    title='製品別の売上と利益比較',
    xaxis_title='製品',
    yaxis_title='金額（万円）',
    barmode='group',
    font=dict(family="Meiryo", size=12),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    hovermode="x unified"
)

fig.update_traces(texttemplate='%{y}', textposition='outside')
fig.update_yaxes(range=[0, max(df['売上'].max(), df['利益'].max()) * 1.1])

st.plotly_chart(fig)

st.header('レッスン7: 円グラフ(plotly,go)の作成')

# サンプルデータの作成
data = {
    '商品': ['A', 'B', 'C', 'D', 'E'],
    '売上': [300, 200, 180, 150, 120]
}
df = pd.DataFrame(data)

st.write('サンプルデータ:')
st.dataframe(df)
# 基本的な円グラフの作成
fig = go.Figure(data=[go.Pie(labels=df['商品'], values=df['売上'])])

fig.update_layout(title='商品別売上比率')

st.plotly_chart(fig)

# カスタマイズされた円グラフの作成
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'lightcoral']
fig = go.Figure(data=[go.Pie(labels=df['商品'],
                             values=df['売上'],
                             hole=.3,
                             marker=dict(colors=colors,
                                         line=dict(color='#000000', width=2)))])

fig.update_traces(textposition='inside',
                  textinfo='percent+label',
                  hoverinfo='label+value+percent',
                  textfont_size=14)

fig.update_layout(
    title='商品別売上比率（詳細版）',
    font=dict(family="Meiryo", size=12),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    annotations=[dict(text='総売上', x=0.5, y=0.5, font_size=20, showarrow=False)]
)

st.plotly_chart(fig)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time
st.header('レッスン8: キャッシュを使用したパフォーマンス最適化')

def generate_large_dataset():
    # 大きなデータセットを生成（約10秒かかる）
    data = pd.DataFrame(np.random.randn(1000000, 5), columns=['A', 'B', 'C', 'D', 'E'])
    return data

@st.cache_data
def load_data_cached():
    return generate_large_dataset()

def load_data_uncached():
    return generate_large_dataset()

st.subheader("キャッシュなしの場合")
start_time = time.time()
data_uncached = load_data_uncached()
end_time = time.time()
st.write(f"データ読み込み時間: {end_time - start_time:.2f} 秒")
st.write(data_uncached.head())

st.subheader("キャッシュありの場合")
start_time = time.time()
data_cached = load_data_cached()
end_time = time.time()
st.write(f"データ読み込み時間: {end_time - start_time:.2f} 秒")
st.write(data_cached.head())

st.write("キャッシュありの場合、2回目以降の読み込みは非常に高速になります。")

@st.cache_resource
def load_large_dataset():
    return pd.DataFrame(
        np.random.randn(10000000, 5),
        columns=['A', 'B', 'C', 'D', 'E']
    )

st.subheader("大規模データセットの処理")
start_time = time.time()
large_data = load_large_dataset()
end_time = time.time()
st.write(f"大規模データセット読み込み時間: {end_time - start_time:.2f} 秒")
st.write(f"データセットの形状: {large_data.shape}")
st.write(large_data.head())

@st.cache_data(ttl=10)
def get_current_time():
    return pd.Timestamp.now()

st.subheader("キャッシュの無効化")
st.write("現在時刻（10秒ごとに更新）:")
st.write(get_current_time())

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time
st.header('レッスン9: セッション状態の管理')

if 'count' not in st.session_state:
    st.session_state.count = 0

st.write(f"現在のカウント: {st.session_state.count}")

if st.button('カウントアップ'):
    st.session_state.count += 1
    st.rerun()

if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'user_email' not in st.session_state:
    st.session_state.user_email = ""

user_name = st.text_input("ユーザー名", value=st.session_state.user_name)
user_email = st.text_input("メールアドレス", value=st.session_state.user_email)

if st.button("ユーザー情報を保存"):
    st.session_state.user_name = user_name
    st.session_state.user_email = user_email
    st.success("ユーザー情報が保存されました！")

st.write(f"セッションに保存されたユーザー名: {st.session_state.user_name}")
st.write(f"セッションに保存されたメールアドレス: {st.session_state.user_email}")

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['商品', '価格'])

product = st.text_input("商品名を入力")
price = st.number_input("価格を入力", min_value=0)

if st.button("商品データを追加"):
    new_data = pd.DataFrame({'商品': [product], '価格': [price]})
    st.session_state.df = pd.concat([st.session_state.df, new_data], ignore_index=True)

st.write("現在の商品データ:")
st.write(st.session_state.df)

if st.button("データをリセット"):
    st.session_state.df = pd.DataFrame(columns=['商品', '価格'])
    st.rerun()
    
