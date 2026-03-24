//Create an array of files you want to load. If you don't need to load
//any files, you can leave this out. Hexi lets you load a wide variety
//of files: images, texture atlases, bitmap fonts, ordinary font files, and
//sounds
let thingsToLoad = [
  "images/scale.png",
  "images/base.png",
  "images/turret.png",
  "images/arrow.png",
  "images/arrowInTarget.png",
  "images/target.png",
  "images/background.png",
  "images/catHead.png",
  "images/catEyes.png",
  "images/eyesBackground.png",
  "images/catBody.png"
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
//let g = hexi(900, 300, setup, thingsToLoad, load);

let g = new Hexi({
  //Required options:
  width: 900, //Width, in pixels
  height: 300, //Height, in pixels
  setup: setup, //Function to run when Hexi starts

  //Optional options:
  assets: thingsToLoad, //Array of assets that should be loaded
  load: load, //Function to run while Hexi is loading asssets
  renderer: "webgl", //"auto", "canvas" or "webgl"
  antialias: true,
  /*
    backgroundColor: 0xCCCCCC,    //Hexadecimal color code
    border: "1px dashed black",   //CSS border string
    scaleToWindow: true,          //Boolean
    scaleBorderColor: "gray",     //Color string
    fps: 30,                      //The frames per second the logic loop should run at
    //An an object of Boolean (true/false) properties that describe which sprite
    //properties should  be smoothly animated. These can be any of 5
    //properties: `position`, `rotation`, `size`, `scale` or `alpha`.
    //(Position and rotation are on by default, unless you set Hexi's
    //`interpolate` property to `false`)
    */
  interpolationProperties: {
    position: true,
    rotation: true,
    size: true,
    alpha: true
  },
  interpolate: true

  //To change PIXI's renderer, set the `renderer` option to
  //"auto", "canvas" or "webgl", like this:
  //renderer: "auto"
  //Add any other Pixi initialization options you need, depending
  //on which Pixi renderer you're using
});

//Optionally Set the frames per second at which the game logic loop should run.
//(Sprites will be rendered independently, with interpolation, at full 60 or 120 fps)
//If you don't set the `fps`, Hexi will default to an fps of 60
g.fps = 30;

//Optionally add a border and set the background color
//g.border = "2px red dashed";
g.backgroundColor = 0xffffff;

//Optionally scale and align the canvas inside the browser window
//g.scaleToWindow();
g.renderer.antialias = true;

//Start Hexi. This is important - without this line of code, Hexi
//won't run!
g.start();

/*
2. Loading Files
----------------
*/

//The `load` function will run while assets are loading. This is the
//same `load` function you assigned as Hexi's 4th initialization argument.
//Its optional. You can leave it out if you don't have any files to
//load, or you don't need to monitor their loading progress

function load() {
  //Display the file currently being loaded
  console.log(`loading: ${g.loadingFile}`);

  //Display the percentage of files currently loaded
  console.log(`progress: ${g.loadingProgress}`);

  //Add an optional loading bar.
  g.loadingBar();
}

/*
Initialize your game objects and variables
----------------------------------------------
*/

//Declare any variables that need to be used in more than one function
let velocityOutput,
  launchButton,
  scale,
  cannon,
  turret,
  base,
  bullets,
  target,
  targetHitArea,
  currentBullet,
  simulationPlaying = false,
  simulationFinished = false,
  simulationRestarted = false,
  turretAngle = 0,
  bulletVelocity = 7,
  bulletLaunched = false,
  firstHit = false,
  secondHit = false,
  gravity = 0.3,
  // these next few config variables were added for the parabolas implementation.
  // showParabola just draws points as the arrow flies.
  showParabola = false,
  // in the projectile motion ILO, the degrees start at 90 (pointing up)
  // and go to 0 (pointing 'right').
  // for parabolas, the degrees are counted from 0 (pointing right) and then
  // go counterclockwise to 90 (pointing up).
  angleAlongXAxis = 0,
  angleDirection = "counterclockwise",
  groundY = 240;

let minAngle, maxAngle, angleInitialValue;

if (angleAlongXAxis == 0) {
  minAngle = 0;
  maxAngle = 90;
  angleInitialValue = 176;
}
if (angleAlongXAxis === 180) {
  minAngle = 180;
  maxAngle = 90;
  angleInitialValue = 45;
}

//The `setup` function will run when all the assets have loaded. This
//is the `setup` function you assigned as Hexi's 3rd argument. It's
//mandatory - every Hexi application has to have a `setup` function
//(although you can give it any name you want)

function setup() {
  //Sprites
  let background = g.sprite("images/background.png");

  //The meter measurement scale
  scale = g.sprite("images/scale.png");
  scale.x = 0;
  scale.y = 249;

  //The cannon
  cannon = g.group();
  base = g.sprite("images/base.png");
  turret = g.sprite("images/turret.png");
  turret.setPivot(0.1, 0.5);
  turret.x = 50;
  turret.y = 25;
  turret.rotation = -0.5;
  cannon.add(base, turret);
  cannon.x = 50;
  cannon.y = 193;

  //The target's invisible hit area that's used just for
  //testing a collision between the target and the arrow
  targetHitArea = g.rectangle(40, 40, "red");
  targetHitArea.setPosition(725, 120);
  targetHitArea.visible = false;

  //The target
  target = g.sprite("images/target.png");
  target.x = 725;
  target.y = 120;

  //Add the cat
  let catHead = g.sprite("images/catHead.png");
  let eyesBackground = g.sprite("images/eyesBackground.png");
  let catBody = g.sprite("images/catBody.png");
  catEyes = g.sprite("images/catEyes.png");
  cat = g.group(catBody, eyesBackground, catEyes, catHead);
  cat.setScale(0.4, 0.4);
  cat.setPosition(520, 220);
  catEyes.startX = catEyes.x;
  catEyes.startY = catEyes.y;

  //Make an array to store the bullets
  bullets = [];

  //Store the points
  points = [];

  //UI
  //References to each of the HTML UI elements
  angleOutput = document.querySelector("#angleOutput");
  velocityOutput = document.querySelector("#velocityOutput");
  distanceOutput = document.querySelector("#distanceOutput");
  angleOutput2 = document.querySelector("#angleOutput2");
  velocityOutput2 = document.querySelector("#velocityOutput2");
  distanceOutput2 = document.querySelector("#distanceOutput2");

  //Buttons
  //Start button
  launchButton = document.querySelector("#launchButton");

  let launchButtonClickHandler = event => {
    // Hide the bubble.
    $("#bubble").fadeOut("fast");

    // remove any points
    g.remove(points);

    //Toggle the `bulletLaunched` flag
    bulletLaunched = !bulletLaunched;

    //Remove all the bullet sprites in the `bullets` array
    g.remove(bullets);

    let button = event.target;
    g.shoot(
      turret, //The shooter
      turret.rotation, //The angle at which to shoot
      75, //The x point on the shooter where the bullet should start
      1, //The y point on the shooter where the bullet should start
      g.stage, //The container you want to add the bullet to
      bulletVelocity, //The bullet's speed (pixels per frame)
      bullets, //The array used to store the bullets

      //A function that returns the sprite that should
      //be used to make each bullet
      () => {
        let bullet = g.sprite(["images/arrow.png", "images/arrowInTarget.png"]);
        bullet.states = {
          flying: 0,
          inTarget: 1
        };
        bullet.visible = false;
        return bullet;
      }
    );
  };
  launchButton.addEventListener("click", launchButtonClickHandler);

  //Angle input
  let angleInput = document.getElementById("angleInput");
  let getAngleInDegrees = () => {
    return angleInput.value;
  };
  let displayAngle = () => {
    let angleInDegrees = getAngleInDegrees();
    let angleOutput = document.querySelector("#angleOutput");
    angleOutput.innerHTML = `${angleInDegrees} degrees`;
    angleOutput2.innerHTML = `${angleInDegrees}`;
  };
  let setTurretAngle = () => {
    let angleInDegrees = getAngleInDegrees();
    if (angleDirection !== "clockwise") {
      // hm.
      angleInDegrees = angleInDegrees * -1;
    }
    let angleInRadians = (angleInDegrees * Math.PI) / 180;
    // console.log(`angleInRadians: ${angleInRadians}`);
    // console.log(`angleInDegrees: ${angleInDegrees}`);
    let radMod = (angleAlongXAxis * Math.PI) / 180;
    turretAngle = angleInRadians + radMod;
  };
  //Set the intitial value
  angleInput.setAttribute("min", minAngle);
  angleInput.setAttribute("max", maxAngle);
  angleInput.setAttribute("value", angleInitialValue);
  displayAngle();
  setTurretAngle();

  //Handle the input
  let angleInputHandler = event => {
    setTurretAngle();
    //Display the value in the angleOutput
    displayAngle();
  };
  angleInput.addEventListener("input", angleInputHandler);

  //Velocity input
  //Set the intitial value
  let velocityInput = document.getElementById("velocityInput");
  velocityInput.value = 7;

  //Handle the input
  let velocityInputHandler = event => {
    let velocity = event.target.value;
    bulletVelocity = velocity;

    //Display the value in the velocityOutput
    let velocityOutput = document.querySelector("#velocityOutput");
    velocityOutput.innerHTML = `${bulletVelocity} m/s`;
    velocityOutput2.innerHTML = `${bulletVelocity}`;
  };
  velocityInput.addEventListener("input", velocityInputHandler);

  //Start the game loop
  g.state = play;
}

//The game logic
//------------------

//The `play` function is called in a continuous loop, at whatever fps
//(frames per second) value you set. This is your *game logic loop*. (The
//render loop will be run by Hexi in the background at the maximum fps
//your system can handle.) You can pause Hexi's game loop at any time
//with the `pause` method, and restart it with the `resume` method

function play() {
  //Make the box and turret angle towards the pointer
  turret.rotation = turretAngle; //-(g.angle(turret, g.pointer));

  //Diable the launch button if a bullet is active
  launchButton.disabled = bulletLaunched;

  //If you just want to move all the bullets without removing them
  //they hit the screen boundaries, you can just use the help of the `move` method
  //g.move(bullets);

  //Remove the bullets if they cross the screen boundaries
  //Loop through the bullets using `filter` so that we can remove
  //the bullet easily
  bullets = bullets.filter(bullet => {
    //Check for a collision with the target
    if (!g.hitTestPoint({ x: bullet.x, y: bullet.y }, targetHitArea)) {
      //Move the bullet
      bullet.vy += gravity;
      bullet.x += bullet.vx;
      bullet.y += bullet.vy;

      //Rotate the bullet based on its velocity
      bullet.rotation = Math.atan2(
        bullet.x - bullet.previousX,
        -(bullet.y - bullet.previousY)
      );

      //Move the cat's eyes
      catEyes.x = -(catEyes.startX - (bullet.x - cat.x) / 80);
      catEyes.y = -(catEyes.startY - (bullet.y - cat.y) / 60);
    } else {
      bullet.layer = 10;
      launchButton.disabled = false;

      //Display the bullet's `inTarget` state
      bullet.show(bullet.states.inTarget);

      // Place and reveal the bubble.
      $("#bubble")
        .css("left", "" + (distanceOutput2.innerHTML * 10 + 101 - 34) + "px")
        .css("top", "100px")
        .removeClass("arrow_box2")
        .addClass("arrow_box");
      $("#bubble").fadeIn();
    }

    if (bulletLaunched && showParabola) {
      if (bullet.previousY < groundY)
        points.push(
          g.circle(5, "#000", "#000", 0, bullet.previousX, bullet.previousY)
        );
    }

    if (!bullet.previousX && !bullet.previousY) {
      bullet.rotation = turret.rotation;
      g.stage.swapChildren(bullet, scale);
    } else {
      bullet.visible = true;
    }

    //Display the bullet's distance
    let distanceOutput = document.querySelector("#distanceOutput");
    if (bullet.y < 239) {
      distanceInMeters = Math.round(bullet.x / 10 - 10);
      distanceOutput.innerHTML = `${distanceInMeters} m`;
      distanceOutput2.innerHTML = `${distanceInMeters}`;
    }

    //Check for a collision with the stage boundary
    let collision = g.outsideBounds(bullet, g.stage);

    //If there's a collision, display the side that the collision
    //happened on, remove the bullet sprite and filter it out of
    //the `bullets` array
    if (collision) {
      if (collision.has("bottom")) {
        bulletLaunched = false;

        // Position the bubble.
        if (distanceOutput2.innerHTML < 80) {
          if (distanceOutput2.innerHTML <= 75)
            $("#bubble")
              .css(
                "left",
                "" + (distanceOutput2.innerHTML * 10 + 101 - 34) + "px"
              )
              .css("top", "240px")
              .removeClass("arrow_box2")
              .addClass("arrow_box");
          else
            $("#bubble")
              .css("left", "" + (76 * 10 + 101 - 34) + "px")
              .css("top", "240px")
              .removeClass("arrow_box2")
              .addClass("arrow_box");
        } else {
          $("#bubble")
            .css("left", "" + (75 * 10 + 101 - 34) + "px")
            .css("top", "180px")
            .removeClass("arrow_box")
            .addClass("arrow_box2");
        }

        //The `remove` function will remove a sprite for its parent.
        g.remove(bullet);

        // Reveal the bubble.
        $("#bubble").fadeIn();

        //Remove the bullet from the `bullets` array
        return false;
      }
    }

    //Update the Verlet physics properties
    bullet.previousX = bullet.x;
    bullet.previousY = bullet.y;

    //If the bullet hasn't hit the edge of the screen,
    //keep it in the `bullets` array
    return true;
  });
}
