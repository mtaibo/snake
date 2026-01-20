/**
 * En este archivo debo de incluir las constantes, valores
 * que no cambian durante el programa y específicamente serán
 * elementos como los "enums", los Colores, las configuraciones
 * bien sean de velocidad, o del tamaño del grid
 */

export const GameStatus = Object.freeze({
    STOPPED: 'stopped',
    PLAYING: 'playing',
    PAUSED: 'paused'
})

export const Direction = Object.freeze({
    UP: 'UP',
    DOWN: 'DOWN',
    LEFT: 'LEFT',
    RIGHT: 'RIGHT'
})

export const Colors = Object.freeze({

})

export const FPS = 10;
export const BlockSize = 20;