import streamlit as st
import streamlit.components.v1 as components

LANGUAGES = ["English", "Arabic"]
EXPERTISE = ["Beginner", "Expert"]
AGES = ["<15", ">15"]

FOCUS_NAMES = [
    "Language / اللغة",
    "Expertise / مستوى الخبرة",
    "Age / العمر"
]

st.set_page_config(page_title="Smart Museum / المتحف الذكي", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "signup"
if "language_idx" not in st.session_state:
    st.session_state.language_idx = 0
if "expert_idx" not in st.session_state:
    st.session_state.expert_idx = 0
if "age_idx" not in st.session_state:
    st.session_state.age_idx = 0
if "focus_idx" not in st.session_state:
    st.session_state.focus_idx = 0
if "last_applied_gesture" not in st.session_state:
    st.session_state.last_applied_gesture = "None"
if "last_action_time" not in st.session_state:
    st.session_state.last_action_time = 0.0
if "scroll_index_signup" not in st.session_state:
    st.session_state.scroll_index_signup = 0
if "scroll_index_login" not in st.session_state:
    st.session_state.scroll_index_login = 0


def bilingual_header(en, ar):
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<div class='title-en'><h3>{en}</h3></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='title-ar'><h3>{ar}</h3></div>", unsafe_allow_html=True)


def bilingual_text(en, ar):
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<div class='en-text'>{en}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='ar-text'>{ar}</div>", unsafe_allow_html=True)


def bilingual_option_row(title_en, title_ar, options_en, options_ar, selected_idx, focused):
    focus_text_en = "⬅ Current" if focused else ""
    focus_text_ar = "⬅ الحالي" if focused else ""

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f"<div class='title-en'><h4>{title_en} {focus_text_en}</h4></div>",
            unsafe_allow_html=True
        )
    with c2:
        st.markdown(
            f"<div class='title-ar'><h4>{title_ar} {focus_text_ar}</h4></div>",
            unsafe_allow_html=True
        )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if selected_idx == 0:
            st.success(options_en[0])
        else:
            st.write(options_en[0])

    with col2:
        if selected_idx == 1:
            st.success(options_en[1])
        else:
            st.write(options_en[1])

    with col3:
        if selected_idx == 0:
            st.success(options_ar[0])
        else:
            st.write(options_ar[0])

    with col4:
        if selected_idx == 1:
            st.success(options_ar[1])
        else:
            st.write(options_ar[1])


def single_header(text_en, text_ar):
    if st.session_state.language_idx == 0:
        st.markdown(f"<h3 class='title-en'>{text_en}</h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h3 class='title-ar'>{text_ar}</h3>", unsafe_allow_html=True)


def single_text(text_en, text_ar):
    if st.session_state.language_idx == 0:
        st.markdown(f"<div class='en-text'>{text_en}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ar-text'>{text_ar}</div>", unsafe_allow_html=True)


def show_camera():
    components.html(
        """
        <video id="video" autoplay playsinline style="width:100%; height:300px; border:1px solid black;"></video>

        <script>
        const video = document.getElementById("video");

        navigator.mediaDevices.getUserMedia({ video: true, audio: false })
            .then(function(stream) {
                video.srcObject = stream;
            })
            .catch(function(error) {
                console.log("Camera error:", error);
            });
        </script>
        """,
        height=320,
    )
    return "None", "None"


def signup_page():
    st.markdown('<div id="signup-top"></div>', unsafe_allow_html=True)

    top_left, top_right = st.columns([6, 1])

    with top_left:
        st.title(" Smart Museum / المتحف الذكي")

    with top_right:
        if st.button("Login instead / تسجيل الدخول"):
            st.session_state.page = "login"
            st.rerun()

    bilingual_header("Sign Up", "إنشاء حساب")

    left_col, right_col = st.columns([1, 1.3])

    with left_col:
        st.markdown('<div id="signup-camera"></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        bilingual_header("Camera", "الكاميرا")

        bilingual_text(
            "1 finger = toggle | 2 fingers = next | open palm = continue as guest | thumbs up = scroll up | thumbs down = scroll down | tilt right = login instead",
            "إصبع واحد = تبديل | إصبعان = التالي | كف مفتوح = المتابعة كضيف | إبهام لأعلى = لأعلى | إبهام لأسفل = لأسفل | إمالة الرأس لليمين = تسجيل الدخول"
        )

        hand_gesture, head_gesture = show_camera()

        st.markdown("</div>", unsafe_allow_html=True)

    with right_col:
        st.markdown('<div id="signup-form"></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        bilingual_header("Choose Preferences", "اختر التفضيلات")

        bilingual_option_row(
            "Language",
            "اللغة",
            LANGUAGES,
            ["الإنجليزية", "العربية"],
            st.session_state.language_idx,
            st.session_state.focus_idx == 0,
        )

        bilingual_option_row(
            "Expertise",
            "مستوى الخبرة",
            EXPERTISE,
            ["مبتدئ", "خبير"],
            st.session_state.expert_idx,
            st.session_state.focus_idx == 1,
        )

        bilingual_option_row(
            "Age",
            "العمر",
            AGES,
            ["أقل من 15", "أكبر من 15"],
            st.session_state.age_idx,
            st.session_state.focus_idx == 2,
        )

        st.markdown("---")

        if st.button("Sign up by saving face embeddings / إنشاء حساب بحفظ بصمة الوجه", use_container_width=True):
            st.info("Face embedding sign up will be added later. / سيتم إضافة إنشاء الحساب ببصمة الوجه لاحقاً.")

        if st.button("Continue as Guest / المتابعة كضيف", use_container_width=True):
            st.session_state.page = "museum"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)


def login_page():
    st.markdown('<div id="login-top"></div>', unsafe_allow_html=True)

    top_left, top_right = st.columns([6, 1])

    with top_left:
        st.title("Smart Museum / المتحف الذكي")

    with top_right:
        if st.button("Back to Sign Up / العودة لإنشاء حساب"):
            st.session_state.page = "signup"
            st.rerun()

    bilingual_header("Login", "تسجيل الدخول")

    left_col, right_col = st.columns([1, 1.2])

    with left_col:
        st.markdown('<div id="login-camera"></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        bilingual_header("Camera", "الكاميرا")

        bilingual_text(
            "Tilt right = login | Tilt left = go back to sign up | thumbs up = scroll up | thumbs down = scroll down",
            "إمالة الرأس لليمين = تسجيل الدخول | إمالة الرأس لليسار = العودة إلى إنشاء حساب | إبهام لأعلى = لأعلى | إبهام لأسفل = لأسفل"
        )

        hand_gesture, head_gesture = show_camera()

        st.markdown("</div>", unsafe_allow_html=True)

    with right_col:
        st.markdown('<div id="login-form"></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        bilingual_header("Login with Face Recognition", "تسجيل الدخول باستخدام التعرف على الوجه")

        bilingual_text(
            "Look at the camera, then press the button below.",
            "انظر إلى الكاميرا ثم اضغط على الزر بالأسفل."
        )

        if st.button("Login with Face Recognition / تسجيل الدخول بالتعرف على الوجه", use_container_width=True):
            st.info("Face recognition login will be connected later. / سيتم ربط تسجيل الدخول بالتعرف على الوجه لاحقاً.")

        st.markdown("</div>", unsafe_allow_html=True)


def museum_page():
    st.title(" Smart Museum / المتحف الذكي")

    single_header("Museum Tour Started", "تم بدء الجولة ")

    marker_id = None

    info_col, profile_col = st.columns([2, 1])

    with profile_col:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)

        single_header("Selected Profile", "الملف المختار")

        single_text(
            f"Language: {LANGUAGES[st.session_state.language_idx]}",
            f"اللغة: {'الإنجليزية' if st.session_state.language_idx == 0 else 'العربية'}"
        )
        single_text(
            f"Expertise: {EXPERTISE[st.session_state.expert_idx]}",
            f"الخبرة: {'مبتدئ' if st.session_state.expert_idx == 0 else 'خبير'}"
        )
        single_text(
            f"Age: {AGES[st.session_state.age_idx]}",
            f"العمر: {'أقل من 15' if st.session_state.age_idx == 0 else 'أكبر من 15'}"
        )
        single_text(
            f"Marker ID: {marker_id if marker_id is not None else 'None'}",
            f"رقم العلامة: {marker_id if marker_id is not None else 'غير موجود'}"
        )

        st.markdown("</div>", unsafe_allow_html=True)


if st.session_state.page == "signup":
    signup_page()
elif st.session_state.page == "login":
    login_page()
elif st.session_state.page == "museum":
    museum_page()