import streamlit as st

# 사이드바 메뉴
st.sidebar.title('안녕하세요')
menu = st.sidebar.radio(
    '위에서 데모를 선택하세요.',
    ['홈', '애니메이션 데모', '콜론 데모', '매핑 데모', '데이터 프레임 데모']
)

# 선택한 메뉴에 따라 다른 페이지 내용 표시
if menu == '홈':
    st.title('Streamlit에 오신 것을 환영합니다! 👋')
    st.write('''
    Streamlit은 머신 러닝 및 데이터 과학 프로젝트를 위해 특별히 구축된 오픈 소스 웹 프레임워크입니다. 🌟 사이드바에서 데모를 선택하여 Streamlit이 무엇을 할 수 있는지 몇 가지 예를 확인하세요!
    ''')
    st.subheader('더 자세히 알고 싶으신가요?')
    st.write('[streamlit.io](https://streamlit.io)로 확인하세요.')
    st.write('[우리 문서로 이동하세요](https://docs.streamlit.io).')
    st.write('[커뮤니티 포럼](https://discuss.streamlit.io)에서 질문해보세요.')

    st.subheader('더 복잡한 데모 보기')
    st.write('신경망을 사용하여 [Udacity 자율주행차 이미지 데이터셋 분석](https://github.com/udacity/self-driving-car)하기')
    st.write('높은 신뢰도 데이터셋 [탐색](https://github.com/streamlit/demo-self-driving)하기')
elif menu == '애니메이션 데모':
    st.title('애니메이션 데모')
    st.write('여기에 애니메이션 데모 내용이 들어갑니다.')
elif menu == '콜론 데모':
    st.title('콜론 데모')
    st.write('여기에 콜론 데모 내용이 들어갑니다.')
elif menu == '매핑 데모':
    st.title('매핑 데모')
    st.write('여기에 매핑 데모 내용이 들어갑니다.')
elif menu == '데이터 프레임 데모':
    st.title('데이터 프레임 데모')
    st.write('여기에 데이터 프레임 데모 내용이 들어갑니다.')
