Preparatory Work
============================================================
To begin with, please register or log in to ["StochSS"](https://live.stochss.org/hub/stochss).
<p align="center">
  <img src="https://github.com/SihaiYu/Combining-Non-Output-Oblivious-Discrete-CRNs/assets/100762924/e2810009-d190-40b4-b59e-3694496f9a37">
</p>


Enhancing Reliability of Composed Non-Output-Oblivious Chemical Reaction Networks
============================================================

## Download this zip file and upload it to StochSS for simulation and viewing simulation results

The ["Composing Non-Output-Oblivious Discrete CRNs"](https://github.com/SihaiYu/Composing-Non-Output-Oblivious-Discrete-CRNs/blob/main/Composing%20Non-Output-Oblivious%20Discrete%20CRNs.zip) file contains the configuration files related to the exploration conducted by Sihai Yu et al. in "Enhancing Reliability of Composed Non-Output-Oblivious Chemical Reaction Networks".

1. Log in to StochSS, then click on "Browse your projects".
<p align="center">
  <img src="https://github.com/SihaiYu/Combining-Non-Output-Oblivious-Discrete-CRNs/assets/100762924/c4f5498b-a2f9-484e-8f72-160ff7c28251">
</p>

2. Locate the "File Browser" at the bottom of the page and click on the "+" button.
<p align="center">
  <img src="https://github.com/SihaiYu/Combining-Non-Output-Oblivious-Discrete-CRNs/assets/100762924/5d1fcd4d-6761-4897-a389-da27efc41388">
</p>

3. Upload the zip file.
<p align="center">
  <img src="https://github.com/SihaiYu/Combining-Non-Output-Oblivious-Discrete-CRNs/assets/100762924/2cec7dd1-7748-4984-a7a8-4739eb264b7f">
</p>

4. View the simulation results in the "Project Browser".
<p align="center">
  <img src="https://github.com/SihaiYu/Composing-Non-Output-Oblivious-Discrete-CRNs/assets/100762924/381d0ff8-9638-4f3a-ba7b-899879da2b76">
</p>

<p align="center">
  <img src="https://github.com/SihaiYu/Composing-Non-Output-Oblivious-Discrete-CRNs/assets/100762924/3a21960e-51fa-40e8-9700-25e47f2ce010">
</p>

## Calculate the accuracy of simulation experiment results

Since StochSS does not provide specific functionality for calculating the accuracy of multiple experiments within the workflow, we wrote a Python program ["Accuracy Statistics"](https://github.com/SihaiYu/Composing-Non-Output-Oblivious-Discrete-CRNs/tree/main/Accuracy%20Statistics) to parse the JSON files corresponding to the results images and further calculate the accuracy.

1. Select the corresponding workflow.
<p align="center">
  <img src="https://github.com/SihaiYu/Composing-Non-Output-Oblivious-Discrete-CRNs/assets/100762924/4d3f23d3-d9ba-4e46-8b44-d6f9c5ea1345">
</p>

2. Download the JSON file for "Plot Trajectories"
<p align="center">
  <img src="https://github.com/SihaiYu/Composing-Non-Output-Oblivious-Discrete-CRNs/assets/100762924/3213de3e-57f9-4ecd-ac6c-175d4318dbd35">
</p>

3. To process the original JSON file, need to remove the certain content at the beginning and end.
<p align="center">
  <img src="https://github.com/SihaiYu/Composing-Non-Output-Oblivious-Discrete-CRNs/assets/100762924/9b2f7fdd-ea51-4586-8ad1-b7c5055df491">
</p>

<p align="center">
  <img src="https://github.com/SihaiYu/Composing-Non-Output-Oblivious-Discrete-CRNs/assets/100762924/2f856b14-c585-42c6-977a-7b45f0f30fe">
</p>

4. Run ["run_this.py"](https://github.com/SihaiYu/Composing-Non-Output-Oblivious-Discrete-CRNs/blob/main/Accuracy%20Statistics/run_this.py).

5. Supplement
   We have already processed all JSON files in ["JSON.zip"](https://github.com/SihaiYu/Composing-Non-Output-Oblivious-Discrete-CRNs/blob/main/Accuracy%20Statistics/JSON.zip) by removing the certain content at the beginning and end. Simply unzip these JSON files to the same folder as the ["run_this.py"](https://github.com/SihaiYu/Composing-Non-Output-Oblivious-Discrete-CRNs/blob/main/Accuracy%20Statistics/run_this.py) file, and then run ["run_this.py"](https://github.com/SihaiYu/Composing-Non-Output-Oblivious-Discrete-CRNs/blob/main/Accuracy%20Statistics/run_this.py).










