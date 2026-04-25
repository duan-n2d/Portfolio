# Professional Data Engineer Portfolio & Technical Ecosystem

A highly optimized, data-driven developer portfolio and learning platform built with Jekyll. This ecosystem serves as a central hub for professional documentation, technical knowledge sharing, and project showcasing.

## Core Pillars

1.  **Professional Portfolio**: Impact-focused landing page and "About" section highlighting enterprise expertise.
2.  **Learning Journey**: A systematic technical knowledge base categorized by domain (Data Engineering, AI, Data Science, etc.).
3.  **Project Gallery**: Structured case studies demonstrating real-world technical problem-solving and impact.
4.  **Admin Portal**: Seamless content management integrated via Decap CMS.

## Tech Stack

- **Static Site Generator**: [Jekyll](https://jekyllrb.com/)
- **Styling**: Vanilla CSS with a centralized Design Token system
- **Design Philosophy**: Minimalist, premium aesthetic with a primary brand color of `#1128be`
- **CMS**: Integrated [Decap CMS](https://decapcms.org/) for programmatic content updates
- **Hosting & CI/CD**: GitHub Pages with automated builds and Link Checker validation

## Data-Driven Architecture

The project employs a structured data-first approach for maximum maintainability:

### Data Layers (`data/`)
- **`dyllan/`**: Personal information and bio data (`about-me.md`).
- **`learning/`**: Hierarchical technical content organized by domain (Data-Engineer, AI-Applications, etc.).
- **`projects/`**: Standardized case study documentation.

### Configuration & Components
- **`_data/`**: Site metadata, navigation hierarchies, and design-related YAML configs.
- **`_includes/`**: Modular Liquid components for headers, footers, sidebars, and cards.
- **`src/images/`**: Centralized asset management for profile, learning materials, and project visuals.

## Visual Design System

The system uses CSS Custom Properties (tokens) defined in `assets/css/design-tokens.css`:
- **Primary Color**: `#1128be` (Deep Blue)
- **Hover/Accent**: `#F8DE22` (Yellow)
- **Background**: `#FFFFFF` (Clean White)
- **Text**: `#000000` (Classic Black)

## Full Project Structure

| Path | Description |
| :--- | :--- |
| **`_data/`** | Global site configuration and data files. |
| ├── `navigation.yml` | Defines the header navigation and menu hierarchies. |
| ├── `learning_nav.yml` | Configures the technical learning sidebar structure. |
| └── `dyllan.yml` | Centralized personal metadata (author info, bio details). |
| **`_includes/`** | Reusable Liquid and HTML components. |
| ├── `header.html` / `footer.html` | Common site-wide layout elements. |
| ├── `sidebar-learning.html` | Dynamic technical navigation sidebar. |
| └── `author-card.html` | Profile component used across the portfolio. |
| **`_layouts/`** | Page templates determining the look of subpages. |
| ├── `default.html` | Baseline layout for all content pages. |
| └── `home.html` | Specialized layout for the landing page. |
| **`data/`** | The systematic content data layer (Source of Truth). |
| ├── `dyllan/` | Detailed "About Me" and personal documentation. |
| ├── `learning/` | Technical guides organized by domain-specific subdirectories. |
| └── `projects/` | Standardized documentation for professional case studies. |
| **`src/`** | Source assets for development and assets processing. |
| └── `images/` | Categorized site imagery (me, learning, projects, banner). |
| **`assets/`** | Built assets served to the browser. |
| ├── `css/` | Contains the design system and centralized tokens. |
| └── `js/` | Site-wide interactive logic and vendor libraries. |
| **`admin/`** | [Decap CMS](https://decapcms.org/) configuration files. |
| **`.github/`** | CI/CD pipeline definitions (Link checking, Deployment). |
| `index.md` | The main landing page of the portfolio. |
| `resume.md` | Dedicated page for viewing professional background. |
| `_config.yml` | Primary Jekyll site configuration and build settings. |

## Deployment & CI/CD

The repository includes a robust CI/CD pipeline in `.github/workflows/`:
- **Link Checker**: Automated validation using Lychee. Configured to handle Jekyll root-relative paths and remap site roots for error-free validation.
- **Auto-Deploy**: seamless promotion to GitHub Pages upon merge to `main`.

---

**Developed and Maintained by [Duan Nguyen Duy](https://github.com/duan-n2d)**
