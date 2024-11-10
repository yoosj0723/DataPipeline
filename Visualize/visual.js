$(document).ready(function() {

	$(function() {
		$("#datepicker1, #datepicker2").datepicker({
			dateFormat : 'yy-mm-dd'
		});
	});

});

function drawingGraph(data, opt) {
	Plotly.newPlot('myDiv', {
		data: data,
		layout: opt,
	});
}

function loadDailyTable() {

	var from_date = document.getElementById("datepicker1").value;
	var to_date = document.getElementById("datepicker2").value;

	if (to_date.length == 0 || from_date.length == 0) {
		from_date = "2022-02-02";
		to_date = "2023-02-03";
	}

	var url = "/finance/open/" + from_date + "/" + to_date;

	$.ajax({
		type: "GET",
		url: url,
		success:function(rows){
			parseDailyData(rows);
			return false;
		},
		error:function(xhr, status, err){
			console.log(xhr.responseText);
			return false;
		}
	});
}

function parseDailyData(rows) {

_date_list  = [];
  _open_list = [];

  data = rows;

  for(var idx = 0 ; idx < data.length; idx++){
    _date_list.push(data[idx].Date);
    _open_list.push(data[idx].Open);
  }

  var graph = {
    x : _date_list,
    y : _open_list,
    name : "open count",
    mode: 'lines',
    marker: {
    size: 10,
    line: { width: 0.5 },
    opacity: 0.8
    }
  } 

  title_type = 'AMD RECENT PRICE';

  var opt = {
    title: title_type,
    titlefont: {
      family: 'Courier New, monospace',
      size: 24,
      color: '#7f7f7f'
    },
    xaxis: {
      title: 'DAILY',
      titlefont: {
        family: 'Arial, sans-serif',
        size: 15,
        color: 'lightgrey'
      },
      showticklabels: true,
      tickfont: {
        family: 'Old Standard TT, serif',
        size: 13,
        color: 'black'
      },
      showgrid: true,
      zeroline: true,
      showline: true,
      mirror: 'ticks',
      gridcolor: '#bdbdbd',
      gridwidth: 2,
      zerolinecolor: '#969696',
      zerolinewidth: 4,
      linecolor: '#636363',
      linewidth: 6
    },
    margin: {
      l: 50,
      r: 50,
      b: 150,
      t: 150,
      pad: 4
    },
  };
 drawingGraph([graph], opt);

}