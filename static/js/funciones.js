
$(document).ready(function() {
   $('#id_unidad_regional').change(function(event){
   		var id = $('#id_unidad_regional').val();
   		var toLoad = '../../obtener_dependencias/'+id+'/';
   		$.get(toLoad, function(data){
 			var options = '<option value=""></option>';
	        for (var i = 0; i < data.length; i++){
	        	options += '<option value="'+data[i]["pk"]+'">' +data[i]["fields"]["descripcion"] +'</option>'
	        }
            $('#id_dependencia').html(options)
            $("#id_dependencia option:first").attr('selected', 'selected');
        }, "json");

   	});
   $('#table').dataTable( {
          "aaSorting": [[ 1, "desc" ]]
    } );
   $('#id_fecha_nac').datepicker({
      format: "dd/mm/yyyy",
      language: "es",
      autoclose: true
    });
    $('#id_fecha_ingreso').datepicker({
      format: "dd/mm/yyyy",
      language: "es",
      autoclose: true
    });

var nbaTeams = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace('team'),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  prefetch: '../data/nba.json'
});
 
var nhlTeams = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace('team'),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  prefetch: '../data/nhl.json'
});
 
nbaTeams.initialize();
nhlTeams.initialize();
 
$('#test').typeahead({
  highlight: true
},
{
  name: 'nba-teams',
  displayKey: 'team',
  source: nbaTeams.ttAdapter(),
  templates: {
    header: '<h3 class="league-name">NBA Teams</h3>'
  }
},
{
  name: 'nhl-teams',
  displayKey: 'team',
  source: nhlTeams.ttAdapter(),
  templates: {
    header: '<h3 class="league-name">NHL Teams</h3>'
  }
});



 });

