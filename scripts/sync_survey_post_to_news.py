# -*- coding: utf-8 -*-
import shutil

src = r"c:\Users\caneu\Downloads\caneup-xyz-restore\content\posts\ganna-survey-data-2026-27-portal-online-check-kaise-kare.md"
dst = r"c:\Users\caneu\Downloads\caneup-xyz-restore\content\news\ganna-survey-data-2026-27-portal-online-check-kaise-kare.md"

with open(src, "r", encoding="utf-8") as f:
    text = f.read()

# Update image path to /images/news/ for the news version
text = text.replace("/images/blog/ganna-survey-data-2026-27-portal-online-check.webp", "/images/news/ganna-survey-data-2026-27-portal-online-check.webp")

with open(dst, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Copied to {dst}")
