const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    baseUrl: 'https://example.cypress.io',  
    specPattern: '**/*.cy.js',  
    supportFile: false,                     
    setupNodeEvents(on, config) {
    },
    retries: {
      runMode: 2,
      openMode: 0,
    },
    viewportWidth: 1280,
    viewportHeight: 720,
  }
})
