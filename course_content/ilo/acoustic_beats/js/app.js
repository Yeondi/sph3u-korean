//var language = language || {};

//
var config = {
        type: Phaser.AUTO,
        width: 560,
        height: 500,
        parent: "phaser-Container",
        scene: {
            preload: preload,
            create: create,
            update: update
        },
        backgroundColor: '#fff0000'
    };

var game = new Phaser.Game(config);
//Constants



/**
*
*
*
*/
function preload ()
{
    /*this.load.atlas('forcemassaccel', 
        'assets/images/forcemassaccel.png',
        'assets/images/forcemassaccel.json'
    );*/
     
    this.load.audio('440hz', [
        'assets/audio/440hz_loop.wav'
    ]);
    this.load.audio('440.5hz', [
        'assets/audio/4405hz_loop.wav'
    ]);
    this.load.audio('441hz', [
        'assets/audio/441hz_loop.wav'
    ]);
}

var graphics;
var combinedGraph;

function create ()
{    
    _this = this;
   
    
    //console.log("Create.");
    graphics = this.add.graphics();
    combinedGraph = new Grapher(440, null, null);
    combinedGraph.generatePoints();
    bindUI();
}

function update(time, delta)
{
    /*if(uiHookups[0])
    {
        if(uiHookups[0].isReady)
        {
            uiHookups[0].getData();
        }
    }*/
    //handle bars
    
    graphics.clear();
    for(var x=0;x<uiHookups.length;x++)
    {
        if(uiHookups[x])
        {
            if(uiHookups[x].isReady)
            {
                uiHookups[x].grapher.updatePoints(delta/1000);
                uiHookups[x].grapher.drawBaseLine();
                uiHookups[x].grapher.drawPoints();
                
            }
        }    
    }
    
    combinedGraph.combinePoints(uiHookups);
    combinedGraph.drawBaseLine();
    combinedGraph.drawPoints();
    
}




var uiHookups= [];
var timingBlockHookup;
var stopAllButton;
function bindUI()
{
    uiHookups.push(new UIHookup("440","440hz", 440, 60));
    uiHookups.push(new UIHookup("4405","440.5hz", 440.5, 180));
    uiHookups.push(new UIHookup("441","441hz", 441, 300));
    
    
    startButton = document.querySelector("#stopAllButton");
    startButton.addEventListener("click", stopAll);
}

function stopAll()
{
    for(var x=0;x<uiHookups.length;x++)
    {
        uiHookups[x].stopAudio();
    }
}

/**
*
*
*
*/
let XOFFSET = 0;
function UIHookup(name, audioName,hz, offset)
{
    this.name = name;
    this.audioName = audioName;
    this.audio;
    //console.log("#start"+this.name);
    this.button = document.querySelector("#start"+this.name);
    this.isReady = false;
    this.hz = hz;
    
    this.currentY = 0;
    
    //
    this.getYPosWithHz = function(pointPosition)
    {
        //console.log(this.hz , pointPosition)
        this.currentY = Math.sin( this.hz  * pointPosition );
        //console.log(this.currentY);
        return this.currentY;
    }
    this.isAudioPlaying = function()
    {
        return this.audio.isPlaying;
    }
    //
    this.grapher = new Grapher(offset, e=>this.getYPosWithHz(e), e=>this.isAudioPlaying(e));
    //
    this.handlePress = function()
    {
        if(this.audio.isPlaying)
        {
            this.stopAudio();
        }
        else
        {
            this.playAudio();
        }
    }
    this.getAudio = function()
    {
        this.audio = _this.sound.add(this.audioName);
        if(this.audio)
        {
            this.audio.loop = true;
            this.button.disable = true;
            this.button.innerHTML = "Play Tone";
            this.isReady = true;
            this.grapher.generatePoints();
        }
        
        console.log("Get audio "+this.audioName,this.audio);
    }
    this.playAudio = function()
    {
        if(this.audio)
        {
            console.log("Play audio "+this.audioName);
            this.audio.play();
            this.button.innerHTML = "Mute Tone";
        }
        else
        {
            this.button.disable = true;
        }
    }
    this.stopAudio = function()
    {
        if(this.audio)
        {
            console.log("Stop audio "+this.audioName);
            this.audio.stop();
            this.button.innerHTML = "Play Tone";
        }
        else
        {
            this.button.disable = true;
        }
    }
    this.getData = function()
    {
        if(this.audio)
        {
            if(this.audio.isPlaying)
            {
                //console.log(this.audio);
            }
        }
    }

    //
    this.button.addEventListener("click", e=>this.handlePress(e));
    this.getAudio();
    //
}

function Grapher(offset, getYPosWithHz, isAudioPlaying)
{
    this.pointPosition = 0;
    this.offset = offset;
    this.getYPosWithHz = getYPosWithHz;
    this.isAudioPlaying = isAudioPlaying;
    this.points = [];
    this.pointsDirty = true;
    this.speed = 1000;
    //

    this.generatePoints = function()
    {
        for(var x=0;x<150;x++)
        {
            this.points.push(new Point(x*4,0));
        }
    }
    //
    this.updatePoints = function(timing)
    {
        //shift to left
        for(var x=0;x<this.points.length-1;x++)
        {
            this.points[x].y = this.points[x+1].y;
        }
        //move last point
        if(this.isAudioPlaying())
        {
            
            this.pointPosition += 0.5; // = timing*this.speed;
            //console.log(this.pointPosition,timing*this.speed,timing);
            var currentY = this.getYPosWithHz(this.pointPosition);
            this.points[this.points.length-1].y = currentY;
        }
        else
        {
            this.pointPosition = 0;
            this.getYPosWithHz(0);
            this.points[this.points.length-1].y = 0;
        }
    }
    //this is only used for the combined graph.
    this.combinePoints = function(otherGraphs)
    {
        //shift to left
        for(var x=0;x<this.points.length-1;x++)
        {
            this.points[x].y = this.points[x+1].y;
        }
        //combine other
        var currentY = 0;
        for(var x=0;x<otherGraphs.length;x++)
        {
            
            currentY += otherGraphs[x].currentY;
        }
        //console.log(currentY);
        this.points[this.points.length-1].y = currentY;
    }
    this.drawPoints = function()
    {
        //if( !this.pointsDirty )
        //    return;        
        graphics.lineStyle(4, 0x00ff00, 1);
        graphics.beginPath();
        
        graphics.moveTo(XOFFSET+this.points[0].x, this.points[0].y*20+this.offset);
        for(var x=1;x<this.points.length;x++)
        {
            graphics.lineTo(XOFFSET+this.points[x].x, this.points[x].y*20+this.offset);
        }
        graphics.strokePath();
        this.pointsDirty = false;
    }
    this.drawBaseLine = function()
    {
        //if( !this.pointsDirty )
        //    return;        
        graphics.lineStyle(1, 0xffffff, 0.5);
        graphics.beginPath();
        
        graphics.moveTo(XOFFSET+this.points[0].x, this.offset);
        graphics.lineTo(XOFFSET+this.points[this.points.length-1].x, this.offset);
    
        graphics.strokePath();    
    }
}

function Point(x,y)
{
    this.x = x;
    this.y = y;
}
//helper function
function listen(element, type, handler) {
  element.addEventListener(type, handler);
  return function() {
    element.removeEventListener(type, handler);
  };
}
