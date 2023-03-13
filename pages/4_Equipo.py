import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import re

# DO_NOT_CHANGE########################################################
#######################################################################

logo = Image.open('images_main/SumiLogoFont.png')

st.set_page_config(
    page_title='Sumi | Equipo',
    page_icon=logo,
    layout='centered',
    initial_sidebar_state='collapsed'
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=['Inicio', 'Artículos', 'Videos', 'Eventos', 'Equipo'],
    icons=['house', 'book', 'play-circle',
           'calendar-event', 'info-circle'],
    menu_icon='cast',
    default_index=4,
    orientation='horizontal',
    styles={
        "container": {"padding": "0!important",
                      "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "15px"},
        "nav-link": {"font-size": "15px", "text-align": "centered",
                     "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#227C70"},
    }
)

image = Image.open('images_main/web_sumi_banner_hd.png')
st.image(image, use_column_width='always', output_format='PNG')

if selected == 'Inicio':
    switch_page('Sumi_la_cacomixtle_científica')

if selected == 'Artículos':
    switch_page('Artículos')

if selected == 'Videos':
    switch_page('Videos')

if selected == 'Eventos':
    switch_page('Eventos')

if selected == 'Equipo':
    st.write('Estas es la pestaña del equipo.')

#######################################################################

ft = """
<style>
a:link , a:visited{
color: #808080;  /* theme's text color at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #BFBFBF; /* theme's text color at 50 percent brightness*/
text-align: left; /* 'left', 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Hecho con <a style='display: inline;
text-align: left;' href="https://streamlit.io/" target="_blank">
Streamlit</a>,<br 'style= top:3px;'>
con <img src=
"https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png"
alt="heart" height= "10"/> por <a style='display: inline; text-align:
left;' href="https://github.com/sape94" target="_blank">sape94</a>.</p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)
