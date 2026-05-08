# Architecture

> **This file is maintained automatically by the AI. Do not edit manually unless correcting an error. The only field you need to fill in is the Project Description below — the AI derives or grows everything else.**

> **Scope:** Single-app project — a vanilla-JS web frontend for Tunefry. No backend, mobile, desktop, or CLI work in this repo.

---

## Project Description

Tunefry is a music distribution & artist dashboard. Current scope of *this* repo: a vanilla-JS web frontend only. A shared REST backend and native iOS/Android artist apps are planned at the product level but are **out of scope here** — this codebase ships only the web client.

---

## Project

- **Name:** Tunefry Web Dashboard
- **Type:** Single-app (web frontend)
- **Purpose:** Artist-facing dashboard for music distribution, releases, royalties, and promotion tools.
- **Target Users:** Independent musicians and label managers using Tunefry to distribute and monitor releases.
- **Stage:** MVP — static HTML/CSS/JS pages, no backend wired in yet.
- **Repo Layout:** Single folder; one HTML file per dashboard route at the root, with shared `css/` and `js/` and an image folder `PHOTOS/`.
- **App Relationship Model:** Standalone web client. A backend exists at the product level but is not part of this repo; this app currently runs entirely client-side with mocked data.

---

## Applications

### Summary

| App | Platform | Kind | Location | Uses | Status |
| --- | -------- | ---- | -------- | ---- | ------ |
| tunefry-web | web | Static multi-page SPA-style dashboard (vanilla HTML/CSS/JS) | `./` (repo root) | — (no backend wired yet) | active |

### Per-App Detail

### App: tunefry-web
- **Platform:** web
- **Location:** repo root
- **Kind:** Vanilla HTML + CSS + JS, multi-page (one `.html` per route), shared `css/styles.css` and `js/app.js`.
- **Purpose:** Artist dashboard UI — releases, uploads, stats, payouts, marketplace, support.
- **Runtime dependencies:** None yet (no backend integration).
- **Platform constraints:** Modern evergreen browsers (Chrome, Edge, Firefox, Safari — last 2 versions). Responsive down to ~360px width; layout pivots at 1200px.
- **Distribution:** Static hosting (TBD).
- **Status:** active

---

## Shared Code / Packages

_Single-app project — no cross-app shared packages. Internal sharing is done via `css/styles.css` and `js/app.js` consumed by every page._

| Package | Location | Contents | Consumed By |
| ------- | -------- | -------- | ----------- |
| styles  | `css/styles.css` | Global design tokens, sidebar, topbar, cards, mobile overrides, notifications dropdown | all HTML pages |
| landing | `css/landing.css` | Landing/marketing styles | `index.html` (and other public pages, as applicable) |
| app     | `js/app.js` | Topbar/notifications wiring, shared interactions | all HTML pages |
| photos  | `PHOTOS/` | Logo and image assets (`tunefry-logo.png`, etc.) | all HTML pages |

---

## Tech Stack

### Web Client
| Layer | Choice | Version | Notes |
| ----- | ------ | ------- | ----- |
| Markup | HTML5 | — | One file per route at repo root |
| Styling | Hand-written CSS | — | `css/styles.css` is the main shared sheet |
| Scripting | Vanilla JavaScript (ES2017+) | — | No framework, no bundler, no build step |
| Module system | Plain `<script>` tags | — | `js/app.js` loaded per page |

### Shared / Tooling
| Layer | Choice | Version | Notes |
| ----- | ------ | ------- | ----- |
| Build | None | — | Files served as-is |
| Package manager | None | — | No `package.json` |
| Lint/format | None configured | — | Manual style consistency |

---

## Dependencies

### Web
| Package | Purpose | Added |
| ------- | ------- | ----- |
| _(none)_ | Project is dependency-free; no npm/CDN runtime libraries | — |

---

## File Structure

```
.
├── ARCHITECTURE.md
├── CLAUDE.md
├── index.html              # Overview / landing dashboard
├── home.html
├── login.html
├── signup.html
├── profile.html
├── profile-mismatch.html
├── current-plan.html
├── pricing.html
├── help.html
├── connect.html
├── refer-earn.html
├── marketplace.html
├── services.html
├── stats.html
├── daily.html
├── releases.html
├── new-album.html
├── new-song.html
├── album-upload.html
├── song-upload.html
├── transfer-album.html
├── transfer-song.html
├── pitch-song.html
├── ai-blog.html
├── insta-link.html
├── claim-removal.html
├── withdrawal.html         # (referenced by app)
├── fix_services.py         # one-off maintenance script (not shipped)
├── rebuild_services.py     # one-off maintenance script (not shipped)
├── update_services.py      # one-off maintenance script (not shipped)
├── css/
│   ├── styles.css
│   └── landing.css
├── js/
│   └── app.js
└── PHOTOS/
    ├── tunefry-logo.png
    └── 102740.png
```

---

## Architecture Overview

Standalone, fully client-side web app. There is no backend in this repo and no API client. Pages are independent HTML documents that share styling via `css/styles.css` and shared interactions (notifications dropdown, etc.) via `js/app.js`. Navigation is plain `<a>` links between pages. State is per-page and ephemeral; any data shown is currently hard-coded or mocked in markup/JS.

A real backend is planned at the product level but explicitly **out of scope** for this repo until contracts are defined.

---

## API Contracts

_No API integration in this repo yet. This section will be populated only when the web client starts calling a real backend. Until then, treat all data as mocked in-page._

---

## Data Models

_No persistent or shared models. Any structures (e.g. the `demoNotifications` array in `js/app.js`) are local mocks scoped to a single page/feature._

---

## State Ownership

- **Server state:** N/A (no backend wired).
- **Per-client cache:** N/A.
- **Local-only state (UI, ephemeral):** Per-page DOM state; e.g. notifications dropdown open/closed and read flags on `demoNotifications` in `js/app.js`.
- **Device persistence:** None currently. No `localStorage`, cookies, or IndexedDB usage.

---

## Auth Flow

_No auth implemented. `login.html` and `signup.html` are UI-only mockups today. To be defined when the backend lands._

---

## Error Contract

_No network errors today (no API calls). Client-side UX errors are surfaced via inline messages / toasts inside each page._

---

## Cross-Cutting Concerns

- **Browser support matrix:** Latest 2 versions of Chrome, Edge, Firefox, Safari.
- **Responsive breakpoints:** Layout pivots at `max-width: 1200px` (right panel hides; mobile fallback panels appear and reorder via flex `order`).
- **Accessibility:** Not formally audited yet. Use semantic HTML and `title`/`aria-label` on icon buttons where added.
- **Internationalization:** English only. No i18n infrastructure.
- **Analytics / telemetry:** None.
- **Feature flags:** None.

---

## Key Design Decisions

- **No framework, no build step.** Project is intentionally vanilla HTML/CSS/JS so pages can be served statically and edited without tooling. Tagged `[WEB]`.
- **Mobile fallback via `display: contents` + flex `order`.** On `index.html`, right-panel-only content is mirrored inside `.mobile-overview-panels`, which becomes `display: contents` below 1200px so its children participate in the main column's flex order. Tagged `[WEB]`.
- **Shared assets centralised under `PHOTOS/`.** Logo and image assets live in `PHOTOS/` and every page references `PHOTOS/tunefry-logo.png`. Tagged `[WEB]`.
- **Notifications dropdown wired globally via `js/app.js`.** Bell icon (`.icon-btn[title="Notifications"]`) gets a dropdown injected on `DOMContentLoaded` so every page that includes `js/app.js` gets the same behaviour without per-page markup. Tagged `[WEB]`.

---

## Environment Variables

### Web
| Variable | Purpose | Required | Default | Public? |
| -------- | ------- | -------- | ------- | ------- |
| _(none)_ | No build step or runtime config | — | — | — |

---

## External Integrations

| Service | Consumed By | Purpose | Auth | Failure Mode |
| ------- | ----------- | ------- | ---- | ------------ |
| _(none yet)_ | — | — | — | — |

---

## Testing Strategy

- **Web unit / component:** None set up. Manual verification via browser.
- **End-to-end:** None set up.
- **How to run locally:** Open any `.html` file directly in a browser, or serve the repo root with any static server (e.g. `python -m http.server`).

---

## Local Development

- **Prereqs:** A modern browser. Optional: any static file server (Python, `npx serve`, VS Code Live Server).
- **First-time setup:** None — clone and open.
- **Run web:** Either:
  - Double-click `index.html` (or any other page) to open it in the browser, **or**
  - From the repo root: `python -m http.server 8000` then visit `http://localhost:8000/index.html`.
- **Seed data / test accounts:** N/A — all data is mocked in markup/JS.

---

## Deployment & Distribution

- **Web hosting / CDN:** TBD (any static host: GitHub Pages, Netlify, Vercel static, S3+CloudFront, etc.).
- **CI/CD pipelines:** None configured.
- **Release cadence:** Ad-hoc.
- **Secrets management:** N/A — no secrets in repo.
- **Rollback plan:** Redeploy previous static snapshot.

---

## Technical Debt

- [ ] `[WEB]` Sidebar markup is duplicated across ~20 HTML pages — any nav change must be applied to every file. Consider extracting via a server-side include or a tiny build step if this grows.
- [ ] `[WEB]` No automated tests of any kind.
- [ ] `[WEB]` `login.html` / `signup.html` are UI-only; no real auth.
- [ ] `[WEB]` Dashboard data is hard-coded — no API integration.

---

## Known Bugs

- [ ]

---

## Out of Scope

- Backend / REST API (lives outside this repo).
- Native iOS and Android apps (planned at product level, not in this repo).
- Desktop and CLI clients.
- Build tooling, bundlers, frameworks (React/Vue/etc.), TypeScript.
- Authentication implementation, payments integration, real data wiring.

---

## Changelog

_Updated every session with a one-line summary. Always include one or more scope tags._

**Scope tag legend** _(trimmed to match this single-app web project):_

- `[WEB]` web client (this app)
- `[DOCS]` documentation only (this file, CLAUDE.md, READMEs)
- `[INFRA]` tooling, hosting, CI

| Date | Scope | Change |
| ---- | ----- | ------ |
| 2025-11-21 | [DOCS] | Bootstrapped ARCHITECTURE.md and CLAUDE.md from multi-platform template; trimmed to single web app (vanilla JS frontend only) per project description. |
| 2026-05-08 | [DOCS] | Confirmed project name "Tunefry Web Dashboard" and stage = MVP. |
