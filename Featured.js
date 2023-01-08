var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";
var f = require('fs')
MongoClient.connect(url, function(err, db) {
  var dbo = db.db("Produits");
    var query = {Kwrd: "testlol" };
    dbo.collection("info").find(query).toArray(function(err, result) {
     console.log("result :" + result[0].Price)

     var div = '<div class="Product">'+
                '<img src="' + result[0].IMGSRC +'"' + ' class="PImage"></img>' +
                '<br><br>' +
                '<span class="marque">'+ result.Kwrd + '</span>'+
                '<br><br>' +
                '<span class="titre">' + result[0].Name + '</span>'+
                '<br><br>'+
                '<span class="Prix">'+ result[0].Price + '</span>'




     f.appendFile('Featured.html', 'Slt' + result[0].Price, function (err) {
      if (err) throw err;
      console.log('Updated!');
    }); 
     
     
     
     
     db.close();
    });

  });


/*<div class="Product">
	 	<img src="favicon.png" class="PImage">
	 	<br><br>
		<span class="marque">adidas</span>
		<br><br>
		<span class="titre">Airforce</span>
		<br><br>
		<span class="Prix">100$</span>

				

	



</div>  */

 