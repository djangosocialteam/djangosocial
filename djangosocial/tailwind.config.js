/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["**/*.html"],
  theme: {
    extend: {
      colors: {
        primary: "#0c4b33",
        green: {
            '50': '#edfcf3',
            '100': '#d4f7e1',
            '200': '#adedc9',
            '300': '#77dea9',
            '400': '#40c786',
            '500': '#1dac6c',
            '600': '#108b57',
            '700': '#0d6f48',
            '800': '#0d583a',
            '900': '#0c4b33',
            '950': '#05291c',
        },
      },
      spacing: {
        initial: "initial",
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
