from selene.support.shared import browser
from selene import have, be

def test_positive_search(open):
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))

def test_negative_search(open):
    browser.element('[name=q]').should(be.blank).type('dfvsdfbfddv').press_enter()
    browser.element('[id="search"]').should(have.text('По запросу dfvsdfbfddv ничего не найдено.'))

