import streamlit as st

st.set_page_config(page_title="MBTI로 알아보는 IT 직업 추천", page_icon="💡", layout="centered")

# 🎉 타이틀과 배경 꾸미기
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #6a0dad;
            text-align: center;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #444;
        }
        .job-card {
            background-color: #ffffffaa;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            margin: 20px 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🌟 MBTI로 알아보는 IT 직업 추천 🌟</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 MBTI에 딱 맞는 IT 직업을 알아보세요! 🤖💼</div>', unsafe_allow_html=True)
st.write("")

# 📋 MBTI 선택
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
selected_mbti = st.selectbox("🧬 당신의 MBTI를 선택하세요:", mbti_types)

# 🧠 MBTI 별 추천 직업
job_recommendations = {
    "INTJ": ("🧠 데이터 과학자", "분석적이고 전략적인 성향으로 데이터 기반 문제 해결에 탁월해요!"),
    "INTP": ("🧪 알고리즘 개발자", "호기심 많고 창의적인 문제 해결사에게 딱이에요."),
    "ENTJ": ("📈 IT 프로젝트 매니저", "리더십과 전략 수립에 강한 당신에게 적합해요."),
    "ENTP": ("🎮 게임 기획자", "창의력과 커뮤니케이션 능력을 활용해 멋진 게임을 설계해보세요."),
    "INFJ": ("🛡️ UX/UI 디자이너", "사용자 중심 사고로 감성적인 디자인을 만들어낼 수 있어요."),
    "INFP": ("🎨 디지털 아티스트", "감성적이고 창의적인 작업을 좋아한다면 이 직업이 딱!"),
    "ENFJ": ("🤝 IT 교육 강사", "사람을 돕고 가르치는 데서 보람을 느끼는 당신께 추천!"),
    "ENFP": ("🌐 웹 기획자", "창의력과 에너지를 기반으로 다양한 웹 아이디어를 펼쳐보세요."),
    "ISTJ": ("💾 시스템 관리자", "꼼꼼하고 체계적인 성향으로 시스템을 안정적으로 관리할 수 있어요."),
    "ISFJ": ("🔒 보안 엔지니어", "신중하고 책임감 있는 당신에게 적합한 분야예요."),
    "ESTJ": ("📊 IT 컨설턴트", "분석력과 추진력으로 기업의 IT 문제를 해결하는 데 탁월해요."),
    "ESFJ": ("📞 기술 지원 전문가", "친절함과 소통 능력으로 사용자들을 돕는 일을 좋아하신다면!"),
    "ISTP": ("🧰 하드웨어 엔지니어", "손재주와 논리적 사고로 기기를 다루는 데 능숙해요."),
    "ISFP": ("📷 디지털 콘텐츠 제작자", "감성적이고 미적 감각이 뛰어난 당신께 어울려요."),
    "ESTP": ("🚀 스타트업 개발자", "도전과 속도를 즐기는 성향에 딱 맞는 직업이에요."),
    "ESFP": ("🎥 유튜브 테크 크리에이터", "재미있고 창의적인 콘텐츠로 IT를 소개해보세요!"),
}

# 🎯 추천 직업 출력
if selected_mbti:
    job, desc = job_recommendations[selected_mbti]
    st.markdown(f"""
        <div class="job-card">
            <h2 style="color:#6a0dad;">{job}</h2>
            <p style="font-size:18px;">{desc}</p>
        </div>
    """, unsafe_allow_html=True)

# 👣 푸터
st.markdown("---")
st.markdown("<div style='text-align:center; color:gray;'>✨ Made with ❤️ by AI Career Guide ✨</div>", unsafe_allow_html=True)
