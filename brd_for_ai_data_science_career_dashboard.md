# Business Requirements Document (BRD): AI, Data Science & Statistics Career & Education Analytics Dashboard

**Target AI Agent / Environment:** Antigravity  
**Project Name:** AI & Data Science Workforce & Education Intelligence Dashboard  
**Architecture:** Python Backend (Dash / Flask / FastAPI) + Plotly for Interactive Visualizations  

---

## 1. Project Overview & Objectives
This dashboard is designed to bridge the gap between academic supply (graduates, curricula, tuition fees, and acquired skills) and industry demand (open job positions, required skills, hiring companies, and salary benchmarks). It provides three interactive tabs with fully interconnected Plotly charts to analyze workforce trends and skill mismatches in AI, Data Science, and Statistics fields.

---

## 2. Technical Stack & Architecture Guidelines
1. **Backend:** Python (utilizing libraries such as Pandas for data manipulation, Dash or Streamlit for the web application framework).
2. **Visualization Engine:** Plotly (Plotly.py / Dash Plotly) as the core charting library.
3. **Interactivity / Cross-Filtering:** All charts within the same tab must feature inter-chart linking (Crossfiltering / Callback reactivity), ensuring that when a user selects a data point on one graph, all other graphs in that tab update dynamically.
4. **Data Format:** Open data datasets stored locally or pulled via APIs in JSON/CSV format.

---

## 3. Detailed Tab Specifications & Component Requirements

### Tab 1: ปริมาณคนที่จบและสเกลล์ที่เรียนมา (Academic Supply & Skills)
*Objective:* Analyze the production of graduates in AI, Data Science, and Statistics, their tuition costs, employment trajectories over 3 years, and core curriculum courses.

* **Required Charts & Components:**
  1. **หลักสูตรและจำนวนผู้สำเร็จการศึกษาต่อปี (Graduates by Program & Year):** 
     * Bar/Line chart displaying program names producing AI, Data Science, and Stat graduates and the count of graduates per year.
  2. **รายวิชาบังคับที่สอดคล้องกับสายงาน (Required Core Courses):**
     * Interactive table or matrix showing core mandatory courses offered by each curriculum mapped to industry requirements.
  3. **อัตราการได้งานทำหลังสำเร็จการศึกษา 3 ปี (Employment Tracking: Years 1-3):**
     * Multi-line chart showing the number/percentage of graduates employed in relevant fields in Year 1, Year 2, and Year 3 post-graduation.
  4. **ค่าเทอมของหลักสูตร (Tuition Fees):**
     * Bar chart or summary cards showing tuition costs across different programs for comparison.

---

### Tab 2: ปริมาณงานที่จ้าง และ Skills ที่ต้องการ (Industry Demand & Required Skills)
*Objective:* Examine open job market demand, required technical and soft skills, top hiring companies, and salary structures across experience levels.

* **Required Charts & Components:**
  1. **ปริมาณตำแหน่งงานว่าง (Open Job Positions):**
     * Bar or donut chart showing open vacancies categorized by sub-fields (AI, Data Science, Statistics).
  2. **ทักษะที่เป็นที่ต้องการสูงสุด (Top Required Skills):**
     * Horizontal bar chart or word cloud showing frequency of skills requested in job applications (e.g., Python, SQL, Machine Learning, PyTorch, R).
  3. **บริษัทที่รับสมัครงาน (Top Hiring Companies):**
     * Ranking chart or grid displaying major companies hiring in these domains.
  4. **โครงสร้างเงินเดือนตามระดับการทำงาน (Salaries by Career Levels):**
     * Box plot or grouped bar chart showing salary ranges across Entry-level, Mid-level, and Senior/Expert tiers.

---

### Tab 3: วิเคราะห์ Skill Mismatch (Skill Gap & Mismatch Analysis)
*Objective:* Compare the supply side (Tab 1 curriculum skills) against the demand side (Tab 2 required job skills) to identify gaps, over-supplied skills, and high-demand missing skills.

* **Required Charts & Components:**
  1. **Skill Gap Comparison Chart:**
     * Diverging bar chart or radar chart comparing curriculum coverage percentage vs. job market demand frequency for key technical skills.
  2. **Mismatch Insights Panel:**
     * Automated summary highlighting critical skills requested by employers that are underrepresented in academic programs.
  3. **Actionable Recommendations:**
     * Structured guidelines for academic institutions and job seekers to bridge identified gaps.

---

## 4. Execution & Implementation Guidelines for Antigravity
* Build a clean, responsive Python script using **Dash** or **Streamlit** integrated with **Plotly**.
* Ensure state management handles click/select events on charts to propagate filters across all components in Tabs 1 and 2.
* Organize code into modular components (`app.py`, `layout.py`, `callbacks.py`, `data_loader.py`).