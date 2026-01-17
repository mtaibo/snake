
// Variables for time on GameLoop
const FPS = 10;
let lastTime = 0;

// Variables for the GameState
let gameStatus = 'stopped';

// Function to control the game state
window.setGameStatus = function(newStatus, canvasId) {

    gameStatus = newStatus;

    if (newStatus === 'playing') {
        initGame(canvasId);
    }
}

// Function to initialize the game
window.initGame = function(canvasId) {
    requestAnimationFrame((timestamp) => {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;

        // Get measures of canvas, and columns/rows of the grid
        canvas.width = canvas.getBoundingClientRect().width;
        canvas.height = canvas.getBoundingClientRect().height;

        const blockSize = 20; 
        const columns = Math.floor(canvas.width / blockSize);
        const rows = Math.floor(canvas.height / blockSize);
        
        lastTime = timestamp;
        requestAnimationFrame(gameLoop);
    });
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


    const deltaTime = currentTime - lastTime;
    const interval = 1000 / FPS; 

    if (deltaTime > interval) {

        lastTime = currentTime - (deltaTime % interval);

        update();
        drawCanvas();
    }
}

function update() {
    console.log('Update');
    return;
}

function drawCanvas() {
    return;
}