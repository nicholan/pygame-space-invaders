# pygame-space-invaders

My first simple game project done with pygame, adapted from Matthes, E. (2019). Python crash course: A hands-on, project-based introduction to programming. no starch press.

The game is basically space invaders; player can move on the x-axis at the bottom of the screen and shoot bullets up the y-axis. Rows of enemies are created on the screen; enemies move left and right, changing direction and moving down the screen when an enemy hits an edge of the screen. A bullet colliding with an enemy grants points and removes the enemy from the screen. If an enemy collides with the player character or the bottom of the screen, player loses one life and a new enemy fleet will be created. Everytime player clears a fleet of enemies, the next fleet will move faster on the x-axis. 

Creating this game was an exercise for me in working with classes, separating code in modules, and getting to learn the pygame framework. 

