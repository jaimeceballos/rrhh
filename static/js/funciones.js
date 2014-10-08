sumaFecha = function(d, fecha)
{
 var Fecha = new Date();
 var sFecha = fecha || (Fecha.getDate() + "/" + (Fecha.getMonth() +1) + "/" + Fecha.getFullYear());
 var sep = sFecha.indexOf('/') != -1 ? '/' : '-'; 
 var aFecha = sFecha.split(sep);
 var fecha = aFecha[2]+'/'+aFecha[1]+'/'+aFecha[0];
 fecha= new Date(fecha);
 fecha.setDate(fecha.getDate()+parseInt(d));
 var anno=fecha.getFullYear();
 var mes= fecha.getMonth()+1;
 var dia= fecha.getDate();
 mes = (mes < 10) ? ("0" + mes) : mes;
 dia = (dia < 10) ? ("0" + dia) : dia;
 dia -=1;
 var fechaFinal = dia+sep+mes+sep+anno;
 return (fechaFinal);
 }



$(document).ready(function() {
   $( "#calcula_fecha" ).click(function() {
      dias = $("#id_cantidad_dias").val();
      fecha = $("#id_fecha_desde").val();
      fecha_hasta = sumaFecha(dias,fecha);
      $("#id_fecha_hasta").val(fecha_hasta);
    });
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
    $('#id_fecha_desde').datepicker({
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
    $("#id_personal").select2({
      minimumInputLength: 7
    });
    $("#id_codigo").select2({
      minimumInputLength: 2
    });
 });

