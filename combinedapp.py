import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="SafeFrame Dashboard", layout="wide")

# Custom CSS to improve the UI
st.markdown("""
<style>
    .main {
        padding: 0rem 1rem;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
    }
    .Widget>label {
        color: white;
        font-family: 'Roboto', sans-serif;
    }
    .st-bb {
        background-color: transparent;
    }
    .st-at {
        background-color: #4c85c5;
    }
    .stTextInput>div>div>input {
        color: #4e4376;
    }
    .stSelectbox>div>div>input {
        color: #4e4376;
    }
</style>
""", unsafe_allow_html=True)

def main():
    
    
    # Create a header
    st.markdown("""
    <h1 style='text-align: center; color: #2e7bcf;'>SafeFrame Dashboard</h1>
    <p style='text-align: center; color: #4e4376;'>Explore our tools in one place!</p>
    """, unsafe_allow_html=True)

    # Create a horizontal menu
    selected = option_menu(
        menu_title=None,
        options=["Home", "BRIGHTENING", "DEHAZING"],
        icons=["house", "app-indicator", "app-indicator"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#2e7bcf", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#2e7bcf"},
        }
    )

    if selected == "Home":
        st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            <h2>Welcome to the SafeFrame Multi-tool Dashboard!</h2>
            <p>enhance the clarity of images and videos in real-time by addressing the challenges of hazy or low-contrast scenes. Leveraging advanced machine learning models and computer vision techniques, our solution provides a sophisticated yet efficient way to dehaze and brighten visual content, ensuring a clearer and more vibrant viewing experience.</p>
            <p>Use the menu above to navigate between different tools.</p>
        </div>
        """, unsafe_allow_html=True)

    elif selected == "BRIGHTENING":
        st.markdown("<h2 style='text-align: center; color: #2e7bcf;'>SafeFrame BRIGHTENING</h2>", unsafe_allow_html=True)
        app1_url = "https://safeframe-brightening.streamlit.app/"
        st.markdown(f"<p style='text-align: center;'>use BRIGHTENING tool from <a href='{app1_url}' target='_blank'>here</a></p>", unsafe_allow_html=True)
        with st.expander("Expand to View BRIGHTENING tool"):
            st.components.v1.iframe(app1_url, height=600, scrolling=True)

    elif selected == "DEHAZING":
        st.markdown("<h2 style='text-align: center; color: #2e7bcf;'>SafeFrame DEHAZING</h2>", unsafe_allow_html=True)
        app2_url = "https://safeframe-dehazing.streamlit.app/"
        st.markdown(f"<p style='text-align: center;'>use DEHAZING tool from <a href='{app2_url}' target='_blank'>here</a></p>", unsafe_allow_html=True)
        with st.expander("Expand to View DEHAZING tool"):
            st.components.v1.iframe(app2_url, height=600, scrolling=True)

    # Footer
    st.markdown("""
    <footer style='text-align: center; padding: 20px; color: #4e4376;'>
        <hr>
        <p>© 2024 SafeFrame application Dashboard. All rights reserved.</p>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()