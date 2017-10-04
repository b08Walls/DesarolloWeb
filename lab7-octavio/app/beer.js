function Beer()
{
 this.marca = 0;
 this.tipo = 0;
 this.ml = "";
 this.presentacion = 0;
};

function insertBeer()
{
  try
  {
   
    var val_marca = $('#marca').val();
    var val_tipo = $('#tipo').val();
    var val_ml = $('#ml').val();
    var val_presentacion = $('#presentacion').val();

    var myBeer = new Beer();
    myBeer.marca = val_marca;
    myBeer.tipo = val_tipo;
    myBeer.ml = val_ml;
    myBeer.presentacion = val_presentacion;
     
    var form_data = new FormData();
      form_data.append("marca",myBeer.marca);
      form_data.append("tipo",myBeer.tipo);
      form_data.append("ml",myBeer.ml);
      form_data.append("presentacion",myBeer.presentacion);


    jQuery.support.cors = true;
    jQuery.ajax({
      url:"/createBeer",
      dataType: "text",
      cache: false,
      contentType: false,
      processData: false,
      data: form_data,
      type: "post",
      crossDomain: true,
      success: function (response) {
        alert("key generada: "+response);
        $('#marca').val(String.empty);
        $('#tipo').val(String.empty);
        $('#ml').val(String.empty);
        $('#presentacion').val(String.empty);
      },
      error: function(error){
        alert(error)
      }
    });
  }
  catch(error)
  {
     alert(error)
  }
}


function getAllBeers() 
{
    jQuery.support.cors = true;
    try
    {                         
     $.ajax({
        url: "/readAllBeer",
        dataType: 'json',
        cache: false,
        contentType: false,
        processData: false,
        type: 'get',
        crossDomain: true,
        success: function(response) {
          $("#lstBeers").empty();
          tweets = response;
          alert(response);
          var myTableBeers = " <table class='table table-striped table-advance table-hover'> " +
                   " <tbody id='devices'> " +
                   "   <tr> " +
                   "      <th>  </th> " +
                   "      <th> entitykey </th> " + 
                   "      <th> marca </th> " +
                   "      <th> tipo </th> " +
                   "      <th> ml </th> " +
                   "      <th> presentacion </th> " +
                   "    <th> Delete </th> " +
                   "   </tr> ";
          tweets.forEach(function (tweet) 
          {
             myTableBeers += "<tr> " +
                         "<td>" +  
    "<button onclick='getOneBeer(\""+ tweet.id +  "\")' class='btn btn-primary' > " +
    " <i class='fa fa fa-ban'></i> ( R ) eadOne </button> " + 
                         "</td>" +
                         "<td > " + tweet.id  + " </td> " +
                         "<td > " + tweet.marca  + " </td> " + 
                         "<td > " + tweet.tipo + "</td> " +
                         "<td > " + tweet.ml + "</td> " +
                         "<td > " + tweet.presentacion + "</td>" +
    
                         "<td>" + 
    "<button onclick='deleteBeer(\""+ tweet.id +"\")' class='btn btn-danger' > " +
    " <i class='fa fa fa-ban'></i> ( D ) elete </button>" + 
                         "</td>" +
                           " </div> " +
                        "</td> " +
                      "</tr> ";               
          });

          myTableBeers += "</tbody>" +
                "</table>";
          $("#lstBeers").append(myTableBeers);
   }
        });          
     
    }
 catch(e)
    {
      alert("error : " +  e);
     }
}



function getOneBeer(beerKey)
{
    alert(beerKey);
    jQuery.support.cors = true;
    try
    {
      $.ajax({
        url:"/readOneBeer",
        dataType: 'json',
        cache: false,
        contentType: false,
        processData: true,
        data: {"key":beerKey},
        type: 'get',
        crossDomain: true,
        success: function(response){
          $('#marca').val(response.marca);
          $('#tipo').val(response.tipo);
          $('#ml').val(response.ml);
          $('#presentacion').val(response.presentacion);

          sessionStorage.setItem('keyUpdate',response.key);
        }
      });
    }
    catch(e)
    {
      alert("error: " + e);
    }
}



function updateBeer()
{
  try
  {
     var myKeyUpdate = sessionStorage['keyUpdate'];
     alert(myKeyUpdate);

     var val_marca = $('#marca').val();
     var val_tipo = $('#tipo').val();
     var val_ml = $('#ml').val();
     var val_presentacion = $('#presentacion').val();
    
     var myBeerUpdate = new Usuario();
     myBeerUpdate.marca = val_marca;
     myBeerUpdate.tipo = val_tipo;
     myBeerUpdate.ml = val_ml;
     myBeerUpdate.presentacion = val_presentacion;

     var form_data = new FormData();
        form_data.append("key", myKeyUpdate);
        form_data.append("marca", myBeerUpdate.marca);
        form_data.append("tipo", myBeerUpdate.tipo);
        form_data.append("ml", myBeerUpdate.ml);
        form_data.append("presentacion", myBeerUpdate.presentacion);
     jQuery.support.cors = true;

     jQuery.ajax({
         url: "/updateBeer",
         dataType: "text",
         cache: false,
         contentType: false,
         processData: false,
         data: form_data,
         type: "post",
         crossDomain: true,
         success: function (response) {
              alert ("key updated : " + response);   
              $('#marca').val(String.empty);
              $('#tipo').val(String.empty);
              $('#ml').val(String.empty);
              $('#presentacion').val(String.empty);
         },
         error: function (error) {    
              alert(error.text)
         }
     });
  }
  catch(error)
  {
     alert(error)
  }
}


function deleteBeer(beerKey)
{
  try
  {
    alert(beerKey);
    var form_data = new FormData();
    form_data.append("key", beerKey);
        
    jQuery.support.cors = true;
    jQuery.ajax({
         url: "/deleteBeer",
         dataType: "text",
         cache: false,
         contentType: false,
         processData: false,
         data: form_data,
         type: "post",
         crossDomain: true,
         success: function (response)
         {
              alert ("key eliminada: " + response);
         },
         error: function (error)
         {
              alert(error)
         }
     });
  }
  catch(error)
  {
     alert(error)
  }
}