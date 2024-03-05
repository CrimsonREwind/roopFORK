import streamlit as st
import os
import subprocess

image_input = st.write("enter input image name ")
video_input = st.write("enter input video name ")
video_output = st.write("enter output video name ")

apic ="/content/gdrive/MyDrive/roop/input/"+image_input
bpic ="/content/gdrive/MyDrive/roop/input/"+video_input
cpic ="/content/gdrive/MyDrive/roop/output/"+video_output

new_directory = '/content/gdrive/MyDrive/roop'

os.chdir(new_directory)

script_name = 'run.py'

if st.button('Run script'):
    if st.checkbox('face enhance'):
        arguments = ['--keep-frames', '--keep-fps', '--execution-provider', 'cuda', '--frame-processor', 'face_swapper',
                     'face_enhancer']
        subprocess.run(['python', script_name, f'-s {apic} -t {bpic} -o {cpic}'] + arguments)

    else:
        arguments = ['--keep-frames', '--keep-fps', '--execution-provider', 'cuda', '--frame-processor', 'face_swapper']
        subprocess.run(['python', script_name, f'-s {apic} -t {bpic} -o {cpic}'] + arguments)








"""!python run.py -s $apic -t $bpic -o $cpic --keep-frames --keep-fps --execution-provider cuda --frame-processor face_swapper face_enhancer
inf('\u2714 Execution Finished','success', '50px')"""