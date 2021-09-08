// add to every input the form-control class (no jquery)
function addFormControl() {
  var inputs = document.getElementsByTagName("input")
  for (var i = 0; i < inputs.length; i++) {
    if (
      inputs[i].getAttribute("type") != "radio" &&
      inputs[i].getAttribute("type") != "checkbox"
    ) {
      inputs[i].classList.add("form-control")
    }
  }
  var selects = document.getElementsByTagName("select")
  for (var i = 0; i < selects.length; i++) {
    selects[i].classList.add("form-control")
  }
  var textareas = document.getElementsByTagName("textarea")
  for (var i = 0; i < textareas.length; i++) {
    textareas[i].classList.add("form-control")
  }
}
document.addEventListener("DOMContentLoaded", addFormControl)
