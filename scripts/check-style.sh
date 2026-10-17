#!/usr/bin/env bash
# Style checks for the handbook.
# Fails on em dashes and on the word "gun" (house style: "electron source").
# Reports word counts against the soft budget.
set -euo pipefail

SRC="${1:-src}"
CHAPTER_BUDGET=500
BOOK_BUDGET=4000
status=0

if grep -rn $'\u2014' "$SRC"; then
  echo "error: em dash found. House style uses none." >&2
  status=1
fi

if grep -rniwE 'guns?' "$SRC"; then
  echo "error: write \"electron source\", never \"gun\"." >&2
  status=1
fi

total=0
for f in "$SRC"/*.md; do
  case "$(basename "$f")" in SUMMARY.md|references.md|glossary.md) continue ;; esac
  n=$(wc -w < "$f")
  total=$((total + n))
  flag=""
  [ "$n" -gt "$CHAPTER_BUDGET" ] && flag="  <- over the ${CHAPTER_BUDGET}-word chapter budget"
  printf '%5d  %s%s\n' "$n" "$(basename "$f")" "$flag"
done
printf '%5d  total (soft budget %d)\n' "$total" "$BOOK_BUDGET"

exit "$status"
