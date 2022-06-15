from selene import be, have
from conftest import *


def test_search_selene():
    browser.element('[name="q"]').should(be.blank).type('selene github').press_enter()
    browser.element('[id="links"]').should(have.text('User-oriented Web UI browser tests in Python'))



def test_search_no_info():
    browser.element('[name="q"]').should(be.blank).type('de465fr7').press_enter()
    browser.element('[id="links"]').should(have.text('По запросу de465fr7 результаты не найдено.'))
