from snake.styles.measures import *
from snake.styles.mixins import * 
from snake.styles.colors import *

sidebar_button = {
    'width' : BUTTON_WIDTH,
    'height' : '100%',

    'border_radius' : CONTENT_BORDER_RADIUS,
    'background_color' : SECONDARY,
    'position' : 'absolute',
    'top' : '0',
    'display' : 'flex',
    'align-items' : 'center',
    'justify-content' : 'center',
    '_hover' : {
        'cursor' : 'pointer'
    }
}

sidebar_content = {
    'width' : '100%',
    'padding' : '16px',
    'padding-left' : '66px',
    'transition' : 'opacity 120ms ease',
}

sidebar_style = {
    'width' : SIDEBAR_WIDTH,
    'height' : SIDEBAR_HEIGHT,

    'position' : 'relative',
    'border-radius' : CONTENT_BORDER_RADIUS,
    'box-shadow' : DEFAULT_SHADOW,
    'background-color' : SECONDARY,
    'transition' : 'transform 300ms ease',
}