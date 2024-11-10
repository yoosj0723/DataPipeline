var express = require('express');
var router = express.Router();

const mysql = require('mysql');
const dbconfig = require('../conf/db.js')
var conn = mysql.createConnection(dbconfig.local);

router.get('/open/:from_date/:to_date', function(req, res){
    var from_date = req.params.from_date;
    var to_date = req.params.to_date;

    console.log(from_date, to_date);

    var query = 'select Date, Open from finance where Date between ? and ?';

    conn.query(query, [from_date, to_date], function(err, rows){
        if (err) {
            console.error(err)
            throw err;
        }
        res.statusCode = 200;
        console.log(rows);
        res.json(rows);
    });
})

router.get('/', function(req,res, next){
    res.render('finance', {title : 'finance'});
});

module.exports = router;
