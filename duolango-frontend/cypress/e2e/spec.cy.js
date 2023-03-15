describe('game start', () => {
  it('passes', () => {
    cy.visit('http://localhost:8080/')
    cy.get('[href="/game1"]').click()
    cy.get('.button').click()
    cy.get(':nth-child(1) > :nth-child(2) > div > :nth-child(2)').click()
    
    
  })
})
