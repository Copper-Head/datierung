if (adfontes_common_loaded != 1) {

/* stylesheet laden */
var headID = document.getElementsByTagName("head")[0];         
var cssNode = document.createElement('link');
cssNode.type = 'text/css';
cssNode.rel = 'stylesheet';
cssNode.href = 'adfontes_ajax.css';
cssNode.media = 'screen';
headID.appendChild(cssNode);

/* jquery laden */
document.write('<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4/jquery.min.js"></script>');

/* variablen setzen */
var loadUserinputUrl = "userinput_load.php";
var saveUserinputUrl = "userinput_save.php";

/* basisfunktion fuer moegliche Uebersetzungen */
function _(s) {
	return s;
}

/* textfelder initialisieren */
function initialisieren_text(data) {
	var input = data.split('|');
	var i = 0;
	while (i<input.length) {
		$('#'+pageID+' input:text:eq('+i+')').val(input[i]);
		i++;
	}
}
/* textfelder initialisieren mit defaultwerten */
function initialisieren_text_defaults(data) {
	var input = data.split('|');
	var i = 0;
	while (i<defaultvalues.length) {
		if (i < input.length && input[i] !="") {
			$('#'+pageID+' input:text:eq('+i+')').val(input[i]);
		} else {
			$('#'+pageID+' input:text:eq('+i+')').val(defaultvalues[i]);
		}
		i++;
	}
}
/* select initialisieren */
function initialisieren_select(data) {
	var input = data.split('|');
	var i = 0;
	while (i<input.length) {
		$('#'+pageID+' select:eq('+i+') option[value=\''+input[i]+'\']').attr('selected', 'selected');;
		i++;
	}
}
/* checkboxes initialisieren */
function initialisieren_checkboxes(data) {
	var input = data.split('');
	var i = 0;
	while (i<input.length) {
		$('#'+pageID+' input:checkbox:eq('+i+')').attr('checked', (input[i]=="1") ? true : false);
		i++;
	}
}

/* textarea initialisieren */
function initialisieren_textarea(data) {
	var input = data.split('|');
	var i = 0;
	while (i<input.length) {
		$('#'+pageID+' textarea:eq('+i+')').val(input[i]);
		i++;
	}
}
/* img initialisieren */
function initialisieren_img(data) {
	var input = data.split('|');
	var i = 0;
	while (i<input.length) {
		$('#'+pageID+' .droparea:eq('+i+')').children('img').attr("src", input[i]);
		$('#'+pageID+' .draggable_image').children("img[src$='"+input[i]+"']").parent().hide();
		i++;
	}
}
/* feedback in blaues feld schreiben */
function setFeedback(f) {
	$("#feedback").html("<br /><br />");
	setTimeout(function(){$("#feedback").html(f);},200);
}

/* feedback in blaues feld schreiben */
function setFeedbacks(f, i) {
	$(".feedback:eq("+i+")").html("<br /><br />");
	setTimeout(function(){$(".feedback:eq("+i+")").html(f);},200);
}

/* benutzereingabe an server senden */
function saveUserinput(id, input, progress) {
	input = addslashes(input);
	$.get(saveUserinputUrl, { inputID: id, input: input, progress: progress, utf8: 1 }, function(data){
		return true;
	});	
}

/* taste "eingabe pruefen" einrichten */
function setup_taste() {
	// set up rollover
	$("img.taste").hover(
		function()
		{
			this.src = this.src.replace(".gif","_hl.gif");
		},
		function()
		{
			this.src = this.src.replace("_hl","");
		}
	);
	// set up button function	
	$("img.taste").click(function(e) {
		e.preventDefault();
		korrigieren();
	});
}

/* taste "neu starten" einrichten */
function setup_restart() {
	$(".restart").click(function(e) {
		e.preventDefault();
		restart();
	});
}

/* checkboxes als radiobuttons behandeln (ein klick auf eine checkbox deaktiviert alle anderen
   optional: groupname angeben, dann werden nur checkboxes mit dieser class beachtet */
function checkboxAsRadio(groupname) {
	var selector = "input:checkbox";
	if (groupname !== undefined ) selector = selector + "."+groupname;
	$(selector).click(function () {
		$(selector).attr('checked', false);
		$(this).attr('checked', true); 
    });
}

/* setup fuer draggable_inline */
function draggable_enable(element) {
	element.draggable("enable");
	element.hover(
		function () {
			$(this).css("color", "blue");
		}, 
  		function () {
   			 $(this).css("color", "black");
		}
	);
	element.css("color", "black");
}
function draggable_disable(element) {
	element.draggable("disable");
	element.unbind('mouseenter mouseleave');
	element.css("color", "blue");
}

/* html codes aus string entfernen */
String.prototype.stripHTML = function()
{
        // What a tag looks like
        var matchTag = /<(?:.|\s)*?>/g;
        // Replace the tag
        return this.replace(matchTag, "");
};

function html_entity_decode(str) {
  var ta=document.createElement("textarea");
  ta.innerHTML=str.replace(/</g,"&lt;").replace(/>/g,"&gt;");
  return ta.value;
}

function addslashes(str) {
	str=str.replace(/\\/g,'\\\\');
	str=str.replace(/\'/g,'\\\'');
	str=str.replace(/\"/g,'\\"');
	str=str.replace(/\0/g,'\\0');
	return str;
}

/* Image Preload */
  var cache = [];
  // Arguments are image paths relative to the current page.
  preLoadImages = function() {
    var args_len = arguments.length;
    for (var i = args_len; i--;) {
      var cacheImage = document.createElement('img');
      cacheImage.src = arguments[i];
      cache.push(cacheImage);
    }
  }

var adfontes_common_loaded = 1;
}