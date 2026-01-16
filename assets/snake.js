window.initGame = function(canvasId) {
    requestAnimationFrame(() => {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;

        const rect = canvas.getBoundingClientRect();
        
        canvas.width = rect.width;
        canvas.height = rect.height;

        console.log(`Canvas ajustado a: ${canvas.width} x ${canvas.height}`);
        
        const tileSize = 20; 
        const columnas = Math.floor(canvas.width / tileSize);
        const filas = Math.floor(canvas.height / tileSize);
        
        console.log(`Tablero de ${columnas}x${filas}`);
    });
}