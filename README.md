# Voice Controlled Departmental Noticeboard


### Clone the project
First of all Fork the repo.

Then type the following command on the terminal to clone the repo keeping in mind to replace the 'your-user-name' with your github user name.
```terminal
git clone https://github.com/your-user-name/voice-controlled-departmental-noticeboard
```
Now you need to move to the project directory.
```terminal
cd voice-controlled-departmental-noticeboard
```

### Virtual Env
First install the virtual environment
```terminal
pip install virtualenv
```
Type the following command to create a virtual environment. Donot change the name of virtual environment because then gitignore won't catch it.
```terminal
virtualenv venv
```
Now activate the virtual environment
```terminal
venv/Scripts/activate
```
Now install all the requirements.
```terminal
pip install -r requiremnets.txt
```

### How to run
Now you need to put the details provided by the host in the directory. If you donot have them, try asking from the host and place it.

Now run the following command, it will Boot the structure and will start working.
```terminal
python init.py
```