# MadGraph tutorial and WZ VBS guide

Note: The Cards folder is outdated as of now. The commit was made before I knew the madgraph configuration.

Included in this repo is an example of:
1. script to generate events
2. run card
3. param card
4. analysis script

The cards have changes from default values. In run card, the changes are in cuts. The param card needs to be changed corresponding to which variable one would like to assess.

Full process directories can be found on the follow google drive link (https://drive.google.com/drive/u/2/folders/1dfcebeW1XrWNl6G8tJm_6dAHqft2VYmC)

For reference, here are the slides: https://docs.google.com/presentation/d/1k3s4BwQIYrz0HTTbY98qibA8hlAi6nlqUY4xTcI-Kb4/edit#slide=id.g88e0da113c_0_31

# Instructions

I highly reccomend people using Windows to set up a linux install or linux virtual machine. 

1. Make sure you have a fortran compiler, like gcc-fortran, and python2. For analysis, root or pyroot is usually used in this group.

2. Install madgraph v2.6.x (https://launchpad.net/mg5amcnlo/+download). Extract the files from the tarball to your desired location, and cd into the new directory. To start madgraph use

> python2 bin/mg5_aMC

You should be in the madgraph program, the terminal should display an input line that looks something like this

> MG5_aMC>

# Introductory tutorial

madgraph has a good built in tutorial for p p > t t~. To begin this tutorial, simply type tutorial into madgraph.

> tutorial

It should print steps to help guide you to determine the cross section of this process.

If you would like, you can edit the beam energies in run_card.dat and see how that effects the cross section. The top quark a very massive quark, so how would you expect the cross section to depend on the beam energy? The most recent LHC run was at a center-of-mass energy of 13 TeV, but older runs were lower energy. The earliest run was about 900 GeV beam energy (or 1.8 TeV center-of-mass energy), what would the cross section be in this case? How about higher energies?

To analyze the results, you can install MadAnalysis5, or ExRootAnalysis. Most groups will use root in their analysis, but you can stick with what you prefer for this. If you do not use root, you will have to read the output .lhe file, which is a text file, and parse it for the information you need.

Either way, you will need to know the particle id's (http://pdg.lbl.gov/2007/reviews/montecarlorpp.pdf) where the anti-particles take the negative value of the particle ID. The example script reads many madgraph runs and plots a histogram of the transverse momentum of particles with id +11 and -11, which correspond to electrons and positrons.

# WZ VBS guide

1. Open smeft-sim-cw-tot . This is only a text file that contains madgraph commands. The set commands are setting up correct madgraph configuration. The "import model" line in the event generation script will automatically download the SMEFT model if you do not already have it. The define lines will make sure multi-particle definitions are consistent between runs. The generate line will generate all Feynman diagrams for the defined process. In this case, it is the inclusive cross section for purely leptonic WZ scattering. 

You will need to change the NP value in line 16 to correspond with which term you would like to generate. More info found here (https://arxiv.org/pdf/1709.06492.pdf). NP stands for "new physics". SMEFT treates the standard model as an effective field theory, or a low energy approximation of another theory. The NP value dictates how strong the effects of the "new physics" is.

SM: NP==0,  
Interference: NP^2==1,  
EFT (quadratic): NP==1,  
Total: NP<=1

Finally, set the output to your choice.

3. Run madgraph with the script.

If you would like to use root analysis, run

> install ExRootAnalysis

> python2 ./bin/mg5_aMC $PATH_TO_SCRIPT

4. Now you will want to edit the cards. You can copy the param_card.dat and run_card.dat from here, or edit your own to match. The changes in run_card.dat are in the cuts section. param_card.dat should be edited based on your run preferences. To replicate results, set all coefficients except for the one of interest to 0.

5. cd to your output directory set earlier. run madevent and generate the events.

> python2 ./bin/madevent
> generate_events

You can set analysis packages here to the one of your choice. Reweight and Spin are not used and should be OFF. Next, you can also edit the cards here, but if you have done that before, you can skip this. After that, the events should be generating, which takes about 10-20 minutes for me on a mid-tier laptop.

6. The root file is stored in output/Runs/run_xx. The python script above will read electron and positron pT from the file, and make a plot using a SM, SMEFT total with cw=+-1. Make sure to adjust the directories to your own.
