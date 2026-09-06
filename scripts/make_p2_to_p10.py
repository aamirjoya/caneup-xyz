# -*- coding: utf-8 -*-
import os

with open("scripts/generate_posts_02_to_10.py", "w", encoding="utf-8") as f:
    f.write('''# -*- coding: utf-8 -*-
import os
import sys
from writer_engine import write_article

# POST 2: eGanna App
from post_data.post_02 import data as p2
write_article(**p2)

print("Posts 2 processed!")
''')

print("make_p2_to_p10.py generated base")
