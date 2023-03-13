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
    page_title='Sumi | Inicio',
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
    default_index=0,
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

    news_col, social_col = st.columns([1.75, 1], gap='medium')

    with news_col:
        st.header('Noticias')
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

        # EVENT_ENTRY##################################################
        # UP_TO_TWO_NEXT_EVENTS########################################
        # Subheader with hover color.
        # Must change href="/link",
        # text content, and CSS/HTML string
        # title.
        subhead_nocheestr = '''
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
        href="/Eventos" target="_self">
        <h3 class="subhead-item">
        Noche de las estrellas
        </h3>
        </a>
        '''
        st.write(subhead_nocheestr, unsafe_allow_html=True)
        nocheestr_lugar = 'Zócalo de la CDMX, 03 de diciembre 2023'
        st.write(
            f'''<div style="text-align: right; color: #3A98B9;">
            {nocheestr_lugar}</div>''',
            unsafe_allow_html=True)
        noche = Image.open('im_evt/images_nocheestr/noche_header.png')
        st.image(noche, use_column_width='always',
                 output_format='PNG')
        noche_tipo = '''
        Talleres y Charlas'''
        st.caption(f'''
                   <p style="text-align: left;
                   font-family: Courier New;
                   font-size: 0.75em; 
                   margin-top: -10px">{noche_tipo}.</p>
                   ''', unsafe_allow_html=True)
        noche_cap = f'''
        Acompánanos este 3 de diciembre en el Zócalo de la ciudad.
        Tendremos algunas charlas y
        habrá distintos talleres como de origami, moco espacial, 
        crea tu propio fósil y más.
        '''
        st.caption(
            f'''
            <div style="text-align: justify;
            margin-top: -15px;
            ">{noche_cap}</div>''',
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

        # VIDEO_ENTRY##################################################
        # NEWEST_VIDEO#################################################
        # Subheader with hover color.
        # Must change href="/link",
        # text content, and CSS/HTML string
        # title.
        subhead_sanacuant = '''
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
        href="/Videos" target="_self">
        <h3 class="subhead-item">
        Desmintiendo la Sanación Cuántica
        </h3>
        </a>
        '''
        st.write(subhead_sanacuant, unsafe_allow_html=True)
        sanacuant_tipo = 'Cazando Mitos'
        st.write(
            f'''<div style="text-align: right; color: #3A98B9;">
            {sanacuant_tipo}</div>''',
            unsafe_allow_html=True)
        st.video('https://www.youtube.com/watch?v=4mzRpDwsBCc')
        sanacuant_eti = '''
        Mesa redonda'''
        st.caption(f'''
                   <p style="text-align: left;
                   font-family: Courier New;
                   font-size: 0.75em; 
                   margin-top: -10px">{sanacuant_eti}.</p>
                   ''', unsafe_allow_html=True)
        sanacuant_cap = f'''
        Como parte de las actividades de #Sumi, se realizó la primer
        actividad del ciclo #CazandoMitos.
        En esta ocasión, se discutió la validez científica de las
        propuestas de la #SanacionCuantica, con el Dr. Luis Andrés
        Martínez Zaldívar y el M. en C. César Alberto Díaz Hernández,
        expertos en #fisicacuantica.
        '''
        st.caption(
            f'''
            <div style="text-align: justify;
            margin-top: -15px;
            ">{sanacuant_cap}</div>''',
            unsafe_allow_html=True)
        st.header('')
        ###############################################################

    with social_col:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown('')
        welcome_1 = f'''
        El equipo Sumi te da la bienvenida a la Sumi-web
        , disfruta leyendo los <b>artículos</b>, entérate de
        los próximos <b>eventos</b> o accede a los diversos
        <b>videos</b> con los que contamos.
        '''
        st.markdown(
            f'''
            <div style="text-align: justify; color: black;
            line-height: 120%;">{welcome_1}</div>''',
            unsafe_allow_html=True)
        st.markdown('')
        sumi_social = Image.open('images_team/SumiLogoFont.png')
        st.image(sumi_social, use_column_width='always',
                 output_format='PNG')
        welcome_2 = f'''
        Diviértete explorando la página.
        '''
        st.markdown(
            f'''
            <div style="text-align: justify; color: black;
            line-height: 120%;">{welcome_2}</div>''',
            unsafe_allow_html=True)
        st.markdown('')
        st.markdown('')
        st.subheader('Sigue a Sumi:')
        social_icons = '''
        <style>
        .icon-item {
            font-size: 20px;
            backgroundcolor: transparent;
            stroke: #31333F;
            margin-left: 60px;
            margin-top: -5px;
        }
        .icon-item:hover {
            color: #31333F;
            stroke: #227C70;
        }
        
        </style>

        <a style='display: inline; text-align: justify; color: #227C70
        ; text-decoration: none;'
        href="
        https://www.tiktok.com/@sumi_fcienciasunam?_t=8aXsj3ZwqWs&_r=1"
        target="_blank">
        
        <p class="icon-item">
        <svg height="27" width="27">
        <circle cx="13.5" cy="13.5" r="12" stroke-width="2.5" 
        fill="transparent" />
        <svg class="icon-item"
        xmlns="http://www.w3.org/2000/svg" 
        width="20" height="24" viewBox="-4 -1.5 24 24">
        <path fill="currentColor" stroke-width="0"
        d="M16.6 
        5.82s.51.5 0 0A4.278 4.278 0 0 1 15.54 3h-3.09v12.4a2.592 2.592 
        0 0 1-2.59 2.5c-1.42 0-2.6-1.16-2.6-2.6c0-1.72 1.66-3.01 
        3.37-2.48V9.66c-3.45-.46-6.47 2.22-6.47 5.64c0 3.33 2.76 
        5.7 5.69 5.7c3.14 0 5.69-2.55 5.69-5.7V9.01a7.35 7.35 0 0 0 
        4.3 1.38V7.3s-1.88.09-3.24-1.48z"/>
        </svg>
        </svg>
        <b>
        Tiktok
        </b>
        </p>
        </a>
        
        <a style='display: inline; text-align: justify; color: #227C70
        ; text-decoration: none;'
        href="
        https://www.youtube.com/@FacultaddeCienciasUNAMOficial"
        target="_blank">
        
        <p class="icon-item">
        <svg height="27" width="27">
        <circle cx="13.5" cy="13.5" r="12" stroke-width="2.5" 
        fill="transparent" />
        <svg class="icon-item"
        xmlns="http://www.w3.org/2000/svg" 
        width="24" height="24" viewBox="-5.5 -2.5 31 25.5">
        <path fill="currentColor" stroke-width="0"
        d="M21.543 6.498C22 8.28 22 12 22 12s0 3.72-.457 
        5.502c-.254.985-.997 1.76-1.938 2.022C17.896 20 12 
        20 12 20s-5.893 
        0-7.605-.476c-.945-.266-1.687-1.04-1.938-2.022C2 
        15.72 2 12 2 12s0-3.72.457-5.502c.254-.985.997-1.76 
        1.938-2.022C6.107 4 12 4 12 4s5.896 0 7.605.476c.945.266 
        1.687 1.04 1.938 2.022zM10 15.5l6-3.5l-6-3.5v7z"/>
        </svg>
        </svg>
        <b>
        Youtube
        </b>
        </p>
        </a>
        '''
        st.write(social_icons, unsafe_allow_html=True)
        st.markdown('')
        st.markdown('')
        st.subheader('Coloabora con Sumi:')
        participa_1 = f'''
        Envía tus <b>comentarios</b>, tus <b>artículos</b> o
        alguna <b>colaboración</b> que quieras realizar con 
        nosotros al correo:
        '''
        st.markdown(
            f'''
            <div style="text-align: justify; color: black;
            line-height: 120%;">{participa_1}</div>''',
            unsafe_allow_html=True)
        mail = '''
        <style>
        .mail-item {
            font-size: 15px;
            backgroundcolor: transparent;
            stroke: #31333F;
            margin-left: 20px;
            margin-top: 30px;
        }
        .mail-item:hover {
            color: #31333F;
            stroke: #227C70;
        }
        
        </style>
        
        <a style='display: inline; text-align: justify; color: #227C70
        ; text-decoration: none;'
        href="
        mailto:sumi@ciencias.unam.mx?subject = Feedback&body = Message">
        
        <p class="mail-item">
        <svg height="27" width="27">
        <circle cx="13.5" cy="13.5" r="12" stroke-width="2.5" 
        fill="transparent" />
        <svg class="mail-item"
        xmlns="http://www.w3.org/2000/svg" width="20" height="20" 
        viewBox="-8.8 -8 31 31"><path fill="currentColor" stroke-width="0"
        d="M22 
        6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 
        2h16c1.1 0 2-.9 2-2V6m-2 0l-8 5l-8-5h16m0 12H4V8l8 
        5l8-5v10Z"/>
        </svg>
        </svg>
        <b>
        sumi@ciencias.unam.mx
        </b>
        </p>
        </a>
        '''
        st.write(mail, unsafe_allow_html=True)
if selected == 'Artículos':
    switch_page('Artículos')

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
