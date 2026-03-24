(function () {

  //This code creates the instructions toggle drawer functionality

  //Get a reference to the toggleDrawer and instructionsContainer elements
  let drawerToggle = document.querySelector("#drawerToggle"),
      instructionsContainer = document.querySelector("#instructionsContainer"),
      toggleArrow = document.querySelector("#toggleArrow");

  //The initial toggle state
  var open = false;

  //The `pressHandler`
  var pressHandler = function(event){
    if (!open) {
      instructionsContainer.style.left = 300 + "px";
      open = true;
      toggleArrow.style.transform = "rotate(-180deg)";
    } else {
      instructionsContainer.style.left = "-" + 300 + "px";
      open = false;
      toggleArrow.style.transform = "rotate(0deg)";
    }
  };

  var keydownHandler = function(event){
    if (event.keyCode === 13) {
      pressHandler(event);
    }
  };

  //Set the `pressHandler` to trigger on a click or keydown event
  drawerToggle.addEventListener("click", pressHandler, false);
  drawerToggle.addEventListener("keydown", keydownHandler, false);
  //drawerToggle.addEventListener("touchstart", pressHandler, false);

})();