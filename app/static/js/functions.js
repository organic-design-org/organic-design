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
  } else { 
    element.className = element.className.replace(" w3-show", "");
  }
}