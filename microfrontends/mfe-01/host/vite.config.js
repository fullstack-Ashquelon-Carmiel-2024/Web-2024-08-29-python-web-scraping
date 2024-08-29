import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

import federation from "@originjs/vite-plugin-federation";
import pkg from "./package.json";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    federation({
      name: "app",
      remotes: {
        remoteA: "http://localhost:5001/remoteA/assets/remoteEntry.js",
        remoteB: "http://localhost:5002/remoteB/assets/remoteEntry.js",
      },
      shared: { ...pkg.dependencies },
    }),
  ],
  build: {
    target: "esnext", // Ensures compatibility with the latest JavaScript features
  },
});