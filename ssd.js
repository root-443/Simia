document.write( '<div class="Product">' +
'<img src= +"' + result[i].IMGSRC + '" class="PImage">'+
'<br><br>'+
'<h1 class="titre">' + result[i].Name + '</span>'+
'<br><br>'+
'  <p class="Price">' + result[i].Price + '</span>'+
' <br><br>' +
'<p class="Site">' + result[i].Site +'</span>'+
'<br><br>'+
'  <form method="get" action="' + result[i].Site + '">'+
'<button class="GOTO"  type="submit">Product page</button>' +
'</form>' +


'</div>')