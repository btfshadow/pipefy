describe('Form Page', () => {
  it('Submits form', () => {
    const date = new Date()
    const currentDate = date.toLocaleDateString('pt-BR', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
    });
    const currentTime = date.toLocaleDateString('pt-BR', {
      hour: '2-digit',
      minute: '2-digit',
      hour12: 'true'
    });
  
    cy.visit('https://app.pipefy.com/public/form/6qhKljB1')
    cy.get('.FormControlContent-pstyle__ia0p8a-3 > [data-testid="textfield-input"]').type('Sophia Simoes')
    cy.get('[data-testid="pstyle-text-area"]').type('Porque eu estou procurando novos locais e Porque vocês estão contratando')
    cy.get('.sc-lgholE > :nth-child(2) > label').click()
    cy.get('[data-testid="add-assignee-button"]').click()
    cy.get('.pp-input-wrap > [data-testid="textfield-wrapper"] > [data-testid="textfield-input"]').type('felipe')
    cy.get('[data-testid="assignee-select-button-968962"]').click()
    cy.get('.pp-input-wrap > [data-testid="textfield-wrapper"] > [data-testid="textfield-input"]').clear()
    cy.get('[data-testid="assignee-select-button-939930"]').click()
    cy.get('.sc-bZZWma').click()
    cy.get('[data-testid="textfield-wrapper"] > [data-testid="textfield-input"]').click()
    cy.get('.DateInputContainer-pstyle__yrfde2-1 > [data-testid="pstyle-masked-input"]').type(currentDate)
    cy.get('.sc-bZZWma').click()
    cy.get('[data-testid="select-field"]').select('B')
    cy.get('[data-testid="publicForm-Time-what_time_is_it_now"]').type(currentTime)
    cy.get('.sc-bZZWma').click()
    cy.get('.selected-flag').click()
    cy.get('[data-dial-code="34"]').click()
    cy.get('[data-testid="phone-field"]').type('982735240')


    cy.get('button[type="submit"]').click()
  })
})