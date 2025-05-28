const express=require("express");
const dbconnect = require("./config/db");
const app=express();
app.use(express.json());
require("dotenv").config()
const PORT=process.env.PORT;


app.get("/",(req,res)=>{
    res.json({msg:"Home"})
})

dbconnect()

.then(()=>{
    app.listen(PORT,()=>{
        console.log(`Server started at ${PORT}`)
    })
})
.catch((err)=>{
    console.log("Error connecting to server", err)
})