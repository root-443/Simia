var express = require("express");
var app = express();
var bodyparser=require("body-parser");
app.use(bodyparser.urlencoded({ extended: true }));
var MongoClient=require("mongodb").MongoClient;
var url="mongodb://localhost:27017/Produits";

app.listen(3000);

app.get("/home.html",function(req,res)
 {
   res.sendFile(__dirname+"/Display.html");
 })

 app.get("/home.html",function(req,res)
 {
   res.sendFile(__dirname+"/Search.html");
 })

 app.post("/home.html",function(req,res)
 {
   MongoClient.connect(url,function(err,db)
    {
      if(err) throw err;
      var dbo=db.db("Produits");
      dbo.collection("info").insertOne(req.body);
    })
   console.log(req.body);
   res.redirect("home.html");
 });