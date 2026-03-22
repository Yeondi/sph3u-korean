//to see the graph inside accordion/tabs/show answer button after resizing the window by AP
$(window).resize(function () {
  $(".graphing-widget svg").css({
    width: "100%",
    height: "100%",
  });
});


(function () {
  $(document).ready(function () {
    setTimeout(() => {
      var script = document.createElement("script");
      script.src = "https://s.brightspace.com/lib/mathjax/3.1.2/tex-chtml.js";
      document.head.appendChild(script);
      MathJax.typeset();
       $('mjx-container').attr('tabindex', '-1');
      $('.graphing-widget:last-of-type').ready(function() {
       MathJax.typeset();
       $('mjx-container').attr('tabindex', '-1');
    });


      const mathElements = document.getElementsByTagName("math"); // getting math element
      var another_check = window.location.href;
      //   var in_brightspace = brightspace_check.includes("d2lSession"); // checkingif the srclink has d2lSession included or not. When in brightspace it will have that d2lSession in the src tag
      var in_ministry = another_check.includes("https"); // checkingif the srclink has d2lSession included or not. When in brightspace it will have that d2lSession in the src tag
      if (
        in_ministry === true &&
        parseFloat(
          window
            .getComputedStyle(mathElements[0], null)
            .getPropertyValue("font-size")
        ) /
        (parseFloat(
          window
            .getComputedStyle(document.getElementsByTagName("p")[0], null)
            .getPropertyValue("font-size")
        ) >
          0.9)
      ) {
        var style = document.createElement("style");
        style.type = "text/css";
        style.innerHTML =
          ".MathJax, mjx-container { font-size:130% !important}";
        document.getElementsByTagName("head")[0].appendChild(style);
      }
    }, 200);
  });
})();



