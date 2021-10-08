import sys, os
import time
import ROOT as r
from ROOT import gSystem
from copy import deepcopy
import CMS_lumi
#import myPlotter_input as effplot 
r.gROOT.SetBatch(True)
from subprocess import call
import myPlotter_input as effplot
from markerColors import markerColors
from allLegends import legends

import argparse
parser = argparse.ArgumentParser(description='Plotter options')
parser.add_argument('-n','--ntuples', action='store_true', default = False)
parser.add_argument('-r','--redoPlots', action='store_true', default = False)
my_namespace = parser.parse_args()

################################# CHANGE BEFORE RUNNING #######################################

categories = ['norpc', 'rpc']
files = {'norpc':[], 'rpc':[], 'DM':[]}
#files['norpc'].append('3h4h') 
#files['norpc'].append('nopu_noage_norpc') 
#files['norpc'].append('mu_pu200') 
#files['norpc'].append('DTDPGNtuple_11_1_0_patch2_Phase2_Simulation_8muInBarrel_woRPC')
#files['norpc'].append('mu_PU200_noRPC_noAgeing_111X_1_0')
#files['norpc'].append('mu_PU200_noRPC_noAgeing_20210223')
#files['norpc'].append('mu_PU200_noRPC_noAgeing_20210308')
#files['norpc'].append('mu_PU200_noRPC_noAgeing_20210315')
#files['norpc'].append('mu_PU200_noRPC_noAgeing_20210315_cmssw')
#files['norpc'].append('mu_pu200_newest_analyzer')
#files['norpc'].append('mu_PU200_withRPC_noAgeing')
#files['norpc'].append('DTDPGNtuple_11_1_0_patch2_Phase2_Simulation_8muInBarrel')
#files['norpc'].append('mu_PU200_noRPC_noAgeing_3h4h')
#files['norpc'].append('mu_PU200_noRPC_noAgeing_grouping2')
#files['norpc'].append('rossin_noRPC_noAgeing_cmssw')
#files['norpc'].append('rossin_noRPC_withAgeing')
#files['norpc'].append('rossin_noRPC_noAgeing_11_2_1')
#files['norpc'].append('rossin_noRPC_noAgeing_newestlut')
#files['norpc'].append('rossin_noRPC_noAgeing_cmssw')
#files['norpc'].append('rossin_noRPC_noAgeing_alignTrue')
#files['norpc'].append('rossin_noRPC_noAgeing_ext_alignTrue')
files['norpc'].append('rossin_noRPC_noAgeing_ext_confok_alignTrue')
#files['norpc'].append('rossin_noRPC_noAgeing_noCor_ext_alignTrue')
#files['norpc'].append('rossin_noRPC_withAgeing_alignTrue')
#files['norpc'].append('rossin_withRPC_noAgeing_alignTrue')
#files['norpc'].append('rossin_withRPC_withAgeing_alignTrue')
#files['norpc'].append('rossin_noRPC_noAgeing_alignFalse')

#qualities = ['']
qualities = {'norpc':[],'rpc':[], 'DM':[]}
#qualities['norpc'].append('All')
qualities['norpc'].append('Correlated')
qualities['norpc'].append('Uncorrelated')
#qualities['norpc'].append('Legacy')
#qualities['norpc'].append('4h')
#qualities['norpc'].append('3h')

#qualities['norpc'].append('Q1')
#qualities['norpc'].append('Q2')
#qualities['norpc'].append('Q3')
#qualities['norpc'].append('Q4')


##############################################################################################

print "GOT IN!"

if my_namespace.ntuples == True: 
    print ("Starting ntuplizer for every sample in input")
    time.sleep(2)
    r.gInterpreter.ProcessLine(".x loadTPGSimAnalysis_Res_All.C")
    gSystem.Load(os.getcwd() + "/DTNtupleBaseAnalyzer_C.so")
    gSystem.Load(os.getcwd() + "/DTNtupleTPGSimAnalyzer_Resolution_All_C.so")
    from ROOT import DTNtupleTPGSimAnalyzer
else :
  print("Not making ntuples. If you want to make them, restart with 'yes' as first argument ")
  time.sleep(2)

path = '/eos/home-j/jleonhol/simulationSamples/'
plotsPath = "./summaryPlots/"
#outputPath = './ntuples/'
outputPath = '/eos/home-j/jleonhol/ntuplesResults/'
eosPath='/eos/home-j/jleonhol/www/resolutionsNote/'


chambTag = ["MB1", "MB2", "MB3", "MB4"]
wheelTag    = [ "Wh-2", "Wh-1", "Wh0", "Wh+1", "Wh+2"];
magnitude = ["Time", "Phi", "PhiB", "TanPsi", "x"]

plottingStuff = { 'lowlimityaxis': 0,
		      'highlimityaxis': {},
		      'markersize': 1,
              'yaxistitle' : {"Time": "Time resolution (ns)", "Phi": "Global Phi resolution (#murad)", "PhiB": "Bending Phi resolution (mrad)", "TanPsi": "Local direction resolution (mrad)", "x":"Position resolution (#mum)"}, 
		      'yaxistitleoffset': 1.5,
		      'xaxistitle': "Wheel",
		      #'legxlow' : 0.7,
              'legxlow' : 0.3075 + 1 * 0.1975,
              #'legxlow' : 0.3075 + 2 * 0.1975,
		      'legylow': 0.65,
		      'legxhigh': 0.9,
		      'legyhigh': 0.75,
		      'markertypedir':{},
		      'markercolordir':{},
              'ageingTag': "",
   		    }

plottingStuff['highlimityaxis']['Time'] = {'Q1': 10, 'Q2': 10, '3h': 10, '4h': 10, 'Q3': 10, 'Q4': 10, 'All':5, 'Correlated':5, 'Uncorrelated':10, 'Legacy':5}
plottingStuff['highlimityaxis']['Phi'] = {'Q1': 50, 'Q2': 50, '3h': 50, '4h': 50, 'Q3': 50, 'Q4': 50, 'All':50,'Correlated':50, 'Uncorrelated':50, 'Legacy':50}
plottingStuff['highlimityaxis']['PhiB'] = {'Q1': 15, 'Q2': 15, '3h': 15, '4h': 10, 'Q3': 10, 'Q4': 10, 'All':5, 'Correlated':5, 'Uncorrelated':20, 'Legacy':5}
plottingStuff['highlimityaxis']['TanPsi'] = {'Q1': 15, 'Q2': 15, '3h': 15, '4h': 10, 'Q3': 10, 'Q4': 10, 'All':5, 'Correlated':5, 'Uncorrelated':20, 'Legacy':5}
plottingStuff['highlimityaxis']['x'] = {'Q1': 200, 'Q2': 200, '3h': 200, '4h': 200, 'Q3': 200, 'Q4': 200, 'All': 200, 'Correlated': 200, 'Uncorrelated':200, 'Legacy':200}

markerColors = [r.kBlue, r.kRed, r.kGreen, r.kOrange, r.kBlack, r.kMagenta]



for cat in files :  
  for fil in files[cat] :
    if my_namespace.ntuples == True:
      print ('Obtaining resolution ntuples for ' + fil )
      time.sleep(2) 
      analysis = DTNtupleTPGSimAnalyzer(path + fil + '.root', outputPath + 'results_resols_' +fil + '_.root')
      analysis.Loop()

    ageingTag = ("" if "withAgeing" not in fil else "3000 fb^{-1}")
    ageingLegend = ("No ageing" if "withAgeing" not in fil else "3000 fb^{-1} ageing")

    if my_namespace.ntuples == True or my_namespace.redoPlots == True: 
      rc = call ('./runPlots.sh ' + fil + " " + ageingLegend, shell=True) 
    
    
    for mag in magnitude :
      for qual in qualities[cat] : 
        listofplots = []
        plotscaffold = "h" + mag + "Res_{al}_" + qual + "_{wh}"
        savescaffold = "h" + mag + "Res_{al}_" + qual

        plottingStuff['markertypedir']["h_" + "AM" + "_" + fil+qual] = 20
        plottingStuff['markercolordir']["h_" + "AM" + "_" + fil+qual] = markerColors[0]
        effplot.makeResolPlot(listofplots, "AM", fil+qual, plotsPath + fil + '/' +  'outPlots.root', plotscaffold)
        #if "withAgeing" in fil:
        #    plottingStuff['ageingTag'] = "3000 fb^{-1}"
        #else:
        #    plottingStuff['ageingTag'] = ""
        print "\nCombining and saving\n"
        effplot.combineResolPlots(listofplots, mag, qual, [], plottingStuff, plotsPath + fil + '/' + qual  + '/', savescaffold.format(al='AM') )
           
   # rc = call('cp -r ' + plotsPath + fil + ' ' + eosPath , shell=True)
   # rc = call('cp -r /eos/home-j/jleonhol/backup/index_resol_php ' + eosPath + fil + "/index.php" , shell=True)
   # for qual in qualities[cat] : rc = call('cp -r /eos/home-j/jleonhol/backup/index_resol_php ' + eosPath + fil + "/" + qual + "/index.php" , shell=True)
     
for cat in files :
  if not files[cat] : continue
  for mag in magnitude :
    for fil in files[cat] :
      listofplots = []
      num = 0
      for qual in qualities[cat] : 
        plotscaffold = "h" + mag + "Res_{al}_" + qual + "_{wh}"
        savescaffold = "h" + mag + "Res_{al}" 

        plottingStuff['markertypedir']["h_" + "AM" + "_" + fil+qual] = 20
        plottingStuff['markercolordir']["h_" + "AM" + "_" + fil+qual] = markerColors[num]
        num+=1
        effplot.makeResolPlot(listofplots, "AM", fil+qual, plotsPath + fil + '/' +  'outPlots.root', plotscaffold)

      print "\nCombining and saving\n"
      if not os.path.isdir(plotsPath + fil + '/mixed/') : os.mkdir(plotsPath + fil + '/mixed/')
      effplot.combineResolPlots(listofplots, mag, qual, qualities[cat], plottingStuff, plotsPath + fil + '/mixed/', savescaffold.format(al='AM') )


for cat in files :
    if not files[cat] : continue
    dirname = "{}/{}/".format(plotsPath, cat)
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    for mag in magnitude:
        for qual in qualities[cat] : 
            listofplots = []
            mylegends = []
            num = 0
            plottingStuff['ageingTag'] = ""
            for fil in files[cat]:
                plotscaffold = "h" + mag + "Res_{al}_" + qual + "_{wh}"
                savescaffold = "h" + mag + "Res_{al}_" + qual 

                plottingStuff['markertypedir']["h_" + "AM" + "_" + fil+qual] = 20
                plottingStuff['markercolordir']["h_" + "AM" + "_" + fil+qual] = markerColors[num]
                #if "withAgeing" in fil:
                    #plottingStuff['ageingTag'] = "3000 fb^{-1}"
                num+=1
                effplot.makeResolPlot(listofplots, "AM", fil+qual, plotsPath + fil + '/' +  'outPlots.root', plotscaffold)
                print legends[fil]
                mylegends.append(legends[fil]) 
            print listofplots
            print [plot.Integral() for plot in listofplots]
            print "\nCombining and saving\n"
            effplot.combineResolPlots(listofplots, mag, qual, mylegends, plottingStuff, dirname, savescaffold.format(al='AM') )



###############################################################################################
#######################################     END     ###########################################
###############################################################################################
