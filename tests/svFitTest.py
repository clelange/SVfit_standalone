#!/bin/env python
import sys
import ROOT
ROOT.gSystem.Load("libSVfitStandaloneAlgorithm")
print "loading libSVfitStandaloneAlgorithm done"


# importing the python binding to the C++ class from ROOT
class SVfitAlgo(ROOT.SVfitStandaloneAlgorithm):
    '''Just an additional wrapper, not really needed :-)
    We just want to illustrate the fact that you could
    use such a wrapper to add functions, attributes, etc,
    in an improved interface to the original C++ class.
    '''
    def __init__(self, *args):
        super(SVfitAlgo, self).__init__(*args)


class measuredTauLepton(ROOT.svFitStandalone.MeasuredTauLepton):
    '''
       decayType : {
                    0:kUndefinedDecayType,
                    1:kTauToHadDecay,
                    2:kTauToElecDecay,
                    3:kTauToMuDecay,
                    4:kPrompt
                   }
    '''
    def __init__(self, decayType, pt, eta, phi, mass, decayMode=-1):
        super(measuredTauLepton, self).__init__(decayType, pt, eta, phi, mass, decayMode)



def main():
    """load compiled SVfit_standalone library and check the output"""
    # define MET
    measuredMETx = 11.7491
    measuredMETy = -51.9172
    # define MET covariance
    covMET = ROOT.TMatrixD(2, 2)
    covMET[0][0] = 787.352
    covMET[1][0] = -178.63
    covMET[0][1] = -178.63
    covMET[1][1] = 179.545
    print covMET
    # define lepton four vectors
    measuredTauLeptons = ROOT.std.vector('svFitStandalone::MeasuredTauLepton')()
    measuredTauLeptons.push_back(ROOT.svFitStandalone.MeasuredTauLepton(ROOT.svFitStandalone.kTauToElecDecay, 33.7393, 0.9409,  -0.541458, 0.51100e-3))  # tau -> electron decay (Pt, eta, phi, mass)
    measuredTauLeptons.push_back(ROOT.svFitStandalone.MeasuredTauLepton(ROOT.svFitStandalone.kTauToHadDecay, 25.7322, 0.618228, 2.79362,  0.13957, 0))  # tau -> 1prong0pi0 hadronic decay (Pt, eta, phi, mass)
    # define algorithm (set the debug level to 3 for testing)
    verbosity = 2
    algo = ROOT.SVfitStandaloneAlgorithm(measuredTauLeptons, measuredMETx, measuredMETy, covMET, verbosity)
    # algo.addLogM(false);
    algo.addLogM(True, 1.)
    inputFileName_visPtResolution = "data/svFitVisMassAndPtResolutionPDF.root"
    ROOT.TH1.AddDirectory(False)
    inputFile_visPtResolution = ROOT.TFile(inputFileName_visPtResolution)
    algo.shiftVisPt(True, inputFile_visPtResolution)
    # algo.shiftVisPt2(true);
    #
    #    the following lines show how to use the different methods on a single event
    #
    # minuit fit method
    # algo.fit();
    # integration by VEGAS (same as function algo.integrate() that has been in use when markov chain integration had not yet been implemented)
    # algo.integrateVEGAS();
    # integration by markov chain MC
    algo.integrateMarkovChain()
    mass = algo.getMCQuantitiesAdapter().getMass()  # full mass of tau lepton pair in units of GeV
    transverseMass = algo.getMCQuantitiesAdapter().getTransverseMass()  # transverse mass of tau lepton pair in units of GeV
    if algo.isValidSolution():
        print "found valid solution: mass =", mass, "(expected value = 124.646), transverse mass =", transverseMass, "(expected value = 123.026)"
    else:
        print "sorry, failed to find valid solution !!"
        sys.exit(1)


if __name__ == '__main__':
    main()
