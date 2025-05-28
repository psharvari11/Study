const mongoose=require("mongoose");
require("dotenv").config();
const MONGO_URI=process.env.MONGO_URI;

const dbconnect=async()=>{
    try{
        await mongoose.connect(MONGO_URI);
        console.log("Connected to DB")
    }
    catch(err){
        console.log("Error connecting to DB", err)
    }
}

module.exports=dbconnect