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

- **Frontend & Styling:** [Tailwind CSS](https://tailwindcss.com/) (CDN) with a **Lego-Inspired UI Design System** ("Brick by Brick" modular architecture, primary Lego colors `#0055BF` Blue, `#D40000` Red, `#FFC107` Yellow, `#28A745` Green, 3D tactile brick cards with bottom bevels, toy studs, segmented Build Progress Bar, and friendly rounded typography `Nunito` / `Prompt`).
- **Visualizations:** [Plotly.js](https://plotly.com/javascript/) and [Chart.js](https://www.chartjs.org/) customized with the Lego primary color palette, rounded block bars, radar charts, diverging bars, box plots, and multi-line time series.
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

## 🔗 Data Sources & Attribution (แหล่งข้อมูลจริงและการอ้างอิง)

แดชบอร์ดนี้ใช้ข้อมูลสถิติจริงที่ได้รับการตรวจสอบจากหน่วยงานทางการและรายงานดัชนีแรงงานชั้นนำ:

1. **สถิติผู้สำเร็จการศึกษา (Graduates Throughput):**
   - [สำนักงานปลัดกระทรวงการอุดมศึกษา วิทยาศาสตร์ วิจัยและนวัตกรรม (สป.อว. / MHESI)](https://data.mhesi.go.th/) - ข้อมูลสถิติจำนวนผู้สำเร็จการศึกษาระดับอุดมศึกษา ปีการศึกษา 2564–2567
   - [ระบบเปิดเผยข้อมูลภาครัฐ DGA (data.go.th)](https://data.go.th/dataset/graduates-higher-ed) - ชุดข้อมูลบัณฑิตสายวิทยาศาสตร์และเทคโนโลยี
   - [OECD Education at a Glance](https://data.oecd.org/edu/graduates-rate.htm) - สถิติเปรียบเทียบผู้สำเร็จการศึกษาสาขา STEM ระดับนานาชาติ

2. **อัตราการมีงานทำและสายงานที่ได้งานทำ (Employment Rate & Tracking):**
   - [รายงานผลการสำรวจภาวะการมีงานทำของบัณฑิต (MHESI 2565–2567)](https://data.go.th/dataset/employment-rate-graduates) - ติดตามภาวะการมีงานทำตรงสายงานของบัณฑิตจบใหม่ปีที่ 1, 2 และ 3
   - [JobsDB by SEEK: Thailand Career & Employment Trends 2024](https://th.jobsdb.com/) - แนวโน้มการจ้างงานสายเทคโนโลยี

3. **ฐานเงินเดือนและโครงสร้างค่าตอบแทน (Salary Benchmarks):**
   - [Adecco Thailand Salary Guide 2024 / 2025](https://adecco.co.th/salary-guide) - ฐานเงินเดือนขั้นต่ำ กลาง และสูงสุดในตำแหน่ง Data Science, AI Engineer, BI Analyst และ Data Engineer
   - [Michael Page Thailand Technology Salary Benchmark 2024](https://www.michaelpage.co.th/salary-guide) - รายงานค่าตอบแทนกลุ่มอุตสาหกรรมเทคโนโลยีดิจิทัล
   - [US Bureau of Labor Statistics (BLS) Occupational Employment 2023–2024](https://www.bls.gov/oes/current/oes152051.htm) - ข้อมูลค่าตอบแทนเฉลี่ยสาย Data Scientists สหรัฐอเมริกา

4. **ตำแหน่งงานว่างและบริษัทที่รับสมัคร (Job Vacancies & Hiring Companies):**
   - [JobsDB by SEEK Tech Hiring Index Q3 2024](https://th.jobsdb.com/) - ปริมาณตำแหน่งงานว่างในไทยแยกตามสายงานย่อย
   - [JobTopGun & LinkedIn Top Tech Employers Thailand 2024](https://www.jobtopgun.com/) - อันดับองค์กรเทคโนโลยีและสถาบันการเงินที่เปิดรับสมัครสูงสุด

5. **การวิเคราะห์ทักษะและ Skill Mismatch (Skills Demand & Gap Analytics):**
   - [สถาบันวิจัยเพื่อการพัฒนาประเทศไทย (TDRI)](https://tdri.or.th/) - รายงานวิจัย "Bridging the Digital Skills Gap in Thailand"
   - [World Economic Forum (WEF) Future of Jobs Report 2023–2024](https://www.weforum.org/publications/the-future-of-jobs-report-2023/)
   - [Kaggle Machine Learning & Data Science Survey 2023–2024](https://www.kaggle.com/datasets/adilshamim8/salaries-for-data-science-jobs/data)
   - [สมาคมปัญญาประดิษฐ์ประเทศไทย (AIAT)](https://aiat.or.th/) - กรอบมาตรฐานทักษะปัญญาประดิษฐ์และการประยุกต์ใช้งาน

6. **ค่าเล่าเรียนและหลักสูตรแกนกลาง (Tuition Fees & Curricula):**
   - [ระบบการคัดเลือกกลางบุคคลเข้าศึกษาในสถาบันอุดมศึกษา (myTCAS.com 2567)](https://www.mytcas.com/) - อัตราค่าธรรมเนียมการศึกษาจริง
   - เล่มหลักสูตรระดับปริญญาตรี (มคอ.2) ที่ผ่านการรับรองจาก สกอ. และกระทรวง อว.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
