
from snake.styles.colors import *


## ! MAIN STRUCTURE STYLES

body = {
    'background-color': PRIMARY,

    'width' : '100vw',
    'height' : '100vh',
}

header = {
    'width' : '100vw',
    
    'padding-top' : '7.23vh',
    'padding-left' : '6.12vw',
    'padding-bottom' : '5.5vh',

    'display' : 'grid',
    'grid-template-columns' : '19vw 34vw 19vw',
    'align-items' : 'center',
    'column_gap' : '8.5vw',
}

content = {
    'width' : '100vw',

    'padding-left' : '6.12vw',

    'display' : 'grid',
    'grid-template-columns' : '19vw 34vw 19vw',
    'align-items' : 'center',
    'column_gap' : '8.5vw',
}

## ! HEADER COMPONENTS STYLES

heading = {
    'font-size': '70px',
}

mid_column = {
    'display' : 'flex',
    'align-items' : 'center',
    'justify-content' : 'center',
    'gap' : '77px',
}

pause_style = {
    'background-color' : SECONDARY,
}