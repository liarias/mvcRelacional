(function(){
	console.log("ccbjkb")
	$.ajax({
		type: "GET",
		url: "/ajax/enviarQuejas/",
		dataType: "json",
		success: obtenerQuejas
	});
	
})();
function obtenerQuejas(data){

}