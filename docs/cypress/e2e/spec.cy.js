describe('game start spanish', () => {
  it('passes', () => {
    cy.visit('http://localhost:8080/')
    cy.clearCookies()
    cy.clearLocalStorage()
    cy.clearAllSessionStorage({log: true})
    cy.get('.login > [type="email"]').click().type('cypress@gmail.com')
    cy.get('.login > [type="password"]').click().type('123!@#')
    cy.get('.login > [type="submit"]').click()
    cy.get('[href="/definer"]').click()
    cy.get('.button').click()
    cy.wait(1000)
    cy.get('#app > :nth-child(2) > div > :nth-child(2)').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(3)').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(4)').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(5)').click()
    cy.get('[href="/tensify"]').click()
    cy.get('.button').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(2)').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(3)').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(4)').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(5)').click()
    cy.get('[href="/puzzler"]').click()
    cy.get('.button').click()
    cy.get('.word-buttons > :nth-child(1)').click()
    cy.get('.word-buttons > :nth-child(2)').click()
    cy.get('[href="/"]').click()
    cy.get('#buttons').click()
    
  })
})

describe('game start swahili', () => {
  it('passes', () => {
    cy.visit('http://localhost:8080/')
    cy.clearCookies()
    cy.clearLocalStorage()
    cy.clearAllSessionStorage({log: true})
    cy.get('.login > [type="email"]').click().type('cypress@gmail.com')
    cy.get('.login > [type="password"]').click().type('123!@#')
    cy.get('.login > [type="submit"]').click()
    cy.get('.language-selector > :nth-child(2)').click()
    cy.get('[href="/definer"]').click()
    cy.get('.button').click()
    cy.wait(1000)
    cy.get('#app > :nth-child(2) > div > :nth-child(2)').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(3)').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(4)').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(5)').click()
    cy.get('[href="/tensify"]').click()
    cy.get('.button').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(2)').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(3)').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(4)').click()
    cy.get('#app > :nth-child(2) > div > :nth-child(5)').click()
    cy.get('[href="/puzzler"]').click()
    cy.get('.button').click()
    cy.get('.word-buttons > :nth-child(1)').click()
    cy.get('.word-buttons > :nth-child(2)').click()
    cy.get('[href="/"]').click()
    cy.get('#buttons').click()
    
  })
})

