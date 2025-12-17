import streamlit as st
import random
import uuid
# ----------------------------
# 전체 배경 & 폰트 & 제목
# ----------------------------
st.markdown(
    """
    <style>
    .stApp{
        background-color: #fff0f6;
        font-family: 'Apple SD Gothic Neo', 'Pretendard', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style="
        text-align:center;
        color:#ff4d6d;
        font-weight:700;
    ">
    우리 300일 됐어 ❤️
    </h1>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# 상태 초기화
# ----------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
if "today_msg" not in st.session_state:
    st.session_state.today_msg = ""
if "heart" not in st.session_state:
    st.session_state.heart = 0
if "reason_idx" not in st.session_state:
    st.session_state.reason_idx = 0

# ----------------------------
# 메시지 & 이유 리스트
# ----------------------------
messages = [
    "오늘두 누나 보고싶어!!!",
    "눈나!!! 사랑해❤️",
    "오늘 하루도 너무너무 수고했어 ㅎㅎ",
    "오늘 왤케 귀엽고 사랑스러워??",
    "너 무야... 내꺼 히지니!!",
    "누나 웃는 거 생각하니까 괜히 기분 좋아!!",
    "내 감쟈 히지니!!! 내 옆에 항상 이써!!!"
]

reasons = [
    "항상 너무 이쁘게 말해줘서",
    "나를 먼저 이해해주고 생각해줘서",
    "같이 노는게 너무 재밌고 좋아.",
    "힘이 되고 누나한테 동기부여도 많이 받아",
    "솔직히 말해도 돼??",
    "그냥.. 희진이 너라서",
    "진짜 이유는 너무너무 많지만... 이 정도면 알지?😊"
]

# ----------------------------
# 버튼 영역
# ----------------------------
st.markdown(
    """
    <div style="
    display: flex;
    justify-content: center;
    gap : 20px;
    margin-bottom:30px;
    ">
    </div>
    """,
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button("💌 오늘의 후니의 한마디!!"):
        st.session_state.today_msg = random.choice(messages)
        st.session_state.step = 1

with col2:
    if st.button("❤️ 하트 키우기"):
        st.session_state.step = 2

with col3:
    if st.button("💭 누나를 좋아하는 이유"):
        st.session_state.step = 3
        st.session_state.reason_idx = 0

st.divider()

# ----------------------------
# STEP 0 - 기본 안내
# ----------------------------
if st.session_state.step == 0:
    st.markdown(
        """
        <div style="
            background:white;
            padding:20px;
            border-radius:20px;
            text-align:center;
            box-shadow:0 4px 12px rgba(0,0,0,0.08);
        ">
            💝 300일 기념으로 준비한 작은 선물이야 💝<br><br>
            누나 생각하면서 한 번 만들어봤어!!<br><br>
            버튼을 하나씩 눌러봐 히히 😊
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# STEP 1 - 오늘의 한마디
# ----------------------------
elif st.session_state.step == 1:
    st.markdown(
        """
        <div style="
            font-size:24px;
            font-weight:bold;
            color:#ff66b3;
            text-align:center;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
            margin-bottom:15px;
        ">
            내가 해주는 말이 글케 듣고 싶어??
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <style>
        @keyframes slideUp {{
            0% {{ transform: translateY(20px); opacity:0; }}
            100% {{ transform: translateY(0); opacity:1; }}
        }}
        .today-msg {{
            font-size:22px;
            color:#ff3399;
            background-color:#ffe6f0;
            padding:15px;
            border-radius:12px;
            text-align:center;
            margin:10px 0;
            box-shadow:2px 2px 8px rgba(0,0,0,0.1);
            animation: slideUp 1.5s ease-out;
        }}
        </style>
        <div class="today-msg">
            {st.session_state.today_msg}
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# STEP 2 - 하트 키우기
# ----------------------------
elif st.session_state.step == 2:
    st.markdown("<br><br>", unsafe_allow_html=True)

    # 리셋 버튼
    if st.button("🔄 우리 사랑을 다시 시작하기"):
        st.session_state.heart = 0

    # 하트 증가 버튼
    if st.button("❤️ 누나의 마음 크기를 보여줘 ❤️"):
        st.session_state.heart += 1

    # 현재 하트 개수 표시
    st.markdown(
        f"<h3 style='text-align:center; color:#cc3366;'>현재 하트 개수: {st.session_state.heart}❤️</h3>",
        unsafe_allow_html=True
    )

    # 하트 멘트 카드 메시지
    if st.session_state.heart < 5:
        msg = [
            "날 이렇게밖에 안 사랑해...?? ㅠㅠ",
            "그래도 더 커질거라구 기대하구 있어 누나!!"
        ]
    elif st.session_state.heart < 10:
        msg = [
            "점점 커진다 헤헤 ㅎㅎ 나 좀 좋아하나 보다!! ❤️",
            "진짜 설레고 좋았을 초반처럼 하트가 커지고 이쎠!",
            "이쯤에서 멈출 건 아니지??"
        ]
    elif st.session_state.heart < 20:
        msg = [
            "조금만 더!!!! 난 누나 사랑이 더 부족해!!",
            "그거 알아? 나도 누나 많이 사랑한다?",
            "근데 난 솔직히 이거보다 더 좋아해..!!"
        ]
    else:
        msg = [
            "나도 사랑해💕💕💕💕",
            "나 많이 좋아하네 누나??",
            "모오오 나도 이만큼 좋아하거든",
            "사랑해 히지니!!"
        ]

    # 카드 HTML 생성 (오늘의 한마디 카드 스타일 적용)
    card_html = f"""
    <div style="
        font-family: 'Apple SD Gothic Neo', Pretendard, sans-serif;
        font-size:18px;
        color:#ff3399;
        background-color:#ffe6f0;
        padding:15px;
        border-radius:12px;
        text-align:center;
        margin:10px 0;
        box-shadow:2px 2px 8px rgba(0,0,0,0.1);
    ">
    """
    for line in msg:
        card_html += f"<p> {line}</p>"
    card_html += "</div>"

    st.markdown(card_html, unsafe_allow_html=True)

    # 커지는 하트 애니메이션
    size = min(32 + st.session_state.heart * 5, 90)
    st.markdown(
        f"""
        <div style="
            font-size:{size}px;
            text-align:center;
            animation: pop 1.5s ease-out;
        ">
            ❤️
        </div>
        <style>
        @keyframes pop {{
            0% {{ transform: scale(0.8); opacity: 0; }}
            50% {{ transform: scale(1.2); opacity: 1; }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# STEP 3 - 좋아하는 이유 카드 디자인
# ----------------------------
elif st.session_state.step == 3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="
            font-size:24px;
            font-weight:bold;
            color:#ff66b3;
            text-align:center;
            margin-bottom:15px;
        ">
            내가 널 왜 좋아하냐면... 💭
        </div>
        """,
        unsafe_allow_html=True
    )

    # 버튼 클릭에 따라 하나씩 이유 표시
    if st.session_state.reason_idx > 0:
        for i in range(st.session_state.reason_idx):
            st.markdown(
                f"""
                <style>
                @keyframes slideUp{i} {{
                    0% {{ transform: translateY(20px); opacity:0; }}
                    100% {{ transform: translateY(0); opacity:1; }}
                }}
                .reason-card{i} {{
                    font-family: 'Apple SD Gothic Neo', Pretendard, sans-serif;
                    font-size:18px;
                    color:#ff3399;
                    background-color:#ffe6f0;
                    padding:15px;
                    border-radius:12px;
                    text-align:center;
                    margin:10px 0;
                    box-shadow:2px 2px 8px rgba(0,0,0,0.1);
                    animation: slideUp{i} 0.6s ease-out;
                }}
                </style>
                <div class="reason-card{i}">
                    💌 {reasons[i]}
                </div>
                """,
                unsafe_allow_html=True
            )

    # 아직 안 보여준 이유가 남아있으면 버튼 생성
    if st.session_state.reason_idx < len(reasons):
        if st.button("하나 더 알려줄게 💕"):
            st.session_state.reason_idx += 1
            st.rerun()
    else:
        st.snow()
        if st.button("마지막으로 하고 싶은 말"):
            st.session_state.step = 4
            st.rerun()

# ----------------------------
# STEP 4 - 엔딩
# ----------------------------
# ----------------------------
# STEP 4 - 엔딩
# ----------------------------
elif st.session_state.step == 4:
    st.markdown("<br><br>", unsafe_allow_html=True)

    # 감동적인 엔딩 카드 스타일 (수정된 문구)
    end_html = """
    <div style="
        background: linear-gradient(135deg, #ffe6f0, #ffccd9);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 4px 4px 20px rgba(0,0,0,0.15);
        text-align: center;
        font-family: 'Apple SD Gothic Neo', Pretendard, sans-serif;
        color: #ff3366;
        font-size: 20px;
        line-height: 1.8;
        margin: 20px;
    ">
        <p>희진아</p>
        <p>300일 동안</p>
        <p>나랑 같이 웃어줘서 고마워</p>
        <br>
        <p>누나 덕분에</p>
        <p>올해가 참 좋았어</p>
        <br>
        <p>지금처럼</p>
        <p>앞으로도 내 곁에 있어줘</p>
        <br>
        <p>고마워</p>
        <p style='font-size:26px; font-weight:bold;'>사랑해 💖</p>
    </div>
    """
    st.markdown(end_html, unsafe_allow_html=True)

    # 마지막으로 벌룬 효과
    st.balloons()

