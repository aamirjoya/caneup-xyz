# -*- coding: utf-8 -*-
import os
import sys

base_dir = r"c:\Users\caneu\Downloads\caneup-xyz-restore"
posts_dir = os.path.join(base_dir, "content", "posts")
os.makedirs(posts_dir, exist_ok=True)

# Master generation function
from writer_engine import write_article

print("Builder ready. Starting article generation...")
