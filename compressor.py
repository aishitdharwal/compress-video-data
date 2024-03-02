#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:51:16 2021

@author: aishit
"""

import pandas as pd
import numpy as np
import subprocess
import glob
import os

class Compressor:
    def create_excel(self):
        mkv_files = glob.glob("D:/*.mkv")
        # mkv_files = glob.glob('C:/Users/Aishit Dharwal/Videos/*.mkv')
        print(mkv_files)
        
        df = pd.DataFrame(columns=['input','n','prefix'])
        df['input'] = mkv_files
        df.to_excel('compress_input - Copy.xlsx', index=False)
        return
        
    def compress(self):
        df = pd.read_excel('compress_input.xlsx')
        for i in range(len(df)):
            input_name = df['input'].iloc[i]
            input_name = input_name.split('/')[-1]
            output_name = df['prefix'].iloc[i] + '_' + input_name.split('.')[0] + '.mp4'
            cmd = """ffmpeg -i ".\\""" + input_name + """" -vcodec libx265 -crf 25 ".\\""" + output_name + '"'
            print(cmd)
            os.system(cmd)
        return

compressor = Compressor()
# compressor.create_excel()
compressor.compress()











