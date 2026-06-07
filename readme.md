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

## Contributing


Contributions are welcome. To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.


Please ensure your code follows [PEP 8](https://peps.python.org/pep-0008/) style guidelines.


---
