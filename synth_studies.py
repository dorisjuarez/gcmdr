import load_synth_extract

from plants import studytreelist as plantslist
from metazoa import studytreelist as metalist
from fungi import studytreelist as fungilist
from microbes import studytreelist as microbelist

studytreelist = []
studytreelist.extend(plantslist)
studytreelist.extend(metalist)
studytreelist.extend(fungilist)
studytreelist.extend(microbelist)

if __name__ == "__main__":
    from wopr_conf_TEMP import *
    
    # synthottolid="805080" # life
    synthottolid="93302" # cellular organisms
    
    studytreelist = [
    "2829_6579", # Thraupidae. Burns et al. 2014. MPE
    "2858_6642", # Turdidae. Nylander et al. 2008. Syst. Biol.
    "1953_3977", # Furnariidae. Derryberry et al. 2001. Evolution 
    ]
    
    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "synth_studies/" + i + ".log"
        ttfntreefn = "synth_studies/" + i + ".tre"
        load_synth_extract.run_load_single_ttfn(dott,dload,studyloc,tstudy_list,javapre,
                                                treemloc,generallogfileloc,dsynth,synthottolid,treefn,ttfntreefn)



