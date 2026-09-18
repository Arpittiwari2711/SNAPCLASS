import streamlit as st


def footer_home():
    logo_url = "https://cdn.creativefabrica.com/2018/12/Letter-A-and-T-Logo-by-meisuseno.jpg"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://cdn.creativefabrica.com/2018/12/Letter-A-and-T-Logo-by-meisuseno.jpg"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by Arpit Tiwari</p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)