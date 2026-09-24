import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';

const require = createRequire('C:/Users/Mutasim/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp/package.json');
const sharp = require('sharp');

const sourceRoot = 'C:/Users/Mutasim/Desktop/Images';
const destinationRoot = 'D:/Claude/mutasim-portfolio/dist/assets/images';
const files = [
  ['Cover Pic.jpg', 'cover.webp', 2200],
  ['DP.jpg', 'profile.webp', 1400],
  ['Achievements/Innovation Fair-2026.jpg', 'achievements/innovation-fair.webp', 1400],
  ['Achievements/NRC 2025.jpg', 'achievements/nrc-2025.webp', 1800],
  ['Achievements/Robo Fusion-1.0.jpg', 'achievements/robo-fusion.webp', 1400],
  ['Best Clicks/1.jpg', 'best-clicks/01-between-light-and-shadow.webp', 1500],
  ['Best Clicks/2.jpg', 'best-clicks/02-reaching-skyward.webp', 1500],
  ['Best Clicks/3.jpg', 'best-clicks/03-where-light-lingers.webp', 1700],
  ['Best Clicks/4.jpg', 'best-clicks/04-precision-in-flight.webp', 1600],
  ['Best Clicks/5.jpg', 'best-clicks/05-a-place-that-lives.webp', 1700],
  ['Best Clicks/6.jpg', 'best-clicks/06-under-garden-lights.webp', 1500],
  ['Best Clicks/7.jpg', 'best-clicks/07-in-full-bloom.webp', 1500],
  ['Best Clicks/8.jpg', 'best-clicks/08-a-wider-view.webp', 1800],
  ['Projects/DurontoJatra/Aqua Guard.png', 'projects/duronto-aqua-guard.webp', 1800],
  ['Projects/DurontoJatra/Dumb Waiter.png', 'projects/duronto-dumb-waiter.webp', 1500],
  ['Projects/DurontoJatra/Team Members.jpg', 'projects/duronto-team.webp', 1800],
  ['Projects/LFR/Head Hunter.png', 'projects/lfr-head-hunter.webp', 1500],
  ['Projects/LFR/Mark-X.png', 'projects/lfr-mark-x.webp', 1500],
  ['Projects/LFR/Team Pagla Ghora.jpg', 'projects/lfr-team.webp', 1800],
  ['Projects/Personal Projects/CPU Scheduler.png', 'projects/cpu-scheduler.webp', 1800],
  ['Projects/Personal Projects/nRF-Box.jpg', 'projects/nrf-box.webp', 1500],
  ['Projects/Quad Bits/All members of QuadBits in one frame in UIU.jpg', 'projects/quadbits-team-uiu.webp', 1800],
  ['Projects/Quad Bits/Me with Project Agro Bot.jpg', 'projects/quadbits-agrobot.webp', 1600],
  ['Projects/Quad Bits/Team Members.jpg', 'projects/quadbits-team-event.webp', 1500],
  ['Projects/Quad Bits/Working 2.jpg', 'projects/quadbits-working-2.webp', 1600],
];

for (const [source, destination, maximum] of files) {
  const input = path.join(sourceRoot, source);
  const output = path.join(destinationRoot, destination);
  await fs.mkdir(path.dirname(output), { recursive: true });
  await sharp(input).rotate().resize({ width: maximum, height: maximum, fit: 'inside', withoutEnlargement: true }).webp({ quality: 84 }).toFile(output);
}

console.log(`Prepared ${files.length} portfolio images.`);
