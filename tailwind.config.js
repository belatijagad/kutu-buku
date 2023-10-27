/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html',
    './**/templatetags/**/*.py',
  ],
  theme: {
    extend: {
      colors: {
        // Using modern `rgb`
        background: 'var(--background)',
        bg_secondary: 'var(--background-secondary)',
        foreground: 'var(--foreground)',
        border: 'var(--border)',
      },
      fontFamily: {
        'raleway': ['Raleway', 'sans-serif'],
        'montserrat': ['Montserrat', 'sans-serif']
      }
    },
  },
  plugins: [],
}

