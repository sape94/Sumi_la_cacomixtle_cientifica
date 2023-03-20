import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import re

# WEN_PAGE_TITLE#######################################################
# ONLY_CHANGE_PAGE_TITLE_OR_HEADER_PICTURE#############################

logo = Image.open('images_main/SumiLogoFont.png')
image = Image.open('im_art/images_bubbles/bubble_header.png')  # HEADER
cap_header = 'La Gran Ola de Kanagawa por Hokusai.'

st.set_page_config(
    page_title='Burbujas',  # PAGE TITLE
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

string = open('texts/burbujas.txt', 'r', encoding='utf-8').read()
paragraphs = re.split(r'\\n\s*\\n', string)

author = 'Sergio Alfonso Pelayo Escalera'
author_extra = 'Maestro en Ciencias e Ingeniería de Materiales'
topico = 'Física, Química y Matemáticas'
fecha = '28 de febrero 2023'

st.header('Burbujas.')

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

# NTH_PARAGRAPH########################################################
#######################################################################

st.subheader('El secreto de la forma')

st.write(paragraphs[1])

pre_col_1, col1, post_col_1 = st.columns([1, 20, 1], gap='medium')

with col1:
    no_polar = Image.open('im_art/images_bubbles/01nop.png')
    cap_no_polar = '''
    Caso no-polar: nube negativa alrededor de zona positiva.
    '''
    st.image(no_polar, caption=cap_no_polar,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[2])

pre_col_2, col2, post_col_2 = st.columns([1, 20, 1], gap='medium')

with col2:
    polar = Image.open('im_art/images_bubbles/02polar.png')
    cap_polar = '''
    Caso polar: nube negativa alrededor de zona positiva.
    '''
    st.image(polar, caption=cap_polar,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[3])

pre_col_3, col3, post_col_3 = st.columns([1, 20, 1], gap='medium')

with col3:
    cohesion = Image.open('im_art/images_bubbles/03surf.png')
    cap_cohesion = '''
    Cohesión en líquidos: dentro del volumen y en la superficie 
    (tensión superficial).
    '''
    st.image(cohesion, caption=cap_cohesion,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[4])

# NTH_PARAGRAPH########################################################
#######################################################################

st.subheader('Flotando por los aires.')

st.write(paragraphs[5])

pre_col_5, col5, post_col_5 = st.columns([1, 20, 1], gap='medium')

with col5:
    zeppelin = Image.open('im_art/images_bubbles/05fn.png')
    cap_zeppelin = '''
    Zeppelin flotanto gracias al principio de Arquímedes, pues el aire 
    caliente es de menor densidad.
    '''
    st.image(zeppelin, caption=cap_zeppelin,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[6])

# NTH_PARAGRAPH########################################################
#######################################################################

st.subheader('Gotas o burbujas.')

st.write(paragraphs[7])

# NTH_PARAGRAPH########################################################
#######################################################################

st.subheader('El misterios de su color.')

st.write(paragraphs[8])

pre_col_8, col8, post_col_8 = st.columns([1, 20, 1], gap='medium')

with col8:
    pinkfloyd = Image.open('im_art/images_bubbles/04pf.png')
    cap_pinkfloyd = '''
    Portada del álbum The Dark Side of the Moon
    de Pink Floyd, donde un haz de luz blanca
    se refracta en sus distintos colores por un prisma.
    '''
    st.image(pinkfloyd, caption=cap_pinkfloyd,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[9])

pre_col_9, col9, post_col_9 = st.columns([1, 20, 1], gap='medium')

with col9:
    introinter = Image.open('im_art/images_bubbles/06ref_2.png')
    cap_introinter = '''
    Interferencia de los rayos reflejados por las superficies
    externa e interna de la película de jabón de una burbuja.
    '''
    st.image(introinter, caption=cap_introinter,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[10])

pre_col_10, col10, post_col_10 = st.columns([1, 20, 1], gap='medium')

with col10:
    iridis = Image.open('im_art/images_bubbles/07bub.png')
    cap_iridis = '''
    Iridiscencia en una burbuja exponiendo
    dintintos colores a través de distintas zonas de su
    superficie.
    '''
    st.image(iridis, caption=cap_iridis,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.subheader('Espuma.')

st.write(paragraphs[11])

pre_col_11, col11, post_col_11 = st.columns([1, 20, 1], gap='medium')

with col11:
    cluster = Image.open('im_art/images_bubbles/08clust.png')
    cap_cluster = '''
    Cúmulo de varias burbujas que muestran cómo las parades
internas, que se comparten entre burbujas, impiden que
sean esferas completas.
    '''
    st.image(cluster, caption=cap_cluster,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[12])

pre_col_12, col12, post_col_12 = st.columns([1, 20, 1], gap='medium')

with col12:
    espuma = Image.open('im_art/images_bubbles/tsunami.jpg')
    cap_espuma = '''
    La Gran Ola de Kanagawa por el artista japonés Hokusai, 
    muestra artísticamente el color blanco de la espuma de las olas.
    '''
    st.image(espuma, caption=cap_espuma,
             use_column_width='auto', output_format='PNG')

# NTH_PARAGRAPH########################################################
#######################################################################

st.write(paragraphs[13])

#######################################################################

# REFERENCIAS##########################################################
#######################################################################

st.subheader('Referencias:')

pre_col_ref, colref, post_col_ref = st.columns([1, 10, 2], gap='medium')

with colref:
    st.caption(paragraphs[14])

#######################################################################

# AUTHOR_ID############################################################
# DO_NOT_CHANGE########################################################

pre_col_author, colauthor = st.columns([2, 1], gap='small')

with colauthor:
    st.markdown('')
    st.markdown('')
    author_photo = Image.open('images_team/author_photo.png')
    # If there is not an author's photo use Sumi's logo:
    # 'images_team/SumiLogoFont.png'
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
