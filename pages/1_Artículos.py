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
    page_title='Sumi | Artículos',
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
    default_index=1,
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
    # ARTICLE_ENTRY################################################
    # Subheader with hover color.
    # Must change href="/link",
    # text content, and CSS/HTML string
    # title.
    subhead_bubbles = '''
        <style>
        .subhead-item {
            backgroundcolor: transparent;
        }
        .subhead-item:hover {
            color: #227C70;
        }
        </style>

        <a style='display: inline; text-align: left; color: #31333F
        ; text-decoration: none; '
        href="/Burbujas" target="_self">
        <h3 class="subhead-item">
        Burbujas
        </h3>
        </a>
        '''
    st.write(subhead_bubbles, unsafe_allow_html=True)
    # st.subheader('Burbujas.')
    bubbles_topico = 'Física, Química y Matemáticas'
    st.write(
        f'''<div style="text-align: right; color: #3A98B9;">
            {bubbles_topico}</div>''',
        unsafe_allow_html=True)
    bubbles = Image.open('im_art/images_bubbles/bubble_header.png')
    st.image(bubbles, use_column_width='always',
             output_format='PNG')
    bubbles_author = '''
        Sergio Alfonso Pelayo Escalera'''
    st.caption(f'''
                   <p style="text-align: left;
                   font-family: Courier New;
                   font-size: 0.75em; margin-top: -10px">
                   Por {bubbles_author}.</p>
                   ''', unsafe_allow_html=True)
    bubbles_cap = f'''
        Ya sea en los parques de la ciudad los fines de
        semana, la espuma del mar de las olas rompiendo
        en la playa o simplemente flotando sobre nuestra
        bebida favorita, las burbujas son un espectáculo
        que guardan a simple vista varios secretos de la
        ciencia...
        '''
    st.caption(
        f'''
            <div style="text-align: justify;
            margin-top: -15px;
            ">{bubbles_cap}</div>''',
        unsafe_allow_html=True)
    st.header('')
    ###############################################################

    # ARTICLE_ENTRY################################################
    # Subheader with hover color.
    # Must change href="/link" and
    # text content, and CSS/HTML string
    # title.
    subhead_superc = '''
        <style>
        .subhead-item {
            backgroundcolor: transparent;
        }
        .subhead-item:hover {
            color: #227C70;
        }
        </style>

        <a style='display: inline; text-align: left; color: #31333F
        ; text-decoration: none; '
        href="/Superconductividad" target="_self">
        <h3 class="subhead-item">
        Superconductividad
        </h3>
        </a>
        '''
    st.write(subhead_superc, unsafe_allow_html=True)
    superc_topico = 'Física y Química'
    st.write(
        f'''<div style="text-align: right; color: #3A98B9;">
            {superc_topico}</div>''',
        unsafe_allow_html=True)
    superc = Image.open('im_art/images_superc/super_header.png')
    st.image(superc, use_column_width='always',
             output_format='PNG')
    superc_author = '''
        Sergio Alfonso Pelayo Escalera'''
    st.caption(f'''
                   <p style="text-align: left;
                   font-family: Courier New;
                   font-size: 0.75em; margin-top: -10px">
                   Por {superc_author}.</p>
                   ''', unsafe_allow_html=True)
    superc_cap = '''
        A presiones tan extremas como en el núcleo de
        Júpiter, que son decenas de millones de veces
        mayores a la Tierra, el hidrógeno llegaría a
        un estado con propiedades extraordinarias.
        Esta fue la predicción de N. W. Ashcroft; y el
        estado en cuestión, el superconductor...
        '''
    st.caption(
        f'''
            <div style="text-align: justify;
            margin-top: -15px;
            ">{superc_cap}</div>''',
        unsafe_allow_html=True)
    ###############################################################


if selected == 'Videos':
    switch_page('Videos')

if selected == 'Eventos':
    switch_page('Eventos')

if selected == 'Equipo':
    switch_page('Equipo')

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
