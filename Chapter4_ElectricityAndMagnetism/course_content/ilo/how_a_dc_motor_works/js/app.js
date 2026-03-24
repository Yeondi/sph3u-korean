var language = language || {};

//

var scene;
var enginePart;
var nSymbol;
var sSymbol;
var plusSymbol;
var negSymbol;
var arrowMove1;
var arrowMove2;
var forceDir1;
var forceDir2;
var currentDirOuter;

window.addEventListener('DOMContentLoaded', function()
{
    doLoad();
});
 
function doLoad()
{
	// get the canvas DOM element
	var canvas = document.getElementById('game-canvas');

	// load the 3D engine
	var engine = new BABYLON.Engine(canvas, true);

	var createScene = function () {

		// This creates a basic Babylon Scene object (non-mesh)
		var scene = new BABYLON.Scene(engine);
		//scene.debugLayer.show();

		// This creates a light, aiming 0,1,0 - to the sky (non-mesh)
		var light = new BABYLON.HemisphericLight("light1", new BABYLON.Vector3(0, 1, 0), scene);
        var light = new BABYLON.HemisphericLight("light2", new BABYLON.Vector3(-1, 1, -2), scene);
		// Camera
    //light.diffuse = new BABYLON.Color3(1, 1, 1);
	//light.specular = new BABYLON.Color3(1, 1, 1);
	//light.groundColor = new BABYLON.Color3(0.6, 0.6, 0.6);

		//scene.camera = new BABYLON.ArcRotateCamera("Camera1", 3 * Math.PI / 2, Math.PI / 2, 30, BABYLON.Vector3(0,0,0), scene);
        scene.camera = new BABYLON.ArcRotateCamera("Camera", 
-2.0054715650876647, 1.4245291773426965, 
4, new BABYLON.Vector3(-0.4, 0.5, 0), scene);
        
        scene.camera.inputs.clear();
        //scene.camera.inputs.addMouse();
        
        //scene.camera = new BABYLON.UniversalCamera("UniversalCamera", new BABYLON.Vector3(-0.3720820224929542, 0.07535147220091183, -0.75217079333057), scene);
        //scene.camera.mode = BABYLON.Camera.ORTHOGRAPHIC_CAMERA;
        
		//scene.camera.attachControl(canvas, true);
		//scene.camera.parent = scene.soccerBall;
		//scene.camera.setPosition(new BABYLON.Vector3(-0.7025925830978504, 0.5176642373515392, -1.4497675848795537));
        
        //scene.camera.rotation = new BABYLON.Vector3(0.10252230565949264, 0.3535281191798699, 0);
		//scene.camera.beta = 1.17;
		scene.camera.speed = 0.1;
        scene.camera.minZ = 0.1;

		// Ball texture
		//var ball = new BABYLON.StandardMaterial("textureBall", scene);
	    //ball.diffuseTexture = new BABYLON.Texture("./assets/images/ball.jpg", scene);
		//ball.backFaceCulling = false;

		
		scene.assetsManager = new BABYLON.AssetsManager(scene);

		scene.billboard = scene.assetsManager.addMeshTask("enginePart", "", "assets/meshes/", "motor.babylon");

		
		/*scene.billboard.onSuccess = function (task) {
            console.log(scene.billboard);
			//task.loadedMeshes[0].position = new BABYLON.Vector3(-20,0,0);		// billboard
			//task.loadedMeshes[0].scaling = new BABYLON.Vector3(0.01,0.01,0.01);
			//task.loadedMeshes[0].rotation.y = Math.PI;
		}*/

        var myMaterial = new BABYLON.StandardMaterial("myMaterial", scene);

        myMaterial.diffuseColor = new BABYLON.Color3(1, 0, 0);
        myMaterial.specularColor = new BABYLON.Color3(0.5, 0.6, 0.87);
        myMaterial.emissiveColor = new BABYLON.Color3(1, 1, 1);
        myMaterial.ambientColor = new BABYLON.Color3(0.23, 0.98, 0.53);



		scene.assetsManager.onFinish = function (tasks) {
			//scene.billboard.loadedMeshes[0].material = ball;
            enginePart = scene.getMeshByName("enginePart");
            nSymbol = scene.getMeshByName("letter_N");
            sSymbol = scene.getMeshByName("letter_S");
            plusSymbol = scene.getMeshByName("sign_plus");
            negSymbol = scene.getMeshByName("sign_negative");
            arrowMove1 = scene.getMeshByName("current_dir_1");
            arrowMove2 = scene.getMeshByName("current_dir_2");
            
            
            forceDir1 = scene.getMeshByName("force_dir_1");
            forceDir2 = scene.getMeshByName("force_dir_2");
            
            currentDirOuter = scene.getMeshByName("current_dir_outer");
            currentDirOuter.rotate(BABYLON.Axis.Z, Math.PI, BABYLON.Space.LOCAL);
            //magnet.material = myMaterial;
//enginePart.rotate(BABYLON.Axis.X,  Math.PI, BABYLON.Space.LOCAL);
            // run the render loop
            
            
            doRotation(0)
			engine.runRenderLoop(function(){
				scene.render();
			});
		};

		scene.assetsManager.load();


		engine.runRenderLoop(function () {
			scene.render();
            //console.log(scene.camera.minZ);
            gameLoop();
		});	

        //Background
        //scene.clearColor = new BABYLON.Color4.FromHexString("#C6CDD0");//new BABYLON.Color3(1, 1, 1);
        scene.clearColor = new BABYLON.Color3(1, 1, 1);
        
        //
        
		scene.registerBeforeRender(function () {
			//scene.camera.target = scene.billboard.position;
		});

		return scene;
	};

	// call the createScene function
	scene = createScene();

	// the canvas/window resize event handler
	window.addEventListener('resize', function(){
		engine.resize();
	});
    
    canvas.tabIndex = -1;
}

var flowSpeedSlider = document.querySelector("#flowSpeedSlider");
let debugText = document.querySelector("#debugText");
let controlButton = document.querySelector("#controlButton");

var direction = 1;
var rotating = false;

var totalRotval = 0;

var radian = 3.14159;
var halfRadian = 1.570795;
var quarterRaidan = 0.7853975;
function gameLoop()
{
    if( !enginePart )
        return;
    if( rotating )
    {
        var rotateVal = direction * flowSpeedSlider.value/50 * Math.PI / 50;// + 0.02 * direction;
        totalRotval += rotateVal;
        
        doRotation(rotateVal);
    }
}  
let flowSpeedSliderInputHandler = event => {
    //debugText.innerHTML = Math.round(event.target.value);
};
flowSpeedSlider.addEventListener("input", flowSpeedSliderInputHandler);

var flip = 1;
function doRotation(rotateVal)
{
    
    enginePart.rotate(BABYLON.Axis.X, rotateVal, BABYLON.Space.LOCAL);
    arrowMove1.rotate(BABYLON.Axis.X, rotateVal, BABYLON.Space.LOCAL);
    arrowMove2.rotate(BABYLON.Axis.X, rotateVal, BABYLON.Space.LOCAL);
    
    //debugText.innerHTML = direction+" "+totalRotval/Math.PI/2;
    if( totalRotval/Math.PI >= 1)
    //if(enginePart._rotationQuaternion.x < 0.78)
    {
        //totalRotval = -0.7853975;
        totalRotval = 0;
        arrowMove1.rotate(BABYLON.Axis.X,  Math.PI * direction, BABYLON.Space.LOCAL);
        arrowMove2.rotate(BABYLON.Axis.X,  Math.PI * direction, BABYLON.Space.LOCAL);

    }
}
                                                                                  
function reverseFlowPress() {
    var pos = plusSymbol.position;
    plusSymbol.position = negSymbol.position;
    negSymbol.position = pos;
    currentDirOuter.rotate(BABYLON.Axis.Z, Math.PI, BABYLON.Space.LOCAL);
    doReverse();   
}

function reverseMagnetPress() {
    var pos = nSymbol.position;
    nSymbol.position = sSymbol.position;
    sSymbol.position = pos;	
    
    doReverse();
}

function doReverse()
{
    direction *= -1;
    forceDir1.rotate(BABYLON.Axis.Y, Math.PI, BABYLON.Space.LOCAL);
    forceDir2.rotate(BABYLON.Axis.Y, Math.PI, BABYLON.Space.LOCAL);
    
    arrowMove1.rotate(BABYLON.Axis.X,  Math.PI * direction, BABYLON.Space.LOCAL);
    arrowMove2.rotate(BABYLON.Axis.X,  Math.PI * direction, BABYLON.Space.LOCAL);
}

function startPause() {
	rotating = !rotating;
    if( rotating )
    {
        controlButton.innerHTML = language.pause;
        controlButton.backgroundColor = "#0e8515";
    }
    else
    {
        controlButton.innerHTML = language.resume;
        controlButton.backgroundColor = "#DEEDDF";
    }
}
function printCamera(){
    console.log(scene.camera);
    console.log(enginePart,enginePart._rotationQuaternion.toEulerAngles());
}
