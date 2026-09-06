# -*- coding: utf-8 -*-
import os
import sys
from writer_engine import write_article

# POST 2: eGanna App
from post_data.post_02 import data as p2
write_article(**p2)

print("Posts 2 processed!")
