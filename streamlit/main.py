import streamlit as st

def main():
    # Initialization
    if 'clicked' not in st.session_state:
        st.session_state['clicked'] = False

    # Contoh writing objects bisa jadi list
    st.write("Most objects") # df, err, func, keras!
    st.write(["st", "is <", 3]) # see *

    # Contoh Markdown Formatting
    st.text("Fixed width text")
    st.markdown("**Markdown**") # see *
    st.latex(r""" e^{i\pi} + 1 = 0 """) # LaTeX formatting -> professional document formatting

    # Contoh HTML-like Formatting
    st.title("My title")
    st.header("My header")
    st.subheader("My sub")
    st.code("for i in range(8): foo()")
    st.html("<p>Hi!</p>")

    # Contoh click button
    if st.button('sebuah tombol', type="primary"):
        st.session_state['clicked'] = not st.session_state['clicked']
    st.write("clicked:", st.session_state['clicked'])
    st.link_button("Go to flask-app", "http://localhost:9999", type="primary")

    # Contoh showing image
    st.image("./messi.jpg")

if __name__ == '__main__':
    main()