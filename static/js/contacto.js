const errores = document.querySelectorAll(".error");
const btnEnviar = document.querySelector(".enviar");
const nombre =document.getElementById("id_nombre");
const mail =document.getElementById("id_email");
const asunto =document.getElementById("id_asunto");
const mensaje =document.getElementById("id_mensaje");


function inputError(){
    for(let i = 0;i<errores.length;i++){
        if(errores[i].querySelector("ul")){
            document.querySelectorAll(".contacto-campo")[i].classList.add("input-error");
        } else {
            document.querySelectorAll(".contacto-campo")[i].classList.remove("input-error");
        }
    }
}

nombre.addEventListener("focusout", ()=>{

    if(!nombre.value){
        nombre.classList.add("input-error");
        errores[0].innerHTML = `<ul class="errorlist"><li>Campo obligatorio</li></ul>`;
    } else {
        nombre.classList.remove("input-error");
        errores[0].textContent = ""
    }
})

mail.addEventListener("focusout", ()=>{
    if(!mail.value){
        mail.classList.add("input-error");
        errores[1].innerHTML = `<ul class="errorlist"><li>Campo obligatorio</li></ul>`;
    } else if(!mail.value.includes("@")){
        mail.classList.add("input-error");
        errores[1].innerHTML = `<ul class="errorlist"><li>Introduce una dirección de correo válida</li></ul>`;
    } else {
        mail.classList.remove("input-error");
        errores[1].textContent = ""
    }
})

asunto.addEventListener("focusout", ()=>{
    let contador = nombre.value.split(' ').length;
    if(!nombre){
        nombre.classList.add("input-error");
        errores[0].innerHTML = `<ul class="errorlist"><li>Campo obligatorio</li></ul>`;
    } else if(contador < 2){
        nombre.classList.add("input-error");
        errores[0].innerHTML = `<ul class="errorlist"><li>Debes introducir nombre y apellido</li></ul>`;
    } else {
        nombre.classList.remove("input-error");
        errores[0].textContent = ""
    }
})


mensaje.addEventListener("keyup", ()=>{
    let contador = mensaje.value.split(' ').length;
    if(!mensaje.value){
        mensaje.classList.add("input-error");
        errores[3].innerHTML = `<ul class="errorlist"><li>Campo obligatorio</li></ul>`;
    } else if(contador < 6){
        mensaje.classList.add("input-error");
        errores[3].innerHTML = `<ul class="errorlist"><li>Tu mensaje es demasiado corto, por favor brinda más detalles</li></ul>`;
    } else {
        mensaje.classList.remove("input-error");
        errores[3].textContent = ""
    }
})

inputError()