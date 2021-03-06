"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""

import load_synth_extract


studytreelist=[
               "244_3855",  # Gnetum, generic level. Won and Renner. 2006. Syst. Biol.
               "2879_6674", # Almost all Bryophyta genera. Cox et al. 2010. Phytotaxa
               "2878_6673", # Lepechinia; generic level. Drew et al. 2013. Bot. J. Linn. Soc.
               "412_2166",  # Coniferophyta; 492 taxa; almost all genera monophyletic. Leslie et al. 2012. PNAS
               "2827_6577",#Ilex NEW
               "1022_1967",#Pontederiaceae
               #"194_2284",#early and nymphaeles
               "562_817", #Poales
               "424_532", #Lonicera
               "1916_3902", #Brassicaceae
               "588_878", #Asparagales
#              "826_1584", #rosaceae #this is actually a fungal tree
               "926_1825",#rosaceae
               "1133_5647", #Rosales
               "2624_6139", #Veronica
               "2128_4437",#Plantago
               "1102_2177",#Collinsia
               "625_1016", #   Hoheria
               "761_1415", #   Drosera
               "2048_4220", #  allium
               "1264_2544",#isoetes
               "1129_2251", #  Solanum
               "1842_3724", #  Oxalis
               "288_5028", #   Croton
               "754_1392", #   Ribes
               "1137_2295", #  Erythronium
               "1109_2201", #  Castilleja
               "2004_4118",#cyrtandra
               "385_458", #    Begonia
               "1843_3725", #  Euphorbia
               "1858_3754", #  Euphorbia
               "330_325", #    Santalum
               "394_483", #   Cucumis
               "56_5821", #  Tsuga
               "53_1280", #  Euryops
               "62_2878", #  Lymania
               "77_5878", #  Anaxagorea
               "2841_6597", #    Sparganium
               "1118_2226", #Mentheae,lamiaceae
               "2669_6213", #Lamiaceae
##               "19_6175", #Verbenaceae
               "2032_5922",#Ruella
               "1901_3877",#Lentibulariaceae
               "713_1287", #Lamiales
               "1131_2265", #Saxifragaceae
               "2608_6288", #saxifrigales
               "2539_6294",#Soltis et al. 2011 ML tree
 #             "2539_5465",#Soltis et al. 2011 bootstrap
 	       "2820_6566",#Streptophyta
               "2712_6296", #Rosids
               "259_142", #Cercis FABALES!
               "264_150", #Coursetia FABALES!
               "267_161", #Ateleia (Swartzieae-Leguminosae) FABALES!
               "2077_4291", #Podalyria (Fabaceae, Podalyrieae) FABALES!
               "293_201", #Mimosa FABALES!
               "197_784", #Phaseolus FABALES!
               "595_896", #Senna FABALES!
               "131_6236", #Trifolium FABALES!
               "2689_6241", #Lupinus FABALES!
               "597_906", #Machaerium (Leguminosae) FABALES!
               "2001_4100", #Astragalus FABALES!
               "606_5290", #Trifolieae and Vicieae FABALES!
               "54_949", #Indigofereae FABALES!
               "596_901", #Genisteae (Leguminosae) FABALES!
               "294_202", #Detarieae (Caesalpinioideae) FABALES!
               "292_199", #(Diocleinae: Papilionoideae) FABALES!
	       "58_775", #Crotalarieae (Fabaceae) FABALES!
               "548_798", #Vigna FABALES!
               "2055_4234",  #Genistoid legumes FABALES!
               "2057_4240", #papilionoid FABALES!
               "2127_4426", #Papilionoideae; Vataireoid Clade FABALES!
               "594_890", #robinioid legumes FABALES!
               "261_145", #Caesalpinieae FABALES!
               "57_777", #Podalyrieae (Fabaceae) FABALES!
               "78_6237", #phaseoloid FABALES!
               "78_5858", #phaseoloid FABALES!
               "2690_6243", #Fabaceae FABALES!
               "2045_4213", #Acacia FABALES!
               "605_947", #Strophostyles (Fabaceae) FABALES!
               "271_5017", #Polygalaceae FABALES!
               #"265_153", #Fabales FABALES!
               #"998_2313", #Fabales
               "2661_6198", #Ericales
               "2645_6165",#Menispermaceae
               "2644_6164",#Ranunculales
               "2610_6117", #malpighiales tree, the best one we have right now, we think6
               "2642_6161",#Cayophyllales; not sure if you have a better study here)
               "2052_4228",#Lundia
               "1103_2178",#Bignonieae
               "14_12", #Bignoniaceae
               "2140_4483",#Annonaceae
               "2648_6171",#Marchantiales
               "650_1147",#Meliaceae, Sapindales
               "2085_4317",#Araceae
               "2044_4212",#Orobanchaceae
               "2626_6142",#Amaranthaceae
               "2598_6020",#Boraginaceae
               "2564_5699",#Polystichum
               "2042_4202",#Bartramiaceae
##               "2034_4191",#Ruellieae
               "2000_4098",#Coffea
               "20_2162",#Gallium
               "1101_2172",#Rubieae
               "2565_5708",#Ericoideae
               "1094_2138",#Apocynaceae
               "2641_6160",#Rubiaceae
               "99_5885",#Barnadesioideae
               "275_167",#Celastraceae
               "93_1411",#Symplocos
               "30_2281",#Illicium
               #"36_36",#Dendropanax NOT ROOTED AND PROBABLY NOT GREAT
               "898_1732",#Schefflera
               "216_5865",#Hedera
               "901_1740",#Meryta
               "2830_6583",#brassaiopsis
               "2831_6584",#Escallonia
               "719_1296",#Nymphoides
               "1975_4041",#Tragopogon
               "1821_3678",#Helichrysum
               "1583_3194",#Gaillardia
               "1581_3188",#Dubautia
               "1575_3164",#Tolpis
               "332_333", #    Polygonaceae
               "1573_3144",#Onoseris
               "934_1832",#Echinops
               "200_6585",#Encelia
               "152_5743",#Coreopsis
               "53_1281",#Euryops
               "2076_4282",#Garrya 
               "2832_6586",#Sedum    
               "37_5871",#Rhus 
               "50_1397",#Anagallis 
               "1866_3765",#Thesium (Santalaceae)
               "59_5731",#Aristolochiaceae
               "73_5787",#Passiflora
               "80_5881",#Rhododendron
               "81_5863",#Pinus
               "82_5792",#Campanula
               "88_5848",#Erodium
               #"231_5505", #caryoph SOME SORT OF LOADING PROBLEM
               "180_794",#Araceae
               #"574_840",#Asparagales upload problems
               "576_849",#Alocasia (Araceae)
               "581_859",#Crocus (Iridaceae)
               "582_862",#Mermuellera (Poaceae)
               "598_926",#Poeae (Poaceae)
               "599_927",#Costaceae
               "603_940",#Maxillaria (orchidaceae)
               "704_1266",#Molluginaceae
               "721_1298",#Commelinaceae
               "723_1300",#Triticum
               #"724_3212",#Pleurothallidinae (Orchidaceae) upload problems
               "921_4103",#Oryzeae (Poaceae)
               "1300_2613",#Hymenophyllum (Hymenophyllaceae)
               #"1302_2616", make for weird euphyllophyta
               "1962_6580",#Viburnum Clement and Donoghue 2011
               "915_1802",#Viburnum
               "915_1803",#Valerianaceae
               "2625_6140",#Utricularia
               "1130_2258",#Nicotiana
               "2047_4217",#Cuscuta
               "386_459",#Brunsfelisia
               "139_5860",#Nierembergia
               "126_2233",#Solanum
               "136_5857",#cestrum               
               "9_1",#Campanulidae
               "2828_6578",#caprifolieae Smith 2009 NEW
               "142_38",#Asclepias
               "2638_6157",#Santalales
               "21_37",#Solanaceae
               "72_801",#Malpighiaceae
               "75_1743",#Apioideae
               "1974_4038",#PolygonaceaeS
               "1974_4039",#Rheum
               #"535_768",#Eriogonoideae
               "61_816",#Bromeliaceae
##               "284_185",#Cucurbitaceae
               "2546_5493",#Sapindaceae
               #"1086_2111",#Cactaceae
               "41_1396",#Feddea
               "283_184",#Celastrales
               #"1116_2217",#Lamiales (Oxelman 2005)
               "225_5991",#deep plants
               "1867_3766", #cycads
               "1278_2572",#Liverworts
               "1268_2560",#hornworts
               "412_2166",#conifers
               "787_1489", #   Ephedra
               "2046_5928" #Trebouxiophyceae, Chlorophyta
               ]
studytreelistTF = [True] * len(studytreelist)

if __name__ == "__main__":
	from stephen_desktop_conf import *

	synthottolid="10218"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)

