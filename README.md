# Room2Room Path Animations

Prototype project for creating animations to show a path from one room/building to another.

This guide will help you set up the environment to create animations that demonstrate paths between rooms or buildings. We are focusing on using Manim, a community-driven animation library in Python. 

Follow the steps below to get your development environment ready.

## Environment Setup

I'm working with `python 3.13` on Windows 11 and NixOS (Linux).

It's essential that your version of Python is compatible with Manim and all other dependencies.

## Quick Setup Overview

You can choose to set up your Python environment in several ways, depending on your preference. In this guide, I will set up **Manim** in a virtual environment. This is the recommended way to manage dependencies and avoid conflicts between projects. If you need more details on alternative setups, refer to the [Manim Community Installation Guide](https://docs.manim.community/en/stable/installation.html).

### Step 1:

The first step is to set up a virtual environment:

1. Open a terminal and navigate to your project folder:

    ```
    cd path/to/project
    ```

2. Create a virtual environment named `r2rpa`:

    ```
    python -m venv r2rpa
    ```

3. Activate the virtual environment:

    - On Windows:

        ```
        venv\Scripts\activate
        ```

    - On Linux (NixOS):

        ```
        source venv/bin/activate
        ```
4. Upgrade `pip` to the latest version:

    ```
    pip install --upgrade pip
    ```

### Step 2: Install Manim

Now that we have our virtual environment activated, let's install **Manim** using `pip`. This command will install Manim with all its dependencies:

```
pip install manim
```

This will ensure you have the latest stable version of Manim installed.

### Step 3: Install Prerequisites

Manim requires some additional tools to render animations properly:

1. FFmpeg:
    - Download from [FFmpeg official site](https://ffmpeg.org/download.html)
    - Add the path of FFmpeg's `bin` directory to your system's PATH variable. If you don't know how, there is instructions [here.](https://www.eukhost.com/kb/how-to-add-to-the-path-on-windows-10-and-windows-11/)

2. LaTex (Optional, but useful for text rendering):
    - For Windows: Install MikTex from [miktex.org](https://miktex.org/download)
    - For Linux (NixOS): You can use your system's package manager to install TeXLive.

### Step 4: Verify Installation

After installing Manim and prerequisites, verify the installation:

```
manim --version
```

### Step 5: Test Manim

In this repository you will find a file `manim-examples/test.py` with the following content:

```python
from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))
```

You can render the scene by running:

```
manim -pql manim-examples/test.py HelloWorld
```

- `p`: Opens the rendered video automatically.
- `ql`: Uses lower quality for a faster preview.

### Summary

- Make sure your Python version is compatible with Manim.
- Set up a virtual environment to keep dependencies isolated.
- Install Manim and required tools (FFmpeg and LaTex).
- Verify and test your installation to ensure everything is working.

Feel free to refer to the [Manim Community Documentation](https://docs.manim.community/en/stable/index.html) for any additional help or detailed setup instructions.