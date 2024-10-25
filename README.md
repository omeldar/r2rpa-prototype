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
        r2rpa\Scripts\activate
        ```

    - On Linux (NixOS):

        ```
        source r2rpa/bin/activate
        ```
4. Upgrade `pip` to the latest version and install packages we need for the installation of manim (in the environment `r2rpa`):

    ```
    pip install --upgrade pip setuptools wheel
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

## Common Issues

### Execution Policies on Windows

If, when trying to activate the environment, you get an error like this:

```
> r2rpa\Scripts\activate
.\r2rpa\Scripts\activate : File Drive:path\r2rpa\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this 
system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
```

This is because of the Execution Policy settings in Windows, which are preventing you from running the scripts. In the terminal you will have to run the following command to allow scripts to be executed:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

There are different execution policies. 

- Restricted: No scripts are allowed to run (likely the current setting)
- RemoteSigned: Allows local scripts to run without signing but requires downloaded scripts to be signed.
- Unrestricted: All scripts can be run. WARNING: This setting could be dangerous due to security risks.

If you're in an environment with strict security policies (e.g., a corporate environment), you may not have the permissions to change the execution policy. You can temporarily change it just for the current session by running:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

### ManimPango Fails to Install

This is what to do, if installing manim fails, and you get an error like this:

```
Collectin manim
  Using cached manim-...
...
Collecting manimpango<version,>=version (from manim)
  ...
  error: subprocess-exited-with-error

  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
```

If ManimPango fails to install, it's likely that pip was not able to use the pre-built wheels for the manimpango dependency. You will need to make sure you have all the necessary build requirements. This is a known issue for Manim, you can check out their FAQ section to this topic [here](https://docs.manim.community/en/stable/faq/installation.html#why-does-manimpango-fail-to-install-when-running-pip-install-manim). Detailed instructions can be found in the [BUILDING section of ManimPango's README](https://github.com/ManimCommunity/ManimPango).

I took these steps to resolve this (last updated 2024-10-25):

1. Install GTK via MSYS2:

    - Download MSYS2 from [here](https://www.msys2.org/)
    - Open the MSYS2 terminal and run:

        ```
        pacman -Syu
        pacman -S wingw-w64-x86_64-gtk3
        ```

        If you're having issues with the second command, try running the following instead:

        ```
        pacman -S mingw-w64-ucrt-x86_64-gtk3
        ```

        If that still doesn't work, try:

        ```
        pacman -S mingw-w64-clang-x86_64-gtk3
        ```

    - Add `C:\msys64\mingw64\bin` to your system's PATH.

2. Install Microsoft Visual C++ Build Tools:

    - Download from Visual [C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
    - During installation, select "Desktop development with C++".

3. Retry Installing Manim after setting up the required tools.