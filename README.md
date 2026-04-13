# 🚀 Unified Developer Portfolio & Ecosystem

Welcome to my unified developer ecosystem! This repository consolidates two primary hubs into a single, high-performance Jekyll-based platform:

1.  **Personal Portfolio**: A high-impact landing page reflecting my current focus as a Data Engineer.
2.  **Learning Journey**: A structured technical knowledge base covering Data Engineering, Data Science, AI, and CS fundamentals.
3.  **Resume**: A direct PDF view of my latest professional background.

---

## 📂 Architecture & Folder Roles

### 🏛️ Structural Components
- **`_data/`**: Centralized configuration.
    - `navigation.yml`: Manages the main header dropdowns and logical grouping.
    - `learning_nav.yml`: Specifically manages the hierarchical learning sidebar.
- **`_includes/`**: Modular Liquid components.
    - `header.html`: Implements the dynamic, nested navigation system.
    - `sidebar-learning.html`: The specialized technical navigation sidebar.
- **`_layouts/`**: Presentation templates.
    - `default.html`: Core structure for the entire site.
- **`assets/`**: Shared CSS design tokens, JavaScript logic, and vendor libraries.

### 🍱 Content Hubs
- **`/learning/`**: Categorized technical notes. Each category (e.g., `Data-Engineer`) has its own `index.md` landing page.
- **`resume.md`**: Dedicated page for the PDF Resume view.

---

## ⚙️ Core Logic

### 1. Context-Aware Sidebars
To maintain a clean user experience, the **Learning Journey Sidebar** only appears when browsing content within the `/learning/` directory. This logic is handled in `_layouts/default.html` using:
```liquid
{% if page.url contains '/learning/' and page.url != '/learning/index.html' %}
  {% include sidebar-learning.html %}
{% endif %}
```

### 2. Grouped Navigation
Navigation is organized into three primary groups in `_data/navigation.yml`:
- **Academic Hub**: Grouped scholarly pages.
- **Learning Journey**: Grouped technical specializations.
- **Admin**: Quick access to content management.

---

## 🧹 Refactoring & Cleanup Note
During the consolidation of this ecosystem, several redundant or placeholder components were removed to ensure maintainability:
- **Redundant Layouts**: Eliminated duplicate `sidebar` inclusions that caused dual-sidebar issues.
- **Placeholder Pages**: Removed template sample pages (e.g., `archive-layout-with-content.md`) and empty HTML stubs.
- **Hardcoded Links**: Replaced manual HTML links in the header with dynamic Liquid loops that pull from `navigation.yml`.

---

## 🚀 Development & Deployment
- **Built with**: [Jekyll](https://jekyllrb.com/)
- **Deployment**: Automated via GitHub Actions (Static Deployment).
- **CMS**: Integrated with Decap CMS at `/admin`.

Developed with ❤️ by [NDoubleD](https://github.com/duan-n2d)
