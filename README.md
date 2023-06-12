# scicomp-summer-project

Repository for SciComp 2023 Summer Intern Project.

## Installation

Here are instructions to set up the appropriate virtual environments from the YAML file or manually (the YAML file may not work if you are using a MAC with M1 chip). 


To view the jupyter notebook, use the jupyter environment and open the notebook as follows.
- Create environment from YAML:
```commandline
conda env create -f jupyter_environment.yml
conda activate jupyter
jupyter notebook
```
- Create environment manually:
```commandline
conda create -y -n jupyter jupyter=1.0.0
conda activate jupyter
jupyter notebook
```

To follow through the SLEAP demo, set up a separate sleap environment and open the SLEAP GUI as follows.

- Create environment from YAML:
```commandline
conda env create -f sleap_environment.yml
conda activate sleap
sleap-label
```
- Create environment manually:
```commandline
conda create -y -n sleap -c sleap -c nvidia -c conda-forge sleap=1.3.0
conda activate sleap
sleap-label
```