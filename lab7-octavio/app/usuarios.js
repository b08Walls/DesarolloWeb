
function Usuario()
{
 this.email = 0;
 this.password = 0;
 this.nickname = "";
 this.edad = 0;
 this.photourl = "";
};

function insertUsuario()
{
  try
  {
   
    var val_email = $('#email').val();
    var val_password = $('#pass').val();
    var val_nickname = $('#nickname').val();
    var val_edad = $('#edad').val();
    var val_photourl = $('#photo').val();

    var myUsuario = new Usuario();
    myUsuario.email = val_email;
    myUsuario.password = val_password;
    myUsuario.nickname = val_nickname;
    myUsuario.edad = val_edad;
    myUsuario.photourl = val_photourl;
     
    var form_data = new FormData();
      form_data.append("email",myUsuario.email);
      form_data.append("password",myUsuario.password);
      form_data.append("nickname",myUsuario.nickname);
      form_data.append("edad",myUsuario.edad);
      form_data.append("photourl",myUsuario.photourl);


    jQuery.support.cors = true;
    jQuery.ajax({
      url:"/createUser",
      dataType: "text",
      cache: false,
      contentType: false,
      processData: false,
      data: form_data,
      type: "post",
      crossDomain: true,
      success: function (response) {
        alert("key generada: "+response);
        $('#email').val(String.empty);
        $('#pass').val(String.empty);
        $('#nickname').val(String.empty);
        $('#edad').val(String.empty);
        $('#photo').val(String.empty);
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


function getAllUsersDont()
{
  jQuery.support.cors = true;
  alert("hola");
  try
  {
    alert("entro al try");
    $.ajax({
      url: "/readAllUser",  
      dataType: 'json',
      cache: false,
      contentType: false,
      processData: false,
      type: 'get',
      crossDomain: true,
      succes: function(response){
        $("#lstUsers").empty();
        tweets = response;

        alert(response);
 
    var myTableUsers="<table class = 'table table-striped table - advance table-hover'>"+
                        " <tbody id = 'devices'> " +
                        " <tr> " +
                        "     <th> </th> " +
                        "     <th> entitykey </th> " +
                        "     <th> email </th>" +
                        "     <th> password </th> " +
                        "     <th> nickname </th> " +
                        "     <th> edad </th>" +
                        "     <th> photourl </th> " +
                        "    <th> Delete </th> " +
                        "   </tr> ";
          tweets.forEach(function(tweet)
          {
            myTableUsers += "<tr> " +
                          "<td> " +
        "<button onclick = 'getOneUser(\""+ tweet.id +
        "\")' class = 'btn btn-primary' > " + 
        " <i class = 'fa fa fa-ban'></i> ( R ) eadOne </button>" +
                              "</td>" +
                              "<td >" + tweet.id +" </td> " +
                              "<td >" + tweet.email + "</td>" +
                              "<td >" + tweet.passwd + "</td> " +
                              "<td >" + tweet.nickname + "</td> " +
                              "<td >" + tweet.edad + "</td> " +
                              "<td >" + tweet.photourl + "</td> " +
                              "<td>" +
        "<button on click = 'deleteUser(\""+ tweet.id +"\")' class = 'btn btn-danger' > "+
        "<i class = 'fa fa fa-ban'></i> ( D ) elete </button>" +
                              "</td>" +
                                " </div> " +
                              "</td>" +
                            "</tr> ";
          });
          myTableUsers += "</tbody>" +
                  "</table>";
          $("#lstUsers").append(myTableUsers);
      }
    });
  }
  catch(e)
  {
    alert("error : "+ e);
  }
}

function getAllUsers() 
{
    jQuery.support.cors = true;
    try
    {                         
     $.ajax({
        url: "/readAllUser",
        dataType: 'json',
        cache: false,
        contentType: false,
        processData: false,
        type: 'get',
        crossDomain: true,
        success: function(response) {
          $("#lstUsers").empty();
          tweets = response;
          alert(response);
          var myTableUsers = " <table class='table table-striped table-advance table-hover'> " +
                   " <tbody id='devices'> " +
                   "   <tr> " +
                   "      <th>  </th> " +
                   "      <th> entitykey </th> " + 
                   "      <th> email </th> " +
                   "      <th> password </th> " +
                   "      <th> nickname </th> " +
                   "      <th> edad </th> " +
                   "      <th> photourl </th> " +
                   "    <th> Delete </th> " +
                   "   </tr> ";
          tweets.forEach(function (tweet) 
          {
             myTableUsers += "<tr> " +
                         "<td>" +  
    "<button onclick='getOneUser(\""+ tweet.id +  "\")' class='btn btn-primary' > " +
    " <i class='fa fa fa-ban'></i> ( R ) eadOne </button> " + 
                         "</td>" +
                         "<td > " + tweet.id  + " </td> " +
                         "<td > " + tweet.email  + " </td> " + 
                         "<td > " + tweet.passwd + "</td> " +
                         "<td > " + tweet.nickname + "</td> " +
                         "<td > " + tweet.edad + "</td>" +
                         "<td > " + tweet.photourl + "</td>" +
    
                         "<td>" + 
    "<button onclick='deleteUser(\""+ tweet.id +"\")' class='btn btn-danger' > " +
    " <i class='fa fa fa-ban'></i> ( D ) elete </button>" + 
                         "</td>" +
                           " </div> " +
                        "</td> " +
                      "</tr> ";               
          });

          myTableUsers += "</tbody>" +
                "</table>";
          $("#lstUsers").append(myTableUsers);
   }
        });          
     
    }
 catch(e)
    {
      alert("error : " +  e);
     }
}



function getOneUser(userKey)
{
    alert(userKey);
    jQuery.support.cors = true;
    try
    {
      $.ajax({
        url:"/readOneUser",
        dataType: 'json',
        cache: false,
        contentType: false,
        processData: true,
        data: {"key":userKey},
        type: 'get',
        crossDomain: true,
        success: function(response){
          $('#email').val(response.email);
          $('#pass').val(response.passwd);
          $('#nickname').val(response.nickname);
          $('#edad').val(response.edad);
          $('#photo').val(response.edad);

          sessionStorage.setItem('keyUpdate',response.key);
        }
      });
    }
    catch(e)
    {
      alert("error: " + e);
    }
}



function updateUser()
{
  try
  {
     var myKeyUpdate = sessionStorage['keyUpdate'];
     alert(myKeyUpdate);

     var val_email = $('#email').val();
     var val_password = $('#pass').val();
     var val_nickname = $('#nickname').val();
     var val_edad = $('#edad').val();
     var val_photourl = $('#photo').val();
    
     var myUserUpdate = new Usuario();
     myUserUpdate.email = val_email;
     myUserUpdate.password = val_password;
     myUserUpdate.nickname = val_nickname;
     myUserUpdate.edad = val_edad;
     myUserUpdate.photourl = val_photourl;

     var form_data = new FormData();
        form_data.append("key", myKeyUpdate);
        form_data.append("email", myUserUpdate.email);
        form_data.append("password", myUserUpdate.password);
        form_data.append("nickname", myUserUpdate.nickname);
        form_data.append("edad", myUserUpdate.edad);
        form_data.append("photourl",myUserUpdate.photourl);
     jQuery.support.cors = true;

     jQuery.ajax({
         url: "/updateUser",
         dataType: "text",
         cache: false,
         contentType: false,
         processData: false,
         data: form_data,
         type: "post",
         crossDomain: true,
         success: function (response) {
              alert ("key updated : " + response);   
              $('#email').val(String.empty);
              $('#pass').val(String.empty);
              $('#nickname').val(String.empty);
              $('#edad').val(String.empty);
              $('#photo').val(String.empty);
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


function deleteUser(userKey)
{
  try
  {
    alert(userKey);
    var form_data = new FormData();
    form_data.append("key", userKey);
        
    jQuery.support.cors = true;
    jQuery.ajax({
         url: "/deleteUser",
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