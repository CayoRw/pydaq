---
title: 'PYDAQ: Data Acquisition and Experimental Analysis with Python'
tags:
  - Python
  - Data Acquisition
  - Arduino
  - NIDAQ
  - System Identification
  - Mathematical Modeling
authors:
  - name: Samir Angelo Milani Martins
    orcid: 0000-0003-1702-8504
    corresponding: true
    affiliation: "1, 2"
affiliations:
  - name: Department of Electrical Engineering at Federal University of São João del-Rei, Brazil.
    index: 1
  - name: GCoM - Modeling and Control Group at Federal University of São João del-Rei, Brazil.
    index: 2
date: 09 March 2023
bibliography: paper.bib

---

# Summary

System identification is a relevant resarch topic that aims to find mathematical models
using acquired data. One of the first relevant contribution is the work of
[@Lju1987], which was substantially developed over the years [@MA2016], [@WMNL2019]. 
Among system identification tools, SysIdentPy [@Lacerda2020] uses Python in a very 
straighforward way, while [@ayala2020r] promises to obtain model using R language.

However, as pointed out by [@Lju1987], experimental data are necessary for obtaining 
black-box models, and this is exactly where this work find its place. PYDAQ is a Python tool
which was primarly developed for experiments with empirical data, either sending and/or 
acquiring data using simple Graphical User Interfaces or command line, with 
few (or any) line of codes required using different solutions provided by the 
market (NIDAQ and Arduino). Thus, even a person working in a biological experiment, for instance, 
is able to use PYDAQ easily and quickly for data acquisition

In what follows it will be shown how PYDAQ can be use by any scientist for 
quickly and efective data acquisition experiments, even if the scientist has no programming skills. 


# PYDAQ - Data Acquisition and Experimental Analysis

# Examples

Figures \autoref{fig:arduino_get_gui} and \autoref{fig:nidaq_get_gui} depicts
the Graphical User Interface developed for Data Acquisition using Arduino or any NIDAQ board.

![Data Acquisition through NIDAQ.\label{fig:nidaq_get_gui}](../docs/img/get_data_nidaq.png){ width=20%, height=20%}

![Data Acquisition through Arduino.\label{fig:arduino_get_gui}](../docs/img/get_data_arduino.png){ width=20%, height=20%}

To start them, only three line of codes (LOC) are necessary, including one for importing PYDAQ: 

```python
from pydaq.get_data import Get_data
# Class Get_data
g = Get_data()

# Arduino or NIDAQ - Use ONE of the following lines 
g.get_data_nidaq_gui() # For NIDAQ devices 
g.get_data_arduino_gui() # For arduino boards
```

Similarly, to send data, only three LOC are required, as showed up in what follow:

```python
from pydaq.send_data import Send_data

# Class Send_data
s = Send_data()

# Arduino or NIDAQ - Use ONE of the following lines 
s.send_data_nidaq_gui()
s.send_data_arduino_gui()
```

If the user decides to save data, it will be saved in .dat format, located at the 
path defined in the GUI. Figure \label{fig:data} shows an example of how data will be saved: i) one file (time.dat) 
with the timestamp, in seconds, when each sample was acquired; ii) file data.dat containing acquired values.

![Example of acquired data.\label{fig:data}](../docs/img/data.png){ width=20%, height=20%}

![GUI for sending data - Arduino.\label{fig:arduino_send_gui}](../docs/img/send_data_nidaq_gui.png){ width=20%, height=20%}

![GUI for sending data - NIDAQ.\label{fig:nidaq_send_gui}](../docs/img/send_data_arduino_gui.png){ width=15%, height=15%}


It should be emphatized that once this code is executed, a Graphical User Interface will
manifest on screen, acording to the board selected by the user, as 
shown in Figures \autoref{fig:nidaq_send_gui} and \autoref{fig:arduino_send_gui}.

Options are straight-forward and ease to understand. For further details and to check 
how to use the same functionality using a command line the reader are invited to 
read the documentation (https://samirmartins.github.io/pydaq/). 

It is noteworthy that any signal can be generated and applied to a physical
system using the presented GUI, being the used board the main constraint. Data
can be either generated manually or using a library (e.g, numpy) to create 
signals as sine waves, PRBS (Pseudo-Random Binary Signal) or other signal 
required to be a persistently exciting input, as necessary for system identification [@Lju1987], [@Bil2013]  

Step-response is a common way to test a system and acquire data, in order to find a model, as well
as system time constant and gain. To facilitate this procedure, a step-response GUI
was also created and can be seen in Figures \label{fig:step_nidaq} and  \label{fig:step_arduino}. 
To use them, user should use the command: 

```python
from pydaq.step_response import Step_response

# Class Step_Response
s = Step_response()

# Arduino or NIDAQ - Use ONE of the following lines 
s.step_response_nidaq_gui()
s.step_response_arduino_gui()
```


![Step Response GUI - NIDAQ.\label{fig:step_nidaq}](../docs/img/step_response_nidaq_gui.png){ width=30%, height=30%}

![Step Response GUI - Arduino.\label{fig:step_arduino}](../docs/img/step_response_arduino_gui.png){ width=20%, height=20%}

Here the user can define when the step will be applied, as well as where data will be saved.
Figures \label{fig:data_sent} and \label{fig:step_data} shows data that were empirically-acquired 
with PYDAQ. In the figures the user will find lables, function (Sending Data/Data Acquisition/Step Response), 
device/channel (for NIDAQ boards) or COM port used (for Arduino devices).


![Data acquired using a NIDAQ board.\label{fig:data_sent}](../docs/img/sending_data_nidaq.png){ width=40%, height=40%}

![Data generated by a step-response experiment.\label{fig:step_data}](../docs/img/step_response_arduino.png){ width=40%, height=40%}


Examples showed above shed light in some functionalities of PYDAQ. For further 
details and for command line use, reader is welcome to consult full 
documentation (https://samirmartins.github.io/pydaq/).


# Future Work

Future releases will include real-time and data-driven system identification using linear and nonlinear approaches.
Also, real-time model based controllers will be implemented through PYDAQ. Saving data 
in a SQL server is a future feature, as well.

# References