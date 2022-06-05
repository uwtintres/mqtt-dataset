# SPDX-License-Identifier: MIT

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from analysis import Dataset
plt.rcParams['figure.figsize'] = [16, 9]

def print_floating_point_list(fp_list):
    formatted = map(lambda fp: '{:.4f}'.format(fp), fp_list)
    print(' & '.join(formatted))

directory = '../data/'

metadata = pd.read_csv(directory + '/metadata.csv')

qos0 = Dataset(directory + '/QoS0Plaintext.txt', metadata)
tls_qos0 = Dataset(directory + '/QoS0TLS.txt', metadata)
tlsma_qos0 = Dataset(directory + '/TLSMAQoS0_CLEANED.txt', metadata)

qos1 = Dataset(directory + '/PlaintextQoS1.txt', metadata)
tls_qos1 = Dataset(directory + '/TLSQoS1.txt', metadata)
tlsma_qos1 = Dataset(directory + '/TLSMAQoS1_take2.txt', metadata)

qos2 = Dataset(directory + '/PlaintextQoS2.txt', metadata)
#qos2_2 = Dataset(directory + '/PlaintextQoS2_take2.txt')
tls_qos2 = Dataset(directory + '/TLSQoS2.txt', metadata)
tlsma_qos2 = Dataset(directory + '/TLSMAQoS2.txt', metadata)

print_floating_point_list(tlsma_qos0.averages(1001, 200))
print_floating_point_list(tlsma_qos0.stdevs(1001, 200))
