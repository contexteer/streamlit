import streamlit as st
import pandas as pd
import math

# 데이터 로드
file_path = 'data_test.csv'  # 상대 경로로 수정
df = pd.read_csv(file_path)

# 사이드바 제목 및 메뉴
st.sidebar.title('대학 입시 추천 시스템')
menu = st.sidebar.radio("메뉴 선택", ['지원 학과 검색', '메뉴 2', '메뉴 3', '메뉴 4'])

if menu == '지원 학과 검색':
    # 지원 학과 입력
    st.title('지원 학과 검색')
    major_input = st.text_input('지원 학과를 입력하세요:')

    # 데이터 필터링
    filtered_df = df[df['Major'].str.contains(major_input, na=False, case=False)]

    # 페이징
    items_per_page = 10
    total_items = len(filtered_df)
    total_pages = math.ceil(total_items / items_per_page)

    # 페이지 번호 입력
    if total_pages > 0:
        page_number = st.number_input('페이지 번호를 입력하세요:', min_value=1, max_value=total_pages, value=1)
    else:
        page_number = 1

    # 페이지에 맞는 데이터 슬라이싱
    start_idx = (page_number - 1) * items_per_page
    end_idx = start_idx + items_per_page
    page_data = filtered_df.iloc[start_idx:end_idx]

    # 결과 출력
    if not page_data.empty:
        st.write(f'총 {total_items}개의 결과 중 {major_input}단어가 일치하는 {start_idx + 1}부터 {end_idx}페이지의'
                 f'결과를 표시합니다.')
        st.write(page_data)
    else:
        st.write('조건에 맞는 학과가 없습니다.')

elif menu == '메뉴 2':
    st.title('메뉴 2')
    st.write('메뉴 2의 내용을 여기에 작성하세요.')

elif menu == '메뉴 3':
    st.title('메뉴 3')
    st.write('메뉴 3의 내용을 여기에 작성하세요.')

elif menu == '메뉴 4':
    st.title('메뉴 4')
    st.write('메뉴 4의 내용을 여기에 작성하세요.')

# 메인 페이지 내용
st.title('대학 입시 추천 시스템')
st.write('사이드바에서 메뉴를 선택하고 내용을 확인하세요.')
