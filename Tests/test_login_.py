import re
import playwright
from playwright.sync_api import Page, expect
from config import Config
from utils import guardar_screenshot

#login exitoso user y password correctos
def test_login_exitoso(playwright: playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.URL)
    page.get_by_role("textbox", name="Email address").fill(Config.usuario_correcto)
    page.get_by_role("textbox", name="Password").fill(Config.pass_correcto)
    page.get_by_role("button", name="Continue", exact=True).click()
    expect(page.get_by_role("heading", name="Bienvenido!")).to_be_visible()
    guardar_screenshot(page,test_name= 'login_exitoso')

#login fallido user correcto y password incorrecto
def test_login_fallido_user_correcto_pass_incorrecto(playwright: playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.URL)
    page.get_by_role("textbox", name="Email address").fill(Config.usuario_correcto)
    page.get_by_role("textbox", name="Password").fill(Config.pass_incorrecto)
    page.get_by_role("button", name="Continue", exact=True).click()
    expect(page.get_by_text(re.compile("Credenciales incorrectas"))).to_be_visible()
    guardar_screenshot(page,test_name= 'login_fallido_user_correcto_pass_incorrecto')

#login fallido user incorrecto y password correcto
def test_login_fallido_user_incorrecto_pass_correcto(playwright: playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.URL)
    page.get_by_role("textbox", name="Email address").fill(Config.usuario_incorrecto)
    page.get_by_role("textbox", name="Password").fill(Config.pass_correcto)
    page.get_by_role("button", name="Continue", exact=True).click()
    expect(page.get_by_text(re.compile("Credenciales incorrectas"))).to_be_visible()
    guardar_screenshot(page,test_name= 'login_fallido_user_incorrecto_pass_correcto')

#login fallido user y password incorrectos
def test_login_fallido_user_incorrecto_pass_incorrecto(playwright: playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.URL)
    page.get_by_role("textbox", name="Email address").fill(Config.usuario_incorrecto)
    page.get_by_role("textbox", name="Password").fill(Config.pass_incorrecto)
    page.get_by_role("button", name="Continue", exact=True).click()
    expect(page.get_by_text(re.compile("Credenciales incorrectas"))).to_be_visible()
    guardar_screenshot(page,test_name= 'login_fallido_user_incorrecto_pass_incorrecto')

#login fallido con user y password vacios
def test_login_fallido_sin_user_ni_pass(playwright: playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.URL)
    page.get_by_role("button", name="Continue", exact=True).click()
    expect(page.get_by_text(re.compile("Por favor, ingrese su correo electrónico y contraseña"))).to_be_visible()
    guardar_screenshot(page,test_name= 'login_fallido_sin_user_ni_pass')
    
#login fallido sin user
def test_login_fallido_sin_user(playwright: playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.URL)
    page.get_by_role("textbox", name="Password").fill(Config.pass_correcto)
    page.get_by_role("button", name="Continue", exact=True).click()
    expect(page.get_by_text(re.compile("Por favor, ingrese su correo electrónico y contraseña"))).to_be_visible()
    guardar_screenshot(page,test_name= 'login_fallido_sin_user')

#login fallido sin password
def test_login_fallido_sin_pass(playwright: playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.URL)
    page.get_by_role("textbox", name="Email address").fill(Config.usuario_correcto)
    page.get_by_role("button", name="Continue", exact=True).click()
    expect(page.get_by_text(re.compile("Por favor, ingrese su correo electrónico y contraseña"))).to_be_visible()
    guardar_screenshot(page,test_name= 'login_fallido_sin_pass')


#login user con formato incorrecto
def test_login_fallido_user_formato_incorrecto(playwright: playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.URL)
    page.get_by_role("textbox", name="Email address").fill(Config.user_formato_incorrecto)
    page.get_by_role("textbox", name="Password").fill(Config.pass_correcto)
    page.get_by_role("button", name="Continue", exact=True).click()
    expect(page.get_by_text(re.compile("Por favor, ingrese un correo electrónico válido"))).to_be_visible()
    guardar_screenshot(page,test_name= 'login_fallido_user_formato_incorrecto')

#ver password
def test_ver_password(playwright: playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.URL)
    page.get_by_role("textbox", name="Email address").fill(Config.usuario_correcto)
    page.get_by_role("textbox", name="Password").fill(Config.pass_correcto)
    page.get_by_role("button", name="Show password Hide password").click()
    tipo_input = page.get_by_role("textbox", name="Password").get_attribute("type")
    assert tipo_input == "text", "La contraseña sigue oculta (type='password')"
    expect(page.get_by_role("textbox", name="Password")).to_have_value(Config.pass_correcto)
    guardar_screenshot(page,test_name= 'ver_password')