var contador;
function calificar(iten){
    console.log(iten);
    contador=iten.id[0];
    let nombre = iten.id.substring(1);
    for(let i=0;i<5;i++){
        if(i<contador){
            document.getElementById((i+1)+nombre).style.color="orange";
        }
    }
}