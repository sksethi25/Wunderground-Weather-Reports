var getPropername = function (name) {
    var names = {
      'tempm': 'Temperature',
      'humidity': 'Humidity',
      'dewptm': 'Dew',
      'vism': 'Visibility',
      'pressurem':'Pressure',
      'wspdm':'Wind Speed'
    };
    return names[name];
  };
  var add_datepicker = function () {
    var dateFormat = "dd/mm/yy",
      from = $("#id_from_date")
        .datepicker({
          defaultDate: "+1w",
          changeMonth: true,
          constrainInput: true,
          dateFormat: dateFormat
        })
        .on("change", function() {
          var date = getDate(this);
          var maxDate = new Date(date);
          maxDate.setDate(maxDate.getDate() + 10);
          to.removeAttr('disabled')

          to.datepicker( "option", "minDate", date);
          to.datepicker( "option", "maxDate", maxDate);
        }),
      to = $("#id_to_date")
        .datepicker({
          defaultDate: "+1w",
          changeMonth: true,
          constrainInput: true,
          dateFormat: dateFormat
        })
        .on( "change", function() {
          to.attr('disabled', 'disabled')
        });

    function getDate (element) {
      var date ;
      try {
        date = $.datepicker.parseDate(dateFormat, element.value);
      } catch( error ) {
        console.log("in exceptin", error);
        date = null;
      }
      return date;
    }
  };
  var showloading = function (show) {
      if(show) {
        $('#chart_container').addClass('show');
        $('#chart').hide();
      } else{
        $('#chart_container').removeClass('show');
        $('#chart').show();
      }
  };
  var onfetch = function () {
    var wcondition = $("#id_select_cond").val();
   
    if($("#id_to_date").val() !== "" && $("#id_from_date").val() !=="") {
      showloading(true);
      $("#id_to_date").removeAttr('disabled');
      $.post('/fetch/', $("#fetch_form").serialize())
        .done(function(response) {
          $("#id_to_date").attr('disabled', 'disabled')
          showloading(false);
          plot_weather(response, wcondition);
        })
        .fail(function() {
          alert( "please Try again" );
        });
    } else {
      alert("select proper date range");
    }
  };
  var plot = function (w_condition, type, dates, min_data, max_data) {
    var layout = {
      title: w_condition + ' Plot',
      width:1000,
      height:500,
      xaxis: {
        title: 'Date'
      },
      yaxis: {
        title: w_condition
      },
      bargap: dates.length < 4 ? 0.9 : null
    },
      min_data = {
        x: dates,
        y: min_data,
        name: 'Min ' + w_condition,
        type: type
      },
      max_data = {
        x: dates,
        y: max_data,
        name: 'Max ' + w_condition,
        type: type,
        barmode:'group'
      };
    Plotly.newPlot('chart', [min_data, max_data], layout, {displayModeBar: false,
      staticPlot: true});
  };
  var plot_weather = function (jresp, w_condition) {
    var resp = JSON.parse(jresp);
    var dates = [];
    var min_data = [];
    var max_data = [];
    resp.forEach(function (set) {
      var min_value = set["min" + w_condition];
      var max_value = set["max" + w_condition];

      dates.push(set['weather_date']); 
      min_data.push(min_value == -9999 ? 0 : min_value);
      max_data.push(max_value == -9999 ? 0 : max_value);
    });
    plot(getPropername(w_condition), "bar", dates, min_data, max_data);
  };
  var onadd = function () {
     $.post('/addcity/', $("#add_form").serialize())
        .done(function(response) {
          location.reload();
        })
        .fail(function() {
          alert( "please Try again" );
        });
  };
  var init_js = function () {
    add_datepicker();
    $("#fetch").on('click', onfetch);
    
  };
  var init_add = function () {
    $("#add").on('click', onadd);
  };