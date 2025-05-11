function hideModal(modalID) {
    if (modalID !== undefined) {
      var modal = document.getElementById(modalID);
      modal.style.display="none";
    }
}

function showModal(modalID) {
    if (modalID !== undefined) {
      var modal = document.getElementById(modalID);
      modal.style.display="block";
    }
}
function toggleHidden(elementID) {
    var element = document.getElementById(elementID);
    if (element.style.display === "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}

function toggleDisplay(elementID) {
  var element = document.getElementById(elementID);
  if (element.className.indexOf("w3-show") == -1) {
    element.className += " w3-show";
    element.className = element.className.replace(" w3-hide-medium", "");
    element.className = element.className.replace(" w3-hide-small", "");
  } else { 
    element.className = element.className.replace(" w3-show", "");
    element.className += " w3-hide-medium";
    element.className += " w3-hide-small";
  }
}

function copyText(field) {
  // Get the text field
  var text = document.getElementById(field);
  // Copy the text inside the text field
  navigator.clipboard.writeText(text.innerText);
  document.getElementById("modal-msg-div").style.display="block";
  document.getElementById("modal-body").innerHTML = "Copied to clipboard";
}