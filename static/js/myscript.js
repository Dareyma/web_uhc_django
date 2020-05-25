// $('.datepicker').datepicker();


function alert_jqueryconfirm(url, id){
    // var url = params;
    console.log("Entra en la funcion");
    var post_url = "{% url '" + url + "' " + id + " %}";
    console.log(post_url);

    $.confirm({
        theme: 'material',
        title: 'Confirmación',
        icon: 'fa fa-info',
        content: '¿Quieres eliminar el registro?',
        columnClass: 'medium',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    
                    Location.href = post_url;
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    });
}