(() => {

  //Initialize variables
  let meters = [];
  let seconds = [];
  let answers = [
    { input: 0, correctAnswer: 1, isCorrect: false},
    { input: 0, correctAnswer: 2, isCorrect: false},
    { input: 0, correctAnswer: 3, isCorrect: false},
  ];

  //Populate the `meters` array
  let getMeterValues = () => {
    let arrayOfMeterValues = [];
    for (let i = 0; i <= 5; i++) {
      if (i === 0) {
        arrayOfMeterValues.push("y"); 
      } else {
        let numberBetweenOneAndTen = getRandomInt(1, 10);
        let numberBetween50And500 = numberBetweenOneAndTen * 50;
        arrayOfMeterValues.push(numberBetween50And500); 
      }
    }
    return arrayOfMeterValues;
  };
  meters = getMeterValues();
  
  //Populate the `seconds` array
  let getSecondsValues = () => {
    let arrayOfSecondsValues = [];
    for (let i = 0; i <= 1; i++) {
      let numberBetweenTenAndNinety = getRandomInt(1, 9) * 10;
      while (numberBetweenTenAndNinety === arrayOfSecondsValues[i - 1] ) {
        numberBetweenTenAndNinety = getRandomInt(1, 4) * 10;
      }
      arrayOfSecondsValues.push(numberBetweenTenAndNinety);
    }
    let sortedArray = arrayOfSecondsValues.sort();
    sortedArray.push(100);
    sortedArray.unshift(0);
    sortedArray.unshift("x");
    console.log(sortedArray); 
    return sortedArray;
  };
  seconds = getSecondsValues();

  //Calculate the answers based on the generated chart
  let calculateAnswers = (meters, seconds) => {
    let velocities = [];

    for (let i = 4; i > 1; i--) {
       let finalTime = seconds[i] - seconds[i - 1];
       let finalPosition = meters[i] - meters[i - 1];
       let velocity = finalPosition / finalTime;
       console.log(velocity);

       //Round down to two decimal places
       let roundedVelocity = parseFloat(velocity.toFixed(2));
       velocities.push(roundedVelocity);
    }

    velocities.reverse();

    answers.forEach((answer, index) => {
      answer.correctAnswer = velocities[index];
      console.log(`Velocity ${index}: ${answer.correctAnswer}`);
    });
  };
  calculateAnswers(meters, seconds);

  //Populate the select boxes
  let populateSelectBoxes = (answers) => {
    let selectBoxes = Array.from(document.querySelectorAll("select"));

    //Get an array of answers
    let answersArray = [];
    answers.forEach(answer => {
      answersArray.push(answer.correctAnswer);
    });

    //A function to shuffle and array
    let shuffle = a => {
      var j, x, i;
      for (i = a.length - 1; i > 0; i--) {
          j = Math.floor(Math.random() * (i + 1));
          x = a[i];
          a[i] = a[j];
          a[j] = x;
      }
      return a;
    };

    //Popuate the select boxes with shuffled answers
    selectBoxes.forEach(select => {

      //Shuffle the answers array
      let shuffledAnswersArray = shuffle(answersArray);

      //Remove any previous option elements that might have 
      //been added to the selection box
      while (select.firstChild) {
         select.removeChild(select.firstChild);
      }

      let element = document.createElement("option");
      element.textContent = "Select...";
      select.appendChild(element);

      //Add an option element for each element in the answers `shuffledAnswersArray` 
      for (let i = 0; i < shuffledAnswersArray.length; i++) {
        let option = shuffledAnswersArray[i];
        let element = document.createElement("option");
        element.textContent = option;
        element.value = option;
        select.appendChild(element);
      }
       
    });
  };
  populateSelectBoxes(answers);
  
  
  var chart = c3.generate({
    bindto: '#graph',
    data: {
        x: 'x',
        columns: [
          seconds,
          meters
        ]
    },
    tooltip: {
      show: false
    },
    size: {
      height: 250,
      width: 850
    },
    legend: {
      show: false
    },
    regions: [
        {start:0, end: seconds[2], class: "one"},
        {start: seconds[2], end: seconds[3], class: "two"},
        {start: seconds[3], end: seconds[4], class: "three"},
    ],
    axis: {
      x: {
          label: {
              text: 'Time (s)',
              position: 'outer-center'
          },
          max: 100,
          min: 0,
          tick: {
            values: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
          } 
      },
      y: {
          label: {
              text: 'Position (m)',
              position: 'outer-middle'
          },
          max: 500,
          min: 50,
      }
    },
    grid: {
      x: {
          show: true
      },
      y: {
          show: true
      }
  }
});

  //UI input
  let velocityOneInput = document.querySelector("#velocityOneInput"),
      velocityTwoInput = document.querySelector("#velocityTwoInput"),
      velocityThreeInput = document.querySelector("#velocityThreeInput");

  let anlayseInput = (inputFieldNumber, inputValue) => {
    let inputFieldObject = answers[inputFieldNumber]; 
    inputFieldObject.input = inputValue
    if (parseFloat(inputValue) === inputFieldObject.correctAnswer) {
      inputFieldObject.isCorrect = true;
    } else {
      inputFieldObject.isCorrect = false;
    }

    //Hide the result output and checkmarks if a new option is being selected
    let resultOutputs = Array.from(document.querySelectorAll(".resultOutput"));  
    let correctIcons = Array.from(document.querySelectorAll(".correctIcon"));
    let resultOutput = resultOutputs[inputFieldNumber];
    let correctIcon = correctIcons[inputFieldNumber];
    correctIcon.classList.add("hidden");
    resultOutput.innerHTML = ""; 



    console.log(`correctAnswer: ${inputFieldObject.correctAnswer}, inputValue: ${parseFloat(inputValue)}`)
  };
  velocityOneInput.addEventListener("change", (event) => {anlayseInput(0, event.target.value)});
  velocityTwoInput.addEventListener("change", (event) => {anlayseInput(1, event.target.value)});
  velocityThreeInput.addEventListener("change", (event) => {anlayseInput(2, event.target.value)});
  
  //Buttons
  //Check input button
  
  let checkResultsButton = document.querySelector("#checkResultsButton");
  let checkResultsButtonClickHandler = event => {
     let resultOutputs = Array.from(document.querySelectorAll(".resultOutput"));  
     let correctIcons = Array.from(document.querySelectorAll(".correctIcon"));  
     resultOutputs.forEach((resultOutput, index) => {
       let correctIcon = correctIcons[index];
     
       correctIcon.classList.remove("hidden");

       if (answers[index].input) {
        if(answers[index].isCorrect) {
          console.log("true")
          resultOutput.innerHTML = "That's correct";
          correctIcon.classList.add("glyphicon-ok");
          correctIcon.classList.add("correct");
          correctIcon.classList.remove("glyphicon-remove");
          correctIcon.classList.remove("incorrect");
        } else {
          console.log("false")
          resultOutput.innerHTML = "That's incorrect";
          correctIcon.classList.add("glyphicon-remove");
          correctIcon.classList.add("incorrect");
          correctIcon.classList.remove("glyphicon-ok");
          correctIcon.classList.remove("correct");
        }
      } else {
        resultOutput.innerHTML = ""; 
      }
     });
  }
  checkResultsButton.addEventListener("click", checkResultsButtonClickHandler);
  
  let resetUI = () => {

    //Reset the input fields
    let inputFields = document.querySelectorAll("input");
    inputFields.forEach((field, index) => {
      field.value = "";
      answers[index].input = 0;
    });

    //Reset the results display
    let resultOutputs = Array.from(document.querySelectorAll(".resultOutput"));  
    let correctIcons = Array.from(document.querySelectorAll(".correctIcon"));
    
    resultOutputs.forEach((resultOutput, index) => {
      let correctIcon = correctIcons[index];
      resultOutput.innerHTML = "";
      correctIcon.classList.add("hidden");
      correctIcon.classList.remove("glyphicon-ok");
      correctIcon.classList.remove("glyphicon-remove");


    });
  };

  let clearPreviousInput = answers => {
    answers.forEach(answer => {
      answer.input = 0;
    });
  };

  //Generate a new random chart
  let generateChartButton = document.querySelector("#generateChartButton");
  let generateChartButtonClickHandler = event => {
    
    //Generate new random values
    meters = getMeterValues();
    seconds = getSecondsValues();
    
    chart.load({
      columns: [
        seconds,
        meters
      ],
    });
    chart.regions([
      {start:0, end: seconds[2], class: "one"},
      {start: seconds[2], end: seconds[3], class: "two"},
      {start: seconds[3], end: seconds[4], class: "three"},
    ]);

    //Calculate answers
    calculateAnswers(meters, seconds);

    //Clear previous input
    clearPreviousInput(answers);

    //Populate the select boxes
    populateSelectBoxes(answers);

    //reset the UI
    resetUI();
  }
  generateChartButton.addEventListener("click", generateChartButtonClickHandler);

  
})();

//Helper functions
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

