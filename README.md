# Pygame Project Setup on WSL (Windows Subsystem for Linux)

This guide will help you set up the project with **Pygame** on **WSL**.

---

## Step 1: Access WSL

1. **Open WSL Terminal**:
   - **Option 1**: Press `Win + S`, type "WSL," and select your WSL distribution (e.g., Ubuntu).
   - **Option 2**: Open Windows Terminal (search "Windows Terminal" in the Start menu), then select your WSL distribution (e.g., Ubuntu) from the dropdown menu.

---

## Step 2: Install Python and Required Libraries

1. Update and install Python:

    ```bash
    sudo apt update && sudo apt upgrade -y
    sudo apt install python3 python3-pip python3-venv build-essential -y
    ```

2. Install **Cython** and **SDL libraries** required for Pygame:

    ```bash
    sudo apt install cython3 -y
    sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev -y
    ```

---

## Step 3: Set Up Project Directory and Virtual Environment

1. Create a project directory and set up a virtual environment:

    ```bash
    git clone git@github.com:omeldar/r2rpa-prototype.git
    cd r2rpa-prototype
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Upgrade `pip` and install **Pygame** in the virtual environment:

    ```bash
    pip install --upgrade pip
    pip install pygame
    pip install spicy
    ```

---

Run the script (in the virtual environment):
```
python main.py
```

You should see a Pygame window if everything is set up correctly.
