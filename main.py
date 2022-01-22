from turtle import left
from pyparsing import condition_as_parse_action
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'スタート！'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'完了！'
    

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')



option = st.sidebar.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(1, 11))
)
'あなたが好きな数字は、', option, 'です'

text= st.sidebar.text_input('あなたの趣味を教えて下さい')
'あなたの趣味：', text

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

# img = Image.open('sample.jpg')
# st.image(img, caption='yosuke in')
