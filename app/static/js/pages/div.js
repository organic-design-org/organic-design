const sliders = ["divHeight", "divWidth", "divDetail", "divVar", "divCol", "divGradCol", "divShadowCol", "divBorderCol"];
sliders.forEach(element => {
    var elementID = document.getElementById(element);
    var outputTxt = element + 'Tag';
    var output = document.getElementById(outputTxt);
    output.innerHTML = elementID.value;
    elementID.oninput = function() {
        output.innerHTML = this.value;
      }
});