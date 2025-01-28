## Evaluating Routing Strategies for Emergency Evacuation: A Spatially Explicit Agent-Based Modeling Approach
## Camp Fire Case Study
#### By Rebecca Vandewalle, Furqan Baig, Santiago Nunez-Corrales, Jeon Young Kang, and Shaowen Wang

### Start here
Run the Camp Fire Notebook for a demonstration of the simulation applied to Paradise, CA.

For more detail on how the wildfire evacuation simulation works, refer to the FireABM_Demo_Notebook.ipynb.

### How to run a Jupyter Notebook
The easiest way to run the code is to open the notebook directly with [CyberGISX](https://cybergisxhub.cigi.illinois.edu/) (requires registration) by clicking this link: [Launch with CyberGISX](https://cybergisx.cigi.illinois.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcybergis%2FFireABM_Modeling_Notebook&urlpath=tree%2FFireABM_Modeling_Notebook%2FFireABM_Demo_Notebook.ipynb&branch=master)

To register for CyberGISX you will need a GitHub account and a working email address. Go to the [registration page](https://cybergisxhub.cigi.illinois.edu/registration/) and fill out the form with your information. You may need to validate your email address. Once you have registered you will be able to directly open this notebook in CyberGISX using the above link.

### Key Jupyter Notebooks

- Camp_Fire_Data.ipynb: description of data input and processing needed for the camp fire simulation
- Run_Camp_Fire_Simulation.ipynb: demonstration of how to run the camp fire simulation
- Collect_Simulation_Data.ipynb: shows how to gather individual simulation results into one file
- Graph_Results.ipynb: shows how to use the combined simulation results file to make graphs used in the manuscript
- Graph_Vehicles.ipynb: shows how to use the combined simulation results file to make traffic figures used in the manuscript

### Key Output Files

- Raw simulation result text and video files are stored in three folders: camp_fire_800_quickest, camp_fire_800_dist, and camp_fire_800_major
- Each of these folders has three subfolders: 1files, 1trajs, and 1videos
- the 1files folder contains simulation output for each simulation, such as for each timestamp the number of vehicles that are active, stuck, or clear
- the 1trajs folder contains trajectories (list of road network segments) for each agent in the simulation as well as the timestamp that each agent transfered from one segment to the next
- the 1videos file shows videos of agents leaving the evacuation zone for each simulation run