# listening-practice
Just a random personal project.

Hope this small program will help you guys improve yourself, even if only a little. 

```Rome wasn’t built in a day.```

## 1. Clone or Download the Repository
Clone this repository or download it as a ZIP and extract it:
```
git clone <repository-url>
cd listening_practice
```
## 2. Open a Command Prompt or PowerShell in the project folder

- Create a virtual environment named .env

```
python -m venv .env
```

- Activate the virtual environment

```
.env\Scripts\activate 
```

- Install dependencies
```
python -m pip install --upgrade pip

pip install -r requirements.txt

mkdir files
```

The folder structure should now look like:
```
listening_practice/
├── .env/              # Virtual environment
├── files/             # Text files with words
├── main.py
├── requirements.txt
└── README.md
```

## 3. Download espeak-ng:

Visit the [espeak-ng releases page](https://github.com/espeak-ng/espeak-ng/releases).

Download the latest Windows installer, e.g., espeak-ng-X.X.X.msi (replace X.X.X with the latest version, like 1.52).

To make espeak-ng accessible from any command prompt, add its binary to the system PATH.

Steps:

1. Open the Start menu, search for "environment variables", and select Edit the system environment variables (requires admin rights).
2. In the System Properties window, click Environment Variables.
3. Under System variables, find and select Path, then click Edit....
4. Click New and add the path to the espeak-ng binary:
- Typically: ```C:\Program Files (x86)\eSpeak NG```
5. Click OK to close all dialogs.

Verify Installation:
- Open a new Command Prompt and run:
```
espeak-ng --version
```
You should see output like ```eSpeak NG text-to-speech: 1.52 Data at: ....```
If you get "command not found", double-check the PATH entry or restart your computer.

## Running the Project

Activate the virtual environment:
```
.env\Scripts\activate
```

Keep only 2 files in vocabularies folder if you don't want listening in a random way.


Run the main script:
```
python main.py
```
