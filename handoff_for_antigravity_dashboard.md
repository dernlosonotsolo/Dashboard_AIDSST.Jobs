# Handoff Specification for Antigravity: Interactive Open Data Dashboard

**Target AI Agent / Environment:** Antigravity  
**Goal:** Build a fully interactive, single-file HTML/JS Dashboard that aggregates, visualizes, and allows user-editing of the Open Data sources, career metrics, salary benchmarks, required skills, and career tiers for AI, Data Science, and Statistics fields.

---

## 1. Core Requirements & Architecture
* **Format:** Single-file HTML (`index.html`) using modern Tailwind CSS (via CDN), Alpine.js or vanilla JavaScript for reactivity, and Chart.js for data visualization.
* **Layout:** Responsive sidebar navigation or tabbed layout with sections matching our structured Markdown data (`ai_data_statistics_resources.md`).
* **Design System:** Professional dark/light mode friendly, clean card layouts, badge tags for career levels, and responsive tables.

---

## 2. Interactive Features to Implement
1. **Data Aggregation & Display:**
   - Render all 7 data categories clearly: Graduate Stats, Employment Rates, Starting Salaries, Top Hiring Companies, Global Countries, Required Skills, and Career Tiers.
   - Display direct hyperlinks to the curated open data download links (Kaggle, OECD, BLS, GitHub).
2. **Interactive CRUD Editor:**
   - Allow users to **Add, Edit, and Delete** data entries dynamically within the UI.
   - Provide a persistent local state using `localStorage` so edits remain during session reloads.
3. **Filtering & Search:**
   - A real-time search bar that filters datasets by keywords (e.g., "Python", "US", "Junior", "OECD").
4. **Export Capability:**
   - A button to export the modified dataset directly back into Markdown (`.md`) or JSON format.

---

## 3. Structured Data Schema to Embed
Antigravity should initialize the dashboard state with this core JSON dataset extracted from our previous findings:

```json
{
  "categories": [
    {
      "id": "graduates",
      "name": "จำนวนผู้สำเร็จการศึกษา (Graduates)",
      "description": "สถิติผู้จบการศึกษาด้าน AI, Data Science และ Statistics",
      "sources": [
        {"title": "OECD Education and Skills Statistics", "url": "https://data.oecd.org/edu/graduates-rate.htm"},
        {"title": "Kaggle STEM Graduates Dataset", "url": "https://www.kaggle.com/datasets"},
        {"title": "MHESI Open Data Thailand", "url": "https://data.go.th/"}
      ]
    },
    {
      "id": "employment",
      "name": "อัตราการมีงานทำ (Employment Rate)",
      "description": "สถิติอัตราการจ้างงานหลังจบการศึกษา",
      "sources": [
        {"title": "US BLS Data Scientists Projections", "url": "https://www.bls.gov/ooh/math/data-scientists.htm"},
        {"title": "Kaggle Data Science Employment Trends", "url": "https://www.kaggle.com/datasets/saurabhshahane/data-science-jobs-salaries"}
      ]
    },
    {
      "id": "salaries",
      "name": "เงินเดือนเริ่มต้น (Starting Salaries)",
      "description": "โครงสร้างค่าตอบแทนและฐานเงินเดือนสำหรับบัณฑิตจบใหม่และผู้มีประสบการณ์น้อย",
      "sources": [
        {"title": "Kaggle Data Science & AI Salaries", "url": "https://www.kaggle.com/datasets/adilshamim8/salaries-for-data-science-jobs/data"},
        {"title": "Open Government Data Thailand Salary Reports", "url": "https://data.go.th/"}
      ]
    },
    {
      "id": "companies",
      "name": "บริษัทที่รับสมัคร (Hiring Companies)",
      "description": "รายชื่อบริษัทเทคโนโลยีและองค์กรชั้นนำที่เปิดรับตำแหน่งสาย Data & AI",
      "sources": [
        {"title": "GitHub Top AI & Tech Companies Dataset", "url": "https://github.com/collections/machine-learning"},
        {"title": "Kaggle Tech Job Postings", "url": "https://www.kaggle.com/datasets"}
      ]
    },
    {
      "id": "countries",
      "name": "ประเทศที่มีตลาดแรงงานสูง (Global Hubs)",
      "description": "ประเทศที่มีอัตราการจ้างงานและความต้องการบุคลากรเข้มข้น",
      "sources": [
        {"title": "OECD.AI Policy Observatory", "url": "https://oecd.ai/en/data-insights"},
        {"title": "Kaggle Global Salary Landscape", "url": "https://www.kaggle.com/datasets/lainguyn123/data-science-salary-landscape"}
      ]
    },
    {
      "id": "skills",
      "name": "ทักษะที่จำเป็น (Required Skills)",
      "description": "Hard Skills & Soft Skills ที่ระบุในประกาศรับสมัครงานมากที่สุด",
      "sources": [
        {"title": "Kaggle Job Description Text Mining", "url": "https://www.kaggle.com/datasets"},
        {"title": "GitHub Awesome Data Science Skills", "url": "https://github.com/topics/data-science-skills"}
      ]
    },
    {
      "id": "career_levels",
      "name": "ระดับของสายงาน (Career Tiers)",
      "description": "แบ่งระดับ Entry, Mid, และ Senior / Expert",
      "sources": [
        {"title": "Industry Standard Career Frameworks", "url": "#"}
      ]
    }
  ]
}
```

---

## 4. Execution Directive for Antigravity
Please generate the fully functional single-file dashboard application incorporating the layout, interactive editor, search, and export features defined above.