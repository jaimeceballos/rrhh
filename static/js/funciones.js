
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
    $("#id_ciudad_nac").select2({
      minimumInputLength: 4
    });
    $("#id_ciudad_res").select2({
      minimumInputLength: 4
    });
    $("#id_escalafon").select2({
      minimumInputLength: 4
    });

 });

