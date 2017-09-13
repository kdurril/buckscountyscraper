
/** https://stackoverflow.com/questions/11944932/how-to-download-a-file-with-node-js-without-using-third-party-libraries **/
/**https://stackoverflow.com/questions/1267283/how-can-i-pad-a-value-with-leading-zeros**/
var http = require('http');
var fs = require('fs');

function zeroPad(num, numZeros) {
    var n = Math.abs(num);
    var zeros = Math.max(0, numZeros - Math.floor(n).toString().length );
    var zeroString = Math.pow(10,zeros).toString().substr(1);
    if( num < 0 ) {
        zeroString = '-' + zeroString;
    }

    return zeroString+n;
}

function baseDate(){
    var start = new Date();
    var y = '' + start.getFullYear();
    var m = '' + zeroPad(start.getMonth(),2);
    var d = '' + zeroPad(start.getDate(),2);
        return y+m+d;
}

function identArray(count){
    var arry = new Array()
    for (var i = 0; i < count; i ++){
        var padded = zeroPad(i,4);
        arry.push(padded);
        }
        return arry;
    }

function grabPdfs(pullDate){
  var baseUrl = "http://appsrv.achd.net/reports/rwservlet?food_rep_insp&P_ENCOUNTER=";
  identArray(60).forEach(function(currentValue){
    var bd = pullDate;
    var request = http.get(baseUrl+bd+currentValue, function(response) {
    if (response.headers['content-type'] == 'application/pdf'){
        var achdFile = fs.createWriteStream(bd+currentValue+".pdf")
        response.pipe(achdFile);
    }
    });
  }
)}

grabPdfs(baseDate());
	


