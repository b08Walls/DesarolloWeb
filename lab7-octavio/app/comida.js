function Food()
{
 this.nombre = 0;
 this.precio = 0;
 this.ingredientes = "";
 this.tiempo = 0;
};

function insertFood()
{
  try
  {
   
    var val_nombre = $('#nombre').val();
    var val_precio = $('#precio').val();
    var val_ingredientes = $('#ingredientes').val();
    var val_tiempo = $('#tiempo').val();

    var myFood = new Food();
    myFood.nombre = val_nombre;
    myFood.precio = val_precio;
    myFood.ingredientes = val_ingredientes;
    myFood.tiempo = val_tiempo;
     
    var form_data = new FormData();
      form_data.append("nombre",myFood.nombre);
      form_data.append("precio",myFood.precio);
      form_data.append("ingredientes",myFood.ingredientes);
      form_data.append("tiempo",myFood.tiempo);


    jQuery.support.cors = true;
    jQuery.ajax({
      url:"/createFood",
      dataType: "text",
      cache: false,
      contentType: false,
      processData: false,
      data: form_data,
      type: "post",
      crossDomain: true,
      success: function (response) {
        alert("key generada: "+response);
        $('#nombre').val(String.empty);
        $('#precio').val(String.empty);
        $('#ingredientes').val(String.empty);
        $('#tiempo').val(String.empty);
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


function getAllFoods() 
{
    jQuery.support.cors = true;
    try
    {                         
     $.ajax({
        url: "/readAllFood",
        dataType: 'json',
        cache: false,
        contentType: false,
        processData: false,
        type: 'get',
        crossDomain: true,
        success: function(response) {
          $("#lstFoods").empty();
          tweets = response;
          alert(response);
          var myTableFoods = " <table class='table table-striped table-advance table-hover'> " +
                   " <tbody id='devices'> " +
                   "   <tr> " +
                   "      <th>  </th> " +
                   "      <th> entitykey </th> " + 
                   "      <th> nombre </th> " +
                   "      <th> precio </th> " +
                   "      <th> ingredientes </th> " +
                   "      <th> tiempo </th> " +
                   "    <th> Delete </th> " +
                   "   </tr> ";
          tweets.forEach(function (tweet) 
          {
             myTableFoods += "<tr> " +
                         "<td>" +  
    "<button onclick='getOneFood(\""+ tweet.id +  "\")' class='btn btn-primary' > " +
    " <i class='fa fa fa-ban'></i> ( R ) eadOne </button> " + 
                         "</td>" +
                         "<td > " + tweet.id  + " </td> " +
                         "<td > " + tweet.nombre  + " </td> " + 
                         "<td > " + tweet.precio + "</td> " +
                         "<td > " + tweet.ingredientes + "</td> " +
                         "<td > " + tweet.tiempo + "</td>" +
    
                         "<td>" + 
    "<button onclick='deleteFood(\""+ tweet.id +"\")' class='btn btn-danger' > " +
    " <i class='fa fa fa-ban'></i> ( D ) elete </button>" + 
                         "</td>" +
                           " </div> " +
                        "</td> " +
                      "</tr> ";               
          });

          myTableFoods += "</tbody>" +
                "</table>";
          $("#lstFoods").append(myTableFoods);
   }
        });          
     
    }
 catch(e)
    {
      alert("error : " +  e);
     }
}



function getOneFood(foodKey)
{
    alert(foodKey);
    jQuery.support.cors = true;
    try
    {
      $.ajax({
        url:"/readOneFood",
        dataType: 'json',
        cache: false,
        contentType: false,
        processData: true,
        data: {"key":foodKey},
        type: 'get',
        crossDomain: true,
        success: function(response){
          $('#nombre').val(response.nombre);
          $('#precio').val(response.precio);
          $('#ingredientes').val(response.ingredientes);
          $('#tiempo').val(response.tiempo);

          sessionStorage.setItem('keyUpdate',response.key);
        }
      });
    }
    catch(e)
    {
      alert("error: " + e);
    }
}



function updateFood()
{
  try
  {
     var myKeyUpdate = sessionStorage['keyUpdate'];
     alert(myKeyUpdate);

     var val_nombre = $('#nombre').val();
     var val_precio = $('#precio').val();
     var val_ingredientes = $('#ingredientes').val();
     var val_tiempo = $('#tiempo').val();
    
     var myFoodUpdate = new Usuario();
     myFoodUpdate.nombre = val_nombre;
     myFoodUpdate.precio = val_precio;
     myFoodUpdate.ingredientes = val_ingredientes;
     myFoodUpdate.tiempo = val_tiempo;

     var form_data = new FormData();
        form_data.append("key", myKeyUpdate);
        form_data.append("nombre", myFoodUpdate.nombre);
        form_data.append("precio", myFoodUpdate.precio);
        form_data.append("ingredientes", myFoodUpdate.ingredientes);
        form_data.append("tiempo", myFoodUpdate.tiempo);
     jQuery.support.cors = true;

     jQuery.ajax({
         url: "/updateFood",
         dataType: "text",
         cache: false,
         contentType: false,
         processData: false,
         data: form_data,
         type: "post",
         crossDomain: true,
         success: function (response) {
              alert ("key updated : " + response);   
              $('#nombre').val(String.empty);
              $('#precio').val(String.empty);
              $('#ingredientes').val(String.empty);
              $('#tiempo').val(String.empty);
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


function deleteFood(foodKey)
{
  try
  {
    alert(foodKey);
    var form_data = new FormData();
    form_data.append("key", foodKey);
        
    jQuery.support.cors = true;
    jQuery.ajax({
         url: "/deleteFood",
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