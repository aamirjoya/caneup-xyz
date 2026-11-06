# upcaneup.info migration branch

This branch (`upcaneup-info`) serves https://upcaneup.info/ — the new home of
CaneUp after the 2026-11-06 migration from caneup.xyz.

- `baseURL` in hugo.toml is https://upcaneup.info/
- All hardcoded `https://caneup.xyz` links in layouts, static files and
  content were replaced with `https://upcaneup.info/` (105 files, 2026-11-06).
- Cloudflare Pages project `upcaneup-info` (account: Pashaaamir143@gmail.com)
  builds this branch with `hugo --gc --minify` and serves upcaneup.info.
- caneup.xyz 301-redirects to upcaneup.info (Redirect Rule on the caneup.xyz
  zone, path-preserving).

Sync: this branch is a snapshot of main as of 2026-11-06. New articles are
still pushed to `main` by the publishing crons — keep this branch in sync
until the crons are repointed (see the migration plan).
