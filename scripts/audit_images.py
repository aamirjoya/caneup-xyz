import os
import glob

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
news_files = sorted(glob.glob(os.path.join(base_dir, 'content', 'news', '*.md')))
post_files = sorted(glob.glob(os.path.join(base_dir, 'content', 'posts', '*.md')))

def check_files(files, section_name):
    missing_frontmatter = []
    missing_file_on_disk = []
    has_image = []
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            txt = fp.read()
        lines = txt.split('---')[1].split('\n') if '---' in txt else []
        feat = None
        for l in lines:
            if l.startswith('featured_image:'):
                feat = l.split(':', 1)[1].strip().strip('"\'')
                break
        if not feat:
            missing_frontmatter.append(f)
        else:
            disk_path = os.path.join(base_dir, 'static', feat.lstrip('/'))
            if not os.path.exists(disk_path):
                missing_file_on_disk.append((f, feat))
            else:
                has_image.append((f, feat))
    print(f"=== {section_name} ===")
    print(f"Total: {len(files)}")
    print(f"Has valid image: {len(has_image)}")
    print(f"Missing frontmatter: {len(missing_frontmatter)}")
    print(f"Missing file on disk: {len(missing_file_on_disk)}")
    if missing_frontmatter:
        print("Sample missing frontmatter:")
        for m in missing_frontmatter[:15]:
            print(" ", os.path.basename(m))
    if missing_file_on_disk:
        print("Sample missing on disk:")
        for m in missing_file_on_disk[:15]:
            print(" ", os.path.basename(m[0]), "->", m[1])

check_files(news_files, 'NEWS')
check_files(post_files, 'POSTS')
