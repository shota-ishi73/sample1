import streamlit as st
import time 

st.title('Streamlit超入門')

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)

'Done!!!'


expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味は', text, 'です。' 

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

# if st.checkbox('Show Image'):
#   img = Image.open('sample.png')
#   st.image(img, caption='sample', use_column_width=True)
