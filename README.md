# Rock, Paper, Scissors

This is a quick python and docker example I created to demo some basic docker functionality to fellow employees.
It's also a fun little CLI ascii text rock, paper, scissors game that has entertained my kids for hours.

To get started:
 * Install Docker
 * Cloning this repo

Note: I use a mac for development and haven't tested this elsewhere.

## Docker
There are just a couple simple docker commands to get you up and playing this game.  
Run these commands from the directory that contains your code and the Dockerfile.  

To see what Docker containers you have on your system, you can run the following command.  
The -a flag lists all containers.  Without the -a flag, only running containers will be shown.

```docker ps -a``` 

This command will build your new docker image from the Dockerfile

```docker build -t rockpaperscissors .```

Running this will list all available Docker images:

```docker images``` 
 
This command will just list your rockpaperscissors image

```docker images rockpaperscissors```

From a command line, running the command will run your container and allow you to play the game.  
* The -i flag allows your container to be interactive 
* The --rm will remove your container after running

```docker run -ti --rm rockpaperscissors```


That's it for this simple demo.  Enjoy playing!


Credit:
Thanks to https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe for the rock, paper, scissors ascii art.