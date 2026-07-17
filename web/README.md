# AI Agents Atlas web catalog

The catalog is a React/Vite presentation layer over repository content. It imports project metadata,
READMEs, source files, course files, and the preserved upstream catalog at build time.

## Run locally

```bash
npm ci
npm run dev
```

## Production build

```bash
npm run build
npm run preview
```

Node.js 20 or newer is required. `package-lock.json` is canonical and must be updated with npm.

## Content architecture

- `src/content.js` parses repository files into catalog records.
- `src/App.jsx` renders hash-based catalog routes.
- `src/styles.css` owns the responsive visual system.
- Project files and metadata remain canonical; do not add a second manual project list.

The web catalog does not execute agents or collect credentials. External catalog links lead to
independently governed repositories and may change without notice.

## License and attribution

The application is distributed under the root [MIT License](../LICENSE). Repository content retains
the attribution described in [ATTRIBUTION.md](../ATTRIBUTION.md).
