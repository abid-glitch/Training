function runFunction() {
  document.getElementById("output").innerHTML = document.getElementById("demo").firstChild.nodeValue;
  document.getElementById("output1").innerHTML = document.getElementById("demo").childNodes[0].nodeValue;
}
