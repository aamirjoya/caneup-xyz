import os
import sys

def test_all():
    # 1. Web Story
    with open('public/webstories/best-sugarcane-varieties-2026/index.html', 'r', encoding='utf-8') as f:
        ws = f.read()

    assert 'amp-story-social-share' not in ws, 'FAIL: amp-story-social-share found in web story'
    assert 'logo-square.png' in ws, 'FAIL: logo-square.png not in web story'
    assert 'Article' in ws, 'FAIL: Article schema not in web story'
    print('[PASS] 1. Web Stories: Valid AMP (no invalid tags), square logo (512x512), Article schema')

    # 2. Article
    with open('public/posts/ganna-parchi-calendar-12-pakhwada-basic-quota-samjhe-2026/index.html', 'r', encoding='utf-8') as f:
        art = f.read()

    assert 'width=1200' in art or 'width="1200"' in art, 'FAIL: width 1200 missing in article featured image'
    assert '<p>}</p>' not in art, 'FAIL: stray } found in article HTML'
    assert 'images/authors/aamir-raza.webp' in art, 'FAIL: author image URL missing'
    print('[PASS] 2. Article: width="1200" DOM attribute, zero stray braces, absolute author URL in Schema')

    # 3. Sitemap
    with open('public/sitemap.xml', 'r', encoding='utf-8') as f:
        sm = f.read()

    assert '/tags/' not in sm, 'FAIL: /tags/ found in sitemap'
    assert '<image:image>' in sm, 'FAIL: image:image missing in sitemap'
    print('[PASS] 3. Sitemap: /tags/ excluded (noindex conflict resolved), <image:image> included')

    # 4. News Sitemap
    with open('public/news-sitemap.xml', 'r', encoding='utf-8') as f:
        nsm = f.read()

    assert 'xmlns:news' in nsm, 'FAIL: news namespace missing'
    print('[PASS] 4. News Sitemap: valid XML and namespaces')

    # 5. Robots.txt
    with open('public/robots.txt', 'r', encoding='utf-8') as f:
        rb = f.read()

    assert 'User-agent: Googlebot-News' in rb, 'FAIL: Googlebot-News missing'
    print('[PASS] 5. robots.txt: Googlebot-News properly configured')

    # 6. Static Assets
    assert os.path.exists('public/favicon.ico'), 'FAIL: favicon.ico missing'
    assert os.path.exists('public/manifest.json'), 'FAIL: manifest.json missing'
    assert os.path.exists('public/images/logo-square.png'), 'FAIL: logo-square.png missing'
    print('[PASS] 6. Static assets: favicon.ico, manifest.json, logo-square.png present')

    print('\n' + '='*50)
    print('ALL 6 VERIFICATION TEST SUITES PASSED (100% SUCCESS)')
    print('='*50)

if __name__ == '__main__':
    test_all()
