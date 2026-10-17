# Innova Physics UPV Handbook

Source of the team handbook, built with [mdBook](https://github.com/rust-lang/mdBook) and published with GitHub Pages.

**Edition 2026-27, version 1.0.**

## Build

Install mdBook 0.5.4 (a single binary from its releases page), then:

    mdbook serve      # local preview at http://localhost:3000
    mdbook build      # static site in ./book

## Publish

The workflow in `.github/workflows/deploy.yml` builds every pull request and deploys `main` to GitHub Pages. In the repository settings, set **Pages > Source** to **GitHub Actions**, then uncomment `site-url` and `git-repository-url` in `book.toml`.

## Editing in one file

`src/` is the source of truth. To review or edit the whole book in one file:

    python3 scripts/reading-copy.py build reading-copy.md   # src/ -> one file
    python3 scripts/reading-copy.py split reading-copy.md   # one file -> src/

`split` matches chapters by their level-1 heading. After a split, run `mdbook build` and `scripts/check-style.sh`, and read `git diff` before committing.

## Rules for this book

- It holds what stays true for a whole season. `src/season.md` is rewritten each September; anything that changes faster belongs on the website or in the internal documentation.
- It is public. Names of people, money, rosters, contacts, access details, the laboratory's location, procedures in force and the list of authorised operators stay out of it. Partners are named only with their agreement.
- Copy: aims are stated as aims ("we aim to"); every number carries its unit and status; "electron source", never "gun"; no em dashes.
- Changes arrive as pull requests and are merged by Direction.
- Soft word budget: 500 words per chapter, 4,000 for the book. `scripts/check-style.sh` reports the counts and fails on em dashes and on "gun".
- Versions follow the team's document convention: 1.0 at release, 1.1 for a correction that changes no rule, 2.0 for a change of substance. Tag each edition, for example `edition-2026-27`.
- Source language is English. Translations derive from it.
