import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import re

one, two, three = st.columns([1, 15, 1], gap='small')

with two:

    image = Image.open('images_main/web_sumi_banner_hd.png')

    Test = '''
    <a href="http://localhost:8501/" target="_self">Test</a>
    '''

    selected = option_menu(
        menu_title=None,
        options=['Inicio', 'Artículos', 'Eventos', 'Videos', 'Equipo'],
        icons=['house', 'book', 'hexagon', 'gem', 'info'],
        menu_icon='cast',
        default_index=1,
        orientation='horizontal',
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#1C315E", "font-size": "15px"},
            "nav-link": {"color": "#1C315E", "font-size": "15px", "text-align": "centered", "margin": "0px", "--hover-color": "#88A47C"},
            "nav-link-selected": {"color": "#E6E2C3", "background-color": "#227C70"},
        }
    )
    #        "icon": {"color": "black", "font-size": "20px"},
    #        "nav-link": {"font-size": "20px", "text-align": "centered", "margin": "0px", "--hover-color": "#eee"},
    #        "nav-link-selected": {"background-color": "#0283C3"},
    #    }
    # )

    st.image(image, use_column_width='always', output_format='PNG')

    if st.button('Regresar al menú principal de artículos'):
        switch_page('Sumi_la_cacomixtle_científica')

    if selected == 'Inicio':
        st.title(f'You have selected {selected}')
    if selected == 'Artículos':
        string = open('texts/superconductividad.txt',
                      'r', encoding='utf-8').read()
        paragraphs = re.split(r'\\n\s*\\n', string)
        author = 'Sergio Alfonso Pelayo Escalera'

        st.header('Una vida de Superconductividad.')

# with col0:
#    st.write(f'Por {author}.')
    st.markdown(
        f'<div style="text-align: right;">Por {author}.</div>', unsafe_allow_html=True)
    st.caption(
        f'<div style="text-align: right;">28 de febrero 2023.</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div style="text-align: right;"> </div>', unsafe_allow_html=True)
    st.markdown(
        f'<div style="text-align: right;"> </div>', unsafe_allow_html=True)

    st.write(paragraphs[0])

    juno = Image.open('im_art/images_superc/juno.png')
    cap_juno = '''
    Fotografía de Júpiter, tomada por la sonda JUNO
    '''
    st.image(juno, caption=cap_juno,
             use_column_width='auto', output_format='PNG')

    st.write(paragraphs[1])
    if selected == 'Eventos':
        st.title(f'You have selected {selected}')
        st.video('https://www.youtube.com/watch?v=IeJybuKb5ns')

    if selected == 'Videos':
        switch_page('Sumi_la_cacomixtle_científica')
    #    html_l = '''
    #    <script type="text/javascript">
    #    function load()
    #    {
    #    window.open('http://localhost:8501/','_blank');
    #    }
    #    </script>
    #    </head>
    #
    #    <body onload="load()">
    #    </body>
    #    '''
    #    html_2 = '''
    #    <script>
    #        function openInNewTab(url) {
    #            var win = window.open(url, '_blank');
    #            win.focus();
    #        }
    #    </script>
    #
    #    <body onload=openInNewTab("https://tutorial.eyehunts.com/")>
    #
    #    </body>
    #    '''
    #    # st.markdown(link_o, unsafe_allow_html=True)
    #    html(html_l)

    st.title('Hello World!')

    pre = 'Revisa nuestro artículo sobre '
    bold = '**burbujas**.'

    link = f'''
    {pre}
    <a href="http://localhost:8501/" target="_self">{bold}</a>
    '''
    st.write(f'{link}', unsafe_allow_html=True)

    st.markdown('''
                Revisa nuestro artículo sobre <a href="http://localhost:8501/" target = "_self">**burbujas**.</a>
                ''',
                unsafe_allow_html=True)

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
