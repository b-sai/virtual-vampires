describe('game start', () => {
  it('passes', () => {
    cy.visit('http://localhost:8080/')
    cy.get('[href="/game1"]').click()
    
  })
})
