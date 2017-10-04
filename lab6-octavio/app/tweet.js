function Tweet()
{
	this.usuario ="";
	this.tweet = "";
};

funciton insertTweet()
{
	try
	{
		var val_usuario = $('#usuario').val();
		var val_tweet = $('#tweet').val();

		var myTweet = new Tweet();
		myTweet.usuario = val_usuario;
		myTweet.tweet = val_tweet;

		var tweetJSON = JSON.stringify(myTweet);
		alert(tweetJSON);

		jQuery.ajax({
			type: "GET",
			url: "/addTweet"
			data: { usuario : myTweet.usuario,
				tweet : myTweet.tweet},
				contentType: "application/text; charset=utf-8",
				dataType: "text",
				success: function(response)
				{
					alert ("key generada: "+response);
				},

				error: function (error)
				{
					alert(error)
				}
		});
	}
	catch(error)
	{
		alert(error);
	}
}