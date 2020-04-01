# wzvbs-madgraph

Note: The Cards folder is outdated as of now. The commit was made before I knew the madgraph configuration.

Included here is an example of:
1. script to generate events
2. run card
3. param card
4. analysis script

The cards have changes from default values. In run card, the changes are in cuts. The param card needs to be changed corresponding to which variable one would like to assess.

Full process directories can be found on the follow google drive link (https://drive.google.com/drive/u/2/folders/1dfcebeW1XrWNl6G8tJm_6dAHqft2VYmC)

Instructions:
1. Install madgraph v2.6.x (https://launchpad.net/mg5amcnlo). Extract the files, and cd into the new directory.

2. Open smeft-sim-cw-tot . This is only a text file that contains madgraph commands. The set commands are setting up correct madgraph configuration. The import model will automatically download the SMEFT model if you do not already have it. The define lines will make sure multi-particle definitions are consistent between everyone. The generate line will generate all Feynman diagrams for the defined process. In this case, it is the inclusive cross section. 

You will need to change the NP value in line 16 to correspond with which term you would like to generate. More info found here (https://arxiv.org/pdf/1709.06492.pdf)

SM: NP==0,  
Interference: NP^2==1,  
EFT (quadratic): NP==1,  
Total: NP<=1

Finally, set the output to your choice.

3. Run madgraph with the script.

> python2 ./bin/mg5_aMC $PATH_TO_SCRIPT

If you would like to use root analysis, run

> install ExRootAnalysis

4. Now you will want to edit the cards. You can copy the param_card.dat and run_card.dat from here, or edit your own to match. The changes in run_card.dat are in the cuts section. param_card.dat should be edited based on your run preferences. To replicate results, set all coefficients except for the one of interest to 0.

5. cd to your output directory set earlier. run madevent and generate the events.

> python2 ./bin/madevent
> generate_events

You can set analysis packages here to the one of your choice. Reweight and Spin are not used and should be OFF. Next, you can also edit the cards here, but if you have done that before, you can skip this. After that, the events should be generating, which takes about 10-20 minutes for me.

6. The root file is stored in output/Runs/run_xx. The python script above will read electron and positron pT from the file, and make a plot using a SM, SMEFT total with cw=+-1. 
