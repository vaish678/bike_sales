# Bike Sales EDA in India (2015-2024)

This project performs **Exploratory Data Analysis (EDA)** on bike sales data in India.  
It uses **Python** along with popular libraries: **NumPy, Pandas, Matplotlib, and Seaborn**.  

The analysis focuses on **brand-wise sales, state-wise sales, and year-wise trends** using different visualization techniques.

---

## 🗂 Dataset
- Filename: `bike_sales_india.csv`
- Columns include:
  - `Brand` – Bike brand (Royal Enfield, Bajaj, KTM, etc.)
  - `State` – Indian state where the bike was sold
  - `Registration Year` – Year the bike was registered (used as purchase year)
  - `Price (INR)` – Sale price
  - `Other columns` – Insurance, City Tier, Seller Type, Resale Price, etc.

> The dataset was cleaned to remove **null values** and **duplicate rows**, and unnecessary columns were dropped.

---

## 🔧 Tools & Libraries
- **Python 3.x**
- **NumPy** – Numerical operations
- **Pandas** – Data manipulation
- **Matplotlib** – Plotting basic charts
- **Seaborn** – Advanced statistical plots and heatmaps

---

## 📊 Analysis & Visualizations

### 1. Year-wise Sales
- Tracked **bike sales per year** for each brand.
- Visualizations:
  - **Line Plot** with markers to show trends.
  - **Bubble Plot** to represent sales counts by year.

### 2. State-wise Sales
- Count of bikes sold in each state.
- Visualizations:
  - **Bar Plot** with counts on top of bars.
  - **Heatmap** for multiple brands vs states.

### 3. Brand-wise Total Sales
- Total sales of each brand across all years and states.
- Visualizations:
  - **Bar Chart**
  - **Pie Chart** (for proportion/market share)

### 4. Multi-brand Comparison
- Combined **line plots and heatmaps** to compare trends and regional distribution among brands like Royal Enfield, Bajaj, KTM, Yamaha, Hero, Honda, Kawasaki, and TVS.

---

## 💡 Key Insights
- Royal Enfield shows a steady upward trend in sales over the years.
- Some states are stronger markets for specific brands.
- Heatmaps help to **identify regional sales patterns** for multiple brands.
- Line and scatter plots effectively show **year-wise trends**.

---

## 📝 How to Run
1. Clone the repository:
```bash
git clone https://github.com/yourusername/bike-sales-eda.git
