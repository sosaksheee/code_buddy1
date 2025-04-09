
import streamlit as st
from corelogic_codebuddy import generate_comment, check_syntax



st.set_page_config(page_title="AI Code Buddy", layout="wide")

st.title("🤖 AI Based Code Buddy")

code_input = st.text_area("Paste your code below:", height=300)

if st.button("Generate Comments"):
    with st.spinner("Analyzing your code..."):
        comment = generate_comment(code_input)
        st.subheader("💡 Generated Comment")
        st.code(comment, language='markdown')

if st.button("Check for Syntax Errors"):
    with st.spinner("Checking syntax..."):
        syntax_result = check_syntax(code_input)
        st.subheader("🛠️ Syntax Check Result")
        st.info(syntax_result)
