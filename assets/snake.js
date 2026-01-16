
window.initGame = function(canvasId) {
    console.log("Intentando inicializar:", canvasId);
    const canvas = document.getElementById(canvasId);
    
    if (canvas) {
        console.log("¡Canvas encontrado con éxito!");
    } else {
        console.error("No se encontró el canvas con id:", canvasId);
    }
}