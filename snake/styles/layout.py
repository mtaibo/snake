from snake.styles.colors import *
from snake.styles.mixins import *
from snake.styles.measures import *


base_style = {
    'background-color': PRIMARY,
    'width' : '100vw',
    'height' : '100vh',
    'overflow' : 'hidden',
}

header_style = {
    'height' : '18.28vh',
    **MAIN_COLUMNS_GRID,
    'padding-top' : '7.23vh',
    'padding-left' : '6.12vw',
    'padding-bottom' : '5.5vh',
}

content_style = {
    **MAIN_COLUMNS_GRID,
    'padding-left' : '5.5vw',
}

mid_header_style = {
    **FLEX_CENTER,
    'gap' : '90px',
}