# login.py

import streamlit as st
from streamlit_oauth import OAuth2Component
import base64
import json

def login_page(st):
    st.title("Google Auth")

    # TODO: get client creds from CLOUD
    CLIENT_ID = ""
    CLIENT_SECRET = ""
    AUTHORIZE_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
    TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
    REVOKE_ENDPOINT = "https://oauth2.googleapis.com/revoke"

    if "auth" not in st.session_state:
        oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_ENDPOINT, TOKEN_ENDPOINT, TOKEN_ENDPOINT, REVOKE_ENDPOINT)
        result = oauth2.authorize_button(
            name="Continue with Google",
            icon="https://www.google.com.tw/favicon.ico",
            redirect_uri="http://localhost:8501",
            scope="openid email profile",
            key="google",
            extras_params={"prompt": "consent", "access_type": "offline"},
            use_container_width=True,
            pkce="S256",
        )
    
        if result:
            st.write(result)
            id_token = result["token"]["id_token"]
            payload = id_token.split(".")[1]
            payload += "=" * (-len(payload) % 4)
            payload = json.loads(base64.b64decode(payload))
            email = payload["email"]
            st.session_state["auth"] = email
            st.session_state["token"] = result["token"]
            st.rerun()
    else:
        st.write("You are logged in!")
        st.write(st.session_state["auth"])
        st.write(st.session_state["token"])
        if st.button("Logout"):
            del st.session_state["auth"]
            del st.session_state["token"]
