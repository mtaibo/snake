from snake.styles.measures import *
from snake.styles.mixins import * 
from snake.styles.colors import *

pause_style = {
    'background-color' : SECONDARY,
    'border-radius' : PAUSE_BORDER_RADIUS,
    'padding' : '23px',
    'box-shadow' : DEFAULT_SHADOW,

    '_hover' : {
        'cursor' : 'pointer',
    }
}

start_style = {
    'background-color' : SECONDARY,
    'border-radius' : CONTENT_BORDER_RADIUS,

    'font-size' : '30px',

    'height' : '60.3vh',
    'width' : '100%',

    'box-shadow' : DEFAULT_SHADOW,

    **FLEX_CENTER,

    '_hover' : {
        'cursor' : 'pointer',
    },

    '_focus': {
        'outline': 'none', 
    },      
}