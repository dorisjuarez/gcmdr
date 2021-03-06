from general_tm_utils import *
from general_utils import *

studytreelist=[
              "2710_6291",  # Metazoa. Ryan et al. 2013. Science *** need to choose best Metazoa tree(s)
              "413_524",
              "2867_6658", # philippe et al 2009
              "2868_6660" #pick et al 2010
            ]

studytreelistTF = [True] * len(studytreelist)

if __name__ == "__main__":
	synthottolid = "691846" #Metazoa
	print "loading studytreelist:",studytreelist
	depth = 3
	#location of studies
	studyloc="/media/data/avatol_nexsons"
	#location of just ott database
	dott="/media/data/neo4j-community-1.8/data/gol.ott_2_6_draft2.db_just_ott"
	dload="/media/data/neo4j-community-1.8/data/metazoa_conflict_loading.db"
	#java prefix
	javapre="java -XX:+UseConcMarkSweepGC -Xmx32g -server -jar"
	#location of treemachine
	treemloc="/media/data/Dropbox/programming/eclipse/opentree-treemachine/target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar"
	generallogfileloc = "TEMP"
	outfn = "/media/data/metazoa_conflict.graphml" #name of the graph figure file
	delete_database(dload)
	copy_database(dott,dload)
	mapcompat = studytreelistTF
	print "loading trees"
        
	for i in studytreelist:
		load_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
	count = 0
	for i in studytreelist:
		if mapcompat[count] == True: 
			mapcompat_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
		count += 1
        
	print "extracting"
	extract_graphml(javapre,treemloc,dload,synthottolid,outfn,depth)
