# Voice Controlled Departmental Noticeboard


## Clone the project
First of all Fork the repo.

Then type the following command on the terminal to clone the repo keeping in mind to replace the `{your-user-name}` with your github user name.
```terminal
git clone https://github.com/{your-user-name}/voice-controlled-departmental-noticeboard
```
Now you need to move to the project directory.
```terminal
cd voice-controlled-departmental-noticeboard
```

## Virtual Env
First install the virtual environment
```terminal
pip install virtualenv
```
Type the following command to create a virtual environment.
```terminal
virtualenv venv
```
Now activate the virtual environment
```terminal
venv/Scripts/activate
```
In case your PC is not allowing the virtual environment to activate, then open the `Windows Powershell` with `Open as administrator` and type the following command on its shell.
```powershell
Set-ExecutionPolicy Unrestricted -Force
```
Then try activating the virtualenv again.  
And to deactivate the virtual environment in any case type following in the terminal where it is activated.
```terminal
deactivate
```

## Requirements

### Step 1
First of all to install cmake library, the `Visual Studio` is required to be installed. Click [here](https://visualstudio.microsoft.com/downloads/) to download the Visual Studio (Community Pack is free).

### Step 2
Install the `Desktop Development with C++` tool with the Visual Studio installer. It will be necessary to compile the cmake lib.

### Step 3
Now install the `cmake` lib with the following command on the terminal with virtual environment activated.
```teerminal
pip install cmake
```

### Step 4
Now download the suitable [pyaudio wheel](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).  
For example in 'PyAudio‑`0.2.11`‑cp`39`‑cp`39`‑`win`_amd`64`.whl', `0.2.11` is showing the version, cp`39` is showing the python version 3.9 whereas `win`_amd`64` is showing that wheel is made for windows 64 bit processor.  
Install the Pyaudio by writing the following command in the terminal.
```terminal
pip install [path-to-downloaded-pyaudio-wheel]
```

### Step 5
Now install all the other requirements.
```terminal
pip install -r requiremnets.txt
```

## How to run
Now you need to put the details provided by the host in the directory. If you donot have them, try asking from the host and place it.

Now run the following command, it will Boot the structure and will start working.
```terminal
python init.py
```