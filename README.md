# Carbon Footprint Calculator - Dependencies and Setup Guide

## Overview

The Carbon Footprint Calculator is a Python-based application with a graphical user interface (GUI) built using `tkinter`. It allows users to calculate their carbon footprint, view results using different graph types, and save or load data from JSON files. The application also suggests ways to reduce carbon emissions if they exceed a certain threshold.

This guide outlines the dependencies required to run the application and steps to set it up on other devices.

---

## Dependencies

To ensure the program runs smoothly, the following dependencies are required:

1. **Python 3.8 or later**

   - The program is written in Python and requires version 3.8 or later to function properly.

2. **Required Python Libraries**

   - `tkinter`: For the GUI. (Comes pre-installed with Python.)
   - `matplotlib`: For generating bar and pie charts.
   - `json`: For saving and loading data. (Part of Python's standard library.)
   - `os`: For file handling. (Part of Python's standard library.)
   - `random`: For generating random suggestions. (Part of Python's standard library.)

---

## Installation Guide

Follow these steps to set up the program on another device:

1. **Install Python**

   - Download and install Python from the [official website](https://www.python.org/downloads/).
   - During installation, ensure you check the option to "Add Python to PATH."

2. **Install Required Libraries**

   - Open a terminal or command prompt and run the following command to install `matplotlib`:
     ```bash
     pip install matplotlib
     ```

3. **Download the Program Files**

   - Save the main Python script (`carbon_footprint_calculator.py`) and ensure all required files are in the same directory.

4. **Run the Program**

   - Navigate to the directory containing the Python script.
   - Execute the script using the command:
     ```bash
     python carbon_footprint_calculator.py
     ```

---

## Notes

- If `tkinter` is not available on your Python installation, you may need to install it separately. Refer to the [tkinter installation guide](https://tkdocs.com/tutorial/install.html).
- The program saves data in JSON format for easy loading and reuse.
- Suggestions for reducing carbon emissions are randomly selected from a predefined list and stored in the JSON file when emissions exceed 40,000 kg CO2.

---

## Troubleshooting

- **Error: Module not found**: Ensure all dependencies are installed. Reinstall missing libraries using `pip`.
- **Graph not displaying**: Ensure `matplotlib` is correctly installed and the Python environment supports GUI operations.
- **Permission Issues**: Run the terminal or command prompt with administrative privileges if file access errors occur.

---

For any issues, consult the program developer or refer to the Python and library documentation.

(∩^o^)⊃━☆
