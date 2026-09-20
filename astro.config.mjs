// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://genuinegeekmedia.com',
  base: '/ready-roofing-georgia',
  vite: {
    plugins: [tailwindcss()]
  }
});