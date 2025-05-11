const sliders = ["divHeight", "divWidth", "divDetail", "divVar", "divCol"];
sliders.forEach(element => {
    var elementID = document.getElementById(element);
    var outputTxt = element + 'Tag';
    var output = document.getElementById(outputTxt);
    output.innerHTML = elementID.value;
    elementID.oninput = function() {
        output.innerHTML = this.value;
      }
});

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})
