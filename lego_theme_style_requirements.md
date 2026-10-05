# Style Requirements Handoff: Lego-Inspired UI Design System

**Target AI Agent / Environment:** Antigravity  
**Objective:** Transform the existing dashboard's visual style, layout aesthetics, color palette, and component design to match the playful, structured, toy-brick ("Lego") aesthetic presented in the reference image (`image_d14a7c.jpg`).

---

## 1. Core Visual Concept & Philosophy
* **Theme:** "Brick by Brick" Modular UI — clean white base contrasted with vibrant primary toy block colors (Blue, Red, Yellow, Green).
* **Card & Container Styling:** Rounded corners with heavy, soft drop shadows (`shadow-md` or custom neumorphic/claymorphism shadows) to mimic physical plastic building blocks.
* **Badges & Progress Bars:** Visualized as interlocking brick studs (`stud-pattern` borders or tactile textures) or segmented block bars.

---

## 2. Color Palette & Typography

### Primary Brand & Accent Colors:
* **Lego Blue:** `#0055BF` (Primary headers, sidebar active states, main accents)
* **Lego Red:** `#D40000` (Alerts, crucial action tabs, important badges)
* **Lego Yellow:** `#FFD700` / `#FFC107` (Highlight cards, upgrade buttons, warnings)
* **Lego Green:** `#228B22` / `#28A745` (Success metrics, completion indicators, build buttons)
* **Background & Surface:**
  * App Background: `#F4F6F9` (Soft light grey-white)
  * Card Surfaces: `#FFFFFF` with crisp rounded borders (`rounded-xl`).

### Typography:
* **Font Family:** Rounded, friendly sans-serif (e.g., *Nunito*, *Quicksand*, or *Inter* with rounded tracking).
* **Hierarchy:** Bold, friendly headers with clear weight distinction between item titles and metadata values.

---

## 3. UI Component Specifications

### A. Sidebar & Navigation
* **Sidebar Background:** Pure white or soft light grey with clean separation.
* **Active Links:** Highlighted using Lego primary colors (e.g., Blue or Yellow background pill with high-contrast text).
* **Branding Header:** Top-left logo featuring stacked toy blocks with bold playful typography.

### B. Progress & Metric Banners ("The Build Progress Bar")
* Progress bars must be styled like stacked Lego studs/bricks divided into colored segments (e.g., Green, Yellow, Blue, White) representing completion milestones.
* Large metric numbers displayed in bold contrasting colors accompanied by friendly mascot or avatar illustrations.

### C. Tabs & Navigation Pills
* Multi-tab interfaces styled as chunky, colored Lego bricks with bold numeric badges (`1 Income`, `2 Deductions`, `3 Credits`, etc.) in primary shades (Blue, Yellow, Red, Orange, Green).

### D. Data Cards & Lists
* **List Items:** Clean rows with status icons (green checkmarks inside circles) and smooth chevron dropdowns.
* **Side Panels / Inventories:** Sectioned cards with mini-brick count indicators and progress bars (e.g., "Forms Added: 3 of 6").

### E. Action Buttons
* **Primary CTA:** Chunky pill or rounded rectangle buttons styled like solid green or yellow Lego bricks with white bold text and subtle directional arrows (e.g., `Build Refund ->`).

---

## 4. Implementation Guidelines for Antigravity

1. **CSS / Tailwind Customization:** Add custom utilities or inline styles for soft toy-block shadows, rounded borders, and primary Lego color hex codes.
2. **Plotly Chart Integration:** Update chart templates (`template='plotly_white'`) to use the Lego color palette (`#0055BF`, `#D40000`, `#FFC107`, `#28A745`) and rounded container wrappers.
3. **Interactive Polish:** Ensure hover states feel tactile (slight scale up or shadow lift) mimicking pressing a brick.