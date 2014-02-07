"""
These shouldn't really ever change, except possibly the taxonomy.
"""

#location of studies
studyloc="/home/josephwb/Work/OToL/avatol_nexsons"

#base directory
bdir="/home/josephwb/Work/OToL/treemachine/Synthesis/"

#location of just ott database
dott=bdir+"Life.2.4.draft17.db"
#location of loading database
dload=bdir+"terp.db"
#location of synth database
dsynth=bdir+"terp-synth.db"
#location of synth treefile
treefn=bdir+"terp-synth.tre"
#location of test output
outl=bdir+"testloc"
#trashing the log file
generallogfileloc=bdir+"TRASHLOG"
#java prefix
javapre="java -XX:+UseConcMarkSweepGC -Xmx32g -server -jar"
#location of treemachine
treemloc="/home/josephwb/Work/OToL/treemachine/target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar"