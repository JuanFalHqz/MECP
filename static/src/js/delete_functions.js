//identificadores de los elementos
/*
* Para que funcione correctamente debes poner en la cabecera de ta tabla un checkbox con id='all-elements'
* y luego a cada checkbox del body de la tabla la clase class='checkbox'.
* En ids se almacenan los id a eliminar
* */
ids = [];
// Selecciona y deselecciona todos los chequed
$("#all-elements").click(() => {
    if ($("#all-elements").prop('checked')) {
        $('.checkbox').each(function (i) {
            $(this).prop('checked', true);
            ids[i] = $(this).val();
        });
    } else {
        $('.checkbox').each(function (i) {
            $(this).prop('checked', false);
            ids = [];
        });
    }
});

$("#btn-all-delete").click((e) => {
    ids = [];
    //guardo los id de los checkbox seleccionados.
    $('.checkbox:checked').each(function (i) {
        ids[i] = $(this).val();
    })
    if (ids.length == 0) {
        alert('Seleccione los elementos a borrar.');
    } else {
        if (confirm("Desea eliminar realmente " + ids.length + " ofertas profesionales.")) {
            let url = $("#btn-all-delete").val();
            $.ajax({
                url: url,
                type: 'get',
                data: {'list_id[]': ids},
                dataType: 'json',
                success: (data) => {
                    console.log(data)
                    if (data.deleted) {
                        $("#modal-delete").modal('hide');
                        ids.forEach((value) => {
                            console.log('value:' + value)
                            $("#example1 tbody #row-" + value).remove();
                        })
                        alert('Se han eliminado' + ids.length + ' elementos correctamente.')
                    } else {
                        alert('Ha ocurrido un error.')
                    }
                }
            })
        }
    }
})

function eliminarObject(id, _url, title) {
    if (confirm("Desea eliminar realmente la oferta profesional: " + title)) {

        $.ajax({
            url: _url,
            type: 'get',
            data: {
                'pk': id
            },
            dataType: 'json',
            success: (data) => {
                if (data.deleted) {
                    $("#modal-delete").modal('hide');
                    $("#example tbody #row-" + id).remove();
                    alert('Oferta profesional: ' + title + ' eliminada correctamente.')

                } else {
                    alert('Ha ocurrido un error.');
                }
            },
        })
    }
}