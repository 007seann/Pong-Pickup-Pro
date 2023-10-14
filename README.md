# Pong-Pickup-Pro

Pong-Pickup-Pro autonomously moves toward a ball and collects it with the suction mechanism. 

<div style="display: inline-block;">
  <img src="https://github.com/007seann/Pong-Pickup-Pro/blob/df56293d2162b62665863c9e296366659079a806/PPP%20prototype.jpg" alt="Image 1" width="45%" />
  <img src="https://github.com/007seann/Pong-Pickup-Pro/blob/df56293d2162b62665863c9e296366659079a806/poster.png" alt="Image 2" width="45%" />
</div>
<br></br>

<span style="font-size: 54px;">**Abstract**</span>

This project consists of an autonomous robot tasked with collecting ping pong balls and delivering them to the user when prompted. This system relies on a few separate functionalities. The robot must be able to map its environment accurately. This is so that the robot does not travel out of the intended area during collection, correctly locates the specified location near the user for delivery and to remain idle at a specific location under the table when collection is not prompted by the user. An accurate representation of the environment is required for these tasks to be completed successfully. Next, for collection of the balls to be successful, the robot needs to be able to recognise the balls with a low rate of error and successfully plan a path to the balls while avoiding obstacles if necessary. The robot uses a vacuum mechanism to collect the balls and stores them in a compartment attached to itself. After collection is completed, the robot travels to a specified location and returns the balls by raising the compartment up to a reasonable height for the user to collect. It then returns under the table, so as to not interrupt play, and waits for further instruction. This project aims to greatly reduce the trouble of manually picking up ping pong balls, especially for people with lack/loss of mobility, thus maximising playing time for all players.

Here is a [YouTube presentation](https://youtube.com/shorts/jVamBR7NoEc?feature=shared) of the project. </br>

Here are [the relevant documents](https://github.com/007seann/Pong-Pickup-Pro/tree/ee2234f18c8329ad9c5b863a30b7155e92f4e1e4/documents) for the project. 


# Project Design


<br><span style="font-size: 54px;">**Hardware Design** </span></br>
<br></br>
<br></br>
![PPP design2](https://github.com/007seann/Pong-Pickup-Pro/blob/902d067e54840020d80ea893cf08a1c365ee2d70/diagram2.png)
<br></br>
<br></br>

<br><span style="font-size: 54px;">**Software Design** </span></br>
![PPP design](https://github.com/007seann/Pong-Pickup-Pro/blob/902d067e54840020d80ea893cf08a1c365ee2d70/diagram1.png)

# Test Outcome
![PPP test](https://github.com/007seann/Pong-Pickup-Pro/blob/902d067e54840020d80ea893cf08a1c365ee2d70/test1.png)
