# Fantasy Football Score Visualizer

## Description
This project uses Dr. James Planks' graphing utility "jgraph" in order to create interesting visual output from a given text file. This project specifically takes a fantasy football matchup between two players containing the scores of each position as a text file, then represents the data as a bar graph overlayed over a football field (modified slightly from Dr. Plank's football field provided in lecture notes).

This output can easily and visually show you where your fantasy team succeeded or struggled in a weekly matchup, giving you insight as to what positions you should look to improve upon.

## Instructions to Run

Firstly, ensure that you have python installed (the version this was created with was 3.8.5, but others should work. If you have any issues with something acting strangely, ensure you use this version) Also ensure that you have ps2pdf installed, otherwise the shell scripts will not function properly.

Shell scripts have been provided for your convenience to run this program, so you have a few options.

1. `sh auto.sh`
 - This program runs with no command line arguments, and will create a pdf for each of the 5 example text files provided in the examples directory. The output will be placed into files named ex*.pdf also located in the examples directory, respectively numbered by the text file it was created with.

 2. `sh manual.sh [input file] [output file (no extension)]`
 - This program takes an input file, such as 'examples/ex1.txt' and an output file, such as 'output' as command line arguments. Simply provide both the input file and the desired name of the output file and view the results (as a pdf) in the output file you specified.

 3. `python parse.py [input file] > temp.jgr`

     `./jgr/jgraph -P temp.jgr | ps2pdf - [output file name (with .pdf)]`

- This option is the total manual way to steer this, basically executing the commands the shell scripts run for you. This should really only be used if you want to examine the .jgr file created in detail.

If you have any questions about how to run this program or if you have any unexpected problems, feel free to reach out to me at jmandzak@vols.utk.edu

## Examples

Now that we've gone over how to run the program and what it is, let's go through a few examples.

1. Week 1: Josh vs Aron:
<embed src="./examples/ex1.pdf" type="application/pdf">