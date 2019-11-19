/* If you're feeling fancy you can add interactivity 
    to your site with Javascript */

// prints "hi" in the browser's dev tools console
document.getElementById("more-section").addEventListener("toggle", event => {
  let text;
  if (event.target.open) {
    text = "less about me";
  } else {
    text = "more about me";
  }
  document.getElementById("more-button").innerHTML = text;
});

// for debugging; comment out when not using
// document.getElementsByTagName("details")[0].open = true;