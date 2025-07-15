let boton=document.getElementById("boton")
let nombres=document.getElementById("producto")
let salario=document.getElementById("salario")
let horas=document.getElementById("horas")
let cargo=document.getElementById("cargo")
let experiencia=document.getElementById("experiencia")

// escuchamos el evento de hacerle click al boton del formulario
boton.addEventListener("click",function(evento){

    evento.preventDefault()

    nombreIngresado=nombres.value
    precioIngresado=nombres.value
    UnidadesIngresadas=horas.value
    diaIngresado=horas.value


    let datos=JSON.stringify({
        nombreProducto:nombreIngresado,
        precioProducto:salarioIngresado,
        unidadesProducto:horasIngresadas,
        cargoEmpleado:cargoIngresado,
        experienciaEmpleado:experienciaIngresada
    })

    Swal.fire({
        title: "Good job!",
        text: "You clicked the button!",
        icon: "success"
    });
})


