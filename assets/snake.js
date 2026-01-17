
// Variables for time on GameLoop
const FPS = 10;
const interval = 1000 / FPS; 
let lastTime = 0;

// Variables for the GameState
let gameStatus = 'stopped';

// Variables de configuración y control
let canvas, ctx;
let columns, rows;
const blockSize = 20;

let snake = [{x: 10, y: 10}]; // La cabeza empieza aquí
let direction = {x: 1, y: 0}; // Se mueve a la derecha inicialmente
let food = {x: 5, y: 5};

// Function to control the game state
window.setGameStatus = function(newStatus, canvasId) {
    gameStatus = newStatus;
    if (newStatus === 'playing') initGame(canvasId);
}

// Function to initialize the game
window.initGame = function(canvasId) {
    requestAnimationFrame((timestamp) => {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;

        // Get measures of canvas, and columns/rows of the grid
        canvas.width = canvas.getBoundingClientRect().width;
        canvas.height = canvas.getBoundingClientRect().height;

        const columns = Math.floor(canvas.width / blockSize);
        const rows = Math.floor(canvas.height / blockSize);

        lastTime = timestamp;
        requestAnimationFrame(gameLoop);
    });
}

window.changeDirection = function(newDir) {
    // Evitar que la serpiente se gire 180 grados sobre sí misma
    if (newDir === 'UP' && direction.y !== 1) direction = {x: 0, y: -1};
    if (newDir === 'DOWN' && direction.y !== -1) direction = {x: 0, y: 1};
    if (newDir === 'LEFT' && direction.x !== 1) direction = {x: -1, y: 0};
    if (newDir === 'RIGHT' && direction.x !== -1) direction = {x: 1, y: 0};
}

// Function to control the game loop
function gameLoop(currentTime) {

    // Check gameStatus to redirect the gameLoop
    if (gameStatus === 'stopped') { return;
    } else if (gameStatus === 'paused') {
        requestAnimationFrame(gameLoop);
        lastTime = currentTime;
        return;
    } else requestAnimationFrame(gameLoop);

    // Adjust currentTime from lastTime
    const deltaTime = currentTime - lastTime;

    if (deltaTime > interval) {

        // Adjust lastTime as last game cycle
        lastTime = currentTime - (deltaTime % interval);

        // Game logic that needs to be updated every cycle
        update();
        drawCanvas();
    }
}

function update() {

    // 1. Calcular nueva posición de la cabeza
    const head = { 
        x: snake[0].x + direction.x, 
        y: snake[0].y + direction.y 
    };

    // 2. Añadir la cabeza al principio
    snake.unshift(head);

    // 3. Comprobar si come comida
    if (head.x === food.x && head.y === food.y) {
        generateFood(); // No quitamos la cola, así crece
    } else {
        snake.pop(); // Quitamos la cola para mantener el tamaño
    }

    // 4. Comprobar colisiones (Paredes)
    // Asumiendo que sabes las columnas y filas de tu canvas
    if (head.x < 0 || head.x >= columns || head.y < 0 || head.y >= rows) {
        gameStatus = 'stopped';
        alert("Game Over");
    }
}

function drawCanvas() {
    const canvas = document.getElementById("game-canvas");
    const ctx = canvas.getContext("2d");

    // Limpiar el canvas
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Dibujar serpiente
    ctx.fillStyle = "lime";
    snake.forEach(part => {
        ctx.fillRect(part.x * blockSize, part.y * blockSize, blockSize - 2, blockSize - 2);
    });

    // Dibujar comida
    ctx.fillStyle = "red";
    ctx.fillRect(food.x * blockSize, food.y * blockSize, blockSize - 2, blockSize - 2);
}