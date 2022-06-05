# SPDX-License-Identifier: MIT

# In[1]:


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import string


# In[2]:


plt.style.use('seaborn-whitegrid')
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
mpl.rcParams['lines.marker'] = 'o'
mpl.rcParams['figure.figsize'] = (18, 6)
mpl.rcParams['font.size'] = 10


# In[3]:


def read_dataset(path):
    data = pd.read_csv(path).transpose()
    # Discard the first row (they are column names)
    data = data.rename(columns=lambda idx: data.iloc[0, idx]).iloc[1:, :]
    return data


# In[4]:


def plot_columns(data, columns, ax, counter):
    subdf = data.loc[:, columns]
    subdf.plot(ax=ax, use_index=True)
    ax.legend(loc='upper left')
    title = '(%s)' % string.ascii_lowercase[counter]
    ax.title.set_text(title)


# In[5]:


def reassign_xticklabels(ax, data):
    # https://numbersmithy.com/how-to-change-axis-tick-labels-in-a-matplotlib-plot/
    xticks = ax.get_xticks()
    new_xticklabels = np.empty(shape=xticks.shape, dtype='object')
    for array_index in range(len(xticks)):
        referring_index = int(np.around(xticks[array_index]))
        if referring_index < 0 or referring_index >= len(data.index):
            new_xticklabels[array_index] = ''
        else:
            new_xticklabels[array_index] = data.index[referring_index]
    ax.set_xticklabels(new_xticklabels)


# In[6]:


dataset = read_dataset('averages.csv')


# In[7]:


matrix = np.array([
    ['QoS 0 PT', 'QoS 0 TLS', 'QoS 0 TLSMA'],
    ['QoS 1 PT', 'QoS 1 TLS', 'QoS 1 TLSMA'],
    ['QoS 2 PT', 'QoS 2 TLS', 'QoS 2 TLSMA']
])


# In[8]:


# Response time as influenced by payload size, QoS, and security level
fig, axes = plt.subplots(1, 3, sharey=True, sharex=True)
for i in range(3):
    plot_columns(dataset, matrix[i], axes[i], i)
    #plot_columns(dataset, matrix.T[i], axes[1, i], i + 3)
axes[0].set_ylabel('Mean response time (ms)')
#axes[1, 0].set_ylabel('Mean response time (ms)')
axes[0].set_xlabel('Payload size (kb)')
axes[1].set_xlabel('Payload size (kb)')
axes[2].set_xlabel('Payload size (kb)')
reassign_xticklabels(axes[0], dataset)
plt.yticks(np.arange(0, 13, 2))
plt.savefig('Averages1.png', bbox_inches='tight')
plt.show()


# In[9]:


# Response time as influenced by payload size, QoS, and security level
fig, axes = plt.subplots(1, 3, sharey=True, sharex=True)
for i in range(3):
    #plot_columns(dataset, matrix[i], axes[i], i)
    plot_columns(dataset, matrix.T[i], axes[i], i)
axes[0].set_ylabel('Mean response time (ms)')
#axes[1, 0].set_ylabel('Mean response time (ms)')
axes[0].set_xlabel('Payload size (kb)')
axes[1].set_xlabel('Payload size (kb)')
axes[2].set_xlabel('Payload size (kb)')
reassign_xticklabels(axes[0], dataset)
plt.yticks(np.arange(0, 13, 2))
plt.savefig('Averages2.png', bbox_inches='tight')
plt.show()


# In[10]:


stdev_dataset = read_dataset('stdev.csv')
fig, axes = plt.subplots(1, 3, sharey=True, sharex=True)
for i in range(3):
    plot_columns(stdev_dataset, matrix[i], axes[i], i)
    #plot_columns(stdev_dataset, matrix.T[i], axes[1, i], i + 3)
axes[0].set_ylabel('Response time stdev (ms)')
#axes[1, 0].set_ylabel('Response time stdev (ms)')
axes[0].set_xlabel('Payload size (kb)')
axes[1].set_xlabel('Payload size (kb)')
axes[2].set_xlabel('Payload size (kb)')
reassign_xticklabels(axes[0], stdev_dataset)
plt.yticks(np.arange(0, 2.25, 0.25))
plt.savefig('Stdev1.png', bbox_inches='tight')
plt.show()


# In[11]:


stdev_dataset = read_dataset('stdev.csv')
fig, axes = plt.subplots(1, 3, sharey=True, sharex=True)
for i in range(3):
    #plot_columns(stdev_dataset, matrix[i], axes[i], i)
    plot_columns(stdev_dataset, matrix.T[i], axes[i], i)
axes[0].set_ylabel('Response time stdev (ms)')
#axes[1, 0].set_ylabel('Response time stdev (ms)')
axes[0].set_xlabel('Payload size (kb)')
axes[1].set_xlabel('Payload size (kb)')
axes[2].set_xlabel('Payload size (kb)')
reassign_xticklabels(axes[0], stdev_dataset)
plt.yticks(np.arange(0, 2.25, 0.25))
plt.savefig('Stdev2.png', bbox_inches='tight')
plt.show()
