import streamlit as st
import FinanceDataReader as fdr
import datetime

# Finance Data Reader
# https://github.com/FinanceData/FinanceDataReader

date = st.date_input(
    "조회 시작일을 선택해 주세요", 
    datetime.datetime(2022, 1, 1)
)

code = st.text_input(
    """종목코드\n
    코스피(KS11), 코스닥(KQ11), S&P500(S&P500), 나스닥(IXIC), 닛케이(N225)\n
    카카오(035720), 삼성전자(005930), 애플(AAPL), NVIDIA(NVDA)""",
    value = '',
    placeholder = '종목코드를 입력해 주세요',
)

if code and date:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'Close']
    st.line_chart(data)
    