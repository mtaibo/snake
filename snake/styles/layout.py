
from snake.styles.colors import *


base_style = {
    'background-color': PRIMARY,

    'width' : '100vw',
    'height' : '100vh',
}

header_style = {
    'width' : '100vw',
    
    'padding-top' : '7.23vh',
    'padding-left' : '6.12vw',
    'padding-bottom' : '5.5vh',

    'display' : 'grid',
    'grid-template-columns' : '19vw 34vw 19vw',
    'align-items' : 'center',
    'column_gap' : '8.5vw',

    'overflow' : 'hidden'
}

content_style = {
    'width' : '100vw',
    'height' : '1fr',

    'padding-left' : '6.12vw',

    'display' : 'grid',
    'grid-template-columns' : '19vw 34vw 19vw',
    'align-items' : 'center',
    'column_gap' : '8.5vw',
}


mid_header_style = {
    'display' : 'flex',
    'align-items' : 'center',
    'justify-content' : 'center',
    'gap' : '90px',
}