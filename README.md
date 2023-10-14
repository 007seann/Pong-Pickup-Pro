# Pong-Pickup-Pro

Pong-Pickup-Pro autonomously moves toward a ball and collects it with the suction mechanism. 

![Pong-Pickup-Pro Prototype](https://github.com/007seann/Pong-Pickup-Pro/blob/902d067e54840020d80ea893cf08a1c365ee2d70/PPP%20prototype.jpg)
![Pong-Pickup-Pro](https://github.com/007seann/Pong-Pickup-Pro/blob/902d067e54840020d80ea893cf08a1c365ee2d70/poster.png)
Abstract 

This project consists of an autonomous robot tasked with collecting ping pong balls and delivering them to the user when prompted. This system relies on a few separate functionalities. The robot must be able to map its environment accurately. This is so that the robot does not travel out of the intended area during collection, correctly locates the specified location near the user for delivery and to remain idle at a specific location under the table when collection is not prompted by the user. An accurate representation of the environment is required for these tasks to be completed successfully. Next, for collection of the balls to be successful, the robot needs to be able to recognise the balls with a low rate of error and successfully plan a path to the balls while avoiding obstacles if necessary. The robot uses a vacuum mechanism to collect the balls and stores them in a compartment attached to itself. After collection is completed, the robot travels to a specified location and returns the balls by raising the compartment up to a reasonable height for the user to collect. It then returns under the table, so as to not interrupt play, and waits for further instruction. This project aims to greatly reduce the trouble of manually picking up ping pong balls, especially for people with lack/loss of mobility, thus maximising playing time for all players.

Here is a YouTube presentation of the project. </br>
Here are the relevant documents for the project. 

# Project Design

photo 1
![PPP design2](https://github.com/007seann/Pong-Pickup-Pro/blob/902d067e54840020d80ea893cf08a1c365ee2d70/diagram2.png)
photo 2
![PPP design](https://github.com/007seann/Pong-Pickup-Pro/blob/902d067e54840020d80ea893cf08a1c365ee2d70/diagram1.png)

# Test Outcome
![PPP test](https://github.com/007seann/Pong-Pickup-Pro/blob/902d067e54840020d80ea893cf08a1c365ee2d70/test1.png)
