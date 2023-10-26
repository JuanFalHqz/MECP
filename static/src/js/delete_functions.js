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
        let toast = {
            title: "Error",
            message: 'Seleccione los elementos a eliminar',
            status: TOAST_STATUS.DANGER,
            timeout: 5000
        }
        Toast.setPlacement(TOAST_PLACEMENT.TOP_RIGHT);
        Toast.setTheme(TOAST_THEME.LIGHT);
        Toast.create(toast);
    } else {
        Swal.fire({
            title: '¿Está seguro?',
            text: "¿Desea realmente eliminar " + ids.length + " ofertas profesionales?",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Eliminar'
        }).then((result) => {
            if (result.isConfirmed) {
                let url = $("#btn-all-delete").val();
                $.ajax({
                    url: url,
                    type: 'get',
                    data: {'list_id[]': ids},
                    dataType: 'json',
                    success: (data) => {
                        console.log(data)
                        if (data.deleted) {
                            ids.forEach((value) => {
                                console.log('value:' + value)
                                $("#example tbody #row-" + value).remove();

                            })
                            let toast = {
                                title: "Correcto",
                                message: 'Han sido eliminados ' + ids.length + ' perfiles satisfactoriamente.',
                                status: TOAST_STATUS.SUCCESS,
                                timeout: 5000
                            }
                            Toast.setPlacement(TOAST_PLACEMENT.TOP_RIGHT);
                            Toast.setTheme(TOAST_THEME.LIGHT);
                            Toast.create(toast);
                        } else {
                            alert('Ha ocurrido un error.')
                        }
                    }
                })
            }
        })
    }
})

function eliminarObject(id, _url, title) {
    Swal.fire({
        title: '¿Está seguro?',
        text: "¿Desea realmente eliminar la oferta profesional: " + title+" ?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Eliminar'
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                url: _url,
                type: 'get',
                data: {
                    'pk': id
                },
                dataType: 'json',
                success: (data) => {
                    if (data.deleted) {
                        $("#example tbody #row-" + id).remove();
                        let toast = {
                            title: "Correcto",
                            message: 'Perfil eliminado satisfactoriamente.',
                            status: TOAST_STATUS.SUCCESS,
                            timeout: 5000
                        }
                        Toast.setPlacement(TOAST_PLACEMENT.TOP_RIGHT);
                        Toast.setTheme(TOAST_THEME.LIGHT);
                        Toast.create(toast);
                    } else {
                        alert('Ha ocurrido un error.');
                    }
                },
            })
        }
    })

}