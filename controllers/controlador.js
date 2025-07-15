let boton=document.getElementById("Enviar")

let nombres=document.getElementById("nombre")
let precio=document.getElementById("precio")
let unidades=document.getElementById("unidades")
let dia=document.getElementById("dia")



boton.addEventListener("click",function(evento){

    evento.preventDefault()

    nombreIngresado=nombres.value 
    precioIngresado=precio.value
    unidadesIngresadas=unidades.value
    diaIngresadas=dia.value
 

    let datos=JSON.stringify({
        nombresProducto:nombreIngresado,
        precioProducto:precioIngresado,
        unidadesProducto:unidadesIngresadas,
        diaProducto:diaIngresadas,
        


    })
  
    Swal.fire({
    title: "Buen trabajo!",
    text: "Exito registrando el empleado!",
    icon: "success"
    });

})