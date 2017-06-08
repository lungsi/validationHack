# models.py
import sciunit

# ============================MODEL INSTANCE===================================
class MicrocircuitModelInstance(sciunit.Model,
                                ProducesSpikeIntervals):
    '''
    A model that always produces spike intervals as the output.
    Declare models capability/ies via inheritance;
    Implement capability/ies.    
    '''
    def __init__(self, spiketrains_as_model, name=None):
        self.spiketrains = spiketrains_as_model
        self.spike_intervals = np.array([])
#       self.name = name
        super(MicrocircuitModelInstance, self).__init__(name=name, 
                                                        spiketrains_as_model=spiketrains_as_model)
      
    def getSI(self):
        # this is where the getSI capability is implemented.
        for st in self.spiketrains:
            self.spike_intervals = np.append(self.spike_intervals, 
                                             isi(st.magnitude, axis=-1))
        return self.spike_intervals

# =========================Pre-MODEL Setup===================================
# Initialize for loading the spike train data from storage
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from quantities import ms
import sys
import imp
from scipy.linalg import eigh
from IPython.core.display import HTML
import urllib2
HTML(urllib2.urlopen('http://bit.ly/1Bf5Hft').read())

# load simulation data
spiketrains_nest = load(client, collab_path, "spikes_L6I_nest.h5")
spiketrains_spinnaker = load(client, collab_path, "spikes_L6I_spinnaker.h5")

# ============================MODEL-NEST=====================================

# Load spiketrain data from storage
from neo.io.hdf5io import NeoHdf5IO
from neo import SpikeTrain

class MicrocircuitModelNEST(MicrocircuitModelInstance):
    '''
    textLoad spiketrain data from storage
    '''
    def __init__(self):
        # Initialize for loading the spike train data from storage
        collab_path = '/3653'
        client = get_bbp_client().document
        # Load NEST data using NeoHdf5I0
        store_path = "./local"
        client.download_file(collab_path + '/' + "spikes_L6I_nest.h5",
                             store_path + "spikes_L6I_nest.h5")
        data = NeoHdf5IO(store_path + "spikes_L6I_nest.h5")
        self.spiketrains = data.read_block().list_children_by_class(SpikeTrain)
    def __rep__(self):
        # returns the model based on the MicrocircuitModelInstance parent class
        return MicrocircuitModelInstance.__init__(self.spiketrains, name='NEST')

# ==========================MODEL-SPINNAKER===================================
class MicrocircuitModelSPINNAKER(MicrocircuitModelInstance):
    '''
    text
    '''
    def __init__(self):
        # Initialize for loading the spike train data from storage
        collab_path = '/3653'
        client = get_bbp_client().document
        # Load NEST data using NeoHdf5I0
        store_path = "./local"
        client.download_file(collab_path + '/' + "spikes_L6I_spinnaker.h5",
                             store_path + "spikes_L6I_spinnaker.h5")
        data = NeoHdf5IO(store_path + "spikes_L6I_spinnaker.h5")
        self.spiketrains = data.read_block().list_children_by_class(SpikeTrain)
    def __rep__(self):
        # returns the model based on the MicrocircuitModelInstance parent class
        return MicrocircuitModelInstance.__init__(self.spiketrains,
                                                  name='SpiNNaker')

# =====================Write to storage to mimick observed data================

