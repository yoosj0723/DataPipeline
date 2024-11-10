var express = require('express');
var router = express.Router();

router.get('/', function(req,res, next){
    res.render('finance', {title : 'finance'});
});

module.exports = router;
