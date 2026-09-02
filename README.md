# disney-plus-data-analysis
# Disney+ Data Analysis & Visualization Project 🎬📊

A Python-based data analysis project that explores the Disney+ streaming catalog. This project cleans real-world streaming data using **Pandas** and generates distinct statistical visualizations using **Matplotlib** to uncover insights about content distribution, runtimes, geographical production trends, and catalog growth.

---

## 📈 Visualizations Included

The project cleans data from a `disney_plus_shows.csv` file and dynamically plots:
1. **Rating Distribution:** A clear breakdown of content ratings across the platform.
2. **Movie Duration Histogram:** A distribution chart showing the typical runtime lengths of movies on Disney+ (filtered and parsed dynamically into integer minutes).
3. **Top Producing Countries:** A horizontal bar chart isolating the top global regions producing content for the platform.
4. **Historical Release Trends:** A side-by-side subplot visualization comparing the volume of **Movies** vs. **TV Shows** released over the years.

---

## 🛠️ Tech Stack & Requirements

Make sure you have Python installed alongside the following standard data analysis libraries:

* **Python 3.x**
* **Pandas** (for data handling and extraction)
* **Matplotlib** (for chart generation and layouts)

To install the required libraries, run the following command in your terminal:
```bash
pip install pandas matplotlib
```

---

## 🚀 How to Run the Project

1. Clone or download this repository to your local system.
2. Ensure your dataset file is named `disney_plus_shows.csv` and is placed in the exact same directory as your Python script.
3. Open the project folder in **VS Code**.
4. Open `project.py` and run the script by clicking the **Play Button** in the top-right corner.

### File Structure Note
The script is configured to auto-save every generated chart directly into your project workspace as a `.png` file (e.g., `disney_releases_per_year.png`, `disney_top_countries.png`) before rendering interactive popup windows.

