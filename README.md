# AI-Playground

This is a simple playground showcasing some AI elements for a basic RAG solution. This guide assumes you are using Visual Studio Code. VS Code can be downloaded here: https://code.visualstudio.com/Download

# Setup Ollama
Ollama is a free open source tool that lets you download LLM models locally onto your machine.

1. Mac Download - https://ollama.com/download/mac
2. Windows Download - https://ollama.com/download/windows

CLI Reference - https://github.com/ollama/ollama?tab=readme-ov-file#cli-reference

Use the CLI reference above to pull a model onto your local. For this particular project, I recommend **llama3.2 and qwen2.5-coder**.

# Install Continue.Dev VS Code Extension

Add the Continue.dev VS Code extension either through the IDE itself or from this link here: https://www.continue.dev/

# Setting up python environment
After pulling this code repository, you will need to have python installed on your machine. You can download the latest python here:
https://www.python.org/downloads/

With python installed, navigate to the root directory of the project. Once there, create a virtual environment with the following command:

> On MacOs/Linux (bash)
```
python3 -m venv .venv
```

> On Windows
```
python -m venv .venv
```

Activate the virtual environment with the following command:

> On MacOS/Linux (bash)
```
source .venv/bin/activate 
```

> On Windows (cmd)
```
.venv\Scripts\activate.bat
```

> On Windows (Powershell)
```
.venv\Scripts\Activate.ps1
```

Once activated, install all dependencies using pip:

pip install -r requirements.txt

You can use the "deactivate" command to exit the venv. 

# Creating a vector database

1. Pull the ollama model Mistral

    ollama pull mistral

2. Add, remove, and/or edit .txt files in the data/documents directory

3. Create a db/vector_store directory if one doesn't already exist. Delete any existing chroma.sqlite3 and other contents within the db/vector_store directory

4. From the project root, run

    python backend/vector_store.py

5. If successful, within the db/vector_store directory, you should now have a chroma.sqlite3 created.

# Run the solution

streamlit run /Users/ashayvakharia/Workspace/AI-Playground/app/main.py
