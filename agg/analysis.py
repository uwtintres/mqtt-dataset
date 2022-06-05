import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# plt.rcParams['figure.figsize'] = [16, 9]

class Dataset:
    def __init__(self, csv_path, metadata_df):
        self.raw_df = pd.read_csv(csv_path)
        assert self.raw_df.columns[0] == 'msg_id'
        ## Insert additional columns
        filename = pathlib.Path(csv_path).name
        self.meta = metadata_df[metadata_df['filename'] == filename].iloc[0]
        for col in ('qos', 'security_level', 'clients', 'topics'):
            self.raw_df[col] = self.meta[col]
        ## Obtain timeout value. Replace large RTs with NaN
        rows = self.raw_df['response_time_ms'] > self.meta['timeout']
        self.raw_df.loc[rows, 'response_time_ms'] = np.nan
        ## Compute average, stdev and sem of response time
        self.agg = self.raw_df.groupby(['payload_size']).agg({
            'response_time_ms': ['mean', 'std', 'sem']
        }).reset_index()

    def plot(self, label, ecolor='#ffbbaa', use_filter=True):
        """Quick plotting - produces noisy results!"""
        xs = self.agg['payload_size'] / 1024
        ys = self.agg['response_time_ms']['mean']
        yerr = self.agg['response_time_ms']['sem']
        if use_filter:
            ys_rolling = ys.rolling(window=10, min_periods=1).mean()
            plt.errorbar(xs, ys_rolling, label=label, ecolor=ecolor)
        else:
            plt.errorbar(xs, ys, yerr=yerr, label=label, ecolor=ecolor)

    @staticmethod
    def show_legend():
        plt.xlabel('payload size (kb)')
        plt.ylabel('response time (ms)')
        plt.legend()

    def partition_agg(self, method, size1_bytes, size2_bytes):
        b1 = self.raw_df['payload_size'] >= size1_bytes
        b2 = self.raw_df['payload_size'] < size2_bytes
        response_times = self.raw_df.loc[b1 & b2]['response_time_ms']
        if method == 'mean':
            return response_times.mean()
        elif method == 'stdev':
            return response_times.std()
        else:
            raise ValueError('Unknown method parameter ' + method)

    def _partition_map(self, method, kb_end, kb_step):
        result = []
        for kb in range(0, kb_end, kb_step):
            pm = self.partition_agg(method, kb * 1024, (kb + kb_step) * 1024)
            result.append(pm)
        return result

    def averages(self, kb_end, kb_step):
        return self._partition_map('mean', kb_end, kb_step)

    def stdevs(self, kb_end, kb_step):
        return self._partition_map('stdev', kb_end, kb_step)
