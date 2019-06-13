function refreshPage(){
    $.ajax({
            url:'/championship',
            type:'GET',
            contentType: 'application/json',
            dataType:'json',
            success: function(response){
                var i = 0;
                $.each(response, function(){
                    a='<div class="row">';
                    a=a+'<div class="col-lg-6 mb-4">';
                    a=a+'<div class="card shadow mb-4">';
                    a=a+'<div class="card-header py-3">';
                    a=a+'<h6 class="m-0 font-weight-bold text-primary">Campeonato N'+response[i].id+': '+response[i].title+'</h6>';
                    a=a+'</div>';
                    a=a+'<div class="card-body">';
                    a=a+'<div class="text-center">';
                    a=a+'<img class="img-fluid px-3 px-sm-4 mt-3 mb-4" style="width: 25rem;" src="{{url_for('static', filename = 'img/undraw_posting_photo.svg')}}" alt="">';
                    a=a+'</div>';
                    a=a+'<div class="text-left">';
                    a=a+'<p> <b>Fecha:</b> 12-06-2019 al 15-06-2019 ARREGLAR ESTO!!</p>';
                    a=a+'</div>';
                    a=a+'<p>Add some quality, svg illustrations to your project courtesy of  a constantly updated collection of beautiful svg images that you can use completely free and without attribution!</p>';
                    a=a+'<div>';
                    a=a+'<a target="_blank" href="https://undraw.co/">Documentos de Interés&rarr;</a>';
                    a=a+'</div>';
                    a=a+'<br>';
                    a=a+'<div class="text-right">';
                    a=a+'<div class="btn btn-primary btn-icon-split">';
                    a=a+'<span class="icon text-white-50">';
                    a=a+'<i class="fas fa-check"></i>';
                    a=a+'</span>';
                    a=a+'<button class="text" onclick="showInscriptionDiv()">Inscribete Aquí</button>';
                    a=a+'</div></div></div></div></div></div>';
                    $('#posts').append(a);
                });
            },
        });
}

function showInscriptionDiv(){
  $('#principal_page').hide();
  $('#inscriptions').show();
}

function inscription(){

}



function cancel_inscription(){
  $('#inscriptions').hide();
  $('#principal_page').show();
}

function ok_inscription(){

}
