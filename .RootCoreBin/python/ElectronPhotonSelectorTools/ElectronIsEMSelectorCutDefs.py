# default configuration of the ElectronIsEMSelectorCutDefs
# This one is used for stadard loose, medium, and tight, not ++ menu

import cppyy
try :
    cppyy.loadDictionary('ElectronPhotonSelectorToolsDict')
except :
    pass

from ROOT import egammaPID

# Import a needed helper
from PATCore.HelperUtils import *

# Define GeV
GeV = 1000.0

def ElectronIsEMSelectorConfig2011(theTool) :
    '''
    These are the "classic" isEM definitions: Loose, Medium, and Tight.
    '''
    
    theTool = GetTool(theTool)

    # the eta ranges
    theTool.CutBinEta += [0.1, 0.6, 0.8, 1.15, 1.37, 1.52, 1.81, 2.01, 2.37, 2.47]
    # range of ET bins for e-ID
    theTool.CutBinET += [5.0*GeV, 10.0*GeV, 15.0*GeV, 20.0*GeV, 30.0*GeV, 40.0*GeV, 50.0*GeV, 60.0*GeV, 70.0*GeV, 80.0*GeV]
    # cut on fraction of energy deposited in 1st sampling
    theTool.CutF1 += [0.005]
    
    # cut on hadronic energy
    #  |eta|             0.0   0.1    0.6    0.8   1.15   1.37   1.52   1.81   2.01  2.37    2.47
    theTool.CutHadLeakage  += [0.031, 0.031, 0.021, 0.021, 0.019, 0.028, 0.065, 0.065, 0.046, 0.034, # < 5   GeV
			   0.018, 0.018, 0.016, 0.015, 0.016, 0.028, 0.053, 0.038, 0.028, 0.025, # 5-10 
			   0.015, 0.015, 0.014, 0.014, 0.016, 0.020, 0.039, 0.032, 0.027, 0.023, # 10-15 
			   0.012, 0.012, 0.010, 0.010, 0.012, 0.015, 0.029, 0.022, 0.015, 0.021, # 15-20 
			   0.010, 0.010, 0.010, 0.010, 0.010, 0.010, 0.020, 0.015, 0.014, 0.014, # 20-30 
			   0.008, 0.008, 0.008, 0.008, 0.008, 0.010, 0.014, 0.015, 0.010, 0.010, # 30-40 
			   0.008, 0.008, 0.008, 0.008, 0.008, 0.010, 0.015, 0.015, 0.010, 0.010, # 40-50 
			   0.008, 0.008, 0.008, 0.008, 0.008, 0.010, 0.015, 0.015, 0.010, 0.010, # 50-60 
			   0.008, 0.008, 0.008, 0.008, 0.008, 0.010, 0.015, 0.015, 0.010, 0.010, # 60-70 
			   0.008, 0.008, 0.008, 0.008, 0.008, 0.010, 0.015, 0.015, 0.010, 0.010, # 70-80 
			   0.008, 0.008, 0.008, 0.008, 0.008, 0.010, 0.015, 0.015, 0.010, 0.010] # 80< 

    
    # cut on ratio e237/e277 
    # |eta|          0.0     0.1    0.6    0.8   1.15   1.37   1.52   1.81    2.01   2.37   2.47 
    theTool.CutReta37 += [ 0.700, 0.700, 0.700, 0.700, 0.700, 0.690, 0.848, 0.876, 0.870, 0.888, # < 5     GeV
		       0.700, 0.700, 0.700, 0.700, 0.700, 0.715, 0.860, 0.880, 0.880, 0.880, # 5-10
		       0.860, 0.860, 0.860, 0.860, 0.860, 0.730, 0.860, 0.880, 0.880, 0.880, # 10-15
		       0.860, 0.860, 0.860, 0.860, 0.860, 0.740, 0.860, 0.880, 0.880, 0.880, # 15-20
		       0.930, 0.930, 0.930, 0.925, 0.925, 0.750, 0.915, 0.915, 0.900, 0.900, # 20-30
		       0.930, 0.930, 0.930, 0.925, 0.925, 0.790, 0.915, 0.920, 0.900, 0.900, # 30-40
		       0.930, 0.930, 0.930, 0.925, 0.925, 0.790, 0.915, 0.920, 0.900, 0.900, # 40-50
		       0.930, 0.930, 0.930, 0.930, 0.925, 0.790, 0.915, 0.920, 0.900, 0.900, # 50-60
		       0.930, 0.930, 0.930, 0.930, 0.925, 0.790, 0.915, 0.920, 0.900, 0.900, # 60-70
		       0.930, 0.930, 0.930, 0.930, 0.925, 0.790, 0.915, 0.920, 0.900, 0.900, # 70-80
		       0.930, 0.930, 0.930, 0.930, 0.925, 0.790, 0.915, 0.920, 0.900, 0.900] # 80<

    # cut on shower width in 2nd sampling                                    
    #                 0.0   0.1    0.6    0.8   1.15   1.37   1.52   1.81    2.01   2.37   2.47
    theTool.CutWeta2c += [ 0.014, 0.014, 0.014, 0.014, 0.014, 0.028, 0.017, 0.014, 0.014, 0.014, # < 5  GeV
		       0.013, 0.013, 0.014, 0.014, 0.014, 0.026, 0.017, 0.014, 0.014, 0.014, # 5-10
		       0.013, 0.013, 0.014, 0.014, 0.014, 0.025, 0.017, 0.014, 0.014, 0.014, # 10-15
		       0.012, 0.012, 0.013, 0.013, 0.013, 0.025, 0.017, 0.014, 0.014, 0.014, # 15-20
		       0.011, 0.011, 0.012, 0.012, 0.013, 0.025, 0.014, 0.013, 0.013, 0.013, # 20-30
		       0.011, 0.011, 0.012, 0.012, 0.012, 0.025, 0.013, 0.013, 0.013, 0.013, # 30-40
		       0.011, 0.011, 0.012, 0.012, 0.012, 0.025, 0.013, 0.013, 0.013, 0.013, # 40-50
		       0.011, 0.011, 0.012, 0.012, 0.012, 0.025, 0.013, 0.012, 0.013, 0.013, # 50-60
		       0.011, 0.011, 0.012, 0.012, 0.012, 0.025, 0.013, 0.012, 0.013, 0.013, # 60-70
		       0.011, 0.011, 0.012, 0.012, 0.012, 0.025, 0.013, 0.012, 0.013, 0.013, # 70-80
		       0.011, 0.011, 0.012, 0.012, 0.012, 0.025, 0.013, 0.012, 0.013, 0.013] # 80<       

    # cut on total width in 1st sampling
    #              0.0   0.1  0.6   0.8   1.15   1.37   1.52  1.81 2.01   2.37   2.47
    theTool.CutWtot  += [3.48, 3.48, 3.78, 3.96, 4.20, 9999., 4.02, 2.70, 1.86,  9999., # < 5    GeV
		     3.18, 3.18, 3.54, 3.90, 4.02, 9999., 3.96, 2.70, 1.80,  9999., # 5-10   
		     2.81, 2.81, 2.97, 3.36, 3.48, 9999., 3.72, 2.42, 1.76,  9999., # 10-15  
		     2.76, 2.76, 2.92, 3.24, 3.41, 9999., 3.67, 2.35, 1.72,  9999., # 15-20  
		     2.50, 2.50, 2.70, 3.14, 3.23, 9999., 3.58, 2.32, 1.59,  9999., # 20-30  
		     2.45, 2.45, 2.70, 2.98, 3.17, 9999., 3.52, 2.25, 1.58,  9999., # 30-40  
		     2.27, 2.27, 2.61, 2.90, 3.17, 9999., 3.36, 2.25, 1.55,  9999., # 40-50  
		     2.27, 2.27, 2.61, 2.90, 3.17, 9999., 3.36, 2.25, 1.55,  9999., # 50-60  
		     2.27, 2.27, 2.61, 2.90, 3.17, 9999., 3.36, 2.25, 1.55,  9999., # 60-70  
		     2.27, 2.27, 2.61, 2.90, 3.17, 9999., 3.36, 2.25, 1.55,  9999., # 70-80  
		     2.27, 2.27, 2.61, 2.90, 3.17, 9999., 3.36, 2.25, 1.55,  9999.  # 80<    
		     ]

    # cut on (Emax - Emax2)/(Emax + Emax2) in 1st sampling 
    #                0.0   0.1    0.6    0.8   1.15   1.37   1.52   1.81    2.01   2.37   2.47
    theTool.CutDEmaxs1 += [0.39,  0.39,  0.20,  0.07, 0.06,  -9999.,  0.07,  0.43,   0.75,  -9999.,  # < 5  GeV
		       0.61,  0.61,  0.32,  0.11, 0.13,  -9999.,  0.12,  0.51,   0.62,  -9999.,  # 5-10  
		       0.67,  0.67,  0.61,  0.43, 0.32,  -9999.,  0.36,  0.82 ,  0.82,  -9999.,  # 10-15  
		       0.75,  0.75,  0.67,  0.51, 0.47,  -9999.,  0.43,  0.86 ,  0.84,  -9999.,  # 15-20  
		       0.835,  0.835,  0.835,  0.73, 0.70,  -9999.,  0.8,  0.9 ,  0.9,  -9999.,  # 20-30  
		       0.835,  0.835,  0.835,  0.73, 0.70,  -9999.,  0.8,  0.9 ,  0.9,  -9999.,  # 30-40  
		       0.835,  0.835,  0.835,  0.73, 0.70,  -9999.,  0.8,  0.9 ,  0.9,  -9999.,  # 40-50  
		       0.835,  0.835,  0.835,  0.73, 0.70,  -9999.,  0.8,  0.9 ,  0.9,  -9999.,  # 50-60  
		       0.835,  0.835,  0.835,  0.73, 0.70,  -9999.,  0.8,  0.9 ,  0.9,  -9999.,  # 60-70  
		       0.835,  0.835,  0.835,  0.73, 0.70,  -9999.,  0.8,  0.9 ,  0.9,  -9999.,  # 70-80  
		       0.835,  0.835,  0.835,  0.73, 0.70,  -9999.,  0.8,  0.9 ,  0.9,  -9999.]  # 80<  



    # cut on Track quality cut
    # cut on pixel-layer hits
    theTool.CutPi  += [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # cut on precision hits
    theTool.CutSi  += [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    # cut on transverse impact parameter
    theTool.CutA0  += [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
    # cut on transverse impact parameter for tight selection
    theTool.CutA0Tight  += [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]


    # cut on delta eta
    #                0.0   0.1    0.6    0.8   1.15   1.37   1.52   1.81    2.01   2.37   2.47
    theTool.CutDeltaEta += [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,  # < 5  GeV  
			0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,  # 5-10      
			0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,  # 10-15     
			0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,  # 15-20     
			0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,  # 20-30     
			0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,  # 30-40     
			0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,  # 40-50     
			0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,  # 50-60     
			0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,  # 60-70     
			0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,  # 70-80     
			0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01   # 80<       
			]

    # cut on delta eta for tight selection
    #                      0.0   0.1    0.6    0.8   1.15   1.37   1.52   1.81    2.01   2.37   2.47
    theTool.CutDeltaEtaTight += [0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005,  # < 5  GeV  
			     0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005,  # 5-10      
			     0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005,  # 10-15     
			     0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005,  # 15-20     
			     0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005,  # 20-30     
			     0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005,  # 30-40     
			     0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005,  # 40-50     
			     0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005,  # 50-60     
			     0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005,  # 60-70     
			     0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005,  # 70-80     
			     0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005   # 80<       
			     ]
    
    theTool.useTRTOutliers  = True 
    # cut on b-layer hits
    theTool.CutBL  += [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    # cut on delta phi
    #                     0.0    0.1    0.6    0.8    1.15   1.37   1.52   1.81  2.01   2.37   2.47
    theTool.CutminDeltaPhi  += [-0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02,  # < 5  GeV  
			     -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02,  # 5-10      
			     -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02,  # 10-15     
			     -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02,  # 15-20     
			     -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02,  # 20-30     
			     -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02,  # 30-40     
			     -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02,  # 40-50     
			     -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02,  # 50-60     
			     -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02,  # 60-70     
			     -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02,  # 70-80     
			     -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02   # 80<       
			     ]
    
    # cut on delta phi
    #                    0.0   0.1   0.6   0.8   1.15  1.37  1.52  1.81 2.01  2.37   2.47
    theTool.CutmaxDeltaPhi  += [0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,  # < 5  GeV  
			    0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,  # 5-10      
			    0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,  # 10-15     
			    0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,  # 15-20     
			    0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,  # 20-30     
			    0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,  # 30-40     
			    0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,  # 40-50     
			    0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,  # 50-60     
			    0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,  # 60-70     
			    0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,  # 70-80     
			    0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02   # 80<       
			    ]
    
    # cut min on E/P
    #               0.0   0.1   0.6   0.8   1.15  1.37  1.52  1.81 2.01  2.37   2.47
    theTool.CutminEp  += [0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80,  # < 5  GeV  
		      0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80,  # 5-10      
		      0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80,  # 10-15     
		      0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80,  # 15-20     
		      0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80,  # 20-30     
		      0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70,  # 30-40     
		      0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70,  # 40-50     
		      0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70,  # 50-60     
		      0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70,  # 60-70     
		      0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70,  # 70-80     
		      0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00   # 80<       
		      ]
    
    # cut max on E/P
    #             0.0   0.1   0.6  0.8 1.15  1.37 1.52 1.81 2.01 2.37 2.47
    theTool.CutmaxEp  += [2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 3.0, 3.0, 3.0, 3.0,  # < 5  GeV  
		      2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 3.0, 3.0, 3.0, 3.0,  # 5-10      
		      2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 3.0, 3.0, 3.0, 3.0,  # 10-15     
		      2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 3.0, 3.0, 3.0, 3.0,  # 15-20     
		      2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 3.0, 3.0, 3.0, 3.0,  # 20-30     
		      3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 4.0, 4.0, 3.0,  # 30-40     
		      3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 4.0, 5.0, 5.0, 4.0,  # 40-50     
		      5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,  # 50-60     
		      5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,  # 60-70     
		      5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,  # 70-80     
		      10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0   # 80<       
		      ]
    
    # cuts on TRT
    # range of eta bins for e-ID for TRT
    theTool.CutBinEta_TRT += [0.1, 0.625, 1.07, 1.304, 1.752, 2.0]
    # cuts on Number of TRT hits with Outliers
    theTool.CutNumTRT  += [-15.,-15., -15., -15., -15., -15.]
    # cuts on TRT ratio with Outliers
    theTool.CutTRTRatio  += [0.08, 0.085, 0.085, 0.115, 0.13, 0.155]
    # cuts on TRT ratio with Outliers for 90% efficiency
    theTool.CutTRTRatio90  += [0.10, 0.10, 0.125, 0.13, 0.13, 0.13]
