const mongoose=require("mongoose");

const userSchema= new mongoose.Schema({
    name:String,
    email:{
        type:String,
        required:true,
        unique:true
    },
    role:{
        type:String,
        enum:["user","admmin"],
        default:"user"
    }
})

const userModel= mongoose.model("User",userSchema)

module.exports=userModel;