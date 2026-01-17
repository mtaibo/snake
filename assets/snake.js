
// Variables for time on GameLoop
const FPS = 10;
let lastTime = 0;

window.initGame = function(canvasId) {
    requestAnimationFrame(() => {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;

        // Get measures of canvas, and columns/rows of the grid
        canvas.width = canvas.getBoundingClientRect().width;
        canvas.height = canvas.getBoundingClientRect().height;

        const blockSize = 20; 
        const columns = Math.floor(canvas.width / blockSize);
        const rows = Math.floor(canvas.height / blockSize);
        
        requestAnimationFrame(gameLoop);
    });
}

function gameLoop() {
    update();
    drawCanvas();

    requestAnimationFrame(gameLoop);
}

function update() {
    console.log(`Update`);
}

function drawCanvas() {
    console.log(`Draw`);
}