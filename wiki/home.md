# Welcome to the RoboCop wiki!

This is our RoboCop control handbook. Your guide for controling your own robotic hand.

### What is this?
The documentation for all technicals aspects of the robitc hand project. It was created as a result of the ZSWIE 2020 semester summer project.

### Aha?
Our goal was controlling a robotic hand via custom gui. The mechanical part of the hand already existed. It was the result of [another project](LINK). We exchanged the custom controller board with a raspberry pi and created a whole new interface.  
TODO: Video  

### Cool! Can I have that as well?
Of course. And really easy as well. But let us start at the beginning.
#### Giving life to the brain of the arm
Plug in the raspberry pi. It is that simple. It will take some time to fully come alive, so feel free to grab a coffe. The next thing we do is opening the gui. You can even find it in this repository. Simply run the [ADD-SHORTCUT](Create_shortcut_in_repositories_main_directory_for_each_operating_system). If it is your first time, it should now look like this:
[IMAGE](image)  
Here you should enter the local ip of the brain. To find out how to find it, please have a look [here](LINK). The default port used is 1880. If you have not yet messed with the project, You do not need to change it. Otherwise you probably know which port you set it to. The one that the raspberry pi's local node-red server is running on. Oh you want to change it? [No problem](LINK).
Once you save the configuration, it will open the main ui. You will be greeted with this screen:
[IMAGE](image)  
Pretty cool, right? Now you can start moving fingers and making gestures.
#### But nothing is moving
In this case, you still need to bring life to the actual arm itself. Simply connect the power supply. In our case, this means attaching a 7.4V 1500mA power supply. If this info does not help you, please ask someone familiar with electronics. In our case it now looks like this:
[IMAGE](LINK)
Once this is done, we are good to go. Move fingers as you please, save current finger extensions with names

#### So. Many. Questions...
What even is this?  
Am I even connected to same local area network?  
What is my raspberry pis ip?  
Why is the UI not starting?  
I plugged everything in but nothing is happening..?  
How is it working?  
Can I change things?  


### What even is this?
This is a university summer semester project. We where given a mechanical arm, which can move it's fingers. Once we get the servoes inside working. So we connected a raspberry pi, created a small api using node-red, and made a beautifully simple ui.

### Am I even connected to the same local area network?
I can not really help you with that one. But have a look [here](LINK).

### What is my raspberry pis ip?  
This is something you need to find out yourself. Luckily other smart people have already created a lot of guids for exactly this topic. Have a look at [this one]() for example.

### Why is the UI not starting?
The UI is created in [python3](LINK) using the [kivy packLINKage](LINK). Make sure you have those installed first.

### How?
We split the work in three different parts.  
 - Controlling the servoes inside the arm 
 - Creating a gougous gui
 - Connect them together  

All three of them work together to make the final result possible. The servoes inside the arm recieve a voltage provided via a raspberry pi. The raspberry pi is reciving its signal on a locally hosted node-red server. Those signals get set by the gui. But lets take these steps slowly. First we

# Start up the hand
Connect the raspberry pi to its power supply. It will start up its OS and lauch the node-red server. Now it is ready to be connected to. If you just want to move some fingers and fast, you will need a screen connected to the raspberry pi. Open a browser and navigate to [128.0.0.1:1800/ui](128.0.0.1:1800/ui). Here you can find sliders for each of fingers extends. Attach the hands servos to their power supply and watch some fingers wiggle. Congratulations on your success if this is all you ever wanted. If you want to be able to control the hand through our custom extended gui, there are a few more things to to. If you are running it the first time, that is.
First we connect the raspberry pi to the same local area network as our controler will connect to. The second thing is to acquire the local network ip of the raspberry pi. If you want to know how, have a look [here]()

# Start up the gui
To start the gui is a bit more exciting. Especially for the first time. 
??? Python stuffs, please add (requirements, start command)
??? configure ip, please add
Now you should be able to move the fingers, as well as performe and define functions in the gui. Very cool. You want more?

# Start extending the project
If you want to extend the system, you first have to understand it. There are a few things we need to go through. Lets start with the raspberr pi. It is running a local node-red server. You can learn more about this [here](). For changing the servers base values , like the port used, please refer to the node-red documentation. To run the node-red server run `node-red start` in your terminal. This should usually be done automatically at startup. Once the server is running, you can use a browser to change its behaviour. Navigate to [128.0.0.1:1880/]. Here you can find our two flows. There is a backup [in this repository](). To use it, follow [this]() guide.
One flow manages the local online debugging interface. The other one is our api implementation. The api consist mainly of a function node. To get into it, some JavaScript knowedge is required. Furthermore you should have a look at the node-red flow system and the message object passed between them.  
Next we will have a look at the python api_wrapper package. You can find it [here]() It creates HTTP requests for the fingers as needed. If you want to create a new ui, you can still use this package for your convenience.
