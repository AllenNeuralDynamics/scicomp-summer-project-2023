# scicomp-summer-project

Repository for SciComp 2023 Summer Intern Project.


## Developer Guideline

If you are not familiar with AppStream, `Appstream-Intro.ipynb` contains a brief overview of AppStream's basic terminology and covers some features of AppStream that has been explored during this project. 

These notebooks have instructions on buiding different kinds of images for AppStream. 

- `Sleap-Windows-Report.ipynb`: Has the most detailed guide ofimage building process for Windows platform
- `Rclone-Windows-Report.ipynb`
- `DLC-Windows-Report.ipynb`
- `Rclone-Sleap-Linux-Report.ipynb`

The `Sleep-Demo.ipynb` notebook contains a simple demonstration of the Sleap Software on a local Windowd computer with no GPU support. `sample_data_analysis.h5` is the sample output from the demonstration. 

The `AppStream-WorkInProgress.ipynb` contains work that are still in progress or work that is already depracated. Attempts at AppStream that have been tried but failed are logged here. 


### Environment Installation

Here are instructions to set up two separate virtual environments for running the jupyter notebook and SLEAP respectively. These instructions work on a Windows 10 machine. 
If you are using a different machine, checkout more detailed instructions to install SLEAP [here](https://sleap.ai/develop/installation.html)

1. Install via Shell script

```commandline
source postinstall.sh
```

2. Install via YAML file

This method only works for setting up the jupyter environment. This method may not work if you are using a MAC with M1 chip. 

```commandline
conda env create -f jupyter_environment.yml
```

3. Install via command line

If none of the above methods work, try installing manually by running the commands below.

```commandline
conda create -y -n jupyter jupyter=1.0.0
conda create -y -n sleap -c sleap -c nvidia -c conda-forge sleap=1.3.0
```

### Environment Activation

To view the jupyter notebook, use the jupyter environment and open the notebook as follows.

```commandline
conda activate jupyter
jupyter notebook
```

To follow through the SLEAP demo, use the sleap environment and open the SLEAP GUI as follows.

```commandline
conda activate sleap
sleap-label
```

## User Guideline

For pose estimation softwares, you can use the Sleap GUI

```commandline
conda activate sleap
sleap-label
```

or the DeepLabCut GUI.

```commandline
conda activate DEEPLABCUT
python -m deeplabcut
```

For mounting S3 buckets on the file system, you can mount them in the foreground with the following command. This process will then occupy the current console. Minimize this console and open another console for other commands. Terminate the process with [ctrl] + [C] or by closing the console to unmount the bucket. 

```commandline
rclone mount s3:aind-appstream-data-dev-temporary MOUNT_PATH
```

You can also mount them in the background with the first command. The console will close immediately and you can open a new console to continue with other commands. Run the second command to unmount all buckets. 

```commandline
rclone mount s3:aind-appstream-data-dev-temporary MOUNT_PATH --no-console

taskkill /F /IM rclone.exe
```