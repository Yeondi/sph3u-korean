var language = language || {};

//
var config = {
        type: Phaser.AUTO,
        width: 670,
        height: 370,
        parent: "phaser-Container",
        scene: {
            preload: preload,
            create: create,
            update: update
        },
        backgroundColor: '#ffffff'
    };

var game = new Phaser.Game(config);
//Constants
let WEIGHTHEIGHT = 16;
let HOOKHEIGHT = 180;
let MAXWEIGHT = 3;
let ONENEWTONDISTANCE = 2.5;
var _this = this;

//Model of the scale
function Scale()
{
    this.gravity = 9.8;
    this.mass = 0;
    //
    this.ChangeGravity = function(newGravity)
    {
        if( newGravity=="earth" )
            this.gravity = 9.8;
        else if( newGravity=="moon" )
            this.gravity = 1.625;
        else if( newGravity=="jupiter" )
            this.gravity = 24.79;
        else 
            this.gravity = 0;
    }
    this.CalculateWeight = function()
    {
        return Math.floor(100*this.mass * this.gravity)/100;
    }
    this.AddMass = function()
    {
        this.mass++;
        if(this.mass>MAXWEIGHT)
        {
            this.mass = MAXWEIGHT;
            //disable button
        }
        return this.mass;
    }
    this.RemoveMass = function()
    {
        this.mass--;
        if(this.mass<0)
            this.mass = 0;
        return this.mass;
    }
}
function ScaleVisual(model)
{
    this.model = model;
    this.hook;
    this.hookInner;
    this.weights = [];
    
    this.tween;
    this.targetLocation = 0;
    
    this.UpdateWeights = function()
    {
        var diff = this.model.mass - this.weights.length;
        if(diff>0)
        {
            //add 1
            for(var x=0;x<diff;x++)
            {
                var w = _this.add.image( this.hookInner.x + 10, this.hookInner.y, 'weight');//.setOrigin(0, 0);
                this.hook.add(w);
                this.weights.push(w);
                w.y = HOOKHEIGHT - WEIGHTHEIGHT * this.weights.length
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
    this.DoChangeMove = function()
    {
        var target = this.model.CalculateWeight();
        
        this.targetLocation = target*ONENEWTONDISTANCE
        //this.hook.y = this.targetLocation;
        if(this.tween)
            this.tween.stop();
        
        this.tween = _this.tweens.add({
        targets: this.hook,
        props: {
                y: { value: this.targetLocation, duration: 1000, ease: 'Bounce.easeOut' }
            }
        });
        
    }
}
//
var scaleModel1 = new Scale();
var scale1 = new ScaleVisual(scaleModel1);
var scaleModel2 = new Scale();
var scale2 = new ScaleVisual(scaleModel2);
var scaleModel3 = new Scale();
var scale3 = new ScaleVisual(scaleModel3);

/**
*
*
*
*/
function preload ()
{
    //this.load.setBaseURL('http://labs.phaser.io');
    
    this.load.image('sky', 'assets/space3.png');
    this.load.image('hook', 'assets/images/hook.png');
    this.load.image('scale', 'assets/images/scale.png');
    this.load.image('weight', 'assets/images/weightWithkg.png');
}


var hook1, hook2, hook3;
function create ()
{    
    _this = this;
    this.add.image(40, 20, 'scale').setOrigin(0, 0);
    this.add.image(245, 20, 'scale').setOrigin(0, 0);
    this.add.image(447, 20, 'scale').setOrigin(0, 0);
    
    createHook(hook1, scale1, 63);
    createHook(hook2, scale2, 273);
    createHook(hook3, scale3, 470);
    
    bindUI();
}
function createHook(hook, scale, offset)
{
    hook = _this.add.container(0, 0);    
    var h = _this.add.image(offset+10, 35, 'hook').setOrigin(0, 0);
    hook.add(h);
    scale.hook = hook;
    scale.hookInner = h;
}
function update ()
{
}


var hookup1, hookup2, hookup3;

function bindUI()
{
    hookup1 = new UIHookup(1, scale1, scaleModel1);
    hookup2 = new UIHookup(2, scale2, scaleModel2);
    hookup3 = new UIHookup(3, scale3, scaleModel3);
}

/**
*
*
*
*/
function UIHookup(num, scale, scaleModel)
{
    this.num = num;
    this.scale = scale;
    this.scaleModel = scaleModel;
    this.UIHookup = this;
    //Constructor
    
    this.select = document.querySelector("#select"+this.num);
    this.add = document.querySelector("#add"+this.num);
    this.remove = document.querySelector("#remove"+this.num);
    this.output = document.querySelector("#value"+this.num);
    //
    this.changeGravity = function()
    {
        this.scaleModel.ChangeGravity(this.select.options[this.select.selectedIndex].value);
        this.scale.DoChangeMove();
        this.updateOutput();
    }
    this.doAdd = function()
    {
        this.scaleModel.AddMass();
        this.scale.UpdateWeights();
        this.scale.DoChangeMove();
        this.updateOutput();
        this.remove.disabled = false;
        if (this.scaleModel.mass >= MAXWEIGHT) {
            this.add.disabled = true;
        }
    }
    this.doRemove = function()
    {
        this.scaleModel.RemoveMass();
        this.scale.UpdateWeights();
        this.scale.DoChangeMove();
        this.updateOutput();
        this.add.disabled = false;
        if (this.scaleModel.mass === 0) {
            this.remove.disabled = true;
        }
    }
    //    
    listen(this.select, 'change', e => this.changeGravity(e));
    listen(this.add, 'click', e => this.doAdd(e));
    listen(this.remove, 'click', e => this.doRemove(e));
    
    //
    this.updateOutput = function()
    {
        this.output.innerHTML = ""+ this.scaleModel.CalculateWeight()+" N ("+this.scaleModel.mass+" kg "+" x "+this.scaleModel.gravity+" N/kg)";
    }
    this.updateOutput();
}
//helper function
function listen(element, type, handler) {
  element.addEventListener(type, handler);
  return function() {
    element.removeEventListener(type, handler);
  };
}

//is this needed?
document.querySelector('button').addEventListener('click', function() {
  context.resume().then(() => {
    console.log('Playback resumed successfully');
  });
});