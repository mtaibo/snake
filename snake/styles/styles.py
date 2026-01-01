
from snake.styles.measures import *
from snake.styles.colors import *

## ? HEADER COMPONENTS STYLES

title_style = {
    'font-size': '70px',
    'display' : 'flex',
    'align-items' : 'center',
    'justify-content' : 'center',
}

score_style = {
    'font-size' : '30px',

    'display' : 'flex',
    'align-items' : 'center',
    'justify-content' : 'center',

    'gap' : '30px',
}

pause_style = {
    'background-color' : SECONDARY,
    'border-radius' : '40px',
    'padding' : '23px',
    'box-shadow' : '0 16px 32px rgba(0,0,0,0.30)',

    '_hover' : {
        'cursor' : 'pointer',
    }
}

## ? CONTENT COMPONENTS STYLES

# * Sidebar styles

sidebar_shown_style = {
    'background-color' : SECONDARY,

    'padding-top' : '25px',

    'height' : '48.85vh',
    'border-radius' : '25px',
    'box-shadow' : '0 16px 32px rgba(0,0,0,0.30)',

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
    'border-radius' : '25px',
    'box-shadow' : '0 16px 32px rgba(0,0,0,0.30)',

    'display' : 'flex',
    'flex-direction' : 'row',
    'align-items' : 'flex-start',
    'justify-content' : 'center',
}

left_sidebar_hidden_style = {
    'background-color' : SECONDARY,

    'height' : '48.85vh',
    'width' : '6vw',
    'border-radius' : '25px',
    'box-shadow' : '0 16px 32px rgba(0,0,0,0.30)',

    'display' : 'flex',
    'flex-direction' : 'row',
    'align-items' : 'flex-start',
    'justify-content' : 'center',
}

sidebar_toggle = {
    'background' : SECONDARY,

    'border-radius' : '25px',

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

## * Canvas and Start Button styles

canvas_style = {
    'background-color' : SECONDARY,

    'height' : '60.3vh',
    'border-radius' : '25px',
    'box-shadow' : '0 16px 32px rgba(0,0,0,0.30)'
}

start_style = {
    'background-color' : SECONDARY,

    'font-size' : '30px',

    'height' : '60.3vh',
    'width' : '100%',

    'border-radius' : '25px',
    'box-shadow' : '0 16px 32px rgba(0,0,0,0.30)',

    'display' : 'flex',
    'align-items' : 'center',
    'justify-content' : 'center',

    '_hover' : {
        'cursor' : 'pointer',
    },
}

soft_text = {
    'font-size' : '15px',
    'font-weight' : '200',
}

instructions_style = {
    'font-size' : '15px',
    'font-weight' : '200', 
    'padding-top' : '20px',
    'display' : 'flex',
    'align-items' : 'center',
    'justify-content' : 'center',
}