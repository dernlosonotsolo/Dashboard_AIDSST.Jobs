# AI & Data Science Workforce & Education Intelligence Dashboard
*(Dashboard_AIDSST.Jobs)*

An interactive analytics and open data intelligence dashboard designed to bridge the gap between academic supply (graduates, curricula, tuition fees, and acquired skills) and industry demand (open job vacancies, required skills, hiring companies, and salary benchmarks) across **Artificial Intelligence (AI)**, **Data Science (DS)**, and **Statistics (ST)**.

---

## 📌 Project Overview & Objectives

In modern higher education and tech industries, rapid advances in AI and Data Science have widened the gap between what universities teach and what employers actively demand. This project delivers a unified intelligence dashboard providing:
1. **Academic Supply Intelligence**: Tracking graduate throughput, curriculum alignment, tuition costs, and 3-year post-graduation employment outcomes.
2. **Industry Demand Intelligence**: Aggregating open job vacancies, critical skill frequencies, top hiring companies, and compensation tiers.
3. **Skill Mismatch & Gap Analytics**: Quantifying the disconnect between university curricula and labor market needs, generating actionable recommendations for educators and job seekers.
4. **Open Data Management & CRUD Editor**: An interactive data catalog covering 7 core dimensions with real-time editing, local persistence, live search filtering, and one-click export to JSON and Markdown.

---

## 🏛️ Architecture & Technology Stack

The project employs a modern, lightweight, dependency-free architecture that can run instantly in any web browser or via a built-in Python runner:

- **Frontend & Styling:** [Tailwind CSS](https://tailwindcss.com/) (CDN) with modern responsive layout, slate/indigo styling, dark/light theme support, and accessible UI controls.
- **Visualizations:** [Plotly.js](https://plotly.com/javascript/) and [Chart.js](https://www.chartjs.org/) for responsive, high-performance charts, radar charts, diverging bars, box plots, and multi-line time series.
- **Reactivity & State Management:** Reactive client-side architecture with `localStorage` persistence for dynamic dataset updates, real-time filtering, and cross-filtering reactivity across charts.
- **Backend / Local Server:** Python 3 standard library server (`app.py`), requiring zero external pip dependencies and compatible with Python 3.14+.
- **Data Interchange:** Structured JSON schemas (`data/career_data.json`) with two-way Markdown (`.md`) export and import support.

---

## 📊 Core Dashboard Features & Tabs

### 🎓 Tab 1: ปริมาณคนที่จบและสเกลล์ที่เรียนมา (Academic Supply & Skills)
- **Graduates by Program & Year (หลักสูตรและจำนวนผู้สำเร็จการศึกษาต่อปี):** Interactive bar & line chart visualizing graduation counts across AI, Data Science, and Statistics degrees (2021–2024).
- **Required Core Courses Matrix (รายวิชาบังคับที่สอดคล้องกับสายงาน):** Structured matrix mapping mandatory university courses to corresponding industry domains (e.g., Deep Learning, Statistical Modeling, Big Data Systems).
- **3-Year Employment Tracking (อัตราการได้งานทำหลังสำเร็จการศึกษา 3 ปี):** Longitudinal multi-line chart tracking employment rates in relevant fields across Year 1, Year 2, and Year 3 post-graduation.
- **Tuition Fee Benchmarks (ค่าเทอมของหลักสูตร):** Comparative bar charts and summary cards illustrating total program tuition fees across universities.

### 💼 Tab 2: ปริมาณงานที่จ้าง และ Skills ที่ต้องการ (Industry Demand & Required Skills)
- **Open Job Vacancies (ปริมาณตำแหน่งงานว่าง):** Donut and bar charts breaking down open positions across AI, Data Science, Data Analytics, and Statistics.
- **Top Required Skills (ทักษะที่เป็นที่ต้องการสูงสุด):** Horizontal frequency ranking of high-demand technical and soft skills (Python, SQL, Machine Learning, PyTorch, Cloud/MLOps, R, BI tools).
- **Top Hiring Companies (บริษัทที่รับสมัครงาน):** Leaderboard displaying leading tech enterprises, financial institutions, telecom operators, and consulting firms actively hiring.
- **Salary Structure by Career Level (โครงสร้างเงินเดือนตามระดับการทำงาน):** Box plots and salary bands detailing compensation ranges across Entry-level, Mid-level, and Senior/Lead tiers.

### ⚖️ Tab 3: วิเคราะห์ Skill Mismatch (Skill Gap & Mismatch Analysis)
- **Skill Gap Comparison Chart:** Diverging bar and radar visualizations contrasting academic curriculum coverage percentage against industry demand frequency.
- **Automated Mismatch Insights Panel:** Algorithmic detection of critical high-demand skills underrepresented in academic curricula (e.g., MLOps, Cloud Infrastructure, Production Pipelines).
- **Actionable Strategic Recommendations:** Structured guidelines for academic institutions (curriculum modernization, industry co-ops) and job seekers (upskilling priorities, portfolio building).

### 🗂️ Tab 4: Open Data Catalog & Interactive CRUD Editor
- **7 Curated Data Categories:**
  1. `graduates`: จำนวนผู้สำเร็จการศึกษา (Graduates)
  2. `employment`: อัตราการมีงานทำ (Employment Rate)
  3. `salaries`: เงินเดือนเริ่มต้น (Starting Salaries)
  4. `companies`: บริษัทที่รับสมัคร (Hiring Companies)
  5. `countries`: ประเทศที่มีตลาดแรงงานสูง (Global Hubs)
  6. `skills`: ทักษะที่จำเป็น (Required Skills)
  7. `career_levels`: ระดับของสายงาน (Career Tiers)
- **Interactive CRUD Operations:** Add new records, edit existing entries, and delete data points dynamically within the UI.
- **Persistent State:** Saves all edits to browser `localStorage` with a 1-click "Reset to Default" feature.
- **Real-Time Global Search:** Instant keyword filtering across all dataset attributes and sources.
- **Data Export:** Export current live or modified datasets directly to Markdown (`.md`) or formatted JSON.
- **Direct Source Links:** Integrated hyperlinks to reputable open data sources (OECD, Kaggle, MHESI Open Data Thailand, US BLS, GitHub).

---

## 🚀 Getting Started

### Option 1: Run with Python Server (Recommended)
Clone the repository and run the built-in server with Python (Python 3.8+ or Python 3.14+ supported):

```bash
# Clone the repository
git clone https://github.com/dernlosonotsolo/Dashboard_AIDSST.Jobs.git
cd Dashboard_AIDSST.Jobs

# Start the local server
python app.py
```
Open your browser and navigate to:
```
http://localhost:8000
```

### Option 2: Standalone Browser Launch
Because the application is built as an interactive self-contained web app, you can also open `index.html` directly in any modern browser:
- Double-click `index.html`, or
- Right-click `index.html` → Open With → Chrome / Edge / Firefox / Safari.

---

## 📁 Project Structure

```
Dashboard_AIDSST.Jobs/
│
├── README.md                                # Comprehensive project documentation
├── PROJECT_STATUS.md                        # Step-by-step milestone and progress tracker
├── brd_for_ai_data_science_career_dashboard.md  # Original Business Requirements Document
├── handoff_for_antigravity_dashboard.md    # Original Antigravity handoff specification
│
├── index.html                               # Main interactive dashboard application
├── app.py                                   # Lightweight Python local server runner
│
└── data/
    └── career_data.json                     # Curated baseline dataset covering all 7 categories
```

---

## 🔗 Data Sources & Attribution

This project synthesizes open datasets and benchmarks from:
- [OECD Education and Skills Statistics](https://data.oecd.org/edu/graduates-rate.htm) - Graduate outputs and tertiary education metrics.
- [OECD.AI Policy Observatory](https://oecd.ai/en/data-insights) - AI labor market trends and international policy metrics.
- [US Bureau of Labor Statistics (BLS)](https://www.bls.gov/ooh/math/data-scientists.htm) - Data Scientists & Mathematical Sciences projections.
- [MHESI Open Data Thailand](https://data.go.th/) - Thai higher education graduate numbers and curriculum data.
- [Kaggle Data Science & AI Salaries](https://www.kaggle.com/datasets/adilshamim8/salaries-for-data-science-jobs/data) - Industry salary distributions.
- [Kaggle Data Science Employment Trends](https://www.kaggle.com/datasets/saurabhshahane/data-science-jobs-salaries) - Job postings and skill co-occurrence datasets.
- [GitHub Collections & Topics](https://github.com/topics/data-science-skills) - Curated industry skills frameworks.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
