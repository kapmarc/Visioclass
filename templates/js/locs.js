function nextColor(colorName) {
	var colors = ['gray','beige','lime','brown','green','cyan','blue','yellow','orange','red','pink','Violet'];
	var colorsRgb = ["rgb(128, 128, 128)", "rgb(245, 245, 220)", "rgb(0, 255, 0)", "rgb(165, 42, 42)",
	                 "rgb(0, 128, 0)", "rgb(0, 255, 255)", "rgb(0, 0, 255)", "rgb(255, 255, 0)",
	                 "rgb(255, 165, 0)", "rgb(255, 0, 0)", "rgb(255, 192, 203)", "rgb(238, 130, 238)"]
	colIndex = colorsRgb.indexOf(colorName);
	newColIndex = (colIndex+1) %12
	return colorsRgb[newColIndex]
}
function previousColor(colorName) {
	var colors = ['gray','beige','lime','brown','green','cyan','blue','yellow','orange','red','pink','Violet'];
	var colorsRgb = ["rgb(128, 128, 128)", "rgb(245, 245, 220)", "rgb(0, 255, 0)", "rgb(165, 42, 42)",
	                 "rgb(0, 128, 0)", "rgb(0, 255, 255)", "rgb(0, 0, 255)", "rgb(255, 255, 0)",
	                 "rgb(255, 165, 0)", "rgb(255, 0, 0)", "rgb(255, 192, 203)", "rgb(238, 130, 238)"]
	colIndex = colorsRgb.indexOf(colorName);
	if (colIndex==0) {
		newColIndex =11
	} else {
		newColIndex = colIndex-1
	}
	return colorsRgb[newColIndex]
}

function abrevColor(colorRgb) {
	var colorAbr = {"rgb(128, 128, 128)" : 'Gr', "rgb(245, 245, 220)" : "Bg", "rgb(0, 255, 0)" : "Lm", "rgb(165, 42, 42)" : "Br",
     "rgb(0, 128, 0)" : "Gn", "rgb(0, 255, 255)" : "Cy", "rgb(0, 0, 255)" : "Bl", "rgb(255, 255, 0)" : "Yw",
     "rgb(255, 165, 0)" : "Or", "rgb(255, 0, 0)" : "Rd", "rgb(255, 192, 203)" : "Rs", "rgb(238, 130, 238)": "Vt"}
	return colorAbr[colorRgb]
}


$(document).ready(function() {
	$('.action-panel').hide()
	
	$("#newloc-button").click(function() {
		$('#newloc-action-panel').slideToggle()
	})
	$("#close-newloc-panel").click(function() {
		$('#newloc-action-panel').slideToggle()
	})
	
	$("#edit-button").click(function() {
		$('#edit-action-panel').slideToggle()
	})
	$("#close-edit-panel").click(function() {
		$('#edit-action-panel').slideToggle()
	})
	
	$("#erase-button").click(function() {
		$('#erase-action-panel').slideToggle()
	})
	$("#close-erase-panel").click(function() {
		$('#erase-action-panel').slideToggle()
	})
	{% for col in colors %}
	$(".col{{forloop.counter}}").attr("style", 'background-color:{{ col }}');
	{% endfor %}
	
	$("#colorbox").css('background-color', 'rgb(128, 128, 128)')
	
	$("#nextcolor-button").click(function() {
		color =$("#colorbox").css('background-color')
		$("#colorbox").css('background-color', nextColor(color))
		$("select#id_couleur_create").val(abrevColor(nextColor(color)))
	})
	$("#prevcolor-button").click(function() {
		color =$("#colorbox").css('background-color')
		$("#colorbox").css('background-color', previousColor(color))
		$("select#id_couleur_create").val(abrevColor(previousColor(color)))
	})
	$("label[for='id_couleur_create']").hide();
	$("#id_couleur_create").hide();
	
	$("#id_nom_edit").val("{{ currentloc.name }}")
	$("#id_description_edit").val("{{ currentloc.description }}")
	$("#id_couleur_edit").val("{{ currentloc.color }}")
	$("#colorbox-edit").css('background-color', '{{ currentcol }}')
	
	$("#nextcolor-edit-button").click(function() {
		color =$("#colorbox-edit").css('background-color')
		$("#colorbox-edit").css('background-color', nextColor(color))
		$("select#id_couleur_edit").val(abrevColor(nextColor(color)))
	})
	$("#prevcolor-button").click(function() {
		color =$("#colorbox").css('background-color')
		$("#colorbox-edit").css('background-color', previousColor(color))
		$("select#id_couleur_edit").val(abrevColor(previousColor(color)))
	})
	$("label[for='id_couleur_edit']").hide();
	$("#id_couleur_edit").hide();
})