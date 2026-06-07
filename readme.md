# Addis Ababa Climate Trend Analysis (1950-2024)

## Project Overview

This project analyzes 75 years of historical weather data for Addis Ababa, Ethiopia, to detect and quantify climate change trends.

### Key Findings

- **Total warming:** +1.53°C (1950-2024)
- **Warming rate:** 0.20°C per decade
- **Average temperature:** 14.9°C
- **Data analyzed:** 657,456 hourly observations

### Files

| File       | Purpose                                |
| ---------- | -------------------------------------- |
| `save.py`  | Fetches data from API and saves to CSV |
| `local.py` | Loads CSV and analyzes trends          |

---

## Step 1: Create Virtual Environment

**Windows:**

```bash
python -m venv venv
```

**Mac/Linux:**

```bash
python3 -m venv venv
```

## Step 2: Activate Virtual Environment

**Windows (Command Prompt):**

```bash
venv\Scripts\activate
```

**Windows (PowerShell):**

```bash
venv\Scripts\Activate.ps1
```

**Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

You'll know it worked when you see `(venv)` in your terminal prompt.

## Step 3: Set Up VS Code

Open your project folder in VS Code:

```bash
code .
```

Select Python interpreter:

1. Press `Ctrl+Shift+P`
2. Type `Python: Select Interpreter`
3. Choose `./venv/Scripts/python.exe` (Windows) or `./venv/bin/python` (Mac/Linux)

Open a new terminal (`Ctrl + \``) - venv should activate automatically.

## Step 4: Install Libraries

```bash
pip install requests pandas numpy matplotlib seaborn scipy
```

## Step 5: Fetch Data (First Time Only)

```bash
python save.py
```

This takes 2-3 minutes and creates:

- `addis_weather_1950_2024_hourly.csv`
- `addis_weather_1950_2024_daily.csv`

## Step 6: Run Analysis

```bash
python local.py
```

This generates `addis_climate_analysis.png`.


## Team Members
1. Abem Tigist FTP0053/14 
2. Betselot Tesfa FTP0327/14 
3. Birhan Aklilu FTP0363/14 
4. Edom Mulugeta FTP0503/14 
5. Eyoel Tedla FTP0598/14 

