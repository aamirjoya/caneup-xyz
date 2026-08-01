#!/usr/bin/env node
/**
 * Generate Google Discover optimized featured images for CaneUp.xyz
 * Uses Node.js canvas for proper Hindi/Devanagari text rendering
 * Fetches real photos from Pexels API
 */

import { createCanvas, registerFont, loadImage } from 'canvas';
import fs from 'fs';
import path from 'path';
import https from 'https';
import http from 'http';

// ============================================================
// CONFIG
// ============================================================
const CONTENT_DIR = 'content/posts';
const OUTPUT_DIR = 'static/images/blog';
const WIDTH = 1200;
const HEIGHT = 630;

// Pexels API key
const PEXELS_API_KEY = process.env.PEXELS_API_KEY || '';  // Set via env var or GitHub Secrets

// Register Hindi fonts
const FONT_DIR = path.join(path.dirname(new URL(import.meta.url).pathname), 'fonts');
registerFont(path.join(FONT_DIR, 'NotoSansDevanagari-Bold.ttf'), { family: 'NotoDevanagari', weight: 'bold' });
registerFont(path.join(FONT_DIR, 'NotoSansDevanagari-Regular.ttf'), { family: 'NotoDevanagari', weight: 'normal' });

// ============================================================
// CATEGORY CONFIGS
// ============================================================
const CATEGORY_CONFIG = {
  'parchi calendar': {
    searchQueries: ['sugarcane harvest', 'indian sugarcane farmer field', 'sugarcane plantation india'],
    accent: '#F59E0B',
    emoji: '📋',
    label: 'पर्ची कैलेंडर',
    gradientTop: 'rgba(21,128,61,0.3)',
    gradientBottom: 'rgba(0,0,0,0.7)',
  },
  'msp rate': {
    searchQueries: ['sugarcane price market', 'indian farmer money rupee', 'sugarcane market'],
    accent: '#F59E0B',
    emoji: '💰',
    label: 'MSP रेट',
    gradientTop: 'rgba(245,158,11,0.25)',
    gradientBottom: 'rgba(0,0,0,0.7)',
  },
  'ganna kheti': {
    searchQueries: ['sugarcane farming', 'green sugarcane field', 'sugarcane plantation'],
    accent: '#F59E0B',
    emoji: '🌾',
    label: 'गन्ना खेती',
    gradientTop: 'rgba(21,128,61,0.25)',
    gradientBottom: 'rgba(0,0,0,0.65)',
  },
  'sarkari yojana': {
    searchQueries: ['indian government farmer', 'pm kisan scheme', 'farmer subsidy india'],
    accent: '#7C3AED',
    emoji: '🏛️',
    label: 'सरकारी योजना',
    gradientTop: 'rgba(124,58,237,0.25)',
    gradientBottom: 'rgba(0,0,0,0.7)',
  },
  'business': {
    searchQueries: ['sugar mill factory', 'jaggery production india', 'sugarcane business'],
    accent: '#F59E0B',
    emoji: '💼',
    label: 'बिज़नेस',
    gradientTop: 'rgba(234,88,12,0.25)',
    gradientBottom: 'rgba(0,0,0,0.7)',
  },
  'eganna app': {
    searchQueries: ['mobile app farmer india', 'smartphone agriculture', 'digital farming'],
    accent: '#0EA5E9',
    emoji: '📱',
    label: 'eGanna App',
    gradientTop: 'rgba(14,165,233,0.25)',
    gradientBottom: 'rgba(0,0,0,0.7)',
  },
  'sugar mill': {
    searchQueries: ['sugar mill factory', 'sugarcane crushing', 'sugar refinery india'],
    accent: '#F59E0B',
    emoji: '🏭',
    label: 'शुगर मिल',
    gradientTop: 'rgba(71,85,105,0.25)',
    gradientBottom: 'rgba(0,0,0,0.72)',
  },
  'kcc loan': {
    searchQueries: ['kisan credit card', 'farmer bank loan india', 'agriculture loan'],
    accent: '#DC2626',
    emoji: '🏦',
    label: 'KCC लोन',
    gradientTop: 'rgba(220,38,38,0.25)',
    gradientBottom: 'rgba(0,0,0,0.7)',
  },
  'caneup': {
    searchQueries: ['sugarcane farming india', 'green sugarcane field', 'indian farmer'],
    accent: '#F59E0B',
    emoji: '🌾',
    label: 'CaneUp',
    gradientTop: 'rgba(21,128,61,0.25)',
    gradientBottom: 'rgba(0,0,0,0.65)',
  },
  'default': {
    searchQueries: ['sugarcane field india', 'green farming', 'rural india agriculture'],
    accent: '#F59E0B',
    emoji: '🌾',
    label: 'गन्ना जानकारी',
    gradientTop: 'rgba(21,128,61,0.25)',
    gradientBottom: 'rgba(0,0,0,0.65)',
  },
};

// ============================================================
// HTTP HELPERS
// ============================================================
function httpGet(url, headers = {}) {
  return new Promise((resolve, reject) => {
    const mod = url.startsWith('https') ? https : http;
    const req = mod.get(url, { headers, timeout: 15000 }, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        return httpGet(res.headers.location, headers).then(resolve, reject);
      }
      const chunks = [];
      res.on('data', (c) => chunks.push(c));
      res.on('end', () => resolve({ status: res.statusCode, data: Buffer.concat(chunks) }));
    });
    req.on('error', reject);
    req.on('timeout', () => { req.destroy(); reject(new Error('timeout')); });
  });
}

// ============================================================
// IMAGE FETCHING
// ============================================================
async function fetchFromPexels(query) {
  if (!PEXELS_API_KEY) return null;
  try {
    const url = `https://api.pexels.com/v1/search?query=${encodeURIComponent(query)}&per_page=5&orientation=landscape`;
    const res = await httpGet(url, { Authorization: PEXELS_API_KEY });
    if (res.status !== 200 || !res.data) return null;
    const data = JSON.parse(res.data.toString());
    for (const photo of data.photos || []) {
      try {
        const imgUrl = photo.src.large2x;
        const imgRes = await httpGet(imgUrl);

        if (imgRes.status === 200 && imgRes.data && imgRes.data.length > 5000) {
          const tmpPath = path.join(OUTPUT_DIR, '.tmp_fetch.jpg');
          fs.writeFileSync(tmpPath, imgRes.data);
          const img = await loadImage(tmpPath);
          try { fs.unlinkSync(tmpPath); } catch {}
          return img;
        }
      } catch (e2) {
        console.log(`    Image load error: ${e2.message}`);
      }
    }
  } catch (e) {
    console.log(`    Pexels error: ${e.message}`);
  }
  return null;
}

async function fetchFromPicsum(seed) {
  try {
    const url = `https://picsum.photos/seed/${seed}/1200/630`;
    const res = await httpGet(url);
    if (res.status === 200 && res.data && res.data.length > 5000) {
      const tmpPath = path.join(OUTPUT_DIR, '.tmp_picsum.webp');
      fs.writeFileSync(tmpPath, res.data);
      const img = await loadImage(tmpPath);
      fs.unlinkSync(tmpPath);
      return img;
    }
  } catch (e) {
    console.log(`    Picsum error: ${e.message}`);
  }
  return null;
}

async function fetchRealImage(queries, seed) {
  // 1. Try Pexels
  if (PEXELS_API_KEY) {
    for (const q of queries) {
      console.log(`    🔍 Pexels: '${q}'...`);
      const img = await fetchFromPexels(q);
      if (img) { console.log(`    ✅ Got image from Pexels!`); return img; }
      await sleep(300);
    }
  }
  // 2. Try Picsum
  console.log(`    🔍 Picsum (real photo)...`);
  const img = await fetchFromPicsum(seed);
  if (img) { console.log(`    ✅ Got image from Picsum!`); return img; }
  return null;
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

// ============================================================
// IMAGE RENDERING
// ============================================================
function wrapText(ctx, text, maxWidth) {
  const words = text.split(/\s+/);
  const lines = [];
  let current = '';
  for (const word of words) {
    const test = current ? `${current} ${word}` : word;
    if (ctx.measureText(test).width <= maxWidth) {
      current = test;
    } else {
      if (current) lines.push(current);
      current = word;
    }
  }
  if (current) lines.push(current);
  return lines;
}

function drawRoundedRect(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.lineTo(x + w - r, y);
  ctx.quadraticCurveTo(x + w, y, x + w, y + r);
  ctx.lineTo(x + w, y + h - r);
  ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  ctx.lineTo(x + r, y + h);
  ctx.quadraticCurveTo(x, y + h, x, y + h - r);
  ctx.lineTo(x, y + r);
  ctx.quadraticCurveTo(x, y, x + r, y);
  ctx.closePath();
}

async function createFeaturedImage(title, category, slug, outputPath) {
  const catLower = (category || 'default').toLowerCase();
  const config = CATEGORY_CONFIG[catLower] || CATEGORY_CONFIG['default'];

  // 1. Fetch background image
  console.log(`  📸 Fetching image for: ${title.substring(0, 50)}...`);
  let bgImage = await fetchRealImage(config.searchQueries, config.emoji);
  if (!bgImage) {
    console.log(`    ⚠️ No image, using gradient fallback`);
  }

  // 2. Create canvas
  const canvas = createCanvas(WIDTH, HEIGHT);
  const ctx = canvas.getContext('2d');

  // 3. Draw background
  if (bgImage) {
    // Crop to fit 1200x630
    const imgRatio = bgImage.width / bgImage.height;
    const targetRatio = WIDTH / HEIGHT;
    let sx = 0, sy = 0, sw = bgImage.width, sh = bgImage.height;

    if (imgRatio > targetRatio) {
      sw = Math.floor(bgImage.height * targetRatio);
      sx = Math.floor((bgImage.width - sw) / 2);
    } else {
      sh = Math.floor(bgImage.width / targetRatio);
      sy = Math.floor((bgImage.height - sh) / 4);
    }

    ctx.drawImage(bgImage, sx, sy, sw, sh, 0, 0, WIDTH, HEIGHT);

    // Darken
    ctx.fillStyle = 'rgba(0,0,0,0.3)';
    ctx.fillRect(0, 0, WIDTH, HEIGHT);
  } else {
    // Gradient fallback
    const grad = ctx.createLinearGradient(0, 0, 0, HEIGHT);
    grad.addColorStop(0, '#15803D');
    grad.addColorStop(1, '#052E16');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, WIDTH, HEIGHT);
  }

  // 4. Gradient overlay (bottom dark)
  const overlay = ctx.createLinearGradient(0, 0, 0, HEIGHT);
  overlay.addColorStop(0, config.gradientTop);
  overlay.addColorStop(0.7, config.gradientBottom);
  overlay.addColorStop(1, 'rgba(0,0,0,0.85)');
  ctx.fillStyle = overlay;
  ctx.fillRect(0, 0, WIDTH, HEIGHT);

  // 5. Left dark panel for text
  const panelGrad = ctx.createLinearGradient(0, 0, 780, 0);
  panelGrad.addColorStop(0, 'rgba(0,0,0,0.7)');
  panelGrad.addColorStop(0.7, 'rgba(0,0,0,0.4)');
  panelGrad.addColorStop(1, 'rgba(0,0,0,0)');
  ctx.fillStyle = panelGrad;
  ctx.fillRect(0, 0, 780, HEIGHT);

  // 6. Category badge
  const badgeFont = 'bold 20px NotoDevanagari';
  ctx.font = badgeFont;
  const badgeText = `  ${config.emoji}  ${config.label}  `;
  const badgeMetrics = ctx.measureText(badgeText);
  const badgeW = badgeMetrics.width + 24;
  const badgeH = 36;
  const badgeX = 50;
  const badgeY = 45;

  drawRoundedRect(ctx, badgeX, badgeY, badgeW, badgeH, 8);
  ctx.fillStyle = config.accent;
  ctx.fill();

  ctx.fillStyle = '#000000';
  ctx.font = badgeFont;
  ctx.fillText(badgeText, badgeX + 12, badgeY + 25);

  // 7. Title text
  const titleFont = 'bold 44px NotoDevanagari';
  ctx.font = titleFont;
  const titleMaxW = 700;
  const lines = wrapText(ctx, title, titleMaxW).slice(0, 4);
  const titleY = badgeY + badgeH + 35;
  const lineHeight = 56;

  for (let i = 0; i < lines.length; i++) {
    const y = titleY + i * lineHeight;
    // Shadow
    ctx.fillStyle = 'rgba(0,0,0,0.8)';
    ctx.fillText(lines[i], 52, y + 3);
    // Main text
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText(lines[i], 50, y);
  }

  // 8. Bottom CTA bar
  const barX = 50, barY = HEIGHT - 75, barW = 500, barH = 50;
  drawRoundedRect(ctx, barX, barY, barW, barH, 10);
  ctx.fillStyle = config.accent;
  ctx.fill();

  ctx.fillStyle = '#000000';
  ctx.font = 'bold 19px NotoDevanagari';
  ctx.fillText('📖  CaneUp.xyz — पूरी जानकारी पढ़ें →', barX + 22, barY + 32);

  // 9. Right side accent circle
  const circleX = WIDTH - 160, circleY = HEIGHT / 2 - 50, circleR = 75;
  ctx.beginPath();
  ctx.arc(circleX, circleY, circleR, 0, Math.PI * 2);
  ctx.fillStyle = config.accent + '30';
  ctx.fill();

  // Emoji
  ctx.font = '72px NotoDevanagari';
  ctx.fillStyle = 'rgba(255,255,255,0.8)';
  const emojiW = ctx.measureText(config.emoji).width;
  ctx.fillText(config.emoji, circleX - emojiW / 2, circleY + 25);

  // 10. Watermark
  ctx.font = 'bold 16px NotoDevanagari';
  const wmText = '🌾 CaneUp.xyz';
  const wmW = ctx.measureText(wmText).width;
  ctx.fillStyle = 'rgba(255,255,255,0.6)';
  ctx.fillText(wmText, WIDTH - wmW - 25, HEIGHT - 20);

  // 11. Save as WebP using sharp or PNG fallback
  let buffer;
  try {
    // Try WebP via canvas
    buffer = canvas.toBuffer('image/webp');
  } catch {}
  if (!buffer || buffer.length === 0) {
    // Fallback: save as PNG then convert with sharp if available
    buffer = canvas.toBuffer('image/png');
  }
  fs.writeFileSync(outputPath, buffer);
  const sizeKB = Math.floor(buffer.length / 1024);
  console.log(`    💾 Saved: ${outputPath} (${sizeKB}KB)`);
  return true;
}

// ============================================================
// FRONT MATTER PARSER
// ============================================================
function parseFrontMatter(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  if (!content.startsWith('---')) return { fm: null, content };
  const parts = content.split('---', 2);
  if (parts.length < 2) return { fm: null, content };

  const fm = {};
  const lines = parts[1].trim().split('\n');
  let currentKey = null;
  let currentList = null;

  for (const line of lines) {
    const listMatch = line.match(/^- (.+)$/);
    const kvMatch = line.match(/^(\w[\w\s]*):\s*(.*)$/);

    if (listMatch && currentKey) {
      if (!currentList) currentList = [];
      currentList.push(listMatch[1].trim());
      fm[currentKey] = currentList;
    } else if (kvMatch) {
      currentKey = kvMatch[1].trim();
      const val = kvMatch[2].trim();
      currentList = null;
      if (val.startsWith('[') && val.endsWith(']')) {
        fm[currentKey] = val.slice(1, -1).split(',').map(s => s.trim().replace(/^["']|["']$/g, ''));
      } else {
        fm[currentKey] = val.replace(/^["']|["']$/g, '');
      }
    } else if (line.trim() === '') {
      currentList = null;
    }
  }
  return { fm, content };
}

function updateFrontMatter(filePath, fm, originalContent) {
  const parts = originalContent.split('---', 2);
  if (parts.length < 2) return;

  let fmStr = '';
  for (const [key, val] of Object.entries(fm)) {
    if (Array.isArray(val)) {
      fmStr += `${key}:\n`;
      for (const item of val) fmStr += `- ${item}\n`;
    } else {
      fmStr += `${key}: ${val}\n`;
    }
  }
  fs.writeFileSync(filePath, `---\n${fmStr}---${parts[1]}`);
}

// ============================================================
// MAIN
// ============================================================
async function main() {
  const args = process.argv.slice(2);
  const force = args.includes('--force');
  let limit = null;
  for (const arg of args) {
    const m = arg.match(/^--limit=(\d+)$/);
    if (m) limit = parseInt(m[1]);
  }

  if (!fs.existsSync(CONTENT_DIR)) {
    console.log(`ERROR: ${CONTENT_DIR} not found!`);
    return;
  }

  fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  let mdFiles = fs.readdirSync(CONTENT_DIR)
    .filter(f => f.endsWith('.md'))
    .sort();
  if (limit) mdFiles = mdFiles.slice(0, limit);

  console.log(`Found ${mdFiles.length} posts to process`);
  console.log(`Force mode: ${force}`);
  console.log(`Pexels API: ${PEXELS_API_KEY ? '✅ Set' : '❌ Not set'}`);
  console.log(`${'='.repeat(60)}\n`);

  let success = 0, skipped = 0, errors = 0;

  for (let i = 0; i < mdFiles.length; i++) {
    const mdFile = mdFiles[i];
    const filePath = path.join(CONTENT_DIR, mdFile);
    const { fm, content } = parseFrontMatter(filePath);

    if (!fm) {
      console.log(`[${i + 1}/${mdFiles.length}] SKIP (no front matter): ${mdFile}`);
      skipped++;
      continue;
    }

    const title = fm.title || mdFile.replace(/\.md$/, '').replace(/-/g, ' ');
    const categories = fm.categories || ['default'];
    const category = Array.isArray(categories) ? categories[0] : categories;
    const slug = mdFile.replace(/\.md$/, '');

    const outputFilename = `${slug}.webp`;
    const outputPath = path.join(OUTPUT_DIR, outputFilename);
    const webPath = `/images/blog/${outputFilename}`;

    if (!force && fs.existsSync(outputPath) && fm.featured_image === webPath) {
      console.log(`[${i + 1}/${mdFiles.length}] SKIP (exists): ${mdFile}`);
      skipped++;
      continue;
    }

    console.log(`[${i + 1}/${mdFiles.length}] Processing: ${mdFile}`);

    try {
      await createFeaturedImage(title, category, slug, outputPath);

      fm.featured_image = webPath;
      fm.image = webPath;
      updateFrontMatter(filePath, fm, content);
      console.log(`  ✅ Done!\n`);
      success++;

      if (i < mdFiles.length - 1) await sleep(1000);
    } catch (e) {
      console.log(`  ❌ Error: ${e.message}\n`);
      errors++;
    }
  }

  console.log(`\n${'='.repeat(60)}`);
  console.log(`✅ Generated: ${success}`);
  console.log(`⏭️  Skipped:   ${skipped}`);
  console.log(`❌ Errors:    ${errors}`);
  console.log(`📁 Output:    ${OUTPUT_DIR}/`);
}

main().catch(console.error);
