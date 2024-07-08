module.exports = {
  root: true,
  env: { browser: true, es2020: true, jest: true},
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:react/jsx-runtime',
    'plugin:react-hooks/recommended',
  ],
  ignorePatterns: ['dist', '.eslintrc.cjs'],
  parserOptions: { ecmaVersion: 12, sourceType: 'module', ecmaFeatures: { jsx: true }},
  settings: { react: { version: '18.3' } },
  plugins: ['react', 'jest'],
  rules: {
    'react/react-in-jsx-scope': 'off', // Disable rule requiring React in scope for JSX (for React 17+)
    'no-undef': 'off', // Turn off 'no-undef' for jest globals
  },
}
