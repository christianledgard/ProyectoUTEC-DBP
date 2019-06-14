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
                    i = i +  1;
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

  // if(idChampionship){
  //$("#firstCondition").html("Número de Vela");
  //$("#secondCondition").html("Tipo de vela");
  //$('#send_button').attr('onclick', 'sailingLoadData('+idChampionship+')');
  //$('#insOK').attr('onclick', 'sailingLoadData('+idChampionship+')');

    //} else {
    //$("#firstCondition").html("Peso en kg");
    //$("#secondCondition").html("Equipo");
    //$('#insOK').attr('onclick', 'soccerLoadData('+idChampionship+')');
  //}

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
    $.ajax({
            url:'/loadSailData',
            type:'POST',
            contentType: 'application/json',
            data : message,
            dataType:'json',
            success: function(response){
                alert(JSON.stringify(response));
            },
            error: function(response){
              if(response["status"]==401){
                    alert(JSON.stringify("FAIL :("));
    				}else{
              alert(JSON.stringify("OK :)"));
              window.location.href = "http://0.0.0.0:8020";
    				    }
            }
        });
}

function soccerLoadData(idChampionship){
    $.ajax({
            url:'/loadSoccerData',
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
    $.ajax({
            url:'/loadSoccerData',
            type:'POST',
            contentType: 'application/json',
            data : message,
            dataType:'json',
            success: function(response){
                alert(JSON.stringify(response));
            },
            error: function(response){
              if(response["status"]==401){
                    alert(JSON.stringify("FAIL :("));
				     }else{
                    alert(JSON.stringify("OK :)"));
                    window.location.href = "http://0.0.0.0:8020";
    				            }
            }
        });
}


function cancel_inscription(){
  $('#inscriptions').hide();
  $('#principal_page').show();
}


function culqi() {
  if (Culqi.token) { // ¡Objeto Token creado exitosamente!
      var token = Culqi.token.id;
      paymentsPOST(token);
      alert('Se ha creado un token:' + token);
  } else { // ¡Hubo algún problema!
      // Mostramos JSON de objeto error en consola
      console.log(Culqi.error);
      alert(Culqi.error.user_message);
  }
};

function paymentsPOST(token) {
    var message = JSON.stringify({
        "paymentToken": token,
        "user_id": 1,
        "championship_id": 1
    });
    $.ajax({
        url: '/payments',
        type: 'POST',
        contentType: 'application/json',
        data: message,
        dataType: 'json',
        success: function (response) {
            alert(JSON.stringify(response));
        },
        error: function (response) {
            alert(JSON.stringify(response));}
        });
        }

/*
function culqi() {
  if (Culqi.token) { // ¡Objeto Token creado exitosamente!
      var token = Culqi.token.id;
      alert('Se ha creado un token:' + token);
      var message = JSON.stringify({
              "paymentToken": token,
              "user_id": 1,
              "championship_id":1
          });
      $.ajax({
          url:'/payments',
          type:'POST',
          contentType: 'application/json',
          data : message,
          dataType:'json',
          success: function(response){
              alert(JSON.stringify(response));
          },
          error: function(response){

          };

  } else { // ¡Hubo algún problema!
      // Mostramos JSON de objeto error en consola
      console.log(Culqi.error);
      alert(Culqi.error.user_message);
  }

  */
