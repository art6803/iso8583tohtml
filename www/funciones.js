 function resalta (id){
var hex = "hex"+id;
 var bin = "bin"+id;
 var num = "num"+id;
 var tex = "tex"+id;
 var lor = "lor"+id;
 var idc = "idc"+id;
 cambia(hex, "white", "yellow");
 cambia(bin, "white", "yellow");
 cambia(num, "white", "yellow");
 cambia(tex, "white", "yellow");
 cambia(lor, "white", "yellow");
 cambia(idc, "white", "yellow");
 cambia(hex+"a", "white", "yellow");
 cambia(bin+"a", "white", "yellow");
  };
 function normal (id){
var hex = "hex"+id;
 var bin = "bin"+id;
 var num = "num"+id;
 var tex = "tex"+id;
 var lor = "lor"+id;
 var idc = "idc"+id;
 cambia(hex, "yellow", "white");
 cambia(bin, "yellow", "white");
 cambia(num, "yellow", "white");
 cambia(tex, "yellow", "white");
 cambia(lor, "yellow", "white");
  cambia(idc, "yellow", "white");
  cambia(hex+"a", "yellow", "white");
 cambia(bin+"a", "yellow", "white");
 };
 function cambia (id, clase1, clase2){
if ( document.getElementById(id).classList.contains(clase1) ){
document.getElementById(id).classList.remove(clase1);
}
else{
document.getElementById(id).classList.add(clase2);
 };
 };