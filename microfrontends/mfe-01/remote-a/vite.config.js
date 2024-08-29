import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

import federation from "@originjs/vite-plugin-federation";
import pkg from "./package.json";

// https://vitejs.dev/config/
export default defineConfig({
  base: "/remoteA",
  plugins: [
    react(),
    federation({
      name: "remote_a",
      filename: "remoteEntry.js",
      exposes: {
        "./App": "./src/App",
      },
      shared: { ...pkg.dependencies },
    }),
  ],
  build: {
    target: "esnext", // Set the target environment to esnext
  },
})
