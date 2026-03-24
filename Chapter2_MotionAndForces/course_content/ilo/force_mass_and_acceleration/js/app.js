//var language = language || {};

//
var config = {
        type: Phaser.AUTO,
        width: 570,
        height: 500,
        parent: "phaser-Container",
        scene: {
            preload: preload,
            create: create,
            update: update
        },
        pixelArt: false,
        backgroundColor: '#ffffff'
    };

var game = new Phaser.Game(config);
//Constants


let RULERWIDTH = 380;
let RULEROFFSET = 100;
var _this = this;

var useTimingBlock = false;  // note that the timing block doesn't stop time right now.

//Model of the scale
function Model()
{
    this.gravity = 9.8;
    this.massOfHanging = 0;
    this.massOfWagon = 0;
    this.friction = 1;//if friction is 1 then no friction????
    
    this.blockDistance = 0.5;
    
    this.getNumWagonWeights = function()
    {
        var offset = this.massOfWagon - 100;
        return Math.floor(offset/10);
    }
    this.getMassOfHanging = function()
    {   
        return this.massOfHanging;
    }
    this.getNumHangingWeights = function()
    {
        return Math.floor(this.massOfHanging/10);
    }
    this.getBlockPosition = function()
    {
        return this.blockDistance;
    }
    
    this.calcForceOfHanging = function()
    {
        //console.log("calcForceOfHanging",this.massOfHanging,this.gravity);
        return this.massOfHanging/1000 * this.gravity;
    }
    
    /*this.velocityOfCar = function(force, time)
    {
        
        var wagoninkg = this.massOfWagon;
        //console.log("velocityOfCar",time, wagoninkg);
        return (force * time) / wagoninkg;
    }*/
    
    this.accOfCar = function(force)
    {
        var wagoninkg = this.massOfWagon/1000;
        return force/wagoninkg;
    }
    
    this.applyFriction = function()
    {
        return input * this.friction;
    }
}

function WeightHandler(model, isX, weightSize, offsetx, offsety, weightName, weightContainer)
{
    this.model = model;
    this.weightContainer = weightContainer;
    this.weights = [];
    this.weightName = weightName;
    this.isX = isX;
    this.offsetx = offsetx
    this.offsety = offsety;
    
    this.UpdateWeights = function()
    {
        var diff = this.model() - this.weights.length;
        if(diff>0)
        {
            //add 1
            for(var x=0;x<diff;x++)
            {
                var w = _this.add.image( 10,0,'forcemassaccel', weightName+' instance 10000');//.setOrigin(0, 0);
                this.weightContainer.add(w);
                this.weights.push(w);
                if(isX)
                {
                    w.x = weightSize * this.weights.length + offsetx;
                    w.y = offsety;
                }
                else
                {
                    w.x = offsetx;
                    w.y = weightSize * this.weights.length + offsety;

                }
            }
        }
        else if(diff<0)
        {
            //remove 1
            while(diff<0)
            {
                if(this.weights.length<=0)
                    break;
                
                var w = this.weights.pop();
                w.destroy();
                diff++;
            }
            
        }
    }
}
function TimingHandler(model)
{
    this.model = model;
    this.UpdateWeights = function()
    {
        var distance = this.model();
        timingBlock.x = RULEROFFSET + RULERWIDTH * distance;
    }
}

//
var model = new Model();
var carHandler;
var hangingHandler;
var blockHandler;
/**
*
*
*
*/
function preload ()
{
    this.load.atlas('forcemassaccel', 
        'assets/images/forcemassaccel.png',
        'assets/images/forcemassaccel.json'
    );
}

var car, wheel1, wheel2;
var wheelPiece, wheelHolder, timingBlock;
var lineTop, lineSide;//later
var hook, lineSide, lineTop;
function create ()
{    
    _this = this;
    
    car = _this.add.container(0, 0);    
    
    lineTop = this.add.image(101, 80, 'forcemassaccel', 'lineTop instance 10000').setOrigin(0, 0);    
    var cart = this.add.image(20, 68.1, 'forcemassaccel', 'cart instance 10000').setOrigin(0, 0);    
    
    car.add(cart);
    //car.add(lineTop);
    
    wheel1 = this.add.image(31, 93, 'forcemassaccel', 'wheel instance 10000');
    wheel2 = this.add.image(95, 93, 'forcemassaccel', 'wheel instance 10000');
    car.add(wheel1);
    car.add(wheel2);
    
    lineSide = this.add.image(525, 110-411.2, 'forcemassaccel', 'lineSide instance 10000').setOrigin(0, 0);    //19, -411.2
    wheelPiece = this.add.image(513, 91, 'forcemassaccel', 'wheelPiece instance 10000');    
    wheelHolder = this.add.image(494, 91, 'forcemassaccel', 'wheelHolder instance 10000').setOrigin(0, 0);    
    
    if (useTimingBlock) {
        timingBlock = this.add.image(100, 79, 'forcemassaccel', 'timingBlock instance 10000').setOrigin(0, 0);    
    }
    
    hook = _this.add.container(504, 110);    
    
    var hookGraphic = this.add.image(0, 0, 'forcemassaccel', 'hook instance 10000').setOrigin(0, 0);     
    hook.add( hookGraphic );
    //hook.add(lineSide);
    //
    
    var shape = this.make.graphics();
    shape.fillStyle(0xffffff);
    shape.beginPath();
    shape.fillRect(75, 60, 436, 30);
    shape.fillRect(511, 91, 30, 536);
    shape.closePath();
    
    var mask = shape.createGeometryMask();
    lineTop.setMask(mask);
    lineSide.setMask(mask);
    //
    carHandler = new WeightHandler( e => model.getNumWagonWeights(e), true, 7.5, 21, 62, "weightCar", car);
    hangingHandler = new WeightHandler(e => model.getNumHangingWeights(e), false, 8, 21, 15, "weight", hook);
    if (useTimingBlock) {
        blockHandler = new TimingHandler( e=>model.getBlockPosition(e));
    } else {
        document.getElementById('timingBlockUI').style="display:none";
    }
    // 
    //
    bindUI();
    //
    carHandler.UpdateWeights();
    hangingHandler.UpdateWeights();
    // blockHandler.UpdateWeights();
}

var simulationActive = false;
var timingActive = false;
var simulationTime = 0;
var doReset = false;
var vel = 0;
function update(time, delta)
{
    if(simulationActive)
    {
        simulationTime += delta;
        timeOutput.innerHTML = msToTime(simulationTime);
        
        var forceHanging = model.calcForceOfHanging();
        
        var acc = model.accOfCar(forceHanging);
        
        vel = acc * simulationTime/1000;
        var displacement = vel * delta/1000;
        // console.log(vel, displacement);
        
        //rotate these based on 
        //wheelPiece
        wheelPiece.rotation = vel;
        //wheel1.rotation = vel;
        //wheel2.rotation = vel;
        
        let displacementInPixels = displacement * RULERWIDTH; // 1 m = RULERWIDTH pixels
        
        if(car.x+120+80+displacementInPixels >= 580)
        {
           simulationActive = false;
        }
        else
        {
            car.x += displacementInPixels;
            lineTop.x += displacementInPixels;
            hook.y += displacementInPixels;
            lineSide.y += displacementInPixels;
        }

        
        //test for touch sensor
        /*if(car.x+120+80 > 580)
        {
        }*/

    }
}

function msToTime(duration) {
    var milliseconds = parseInt((duration%1000))
        , seconds = parseInt((duration/1000)%60);
    
    milliseconds = addZero(milliseconds, 3);
    seconds = (seconds < 10) ? "0" + seconds : seconds;

    return seconds + "." + milliseconds;
}
function addZero(x, n) {
    while (x.toString().length < n) {
        x = "0" + x;
    }
    return x;
}

function resetSimulation()
{
}
var carInit, lineTopInit, hookInit, lineSideInit;

let startSimulation = event => 
{
    //    
    // console.log("start");
    if(!doReset)
    {
        startButton.innerHTML = "Reset";
        simulationActive = true;
        timingActive = true;
       doReset = true;
       
       carInit = car.x;
       lineTopInit = lineTop.x;
       hookInit = hook.y
       lineSideInit = lineSide.y;
        
        hangingMassHookup.select.disabled = true;
        wagonMassHookup.select.disabled = true;
        if(frictionHookup)
            frictionHookup.select.disabled = true;
        if (useTimingBlock) {
            timingBlockHookup.select.disabled = true;
        }

            
    }
    else
    {

        simulationTime = 0;
        doReset = true;
        startButton.innerHTML = "Start";
        simulationActive = false;
        timingActive = false;
        doReset = false;
        
        
        car.x  = carInit;
        lineTop.x = lineTopInit;
        hook.y = hookInit;
        lineSide.y = lineSideInit;

        // reset values of sliders. (We can safely
        // set to zero and the select will use its min
        // property.)
        hangingMassHookup.changeSelect(0);
        wagonMassHookup.changeSelect(0);
       
        hangingMassHookup.select.disabled = false;
        wagonMassHookup.select.disabled = false;
        if(frictionHookup)
            frictionHookup.select.disabled = false;
        if (useTimingBlock) {
            timingBlockHookup.select.disabled = false;
        }

        document.getElementById("selecthangingMass").focus();
        
        timeOutput.innerHTML = msToTime(0);
    }
    
};
  


var hangingMassHookup, wagonMassHookup, frictionHookup;
var timingBlockHookup;
var startButton, timeOutput;
function bindUI()
{
    hangingMassHookup = new UIHookup(1, "hangingMass", function(val){model.massOfHanging=val;},"g", hangingHandler);
    wagonMassHookup = new UIHookup(100, "wagonMass", function(val){model.massOfWagon=val;},"g", carHandler);
    
    //if doing friction
    //frictionHookup = new UIHookup(0.1, "firction", function(val){model.friction=val;},"", null);
    
    if (useTimingBlock) {
        timingBlockHookup = new UIHookup(0.5, "TimingBlock", function(val){model.blockDistance=val;},"m", blockHandler);

    }
    
    startButton = document.querySelector("#startButton");
    startButton.addEventListener("click", startSimulation);
    
    timeOutput = document.querySelector("#timeOutput");
    timeOutput.innerHTML = "0.0000";
}

      
        
/**
*
*
*
*/
function UIHookup(num, name, model, unit, handler)
{
    this.value = num;
    this.name = name;
    this.model = model;
    this.unit = unit;
    this.handler = handler;
    
    this.select = document.querySelector("#select"+this.name);
    this.output = document.querySelector("#output"+this.name);
    //
    this.changeSelect = function(val)
    {
        // if val is numeric, change the select to that value,
        // otherwise change it to the select's value.
        if (typeof !isNaN(parseFloat(val)) && isFinite(val)) {
            this.select.value = val;
        } 
        this.value = this.select.value; 
        
        this.updateOutput();
        if(model)
        {
            model(this.value);
        }
        if(handler)
        {
            handler.UpdateWeights();
        }
    }
    //
    listen(this.select, 'input', e => this.changeSelect(e));
    listen(this.select, 'change', e => this.changeSelect(e));
    //
    this.updateOutput = function()
    {
        this.output.innerHTML = this.value+""+this.unit;
    }
    this.changeSelect();
    this.updateOutput();
}
//helper function
function listen(element, type, handler) {
  element.addEventListener(type, handler);
  return function() {
    element.removeEventListener(type, handler);
  };
}
