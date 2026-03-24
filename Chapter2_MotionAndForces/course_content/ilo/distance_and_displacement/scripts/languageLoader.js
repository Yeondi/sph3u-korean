//# A. Load the JSON data file and copy it into a JS object called `language`

//Define an object that the JSON data will be loaded into
var language = language || {};

(function () {

//A. Load the file
loadJsonFile("./data/english.json");


//A function to load the JSON file
function loadJsonFile(fileName) {

  //Create the XML request to load the JSON data
  let request = new XMLHttpRequest();
  request.open("GET", fileName, true);

  //What to do when the data loads, or fails to load
  request.onload = () => {
    if (request.status >= 200 && request.status < 400) {

      //Success, the file was loaded.
      //First, copy the JSON data into the JS `language` object
      language = JSON.parse(request.responseText);

      //Run a function that does whatever should happen when the data has loaded
      loadText(); 

    //If the data didn't load for some reason, display an error
    } else {
      throw new Error("There was some kind of error with the file");
    }
  };

  //What happens if the file can't be loaded
  request.onerror = () => {
    throw new Error("The file can't be loaded");
  };

  //Initiate the request to load the data
  request.send();
}

//# B. Copy the values from `language` object into the matching HTML tags

//When the data has loaded, this `loadText` function loops through all the 
//keys in the `language` object and copies their values into the `innerHTML` of 
//tags with matching id names 
function loadText() {

  //Find all the elements with `data-lang-id` attribute
  let elementNodeList = document.querySelectorAll('[data-lang-id]');

  //Loop through all the elements in the list
  if (elementNodeList) {
      Array.from(elementNodeList).forEach((element) => {

      //Use the `dataset.langId` to grab the matching key value from the `language` object
      let key = element.dataset.langId;
      let content = language[key];
      let fileString = ".md";

      if (content.indexOf(fileString) === -1) {
        element.innerHTML = content;
      } else {
  
        //Load the markdown file
        loadMarkdownFile(content, element);
      }
      

      //Set the `data-lang-processed` flag to `true` to show that the new html has been processed
      element.setAttribute("data-lang-processed", "true");
      
    });
  }
}

//C. If any content is appended with "markdownFile:", the associated file will be loaded
//into the element with the corresponding `data-lang-id` value

//A function to load the markdown file
function loadMarkdownFile(fileName, element) {

  //Create the XML request to load the JSON data
  let request = new XMLHttpRequest();
  request.open("GET", fileName, true);

  //What to do when the data loads, or fails to load
  request.onload = () => {
    if (request.status >= 200 && request.status < 400) {

      //Success, the file was loaded.
      //Parse the file as markdown text and copy it into the element's `innerHTML`
      element.innerHTML = marked(request.responseText);

    //If the data didn't load for some reason, display an error
    } else {
      throw new Error("There was some kind of error with the markdown file");
    }
  };

  //What happens if the file can't be loaded
  request.onerror = () => {
    throw new Error("The markdown file can't be loaded");
  };

  //Initiate the request to load the data
  request.send();
}

})();
