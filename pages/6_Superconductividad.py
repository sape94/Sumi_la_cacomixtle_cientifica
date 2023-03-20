import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import re

# WEN_PAGE_TITLE#######################################################
# ONLY_CHANGE_PAGE_TITLE_OR_HEADER_PICTURE#############################

logo = Image.open('images_main/SumiLogoFont.png')
image = Image.open('im_art/images_superc/super_header.png')  # HEADER
cap_header = 'Hover board superconductora.'

st.set_page_config(
    page_title='Superconductividad',  # PAGE TITLE
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
    options=['Inicio', 'Artículos', 'Videos', 'Eventos', 'Equipo', ''],
    icons=['house', 'book', 'play-circle',
           'calendar-event', 'info-circle', 'bookmark-heart-fill'],
    menu_icon='cast',
    default_index=5,
    orientation='horizontal',
    styles={
        "container": {"padding": "0!important",
                      "background-color": "#fafafa"},
        "icon": {"color": "#7DB9B6", "font-size": "15px"},
        "nav-link": {"color": "#31333F", "font-size": "15px", "text-align": "centered",
                     "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"color": "#FFFFFF", "background-color": "#3A414D"},
    }
)

st.image(image,
         use_column_width='always', output_format='PNG')
st.markdown(
    f'''<div style="text-align: right; color: #C3C3C3; 
    font-size: 12px; margin-top: -10px">{cap_header}</div>''',
    unsafe_allow_html=True)

if selected == 'Inicio':
    switch_page('Sumi_la_cacomixtle_científica')

if selected == 'Artículos':
    switch_page('Artículos')

if selected == 'Videos':
    switch_page('Videos')

if selected == 'Eventos':
    switch_page('Eventos')

if selected == 'Equipo':
    switch_page('Equipo')

#######################################################################

# ARTICLE_IMPORTANT_INFO###############################################
#######################################################################

string = open('texts/superconductividad.txt', 'r', encoding='utf-8').read()
paragraphs = re.split(r'\\n\s*\\n', string)

author = 'Sergio Alfonso Pelayo Escalera'
author_extra = 'Maestro en Ciencias e Ingeniería de Materiales'
topico = 'Física y Química'
fecha = '28 de octubre 2022'

st.header('Una vida de Superconductividad.')

# DO_NOT_CHANGE########################################################

st.markdown(
    f'<div style="text-align: left; color: #3A98B9;">{topico}</div>',
    unsafe_allow_html=True)
st.markdown(
    f'<div style="text-align: right;">Por {author}.</div>',
    unsafe_allow_html=True)
st.caption(
    f'<div style="text-align: right;">{fecha}.</div>',
    unsafe_allow_html=True)
st.markdown(
    f'<div style="text-align: right;"> </div>',
    unsafe_allow_html=True)

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[0])

pre_col_0, col0, post_col_0 = st.columns([1, 20, 1], gap='medium')

with col0:
    juno = Image.open('im_art/images_superc/juno.png')
    cap_juno = '''
    Fotografía de Júpiter, tomada por la sonda JUNO.
    '''
    st.image(juno, caption=cap_juno,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[1])

pre_col_1, col1, post_col_1 = st.columns([1, 20, 1], gap='medium')

with col1:
    resis = Image.open('im_art/images_superc/resistencia.png')
    cap_resis = '''
    Fig. 1: Resistencia eléctrica en función de la temperatura 
    en un superconductor. La resistencia cae abruptamente a la 
    temperatura crítica.
    '''
    st.image(resis, caption=cap_resis,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[2])

pre_col_2, col2, post_col_2 = st.columns([1, 20, 1], gap='medium')

with col2:
    meiss = Image.open('im_art/images_superc/meissner.png')
    cap_meiss = '''
    Fig. 2: Superconductor tipo II: el campo magnético 
    penetra al interior de la muestra en estado normal (a), 
    algunas líneas de campo magnético penetran al interior 
    de la muestra en estado mixto mientras que otras son 
    repelidas (b), ninguna línea de campo magnético penetra 
    al superconductor (c); superconductor cerámico por 
    debajo de un imán basado en neodimio (d); las líneas de 
    campo repelidas del superconductor permiten que este 
    levite, mientras las líneas de campo que penetran 
    anclan al superconductor.
    '''
    st.image(meiss, caption=cap_meiss,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[3])

pre_col_3, col3, post_col_3 = st.columns([1, 20, 1], gap='medium')

with col3:
    shink = Image.open('im_art/images_superc/shinkansen.png')
    cap_shink = '''
    Figura 3. Tren Maglev, Chūō Shinkansen . Tren de 
    levitación magnética con superconductores que une 
    las ciudades japonesas de Tokyo y Nagoya.
    '''
    st.image(shink, caption=cap_shink,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[4])

# REFERENCIAS##########################################################
#######################################################################

st.subheader('Referencias:')

pre_col_ref, colref, post_col_ref = st.columns([1, 10, 2], gap='medium')

with colref:
    st.caption(paragraphs[5])

#######################################################################

# AUTHOR_ID############################################################
# DO_NOT_CHANGE########################################################

pre_col_author, colauthor = st.columns([2, 1], gap='small')

with colauthor:
    st.markdown('')
    st.markdown('')
    # If there is not an author's photo use Sumi's logo:
    # 'images_team/SumiLogoFont.png'
    author_photo = Image.open('images_team/SumiLogoFont.png')
    if author_extra == '':
        cap_author_photo = f'''
        {author}.
        '''
    else:
        cap_author_photo = f'''
        {author}, {author_extra}.
        '''
    st.image(author_photo, caption=cap_author_photo,
             use_column_width='always', output_format='PNG')

# DO_NOT_CHANGE########################################################

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
