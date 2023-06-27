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


const errores = document.querySelector("error");
const btnEnviar = document.querySelector("enviar");
const nombre =document.getElementById("id_nombre");
const mail =document.getElementById("id_email");
const  asunto  = documento . getElementById ( "id_asunto" ) ;
const mensaje =document.getElementById("id_mensaje");


