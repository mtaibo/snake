from snake.styles.measures import *
from snake.styles.mixins import * 
from snake.styles.colors import *


canvas_style = {
    'background-color' : PRIMARY,

    'height' : '60.3vh',
    'border-radius' : CONTENT_BORDER_RADIUS,
    'box-shadow' : DEFAULT_SHADOW,
}

instructions_style = {
    'width' : '100%',
    'font-size' : '15px',
    'font-weight' : '100', 
    'padding-top' : '20px',
    **FLEX_CENTER,
}