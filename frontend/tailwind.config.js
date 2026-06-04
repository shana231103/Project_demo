/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts}"],
  theme: {
    extend: {
      fontFamily: {
        display: ["'Syne'", "sans-serif"],
        body: ["'DM Sans'", "sans-serif"],
        mono: ["'JetBrains Mono'", "monospace"],
      },
      colors: {
        ink: {
          950: "#08090a",
          900: "#0f1012",
          800: "#1a1c1f",
          700: "#252729",
          600: "#3a3d42",
        },
        acid: {
          DEFAULT: "#c8f53b",
          dim: "#a8d020",
        },
        ember: "#ff4d2b",
        frost: "#a0c8ff",
      },
      keyframes: {
        "slide-up": {
          "0%": { opacity: "0", transform: "translateY(16px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        "fade-in": {
          "0%": { opacity: "0" },
          "100%": { opacity: "1" },
        },
        shimmer: {
          "0%": { backgroundPosition: "-200% 0" },
          "100%": { backgroundPosition: "200% 0" },
        },
        pulse: {
          "0%, 100%": { opacity: "1" },
          "50%": { opacity: "0.4" },
        }
      },
      animation: {
        "slide-up": "slide-up 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards",
        "fade-in": "fade-in 0.3s ease forwards",
        shimmer: "shimmer 1.8s linear infinite",
        pulse: "pulse 1.5s ease-in-out infinite",
      },
    },
  },
  plugins: [],
};
