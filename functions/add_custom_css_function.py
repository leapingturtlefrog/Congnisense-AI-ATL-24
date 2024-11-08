import streamlit as st

def add_custom_css(st):
    st.markdown(
    """
    <style>
    button {
        background: none!important;
        border: none;
        padding: 0!important;
        color: #6EAEA1 !important;
        text-decoration: none;
        cursor: pointer;
        border: none !important;
    }
    button:hover {
        text-decoration: none;
        color: black !important;
    }
    audio {
        display: none;
    }
    .sidebar-icon {
        width: 16px; 
        height: 16px;
        margin-bottom: 10px;
        display: block;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
