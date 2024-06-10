const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    userID : {type:String, require: true },
    userName : {type:String, require: true },
    lastMessage: { type:String, require },
    status : {type:String, require: true },
    deleted : {type:Boolean}
})

const user = mongoose.model('user', userSchema);

module.exports = user;