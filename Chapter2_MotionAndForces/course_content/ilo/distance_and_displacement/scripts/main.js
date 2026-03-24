//Create or use the `language` object that was created by the `languageLoader.js` file
var language = language || {};

(function () {

let thingsToLoad = [
  "images/smoke1.png",
  "images/smoke2.png",
  "images/smoke3.png",
  "images/wheel_20x20.png",
  "images/offRoadCar.png",
  "images/flag.png",
  "images/flagCanvas.png",
  "images/tallFlagPole.png",
  "images/rulerPadded_60m_zeroInMiddle_600x64.png",
  "images/rulerMarker.png",
  "images/distanceAndDisplacementBackground.png",
  "images/newWheel_20x20.png",
  "images/cloud1.png",
  "images/cloud2.png",
  "images/cloud3.png",
  "images/waypointMarker.png",
  "images/catHead.png",
  "images/catEyes.png",
  "images/eyesBackground.png",
  "images/catBody.png",
  "fonts/Bungee-Regular.ttf",
];


//Initialize Hexi with the `hexi` function. It has 5 arguments,
//although only the first 3 are required:
//a. Canvas width.
//b. Canvas height.
//c. The `setup` function.
//d. The `thingsToLoad` array you defined above. This is optional.
//e. The `load` function. This is also optional.
//If you skip the last two arguments, Hexi will skip the loading
//process and jump straight to the `setup` function.
let g = hexi(600, 500, setup, thingsToLoad);

//Add Hexi's canvas element to the `mainContainer` <div>
let mainContainer = document.querySelector("#mainContainer");
mainContainer.appendChild(g.canvas);

//Optionally Set the frames per second at which the game logic loop should run.
//(Sprites will be rendered independently, with interpolation, at full 60 or 120 fps)
//If you don't set the `fps`, Hexi will default to an fps of 60
g.fps = 60;

//Optionally add a border and set the background color
//g.border = "2px red dashed";
g.backgroundColor = 0x6ed8fb;

//Optionally scale and align the canvas inside the browser window
//g.scaleToWindow();


//Start Hexi. This is important - without this line of code, Hexi
//won't run!
g.start();

// module aliases 
var Engine = Matter.Engine,
    Render = Matter.Render,
    World = Matter.World,
    Bodies = Matter.Bodies,
    Body = Matter.Body,
    Composites = Matter.Composites,
    Composite = Matter.Composite,
    Constraint = Matter.Constraint,
    Svg = Matter.Svg;

//Declare any variables that need to be used in more than one function
var rightArrow, leftArrow, car, acceleration, phyicsSprites, startFlag, endFlag, flagPoints, ropeLength,
    ruler, carBodySprite, startX, endX, carStartX, carStartY, slowerButton, fasterButton, displacementLine,
    carPositionInput, flagPositionInput, timer, timeDisplayContainer, enterKey, speedChart, uniformMotion,
    smokeEmitter, positionChart, distanceBox, leftButton, rightButton, leftWheelSprite, rightWheelSprite,
    carPowerInputValue, waypointMarkers, cat, catEyes,
    moveCar = false,
    uniformMovement = true,
    frameCounter = 0,
    metersPerSecond = 0,
    carPowerBase = 0.06, //0.4 <- Use this value if you need to set the engine power,
    carPowerIncrement = 35,
    carPower = 5//carPowerBase,
    startStopCarPower = 0.06,
    acceleration = 0,
    accelerationLimit = 0.28,
    accelerate = false,
    maxCarSpeed = 0.6,
    gameSprites = [],
    activityFinished = false,
    motionType = "uniform",
    carX = 52,
    flagX = 300,
    carSpeedValues = [],
    carPositionValues = [],
    constantSpeedOn = false,
    nonUniformButtonPressed = false,
    carPositions = [],
    cloudSprites = [], 
    cloudSpeeds = [],
    cloudPositions = [],
    timeLimit = 20,
    direction = "right",
    carPowerInputNumber = 1,
    displacementX = 0,
    distanceTraveled = 0,
    resetDistanceTraveled = false,
    leftWheelOrigins = [],
    rightWheelOrigins = [],
    rightWallHit = false,
    leftWallHit = false,
    flagToTheRight = false,
    flagToTheLeft = false,
    rulerPaddingOffset = 50,
    rulerCalibration = 250;
    //waypointMarkers = [];

function setup(){

  // create an engine
  var engine = Engine.create({
    enableSleeping: true
  });

  //Hide Pixi's canvas and enable MatterJS's renderer
  //if you need to test the physics simulation
  /*
  g.renderer.view.style.display = "none";

  var render = Render.create({
        element: document.body,
        engine: engine,
        options: {
            width: 600,
            height: 500,
        }
    });

  Render.run(render);
  */
  
    
  let createWorld = () => {
 
    //Reset MatterJS and Hexi's sprites
    World.clear(engine.world);
    Engine.clear(engine);
    engine.events = {};
    g.stage.children = [];

    moveCar = false;

    //A 2D array to store all the physics bodies and sprites. This is convenient because we can then
    //loop through each pair to match the position and rotation of the sprite to the the physics body
    //inside the game loop (the play function)
    phyicsSprites = [];

    //Add keyboard events
    //Use the `keyboard` function to capture each of the 4 arrow keys, using their 
    //ASCII key code values
    //rightArrow = keyboard(39),
    //leftArrow = keyboard(37);
    //upArrow = keyboard(38),
    //downArrow = keyboard(40);
    //enterKey = keyboard(13);

    //Assign events to the `press` method of each arrow key
    /*
    enterKey.press = () => {
      console.log("right arrow pressed");
    };

    enterKey.release = () => {
      //console.log("left arrow pressed");
    };
    */

    //The car's starting angular velocity acceleration
    acceleration = 0;

    //Create the left and right walls
    var leftWall = Bodies.rectangle(-50, 250, 100, 500, { 
      isStatic: true 
    });
    var rightWall = Bodies.rectangle(650, 250, 100, 500, { 
      isStatic: true 
    });

    //Create the car 
    //Arguments: xPos, yPos, bodyLength, leftWheelRadius, rightWheelRadius
    carStartX = carX;
    carStartY = 385; 
    car = customCar(carStartX, carStartY, 32, 10, 10);

    //The ground

    //An array of vertices for the shape you want to create, starting at
    //the bottom left hand corner and working around clockwise
    /*
    var groundArray = [
        [0, 0,],
        [0, -34],
        [35, -54],
        [68, -40],
        [110, -80],
        [144, -80],
        [165, -69],
        [193, -100],
        [238, -100],
        [279, -54],
        [332, -45],
        [382, -73],
        [415, -73],
        [427, -86],
        [465, -93],
        [600, -82],
        [600, 0],
        [0, 0]
      ];
    */
    var groundArray = [
        [0, 0,],
        [0, -134],
        [600, -134],
        [600, 0],
        [0, 0]
      ];

    //customShape: x, y, width, height, verticesArray isStatic?
    var ground = customShape(300, 470, 600, 70, groundArray, true);

    /*
    // add mouse control
    var canvas = document.querySelector("canvas");
    var mouse = Matter.Mouse.create(canvas);
    var mouseConstraint = Matter.MouseConstraint.create(engine, {
        mouse: mouse,
        constraint: {
            stiffness: 0.1,
            render: {
                visible: false
            }
        }
    });

    


    // keep the mouse in sync with rendering
    //render.mouse = mouse;
    World.add(engine.world, mouseConstraint);
    */

    // add all of the bodies to the world
    World.add(engine.world, [leftWall, rightWall, car, ground]);

    // run the engine
    Engine.run(engine);

    // run the renderer
    //Render.run(render);

    //# B. Create the sprites

    //The background
    var background = g.sprite("images/distanceAndDisplacementBackground.png");
    background.layer = -1;

    //Add the cat

    let catHead = g.sprite("images/catHead.png");
    let eyesBackground = g.sprite("images/eyesBackground.png");
    let catBody = g.sprite("images/catBody.png")
    catEyes = g.sprite("images/catEyes.png");
    cat = g.group(catBody, eyesBackground, catEyes, catHead);
    cat.setScale(0.4, 0.4);
    cat.setPosition(280, 378);
    catEyes.startX = catEyes.x;

    //The waypoint markers group
    waypointMarkers = g.group();
    waypointMarkers.layer = 1;

    //The clouds
    cloudSpeeds = [0.05, 0.03, 0.01];
    cloudPositions = [
      {x: 425,y: 100 },
      {x: 75,y: 72 },
      {x: 275,y: 24 },
    ]

    for (let i = 0; i < 3; i++) {
      let cloudSprite = g.sprite(`images/cloud${i + 1}.png`, 32, 20);
      cloudSprite.x = cloudPositions[i].x;
      cloudSprite.y = cloudPositions[i].y;
      cloudSprites.push(cloudSprite);
    }

    //The ground
    /*
    var groundSprite = spriteFromArray(groundArray, 0x669900);
    //groundSprite.setPivot(0.38, 0.68);
    groundSprite.setPivot(0.5, 0.5);
    phyicsSprites.push([ground, groundSprite]);
    */

    //The end Flag
    endFlag = tallFlagSprite("images/flagCanvas.png", "images/tallFlagPole.png");
    endFlag.flagContainer.x = flagX + 250;
    endFlag.flagContainer.y = 327;
    endFlag.flagContainer.scaleX = 0.8;
    endFlag.flagContainer.scaleY = 0.8;

    //The start flag
    startFlag = tallFlagSprite("images/greenFlagCanvas.png", "images/tallFlagPole.png");
    startFlag.flagContainer.x = car.bodies[0].position.x;
    startFlag.flagContainer.y = 327;
    startFlag.flagContainer.scaleX = 0.8;
    startFlag.flagContainer.scaleY = 0.8;


    //Car body
    carBodySprite = g.sprite("images/offRoadCar.png", 32, 20);
    carBodySprite.setPivot(0.5, 0.63);
    carBodySprite.setPosition(carX, 385);
    carBodySprite.vx = 0;
    //phyicsSprites.push([car.bodies[0], carBodySprite]);

    //Wheels
    leftWheelSprite = g.sprite("images/newWheel_20x20.png", 20, 20);
    leftWheelSprite.setPivot(0.5, 0.5);
    carBodySprite.add(leftWheelSprite);
    leftWheelSprite.setPosition(13, 10);
    //phyicsSprites.push([car.bodies[1], leftWheelSprite]);

    rightWheelSprite = g.sprite("images/newWheel_20x20.png", 20, 20);
    rightWheelSprite.setPivot(0.5, 0.5);
    carBodySprite.add(rightWheelSprite);
    rightWheelSprite.setPosition(-13, 10);
    //phyicsSprites.push([car.bodies[2], rightWheelSprite]);

    //The displacement line
    displacementLine = createDisplacementLine("red", 2, carBodySprite, startFlag.flagContainer, "images/rulerMarker.png");

    //The distance box
    distanceBox = createDistanceBox(carBodySprite, "images/rulerMarker.png");
    distanceBox.container.y = 412;
  

    //freeBodyDiagram: sprite, orientation, padding, physicsProperty, label
    freeBodyDiagram(carBodySprite, "horizontal", -73, "velocity", "velocity x");
    freeBodyDiagram(carBodySprite, "vertical", -70, "velocity", "velocity y");
    //carBodySprite.displayForceBodyDiagrams = true;

    //Ruler
    ruler = rulerSprite("images/rulerPadded_60m_zeroInMiddle_600x64.png", "images/rulerMarker.png", carBodySprite, 0, 0, 436); 

    //Timer
    timer = createTimer();

  };

  createWorld();


  //Create the smoke emitter
  smokeEmitter = createSmokeEmitter(carPowerInputNumber, direction);

  //Make the particle stream start playing
  //smokeEmitter.play();

  //# C. UI elements
  let uniformGoButton = document.querySelector("#uniformGoButton"),
      nonUniformGoButton = document.querySelector("#nonUniformGoButton"),
      startStopButton = document.querySelector("#startStopButton");

  leftButton = document.querySelector("#leftButton");
  rightButton = document.querySelector("#rightButton");
  carPositionInput = document.querySelector("#carPositionInput");
  flagPositionInput = document.querySelector("#flagPositionInput");
  carPowerInput = document.querySelector("#carPowerInput");
  
  //Get a reference to the timeDisplay container and activityResult
  timeDisplayContainer = document.querySelector("#timeDisplayContainer");
  activityResultContainer = document.querySelector("#activityResultContainer");

  //Add all the UI elements into an array so that we can easily disable/enable them
  let uiElements = [
    //uniformGoButton,
    //nonUniformGoButton,
    carPositionInput,
    //flagPositionInput,
    carPowerInput,
  ];

  //A function to disable all the ui elements
  let disableUi = () => uiElements.forEach(element => element.disabled = true);

  //A function to enable all the ui elements
  let enableUi = () => uiElements.forEach(element => element.disabled = false);

  uniformMotion = (element, carPower, toggleOnText, toggleOffText) => {
    console.log("uniformMotion")
    //if (!activityFinished) {
      uniformMovement = true;
      moveCar = true;
      disableUi();
      //nonUniformGoButton.disabled = true;
      timer.running = true;
      speedChartContainer.style.opacity = 1;
      positionChartContainer.style.opacity = 1;
      motionType = "uniform";

      //Toggle the constant speed
      if (!constantSpeedOn) {
        constantSpeedOn = true;
        element.innerHTML = toggleOnText;
        element.style.backgroundColor = "#DEEDDF";

        if (Math.abs(carBodySprite.rotation) < 1) {
          smokeEmitter.play();
        }
      } else {
        constantSpeedOn = false;
        element.innerHTML = toggleOffText;
        element.style.backgroundColor = "#D4DADC";

        //add some natural looking deceleration when constant power is turned off
        acceleration = carPower + acceleration;

        //Make the car stop
        moveCar = false;

        //Stop the smoke emitter
        smokeEmitter.stop();
      }
    //}
  };

  //The uniformGoButton
  let uniformGoButtonHandler = event => {

    //Get a reference to the button
    let element = event.target;
    uniformMotion(element, carPower, language.uniformGoButtonTextOn, language.uniformGoButtonTextOff);
  };
  uniformGoButton.addEventListener("click", uniformGoButtonHandler);
  uniformGoButton.addEventListener("touchstart", uniformGoButtonHandler);

  //The startStop button
  let startStopButtonHandler = event => {

    //Get a reference to the button
    let element = event.target;
    uniformMotion(element, carPower, language.startStopButtonTextOff, language.startStopButtonTextOn);
  };
  startStopButton.addEventListener("click", startStopButtonHandler);
  //startStopButton.addEventListener("touchstart", startStopButtonHandler);


  //The non-uniform buttons
  let accelerateHandler = event => {
    //Get a reference to the button
    let element = event.target;

    if (!activityFinished) {
      uniformMovement = false;
      moveCar = true;
      //accelerate = true;
      disableUi();
      //uniformGoButton.disabled = true;
      timer.running = true;
      speedChartContainer.style.opacity = 1;
      positionChartContainer.style.opacity = 1;
      motionType = "nonuniform";

      if (!accelerate) {
        accelerate = true;
        element.style.backgroundColor = "#DEEDDF";
        nonUniformButtonPressed = true;
        element.innerHTML = language.nonUniformGoButtonTextOn;
        if (Math.abs(carBodySprite.rotation) < 1) {
          smokeEmitter.play();
        }
      } else {
        accelerate = false;
        element.style.backgroundColor = "#D4DADC";
        element.innerHTML = language.nonUniformGoButtonTextOff;
        if (!constantSpeedOn) {
          smokeEmitter.stop();
        }
      }
    }
  };
  nonUniformGoButton.addEventListener("click", accelerateHandler);
  //nonUniformGoButton.addEventListener("touchstart", accelerateHandler);

  /*
  let deccelerateHandler = event => {

    //Get a reference to the button
    let element = event.target;

    uniformMovement = false;
    moveCar = true;
    accelerate = false;
    element.style.backgroundColor = "#D4DADC";
    if (!constantSpeedOn) {
      smokeEmitter.stop();
    }
  };
  nonUniformGoButton.addEventListener("mouseup", deccelerateHandler);
  nonUniformGoButton.addEventListener("touchend", deccelerateHandler);
  */

  //The car position input
  let carPositionInputHandler = event => {

    //Find the value by which to update the car's position
    let inputX = event.target.value * 10;
    //let newCarX = Math.floor(-(carBodySprite.x - inputX));
    //let newCarX = Math.floor(-(carBodySprite.x - inputX)) + rulerPaddingOffset + 2;

    //Set the new car start X
    carStartX = inputX + rulerPaddingOffset + rulerCalibration + 2;

    //Move the car to the new position if it's to the left of the flag
    //if (carBodySprite.x + newCarX < endFlag.flagContainer.x - 24) {
      //Composite.translate(car, { x: newCarX, y: 0 });
    //}

    //Position the car
    carBodySprite.x = carStartX;

    //Position the start flag
    startFlag.flagContainer.x = inputX + rulerPaddingOffset + rulerCalibration + 2; 


    //Display the value in the carPositionOutput
    let carPositionOutput = document.querySelector("#carPositionOutput");
    carPositionOutput.innerHTML = event.target.value;

    //Set distanceTraveled to 0
    resetDistanceTraveled = true;

  };
  carPositionInput.addEventListener("input", carPositionInputHandler);

  //The flag position input
  let flagPositionInputHandler = event => {

    //Find the value by which to update the car's position
    //let inputX = Math.floor(event.target.value * 10);
    let inputX = Math.round(event.target.value * 10) + rulerPaddingOffset + rulerCalibration;

    //Move the flag to the new position if it's to the left of the flag
    //if (inputX > carBodySprite.x + 24 - rulerPaddingOffset) {
      endFlag.flagContainer.x = inputX;
    //} 

    //Display the value in the carPositionOutput
    let flagPositionOutput = document.querySelector("#flagPositionOutput");
    flagPositionOutput.innerHTML = Math.round(event.target.value);
  };
  flagPositionInput.addEventListener("input", flagPositionInputHandler);

  //The car's power
  let carPowerInputHandler = event => {
    carPowerOutput.innerHTML = Math.floor(event.target.value);
    let extraPower = event.target.value / carPowerIncrement;
    carPower = carPowerBase + extraPower;
    carPowerInputNumber = event.target.value;
    smokeEmitter = createSmokeEmitter(carPowerInputNumber, direction);
  };
  carPowerInput.addEventListener("input", carPowerInputHandler); 

  //The left button
  let leftButtonHandler = event => {

    //Get a reference to the button
    let element = event.target;
 
    //Set the new direction
    let newDirection = "left";
    if (newDirection !== direction) {

      //Set the global direction
      direction = "left";

      //Change the car's direction
      changeCarDirection(direction);
    }

    //Change the background colour
    element.style.backgroundColor = "#DEEDDF";
    rightButton.style.backgroundColor = "#D4DADC";
  };
  leftButton.addEventListener("click", leftButtonHandler); 
  //leftButton.addEventListener("touchstart", leftButtonHandler); 


  //The right button
  let rightButtonHandler = event => {
    
    //Get a reference to the button
    let element = event.target;

    //Set the new direction
    let newDirection = "right";
    if (newDirection !== direction) {

      //Set the global direction
      direction = "right";

      //Change the car's direction
      changeCarDirection(direction);
    }

    //Change the background colour
    element.style.backgroundColor = "#DEEDDF";
    leftButton.style.backgroundColor = "#D4DADC";
  };
  rightButton.addEventListener("click", rightButtonHandler); 
  //rightButton.addEventListener("touchstart", rightButtonHandler);

  //Set the background color of button that sets the car's direction
  //to the currently active one
  if (direction === "left") {
    leftButton.style.backgroundColor = "#DEEDDF";
    rightButton.style.backgroundColor = "#D4DADC";
  } else {
    rightButton.style.backgroundColor = "#DEEDDF";
    leftButton.style.backgroundColor = "#D4DADC";
  }

  //The reset button
  let resetButton = document.querySelector("#resetButton");
  let resetButtonHandler = event => {

    //Reset the car's position and rotation
    /*
    let originX = -(carBodySprite.x - carStartX),
        originY = -(carBodySprite.y - carStartY);

    //Reset the start flag's position
    startFlag.flagContainer.x = carStartX;

    Composite.translate(car, { x: originX, y: originY });
    Composite.rotate(car, -carBodySprite.rotation, { x: carStartX, y: carStartY });
    */

    carBodySprite.x = carStartX;
    carBodySprite.y = carStartY;

    //Stop the wheels moving
    moveCar = false;

    /* 
    let carBody = car.bodies[0];
        leftWheel = car.bodies[1],
        rightWheel = car.bodies[2];

    Body.setAngularVelocity(leftWheel, 0);
    Body.setAngularVelocity(rightWheel, 0);

    Body.setVelocity(carBody, {x: 0, y:0});
    Body.setVelocity(leftWheel, {x: 0, y:0});
    Body.setVelocity(rightWheel, {x: 0, y:0});
    */
    carBodySprite.vx = 0;

    //Body.setStatic(carBody, true);
    //Body.setStatic(leftWheel, true);
    //Body.setStatic(rightWheel, true);

    //Body.setInertia(car.bodies[1], Infinity);
    //Body.setInertia(car.bodies[2], Infinity);

    //Reset the acceleration
    acceleration = 0;
    
    //Turn off acceleration
    accelerate = false;
    
    //Reset the activity display
    activityFinished = false;

    //Enable the ui
    enableUi();

    //Reset the buttons
    uniformGoButton.disabled = false;
    nonUniformGoButton.disabled = false;
    uniformGoButton.innerHTML = language.uniformGoButtonTextOff;
    nonUniformGoButton.innerHTML = language.nonUniformGoButtonTextOff;
    uniformGoButton.style.backgroundColor = "#D4DADC";
    nonUniformGoButton.style.backgroundColor = "#D4DADC";
    startStopButton.innerHTML = language.startStopButtonTextOn;
    startStopButton.style.backgroundColor = "#D4DADC";

    //Disable the timer
    timer.running = false;
    timer.reset();

    //Reset the graphs
    carSpeedValues = [language.carGraphLegend];
    carPositionValues = [language.carGraphLegend];

    //Disable the charts
    speedChartContainer.style.opacity = 0;
    positionChartContainer.style.opacity = 0;

    //Remove the timestampTableRows that might have been dynamically
    //added to the table
    [].forEach.call(document.querySelectorAll('.timestampTableRow'), function(e){
      e.parentNode.removeChild(e);
    });

    //Reset the constant speed
    constantSpeedOn = false;

    //Flag that the acceleration button hasn't been pushed yet
    nonUniformButtonPressed = false;

    //Reset the car positions
    carPositions = [];
    
    //Reset the car's direction so that if faces right
    if (direction === "left") changeCarDirection("right");

    //Reset the direction to the right
    direction = "right";

    //Reset the left and right button styles
    rightButton.style.backgroundColor = "#DEEDDF";
    leftButton.style.backgroundColor = "#D4DADC";

    //Stop the smoke emitter
    smokeEmitter.stop();

    //Reset the distance traveled
    distanceTraveled = 0;
    resetDistanceTraveled = true;

    //Remove the waypoint markers
    waypointMarkers.children = [];

  };
  resetButton.addEventListener("click", resetButtonHandler);
  //resetButton.addEventListener("touchstart", resetButtonHandler);



  //# D. The chart

  //Create the chart
  //For formating numbers see: https://github.com/c3js/c3/issues/366

  //Set the first value in the `carSpeedValues` array to a string
  //which identifies which object this graph is tracking
  carSpeedValues = [language.carGraphLegend];

  //Generate the charts

/*  //Speed Vs. Time
  speedChart = c3.generate({
    bindto: '#speedChart',
    padding: {
        right: 5,
        bottom: 5
    },
    data: {
      columns: [carSpeedValues],
    },
    tooltip: {
        show: false
    },

    //Switch on the legend feature here
    legend: {
      show: false
    },
    axis: {
      y: {
        label: { // ADD
          text: language.yGraphLabelText,
          position: 'outer-middle'
        },
        tick: {
            format: d3.format('.1f')
        },
        max: 18,
        min: 1   
      },
      x: {
        show: true,
        label: { // ADD
          text: language.xGraphLabelText,
          position: 'outer-center'
        }
      }
    }
  });

  //Position Vs. Time
  carPositionValues = [language.carGraphLegend];
  positionChart = c3.generate({
    bindto: '#positionChart',
    padding: {
        right: 5,
        bottom: 5
    },
    data: {
      columns: [carPositionValues],
    },
    tooltip: {
        show: false
    },

    //Switch on the legend feature here
    legend: {
      show: false
    },
    axis: {
      y: {
        label: { // ADD
          text: language.yPositionGraphLabelText,
          position: 'outer-middle'
        },
        tick: {
            format: d3.format('.1f')
        },
        max: 61,
        min: 1   
      },
      x: {
        show: true,
        label: { // ADD
          text: language.xPositionGraphLabelText,
          position: 'outer-center'
        }
      }
    }
  });
*/  /*
  //The graphingButton
  
  let graphingButton = document.querySelector("#graphingButton");
  let graphing = false;

  let toggleGraphing = event => {
    if (!graphing) {
      startGraphing();
      graphingButton.innerHTML = language.stopGraphingButtonText;
      graphingButton.style.backgroundColor = "#f5cedb";
      graphing = true;
    } else {
      stopGraphing();
      graphingButton.innerHTML = language.startGraphingButtonText;
      graphingButton.style.backgroundColor = "#DEEDDF";
      graphing = false;
    }
  };
  graphingButton.addEventListener("click", toggleGraphing, false);
  graphingButton.addEventListener("touchstart", toggleGraphing, false);
  */
  //Set the game state to play. This is very important! Whatever
  //function you assign to Hexi's `state` property will be run by
  //Hexi in a loop.
  g.state = play;
  //play();
}


/*
4. The game logic
------------------
*/

//The `play` function is called in a continuous loop, at whatever fps
//(frames per second) value you set. This is your *game logic loop*. (The
//render loop will be run by Hexi in the background at the maximum fps
//your system can handle.) You can pause Hexi's game loop at any time
//with the `pause` method, and restart it with the `resume` method

function play() {


  //The car is a composite object made up of three parts: the body, the left wheel and the right wheel.
  //You can access them like this:
  var carBody = car.bodies[0],
      leftWheel = car.bodies[1],
      rightWheel = car.bodies[2];

  //console.log(carBody.velocity.x);
  //Body.setStatic(carBody, false);
  //Display the cart's velocity in the html output element:
  //output.innerHTML = "carBody.velocity.x: " + carBody.velocity.x;
  //if (moveCar && !activityFinished) {
  if (moveCar) {
      /*
      if (accelerate) {
        if (Math.abs(acceleration) < accelerationLimit) {
          acceleration += carPower / 50;
        }
        
      } else {
        acceleration *= 0.96;
      }
      //if (acceleration < 0.001) acceleration = 0;
      if (constantSpeedOn) {
        Body.setAngularVelocity(leftWheel, carPower + acceleration);
        Body.setAngularVelocity(rightWheel, carPower + acceleration);
      } else {
        Body.setAngularVelocity(leftWheel, acceleration);
        Body.setAngularVelocity(rightWheel, acceleration);
      }
      */
      /*
      if (leftWheel.angularVelocity < 0.001) {
        Body.setAngularVelocity(leftWheel, 0);
        Body.setAngularVelocity(rightWheel, 0);
      } 
      */
      let enginePower = (0.166666666666667) * carPower;
      carBodySprite.vx = enginePower;

  } else {

    //Stop the smoke emitter
    smokeEmitter.stop();

    //Stop the car
    //Slow it down
    //carBodySprite.vx *= 0.92;
    //Complete stop
    carBodySprite.vx = 0;


    //Stop the car completely
    /*
    Body.setAngularVelocity(leftWheel, 0);
    Body.setAngularVelocity(rightWheel, 0);
    Body.setVelocity(carBody, {x: 0, y:0});
    */


  }

  //Use the velocity to move the car and rotate the wheels
  carBodySprite.x += carBodySprite.vx;
  if (direction === "right") {
    leftWheelSprite.rotation += carBodySprite.vx / 6.28;
    rightWheelSprite.rotation += carBodySprite.vx / 6.28;
  } else {
    leftWheelSprite.rotation -= carBodySprite.vx / 6.28;
    rightWheelSprite.rotation -= carBodySprite.vx / 6.28;
  }
  /*    
      console.log(Math.abs(carBody.velocity.x));
    if (carBody.velocity.x < Math.abs(0.03)) {
        console.log("true");
      } else {
        console.log("false");
      }

  */

  //Bring car to a complete stop if it's velocity falls below a certain threshold.
  //(This is to prevent slight position drift due to rounding errors at very low velocities)
  if (!accelerate && !constantSpeedOn) {
    if (Math.abs(carBody.velocity.x) < 0.03) {
    //if (leftWheel.angularVelocity < Math.abs(0.001)) {
      Body.setVelocity(carBody, {x: 0, y:0});
      Body.setVelocity(leftWheel, {x: 0, y:0});
      Body.setVelocity(rightWheel, {x: 0, y:0});
      Body.setAngularVelocity(leftWheel, 0);
      Body.setAngularVelocity(rightWheel, 0);
    }
  }
  

  //Update the flags
  endFlag.update();
  startFlag.update();

  //Update the ruler
  ruler.update();

  //Update all the physics sprites so that they match the positions and
  //rotations of the bodies
  phyicsSprites.forEach(element => {

    //Get a reference to the physics body and the sprite
    let body = element[0];
    let sprite = element[1];
     
    sprite.x = body.position.x;
    sprite.y = body.position.y;
    sprite.rotation = body.angle;
    //sprite.scale.x = body.scaleX;
    //sprite.scale.y = body.scaleY;

    //Update each sprite's force body diagram, if it exists
    if(sprite.freeBodyDiagrams) {
      renderFreeBodyDiagrams(sprite, body);
    }

    //sprite.oldX = tempX;
    //sprite.oldY = tempY;
  });

  //Check for a collision between the flag and the car
  //if (!activityFinished && moveCar) {
  if (moveCar) {
    if ((direction === "right" && carBodySprite.x > endFlag.flagContainer.x && flagToTheRight)
    || (direction === "left" && carBodySprite.x < endFlag.flagContainer.x && flagToTheLeft)) {

      //Display the finish sign
      //endFlag.displayFinish();
      moveCar = false;
      //activityFinished = true;
      timer.running = false;
      let startStopButton = document.querySelector("#startStopButton");
      uniformMotion(uniformGoButton, carPower, language.startStopButtonTextOff, language.startStopButtonTextOn);
      startStopButton.innerHTML = language.startStopButtonTextOn;
      startStopButton.style.backgroundColor = "#D4DADC";

      //Set the car to the destination point
      carBodySprite.x = endFlag.flagContainer.x;

      //Create a waypoint marker, if there currently less than 10
      //(10 is the maximum number there can be)
      if (waypointMarkers.children.length < 10) createWaypointMarker(endFlag.flagContainer.x);

    } else {
      endFlag.collisionOccured = false;
    }
  }

  flagToTheRight = carBodySprite.x < endFlag.flagContainer.x;
  flagToTheLeft = carBodySprite.x > endFlag.flagContainer.x;

  //Move the cat's eyes
  catEyes.x = -(catEyes.startX - ((carBodySprite.x - cat.x) / 40));

  //Bounce the car against the left and right walls
  if (carBodySprite.x >= 575 && direction === "right") {
       direction = "left";
       rightWallHit == true;
       changeCarDirection(direction);
       leftButton.style.backgroundColor = "#DEEDDF";
       rightButton.style.backgroundColor = "#D4DADC";

  }
  if (carBodySprite.x <= 25 && direction === "left") {
       direction = "right";
       leftWallHit = true;
       changeCarDirection(direction);
       rightButton.style.backgroundColor = "#DEEDDF";
       leftButton.style.backgroundColor = "#D4DADC";
  }


  //Figure out the car's speed in meters/second
  frameCounter += 1; 
  if (frameCounter === 1) {
    //startX = carBodySprite.x;

    
  }
  if (frameCounter === 60) {
    /*
    endX = carBodySprite.x;
    metersPerSecond = ((endX - startX) / 10).toFixed(1);
    if (metersPerSecond < 0.1) {
      metersPerSecond = 0; 
    }
    */
    frameCounter = 0;
  }

  //Capture the timer's current `seconds` value so that we can use it
  //further ahead in the code to update the timestamp 
  let previousSecond = timer.seconds;

  //Update the timer
  if (timer.running && timer.seconds < timeLimit) {
    timer.update();
  }
 
  //Update the speed graph

  if (previousSecond !== timer.seconds 
  || timer.time === 1
  && timer.running) {

    //Capture the car's current position
    carPositions.push((carBodySprite.x / 10).toFixed(1));

    //Update the meters per second
    if (timer.time !== 1) {
      metersPerSecond = carPositions[timer.seconds] - carPositions[timer.seconds - 1];
    } else {
      metersPerSecond = 0;
    }

    let newValue;
    //Prepare a cheat for uniform motion
      if (motionType !== "uniform") {
        newValue = metersPerSecond//Math.floor(metersPerSecond);
      } else {
        if (timer.seconds < 2) {
          newValue = 0;
        } else {
          newValue = metersPerSecond //Math.floor(metersPerSecond);
        }
      }

    //Add cheat for uniform motion to make the first value the same
    //as the other values 
    //Update the first uniform motion speed with the new value from second 2
    if (motionType === "uniform" && timer.seconds === 2) {
      carSpeedValues[1] = newValue;
      carSpeedValues[2] = newValue;
    }
    if (motionType === "uniform" && timer.seconds > 2 && constantSpeedOn) {
      if (newValue !== carSpeedValues[timer.seconds - 1]) {
        newValue = carSpeedValues[timer.seconds];
      }
    }
    
    carSpeedValues.push(newValue);

    //console.log(`Time: ${timer.time} metersPerSecond: ${metersPerSecond} carSpeedValues: ${carSpeedValues}`)
    // speedChart.load({
    //     columns: [
    //         carSpeedValues
    //     ]
    // });

  }

  //Update the position graph
  if (previousSecond !== timer.seconds 
  || timer.time === 1
  && timer.running) {

    let newValue;
    /*
    //Prepare a cheat for uniform motion
      if (motionType !== "uniform") {
        newValue = Math.floor(metersPerSecond);
      } else {
        if (timer.seconds < 2) {
          newValue = 0;
        } else {
          newValue = Math.floor(metersPerSecond);
        }
      }

    //Add cheat for uniform motion to make the first value the same
    //as the other values 
    //Update the first uniform motion speed with the new value from second 2
    if (motionType === "uniform" && timer.seconds === 2) {
      carSpeedValues[1] = Math.floor(newValue);
      carSpeedValues[2] = Math.floor(newValue);
    }
    */
    //newValue = Math.floor(carBodySprite.x / 10);
    newValue = carBodySprite.x / 10;
    carPositionValues.push(newValue);
    //console.log(`Time: ${timer.time} metersPerSecond: ${metersPerSecond} carSpeedValues: ${carSpeedValues}`)
    // positionChart.load({
    //     columns: [
    //         carPositionValues
    //     ]
    // });

  }

  //Stop the timer when it reaches 10 second
  if (timer.seconds === timeLimit) {
    timer.running = false;
  }

  //Update the cloud sprites
  cloudSprites.forEach((sprite, index) => {

    //Move the cloud
    sprite.x -= cloudSpeeds[index];

    //Wrap the cloud to the other side of the stage if it has completely disappeared
    if (sprite.x < 0 - sprite.width) {
      sprite.alpha = 0;
      sprite.x = 650;
    }
    if (sprite.x <= 600) {
      sprite.alpha = 1;
    }

  });

  //Calculate the displacement
  if (!activityFinished) {
    displacementX = Math.round((carBodySprite.x - startFlag.flagContainer.x) /10);

    //Fudge the displacement value to force zero so that it doesn't display -1 or 1 when the 
    //reset button is pressed
    //if (Math.abs(displacementX) === 1) displacementX = 0;

    //Calculate the distance traveled 
    let differenceBetweenThisFrameAndLastFrameX = Math.abs(carBodySprite.x - carBodySprite._previousX);

    //The reset button sets `resetDistanceTraveled` to `true` so that we can set the 
    //`distanceTraveled` variable to 0 when the car is repositioned
    if (!resetDistanceTraveled) {
      distanceTraveled += differenceBetweenThisFrameAndLastFrameX / 10;
    } else {
      distanceTraveled = 0;
      resetDistanceTraveled = false;
    }

    //Update the displacement line
    displacementLine.update();
    displacementLine.displacementText.content = `${language.displacementText} ${displacementX}`;

    //Update the distance box
    distanceBox.update();
    distanceBox.distanceText.content = `${language.distanceText} ${Math.round(distanceTraveled)}`;
  }



  //Update the UI

  //Prevent the carPositionInput slider from having a maximum value that's
  //greater than 24 pixels left of the flag's position.
  //if (!carPositionInput.disabled) carPositionInput.setAttribute("max", (endFlag.flagContainer.x - 24) / 10);

  //Prevent the flag from being moved beyond the right edge of the car's position
  //if (!flagPositionInput.disabled) flagPositionInput.setAttribute("min", Math.floor(carBodySprite.x + 24) / 10);

  //Display the timer output
  let timerOutput = document.querySelector("#timeOutput");
  timerOutput.innerHTML = timer.formattedOutput();
  

}

function renderFreeBodyDiagrams(sprite, body) {

  
  sprite.freeBodyDiagrams.forEach(diagram => {

    if (sprite.displayForceBodyDiagrams) {
      diagram.arrow.visible = true;
      diagram.label.visible = true;

      if (diagram.orientation === "horizontal") {
        diagram.arrow.scaleX = body[diagram.physicsProperty].x;
        diagram.label.x = sprite.x + diagram.padding;
        diagram.label.y = sprite.y - 15;
        diagram.arrow.x = sprite.x;
        diagram.arrow.y = sprite.y;
      } else {
        diagram.arrow.scaleY = body[diagram.physicsProperty].y;
        diagram.label.y = sprite.y + diagram.padding;
        diagram.label.x = sprite.x - 0;
        diagram.arrow.x = sprite.x - 7;
        diagram.arrow.y = sprite.y + 5;
      }

    } else {
      diagram.arrow.visible = false;
      diagram.label.visible = false;
    }
    
  });
  
  
}


/* Helper functions*/

//The waypoint markers
function createWaypointMarker(xPosition) {
  let waypointMarker = g.sprite("images/waypointMarker.png");
  waypointMarker.setPosition(xPosition - 9, 240);
  //waypointMarkers.push(waypointMarker);
  waypointMarkers.add(waypointMarker);

  //Letters to be used as waypoint identifiers
  let letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"];
  let letter = letters[waypointMarkers.children.length - 1];
  let labelText = letter;

  //Create the waypoint label
  let label = g.text(labelText, "12px Arial", "red");
  waypointMarker.addChild(label);
  label.setPosition(9, -13);

  //Create the distance text
  let distance = (xPosition - rulerPaddingOffset - rulerCalibration) / 10;
  let distanceText = g.text(distance, "12px Arial", "black");
  waypointMarker.addChild(distanceText);
  distanceText.y = 10;

  //Tweak the positioning of the distance text so that all possible numbers
  //appear correctly centered
  if (distance > 9) distanceText.x = 6;
  if (distance < 10 && distance > -1) distanceText.x = 10;
  if (distance <= -1 && distance > -10) distanceText.x = 8;
  if (distance < -9) distanceText.x = 4;
}

function createDistanceBox(spriteTofollow, markerImage) {

  let o = {};

  //The marker text
  o.distanceText = g.text(language.distanceText, "12px Arial", "black");

  //Add a rounded rectangle
  let graphics = new PIXI.Graphics();
  graphics.beginFill(0xE5E9EA, 1);
  graphics.drawRoundedRect(0, 0, 100, 20, 10);
  graphics.endFill();
  let texture = graphics.generateTexture();
  let rectangleSprite = g.sprite(texture);
  let rectangleContainer = g.group(rectangleSprite);

  //Add the displacement text to the rectangle container
  rectangleContainer.add(o.distanceText);
  rectangleContainer.putCenter(o.distanceText, -12);
  let shadow = g.dropShadowFilter();
  shadow.distance = 3;
  shadow.blur = 5;
  shadow.alpha = 0.2;
  rectangleContainer.filters = [shadow];

  o.container = g.group(rectangleContainer);

  //The update function is called once each frame
  o.update = () => {

    //Set the position of the container
    o.container.x = spriteTofollow.x - o.container.halfWidth;

    //Prevent the sprite from traveling beyond the screen edges
    g.contain(o.container, g.stage)

  };

  return o;
}

function createDisplacementLine(color, strokeThickness, spriteA, spriteB, markerImage){

  let o = {};

  o.line = g.line(color, strokeThickness, spriteA.x, spriteA.y, spriteB.x, spriteB.y - 14);

  let leftMarkerSprite = g.sprite(markerImage),
      rightMarkerSprite = g.sprite(markerImage);

  //The marker text
  o.displacementText = g.text(language.displacementText, "12px Arial", "black");

  //Add a rounded rectangle
  let graphics = new PIXI.Graphics();
  graphics.beginFill(0xE5E9EA, 1);
  graphics.drawRoundedRect(0, 0, 120, 20, 10);
  graphics.endFill();
  let texture = graphics.generateTexture();
  let rectangleSprite = g.sprite(texture);
  let rectangleContainer = g.group(rectangleSprite);

  //Add the displacement text to the rectangle container
  rectangleContainer.add(o.displacementText);
  rectangleContainer.putCenter(o.displacementText, -12);
  let shadow = g.dropShadowFilter();
  shadow.distance = 3;
  shadow.blur = 5;
  shadow.alpha = 0.2;
  rectangleContainer.filters = [shadow];

  o.container = g.group(o.line, leftMarkerSprite, rightMarkerSprite, rectangleContainer);

  //The update function is called once each frame
  o.update = () => {
  
    if (!activityFinished) {

      //Update the line start and end points
      o.line.ax = spriteA.x;
      o.line.ay = spriteA.y - 72;
      o.line.bx = spriteB.x;
      o.line.by = spriteB.y - 14;

      //Position the line end markers
      leftMarkerSprite.setPosition(o.line.ax - 2, o.line.ay - 1);
      rightMarkerSprite.setPosition(o.line.bx -4, o.line.by - 1);

      //Position the displacement text
      rectangleContainer.x = ((o.line.ax + o.line.bx) / 2) - rectangleContainer.halfWidth;
      rectangleContainer.y = ((o.line.ay + o.line.by) / 2) - 28;

      //Prevent the sprite from traveling beyond the screen edges
      g.contain(rectangleContainer, g.stage);
    }

  };

  return o;
}


function changeCarDirection(direction = "right") {

  let carBody = car.bodies[0],
      leftWheel = car.bodies[1],
      rightWheel = car.bodies[2];

  //Body.rotate(carBody, 0);
  Body.setAngle(carBody, 0);
  //Composite.rotate(car, -carBodySprite.rotation, { x: carBodySprite.x, y: carBodySprite.y });
  Body.scale(carBody, -1, 1);
  //Body.scale(leftWheel, -1, 1);
  //Body.scale(rightWheel, -1, 1);
  carBodySprite.scale.x = -carBodySprite.scale.x;
  //Body.setAngularVelocity(leftWheel, -leftWheel.angularVelocity);
  //Body.setAngularVelocity(rightWheel, -rightWheel.angularVelocity);
  Body.setAngularVelocity(leftWheel, -carPower - acceleration);
  Body.setAngularVelocity(rightWheel, -carPower - acceleration);
  carPower = -carPower;
  acceleration = 0; 
  smokeEmitter.stop();
  smokeEmitter = createSmokeEmitter(carPowerInputNumber, direction);
  if (constantSpeedOn || accelerate) {
    smokeEmitter.play();
  }
  /*
  switch (direction) {

    case "left":
      console.log("left")
      Body.scale(carBody, -1, 1);
      carBodySprite.scale.x = -1;
      Body.setAngularVelocity(leftWheel, -leftWheel.angularVelocity);
      Body.setAngularVelocity(rightWheel, -rightWheel.angularVelocity);
      carPower = -carPower;
  }
  */
}



//The particle emitter
function createSmokeEmitter(carPowerInputValue, direction = "right"){
  console.log(direction)
  //Create the frames array for the fairy smoke images
  let smokeFrames = [
    "images/smoke1.png",
    "images/smoke2.png",
    "images/smoke3.png",
  ];

  let numberOfParticles = [0, 3, 6, 9, 12, 16, 20];
  let updateInterval = [0, 300, 260, 230, 170, 140, 100];

  let minAngle,
      maxAngle,
      xPos;

  if (direction === "right") {
    minAngle = 3;
    maxAngle = 3.4;
    xPos = -19;
  } else {
    minAngle = -0.2;
    maxAngle = 0.2;
    xPos = 27;
  }

  //Create the emitter
  let emitter = g.particleEmitter(
    updateInterval[carPowerInputValue], //The interval
    () => {
      g.createParticles( //The function
        carBodySprite.x + xPos, //x position
        carBodySprite.y + 6, //y position
        () => g.sprite(smokeFrames), //Particle sprite
        g.stage, //The container to add the particles to
        numberOfParticles[carPowerInputValue], //Number of particles
        0, //Gravity
        true, //Random spacing
        minAngle, maxAngle, //Min/max angle
        4, 12, //Min/max size
        0.5, 1, //Min/max speed
        0.005, 0.01, //Min/max scale speed
        0.01, 0.05, //Min/max alpha speed
        0.05, -0.05 //Min/max rotation speed
      );
    }
  );

  return emitter;
}

function createTimer() {

  //The return object
  let o = {};

  //Time, seconds and milliseconds
  o.reset = () => {
    o.time = 0;
    o.seconds = 0;
    o.milliseconds = 0;
    o.running = false;
  };

  o.reset();

  o.update = () => {

    if (o.running) {
      //Update the time
      o.time += 1;

      //Find the seconds
      if (o.time % 60 === 0) o.seconds += 1;

      //Find the milliseconds
      if (o.time % 60 !== 0) {
        o.milliseconds += 1;
      } else {
        o.milliseconds = 0;
      }
    }
  };

  o.formattedOutput = () => {
    if (o.milliseconds < 10) {
      return `${o.seconds}:0${o.milliseconds}`;
    } else {
      return `${o.seconds}:${o.milliseconds}`;
    }
  };

  return o;

}

function rulerSprite(rulerImage, markerImage, spriteToFollow, calibration = 0, x = 0, y = 0) {

  //Return object
  let o = {};

  o.rulerSprite = g.sprite(rulerImage);
  o.rulerSprite.setPosition(x, y);

  //The triangular marker
  let markerSprite = g.sprite(markerImage);
  o.rulerSprite.add(markerSprite);
  markerSprite.y = 30;

  //The marker text
  let markerText = g.text("0", "12px Arial", "black");
  o.rulerSprite.add(markerText);
  markerText.y = 16;

  o.update = () => {

    //Position the marker sprite
    markerSprite.x = Math.floor(spriteToFollow.x) - 2;

    //Position the marker text
    if (spriteToFollow.x > rulerPaddingOffset + rulerCalibration
    && spriteToFollow.x < rulerPaddingOffset + rulerCalibration + 100) {
      markerText.x = Math.floor(spriteToFollow.x);
    } else {
      markerText.x = Math.floor(spriteToFollow.x) - 4;
    }
    //markerText.content = ((spriteToFollow.x / 10) + calibration).toFixed(1);
    markerText.content = Math.floor((((spriteToFollow.x - rulerPaddingOffset - rulerCalibration) / 10) + calibration));
  };

  return o;
}


function tallFlagSprite(flagCanvasImage, flagPoleImage, x = 0, y = 0){

  //A return object
  let o = {};

  //A counter required to update the waving flag
  let count = 0;

  o.collisionOccured = false;

  //Add the flag pole
  let flagPole = g.sprite(flagPoleImage);

  // build a rope!
  let ropeLength = Math.floor(58 / 8);

  let flagPoints = [];

  for (var i = 0; i < 10; i++) {
      flagPoints.push(new PIXI.Point(i * ropeLength, 0));
  }

  let strip = new PIXI.mesh.Rope(PIXI.Texture.fromImage(flagCanvasImage), flagPoints);

  strip.x = 0;

  let flagCanvasContainer = new PIXI.Container();
  flagCanvasContainer.x = 4;
  flagCanvasContainer.y = 30;

  flagCanvasContainer.addChild(strip);

  //The finished message
  let finishedMessage = g.text("Finish", "12px Bungee-Regular");
  finishedMessage.setPosition(-18, -75);
  finishedMessage.alpha = 0;

  o.flagContainer = g.group(flagCanvasContainer, flagPole, finishedMessage);

  //The collision flag
  o.collision = false;

  //The `update` function should be called every frame inside the game loop
  o.update = () => {

    //Wave the flag
    count += 0.07;

    // make the snake
    for (var i = 0; i < flagPoints.length; i++) {
        flagPoints[i].y = Math.sin((i * 0.5) + count) * 1;
        flagPoints[i].x = i * ropeLength + Math.cos((i * 0.2) + count) * 1;
    }
  };

  o.displayFinish = () => {
    if (!o.collisionOccured) {
      var finishedMessageFadeIn = g.fadeIn(finishedMessage, 30);
      finishedMessageFadeIn.onComplete = () => {
        g.wait(600, () => {
          var finishedMessageFadeOut = g.fadeOut(finishedMessage, 30)

          //Reset the finishedMessage to its original position
          finishedMessageFadeOut.onComplete = () => finishedMessage.setPosition(-18, -75);
        })
      };
      let finishedMessageSlide = g.slide(finishedMessage, finishedMessage.x, finishedMessage.y - 15, 60, "smoothstep", false);


      //Set `o.collisionOccured` to `false` so this only happens once
      o.collisionOccured = true;
    }

  };
  


  return o;

}

function flagSprite(flagCanvasImage, flagPoleImage, x = 0, y = 0){

  //A return object
  let o = {};

  //A counter required to update the waving flag
  let count = 0;

  o.collisionOccured = false;

  //Add the flag pole
  let flagPole = g.sprite(flagPoleImage);

  // build a rope!
  let ropeLength = Math.floor(58 / 8);

  let flagPoints = [];

  for (var i = 0; i < 10; i++) {
      flagPoints.push(new PIXI.Point(i * ropeLength, 0));
  }

  let strip = new PIXI.mesh.Rope(PIXI.Texture.fromImage(flagCanvasImage), flagPoints);

  strip.x = 0;

  let flagCanvasContainer = new PIXI.Container();
  flagCanvasContainer.x = 4;
  flagCanvasContainer.y = 30;

  flagCanvasContainer.addChild(strip);

  //The finished message
  let finishedMessage = g.text("Finish", "12px Bungee-Regular");
  finishedMessage.setPosition(8, -20);
  finishedMessage.alpha = 0;

  o.flagContainer = g.group(flagCanvasContainer, flagPole, finishedMessage);

  //The collision flag
  o.collision = false;

  //The `update` function should be called every frame inside the game loop
  o.update = () => {

    //Wave the flag
    count += 0.07;

    // make the snake
    for (var i = 0; i < flagPoints.length; i++) {
        flagPoints[i].y = Math.sin((i * 0.5) + count) * 1;
        flagPoints[i].x = i * ropeLength + Math.cos((i * 0.2) + count) * 1;
    }
  };

  o.displayFinish = () => {
    if (!o.collisionOccured) {
      let finishedMessage = g.text("Finish", "12px Bungee-Regular");
      finishedMessage.setPosition(542, 335);
      finishedMessage.alpha = 0;

      var finishedMessageFadeIn = g.fadeIn(finishedMessage, 30);
      finishedMessageFadeIn.onComplete = () => {
        g.wait(600, () => {
          var finishedMessageFadeOut = g.fadeOut(finishedMessage, 30)
        })
      };
      let finishedMessageSlide = g.slide(finishedMessage, finishedMessage.x, finishedMessage.y -10, 60, "smoothstep", false);

      //Set `o.collisionOccured` to `false` so this only happens once
      o.collisionOccured = true;
    }

  };
  


  return o;

}

function freeBodyDiagram(parentSprite, orientation, padding, physicsProperty, label) {

  if (!parentSprite.freeBodyDiagrams) {
    parentSprite.freeBodyDiagrams = [];
  }

  var graphics = new PIXI.Graphics();

  graphics.lineStyle(1, 0x000, 1);
  graphics.beginFill(0xFF3300);

  //Draw an arrow, either horizontally or vertically
  if (orientation === "horizontal") {
    graphics.moveTo(0, -2);
    graphics.lineTo(26 , -2);
    graphics.lineTo(26 , -4);
    graphics.lineTo(32 , 0);
    graphics.lineTo(26 , 4);
    graphics.lineTo(26 , 2);
    graphics.lineTo(0 , 2);
    graphics.lineTo(0 , -2);
    graphics.endFill();
  } else {
    graphics.moveTo(-2, 0);
    graphics.lineTo(-2 , 26);
    graphics.lineTo(-6 , 26);
    graphics.lineTo(0 , 32);
    graphics.lineTo(6 , 26);
    graphics.lineTo(2 , 26);
    graphics.lineTo(2 , 0);
    graphics.lineTo(-2 , 0);
    graphics.endFill();
  }

  //Add a label
  if (label || label !== "") {
    var forceLabel = g.text(label, "12px Arial", "red");
  }

  //Rotate the label is if the orientation is verical
  if (orientation === "vertical") {
    forceLabel.rotation = 1.57;
  }
  

  let texture = graphics.generateTexture();

  let sprite = new PIXI.Sprite(texture);

  g.addProperties(sprite);

  //Add the diagram to the parent sprite
  g.stage.addChild(sprite);

  //Create a `freeBodyDiagram` property on the parent sprite so
  //that we can update it in the game loop
  let freeBodyDiagram = {};
  freeBodyDiagram.arrow = sprite;
  freeBodyDiagram.physicsProperty = physicsProperty;
  freeBodyDiagram.padding = padding;
  if (label || label !== "") {
    freeBodyDiagram.label = forceLabel;
    freeBodyDiagram.labelContent = label;
  }
  freeBodyDiagram.orientation = orientation;

  freeBodyDiagram.arrow.visible = false;
  freeBodyDiagram.label.visible = false;

  parentSprite.freeBodyDiagrams.push(freeBodyDiagram);
  

  //Add the padding
}


function spriteFromArray(verticesArray, fillStyle, lineStyle, lineWidth = 1, lineOpacity = 1){
  var graphics = new PIXI.Graphics();

  // set a fill and line style

  if (fillStyle) graphics.beginFill(fillStyle);
  if (lineStyle) graphics.lineStyle(lineWidth, lineStyle, lineOpacity);

  verticesArray.forEach((vertex, index) => {

    var x = vertex[0];
        y = vertex[1];

    if (index === 0) {
      graphics.moveTo(x,y);
    } else {
      graphics.lineTo(x,y);
    }
  });

  graphics.endFill();

  let texture = graphics.generateTexture();

  let sprite = new PIXI.Sprite(texture);

  g.addProperties(sprite);

  g.stage.addChild(sprite);

  return sprite;
}

/*
keyboard
--------
The `keyboard` helper function creates `key` objects
that listen for keyboard events. Create a new key object like
this:
    var keyObject = keyboard(asciiKeyCodeNumber);
Then assign `press` and `release` methods like this:
    keyObject.press = function() {
      //key object pressed
    };
    keyObject.release = function() {
      //key object released
    };
Keyboard objects also have `isDown` and `isUp` Booleans that you can check.
This is so much easier than having to write out tedious keyboard even capture 
code from scratch.
Like I said, the `keyboard` function has nothing to do with generating sounds,
so just delete it if you don't want it!
*/

function keyboard(keyCode) {
  var key = {};
  key.code = keyCode;
  key.isDown = false;
  key.isUp = true;
  key.press = undefined;
  key.release = undefined;
  //The `downHandler`
  key.downHandler = function(event) {
    if (event.keyCode === key.code) {
      if (key.isUp && key.press) key.press();
      key.isDown = true;
      key.isUp = false;
    }
    event.preventDefault();
  };

  //The `upHandler`
  key.upHandler = function(event) {
    if (event.keyCode === key.code) {
      if (key.isDown && key.release) key.release();
      key.isDown = false;
      key.isUp = true;
    }
    event.preventDefault();
  };

  //Attach event listeners
  window.addEventListener(
    "keydown", key.downHandler.bind(key), false
  );
  window.addEventListener(
    "keyup", key.upHandler.bind(key), false
  );
  return key;
}

//Create a custom physics body based on an array of vertices
function customShape(xx, yy, width, height, verticesArray, isStatic = false) {
  var xStart = xx - (width / 2),
      yStart = yy + (height / 2);
 
  var vertices = verticesArray.map(element => {
    var x = element[0],
        y = element[1];

    return {x, y}

  });


  var body = Bodies.fromVertices(xx, yy, vertices, {
      isStatic: isStatic,
  }, true);

  return body;

}


function customCar(xx, yy, width, height, wheelSize) {
        var group = Body.nextGroup(true),
            wheelBase = 5,
            wheelAOffset = -width * 0.5 + wheelBase,
            wheelBOffset = width * 0.6 - wheelBase,
            wheelYOffset = 9;
            xStart = xx - (width / 2);
            yStart = yy - (height / 2);

        var vertices = [
         {x: xStart, y: yStart},
         {x: xStart, y: yStart - 12},
         {x: xStart + 2, y: yStart - 20},
         {x: xStart + 14, y: yStart - 20},
         {x: xStart + 32, y: yStart - 7},
         {x: xStart + 32, y: yStart},
         {x: xStart, y: yStart}
        ];

        var body = Bodies.fromVertices(xx, yy, vertices, {
            collisionFilter: {
                group: group
            },
           density: 0.0005,//0.005,//0.0005,
            render: {
                fillStyle: '#008B8B',
                strokeStyle: '#008B8B',
                lineWidth: 1,
            }
        }, true);
    
        var car = Composite.create({ label: 'Car' });
    
        var wheelA = Bodies.circle(xx + wheelAOffset, yy + wheelYOffset, wheelSize, { 
            collisionFilter: {
                group: group
            },
        });
                    
        var wheelB = Bodies.circle(xx + wheelBOffset, yy + wheelYOffset, wheelSize, { 
            collisionFilter: {
                group: group
            },
        });
                    
        var axelA = Constraint.create({
            bodyB: body,
            pointB: { x: wheelAOffset, y: wheelYOffset },
            bodyA: wheelA,
            stiffness: 0.1,//0.3, //0.1,
            length: 0
        });
                        
        var axelB = Constraint.create({
            bodyB: body,
            pointB: { x: wheelBOffset, y: wheelYOffset },
            bodyA: wheelB,
            stiffness: 0.1,//0.3, //0.1,
            length: 0
        });
        
        Composite.addBody(car, body);
        Composite.addBody(car, wheelA);
        Composite.addBody(car, wheelB);
        Composite.addConstraint(car, axelA);
        Composite.addConstraint(car, axelB);

        return car;
    };
})();
/*
With this basic Hexi architecture, you can create anything. Just set
Hexi's `state` property to any other function to switch the
behaviour of your application. Here's how:

   g.state = anyStateFunction;

Write as many state functions as you need.
If it's a small project, you can keep all these functions in one file. But,
for a big project, load your functions from
external JS files as you need them. Use any module system you
prefer, like ES6 modules, CommonJS, AMD, or good old HTML `<script>` tags.
This simple architectural model can scale to any size, and is the only
architectural model you need to know. Keep it simple and stay happy!
*/

