#!/home/vvsopov/anaconda3/bin/python

from kick import KickExperiment


class KickExperimentCtr(KickExperiment):
    USE_CTR = True
    
    
if __name__ == '__main__':  
    KickExperimentCtr().run()