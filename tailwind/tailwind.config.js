/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../django/djangosocial/**/*.html"],
  theme: {
    extend: {
      colors: {
        primary: "#0c4b33",
      },
      spacing: {
        initial: "initial",
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
