
from snake.styles.measures import *
from snake.styles.mixins import * 
from snake.styles.colors import *

## ? HEADER COMPONENTS STYLES


## ? CONTENT COMPONENTS STYLES

# * Sidebar styles

sidebar_shown_style = {
    'background-color' : SECONDARY,

    'padding-top' : '25px',

    'height' : '48.85vh',
    'border-radius' : CONTENT_BORDER_RADIUS,
    'box-shadow' : DEFAULT_SHADOW,

    'display' : 'flex',
    'flex-direction' : 'row',
    'align-items' : 'flex-start',
    'justify-content' : 'center',
    'gap' : '60px',
}

right_sidebar_hidden_style = {
    'background-color' : SECONDARY,

    'height' : '48.85vh',
    'width' : '6vw',
    'border-radius' : CONTENT_BORDER_RADIUS,
    'box-shadow' : DEFAULT_SHADOW,

    'display' : 'flex',
    'flex-direction' : 'row',
    'align-items' : 'flex-start',
    'justify-content' : 'center',
}

left_sidebar_hidden_style = {
    'background-color' : SECONDARY,

    'height' : '48.85vh',
    'width' : '6vw',
    'border-radius' : CONTENT_BORDER_RADIUS,
    'box-shadow' : DEFAULT_SHADOW,

    'display' : 'flex',
    'flex-direction' : 'row',
    'align-items' : 'flex-start',
    'justify-content' : 'center',
}

sidebar_toggle = {
    'background' : SECONDARY,

    'border-radius' : CONTENT_BORDER_RADIUS,

    '_hover': {
        'cursor' : 'pointer',
    },
}

sidebar_text = {
    'padding-top' : '3px',
    'padding-left' : '30px',
    'padding-right' : '30px',
    'border-bottom' : '1px solid rgba(255,255,255,0.15)',
}

