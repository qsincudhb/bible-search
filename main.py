import streamlit as st
from bible_data import get_all_verses
from search_utils import search_word, search_verse

# تنظیمات صفحه
st.set_page_config(
    page_title="جستجوی کتاب مقدس",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS سفارشی برای پشتیبانی از RTL و فونت فارسی
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');

    .css-1d391kg, .css-1p05t8e, div.stButton > button, .stRadio > label {
        direction: rtl;
        font-family: 'Vazirmatn', sans-serif !important;
    }

    .stButton>button {
        float: right;
    }

    div[data-testid="stMarkdownContainer"] {
        direction: rtl;
        text-align: right;
        font-family: 'Vazirmatn', sans-serif !important;
    }

    @media (max-width: 768px) {
        .css-1d391kg {
            padding: 1rem;
        }

        .stButton>button {
            width: 100%;
            margin-bottom: 1rem;
        }
    }

    .stTextInput > div > div > input {
        direction: rtl;
        text-align: right;
        font-family: 'Vazirmatn', sans-serif !important;
    }
</style>
""", unsafe_allow_html=True)

# عنوان
st.title("جستجوی کتاب مقدس فارسی")
st.markdown("### توسعه دهنده: محسن ضعیف نژاد")

# راهنمای استفاده
with st.expander("راهنمای جستجو", expanded=True):
    st.markdown("""
    ### راهنمای استفاده
    * برای جستجوی کلمه: کلمه مورد نظر خود را وارد کنید (مثال: یهوه، صلیب)
    * برای جستجوی آیه: قسمتی از متن آیه را وارد کنید (مثال: در ابتدا کلمه بود)
    * نتایج به همراه مرجع آیه نمایش داده می‌شوند
    * در جستجوی کلمه، تعداد تکرار کلمه نیز نمایش داده می‌شود
    """)

# انتخاب نوع جستجو
search_type = st.radio(
    "نوع جستجو را انتخاب کنید:",
    ["جستجوی کلمه", "جستجوی آیه"],
    horizontal=True
)

# دریافت تمام آیات
verses = get_all_verses()

# عملکرد جستجو
if search_type == "جستجوی کلمه":
    search_word_input = st.text_input(
        "کلمه مورد نظر را وارد کنید:",
        placeholder="مثال: یهوه"
    )

    if search_word_input:
        if len(search_word_input.strip()) < 2:
            st.warning("لطفاً حداقل ۲ حرف وارد کنید.")
        else:
            results, total_count = search_word(search_word_input, verses)

            if results:
                st.success(f"تعداد کل تکرار: {total_count}")

                for result in results:
                    highlighted_text = result['text'].replace(
                        search_word_input,
                        f"**{search_word_input}**"
                    )

                    st.markdown(f"""
                    **{result['book']} {result['reference']}** ({result['testament']})  
                    {highlighted_text}  
                    تعداد تکرار در این آیه: {result['count']}
                    ---
                    """)
            else:
                st.warning("نتیجه‌ای یافت نشد.")

else:  # جستجوی آیه
    search_verse_input = st.text_input(
        "عبارت مورد نظر را وارد کنید:",
        placeholder="مثال: در ابتدا کلمه بود"
    )

    if search_verse_input:
        if len(search_verse_input.strip()) < 3:
            st.warning("لطفاً حداقل ۳ حرف وارد کنید.")
        else:
            results = search_verse(search_verse_input, verses)

            if results:
                st.success(f"تعداد نتایج: {len(results)}")

                for result in results:
                    st.markdown(f"""
                    **{result['book']} {result['reference']}** ({result['testament']})  
                    {result['text']}
                    ---
                    """)
            else:
                st.warning("نتیجه‌ای یافت نشد.")
