describe('Hello World Test', () => {
  it('Visits a page and checks title', () => {
    cy.visit('https://example.cypress.io')
    cy.contains('type').click()
    cy.url().should('include', '/commands/actions')
  })
})