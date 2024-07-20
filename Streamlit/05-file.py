import chardet
import streamlit as st
import pandas as pd
import time
import csv 

# 파일 업로드 버튼 (업로드 기능)

uploaded_file = st.file_uploader("파일 선택(csv or excel)", type=['csv', 'xls', 'xlsx'])

# 업로드된 파일의 인코딩 확인
def detect_file_encoding(file):
    # 파일의 처음 몇 줄만 읽어 인코딩 감지
    raw_data = file.read(1024)  # 처음 1024바이트만 읽음
    result = chardet.detect(raw_data)
    file.seek(0)
    return result['encoding']

# 파일이 정상 업로드 된 경우
# if uploaded_file is not None:
#     # 파일 읽기
#     df = pd.read_csv(uploaded_file)
#     # 출력
#     st.dataframe(df)
# file_encoding = detect_file_encoding(uploaded_file)
# st.write(f'파일 인코딩: {file_encoding}')
    
time.sleep(3)

# Excel or CSV 확장자를 구분하여 출력하는 경우
if uploaded_file is not None:
    ext = uploaded_file.name.split('.')[-1]
    file_encoding = detect_file_encoding(uploaded_file)
    
    st.warning(f"감지된 파일 인코딩: {file_encoding}")
    
    # 오류가 날 경우를 대비한 try ~ except 구문 추가
    try:
        if ext == 'csv':
            # 파일 읽기
            df = pd.read_csv(uploaded_file, encoding=file_encoding)
            # 출력
            st.dataframe(df)
        elif 'xls' in ext:
            # 엑셀 로드
            df = pd.read_excel(uploaded_file, engine='openpyxl')
            # 출력
            st.dataframe(df)
    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {str(e)}")