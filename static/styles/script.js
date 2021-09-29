// function CopyURL() {
//   /* Get the text field */
//   var copyText = document.getElementById("myInput");

//   /* Select the text field */
//   copyText.select();
//   copyText.setSelectionRange(0, 99999); /* For mobile devices */

//    /* Copy the text inside the text field */
//   navigator.clipboard.writeText(copyText.value);

//   /* Alert the copied text */
//   alert("Copied the URL: " + copyText.value);
// }

function CopyURL() {
  var copyText = document.getElementById("myInput");
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(copyText.value);
  
  var tooltip = document.getElementById("myTooltip");
  tooltip.innerHTML = "URL copied";
}

function outFunc() {
  var tooltip = document.getElementById("myTooltip");
  tooltip.innerHTML = "Copy URL";
}