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
                    a=a+'<div class="card shadow mb-4">';
                    a=a+'<div class="card-header py-3">';
                    a=a+'<h6 class="m-0 font-weight-bold text-primary">'+response[i].title+'</h6>';
                    a=a+'</div>';
                    a=a+'<div class="card-body">';
                    a=a+'<div class="text-center">';
                    a=a+'<img class="img-fluid px-3 px-sm-4 mt-3 mb-4" style="width: 25rem;" src="{{url_for('static', filename = 'img/undraw_posting_photo.svg')}}" alt="">';
                    a=a+'</div>';
                    a=a+'<div class="text-left">';
                    a=a+'<p> <b>Fecha:</b>'+ response[i].startDate +' al '+ response[i].endDate +'</p>';
                    //a=a+'<p> <b>Numero Máximo de Competidores:</b>'+ response[i].maxCompetitors'</p>';
                    a=a+'</div>';
                    a=a+'<p>'+response[i].description+'</p>';
                    a=a+'<div>';
                    a=a+'<a target="_blank" href="https://undraw.co/">Documentos de Interés&rarr;</a>';
                    a=a+'</div>';
                    a=a+'<br>';
                    a=a+'<div class="text-right">';
                    a=a+'<div class="btn btn-primary btn-icon-split">';
                    a=a+'<span class="icon text-white-50">';
                    a=a+'<i class="fas fa-check"></i>';
                    a=a+'</span>';
                    a=a+'<button class="text" onclick="showInscriptionDiv('+response[i].id+')">Inscribete Aquí</button>';
                    a=a+'</div></div></div></div></div></div>';
                    $('#posts').append(a);
                    i = i +  1
                });
            },
        });
}

function showInscriptionDiv(idChampionship){
  $('#principal_page').hide();
  $("#firstCondition").html("Número de Vela");
  $("#secondCondition").html("Tipo de vela");
  $('#send_button').attr('onclick', 'sailingLoadData('+idChampionship+')');
  $('#insOK').attr('onclick', 'sailingLoadData('+idChampionship+')');

  //meterle un if para saber si es vela o fut

  //$("#firstCondition").html("Peso en kg");
  //$("#secondCondition").html("Equipo");
  //$('#insOK').attr('onclick', 'soccerLoadData('+idChampionship+')');

  $('#inscriptions').show();

  $("#titleInscription").html("Inscripción al Campeonato N"+idChampionship);
}

//<select id="secondInput" name="secondInput" class="form-control" >
//<option value="">-Seleccionar-</option>
//<option value="1">4.7</option>
//<option value="2">Radial</option>
//<option value="3">Standard</option>





function sailingLoadData(idChampionship){
    $.ajax({
            url:'/current',
            type:'GET',
            contentType: 'application/json',
            dataType:'json',
            success: function(response){
                idUser = response['id']
            }
        });
    var firstCondition = $('#firstCondition').val();
    var secondCondition = $("#secondCondition").val();
    var message = JSON.stringify({
                "sailingNumber": firstCondition,
                "category": secondCondition,
                "user_id": idUser,
                "championship_id": idChampionship
            });
            //falta añadir el load con ajax e implementar en server con json.loads(request.data)

}

function soccerLoadData(idChampionship){
    $.ajax({
            url:'/current',
            type:'GET',
            contentType: 'application/json',
            dataType:'json',
            success: function(response){
                idUser = response['id']
            }
        });
    var firstCondition = $('#firstCondition').val();
    var secondCondition = $("#secondCondition").val();
    var message = JSON.stringify({
                "category": firstCondition,
                "soccerTeam": secondCondition,
                "user_id": idUser,
                "championship_id": idChampionship
            });
            //falta añadir el load con ajax e implementar en server con json.loads(request.data)
}


function cancel_inscription(){
  $('#inscriptions').hide();
  $('#principal_page').show();
}
