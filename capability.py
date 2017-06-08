# capability.py
import sciunit
# ======================MODEL CAPABILITY==================================
class ProducesSpikeIntervals(sciunit.Capability):
    '''
    Indicates that the model produces spike intervals
    '''
    def getSI(self):
        '''gets computed spike intervals'''
        raise NotImplementedError("Must implement produce_number.")
