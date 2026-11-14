# Master Electric, LLC website

Live at https://masterelectricdenver.com (GitHub Pages, custom domain).

## Structure
- `site/` — the live website: plain HTML/CSS, one file per page. This folder is what gets published.
- `tools/build_site.py` — generates every page in `site/` from one place (shared header, footer, SEO tags, sitemap). Edit content there and run `python3 tools/build_site.py`.
- `src/`, `public/` — the previous React version, kept for reference (no longer deployed).

## Deploy
```
npm install        # first time only
npm run deploy     # publishes site/ to the gh-pages branch
```
Changes show up on masterelectricdenver.com within a few minutes.

## Contact form
The quote form posts to Web3Forms (web3forms.com, free plan, 250 submissions/month), which emails submissions to masterelectricllc@outlook.com. The access key is `WEB3FORMS_KEY` in `tools/build_site.py`; it is public by design. After sending, visitors are redirected to thank-you.html.
