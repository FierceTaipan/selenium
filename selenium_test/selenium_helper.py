# Selenium
# 1.Selenium - Инструмент для автоматизированного управления браузерами. Selenium – это драйвер для браузера
# 2.Почему Selenium называется "драйвер браузера"? - Потому что он управляет браузером, "drive" значит "управлять"
# 3.Какой способ интеграции в браузер использует Selenium? - Selenium WebDriver инструмент, который внедряется "спереди"
# 4.Серьёзным недостатком, характерным для схемы внедрения "спереди", используемой в инструменте Selenium. -
# недостаточно универсален, для каждого браузера нужно разрабатывать отдельный драйвер.
# 5.Какую роль выполняют вспомогательные исполняемые файлы, которые Selenium использует для взаимодействия с браузерами?
# - они преобразуют команды из формата, который понимает Selenium, в формат, который понимают браузеры.
# 6.Какой основной цели стремились достичь разработчики Selenium, создавая стандарт W3C WebDriver? -
# убедить разработчиков браузеров самостоятельно делать драйверы в соответствии с этим стандартом.
# 7.Что описывает стандарт W3C WebDriver?
# - Сетевой протокол взаимодействия между клиентскими библиотеками Selenium и драйвером.

# *********************************************************************************************************************
# Ссылки
# Официальный сайт Selenium: http://www.seleniumhq.org/
# Русскоязычный сайт про Selenium: http://selenium2.ru/
# Рабочая версия текста стандарта: https://w3c.github.io/webdriver/webdriver-spec.html
# Исходный код стандарта и баг-трекер: https://github.com/w3c/webdriver
# Официальный блог: https://seleniumhq.wordpress.com/, никакой технической информации, только новости
# Форум (на русском): http://software-testing.ru/forum/index.php?/forum/129-selenium-functional-testing/
# Группа в Facebook (на русском): https://www.facebook.com/groups/selenium.ru/
# IRC-чат (на английском): http://webchat.freenode.net/?channels=%23selenium
# Клиентская библиотека Selenium в репозитории PyPI: https://pypi.python.org/pypi/selenium
# Selenium Python API documentation: http://seleniumhq.github.io/selenium/docs/api/py/index.html
# Неофициальная (но весьма хорошая документация): http://selenium-python.readthedocs.io/
# Список Capabilities https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities
# Опции командной строки Chrome: http://peter.sh/experiments/chromium-command-line-switches/
# Опции командной строки Firefox: https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options
# Опции командной строки Internet Explorer: https://msdn.microsoft.com/ru-ru/library/hh826025(v=vs.85).aspx
# Статья про активацию микрофона http://www.testautomationguru.com/selenium-webdriver-google-voice-search-automation-using-arquillian-graphene/
# Capabilities & ChromeOptions: https://sites.google.com/a/chromium.org/chromedriver/capabilities
# Capabilities IE: https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities#ie-specific
# Драйвер для PhantomJS: https://github.com/detro/ghostdriver
# Драйвер для WebKit: https://github.com/MachinePublishers/jBrowserDriver/
# Headless automation for Internet Explorer: http://triflejs.org/
# Список headless-браузеров: https://github.com/dhamaniasad/HeadlessBrowsers
# Список headless-браузеров: https://gist.github.com/evandrix/3694955
# Спецификация CSS Selectors Level 2 - https://www.w3.org/TR/CSS21/
# Спецификация CSS Selectors Level 3 - https://www.w3.org/TR/css3-selectors/
# Информация, в каких версиях браузеров можно использовать CSS Selectors Level 3 -- http://caniuse.com/#feat=css-sel3
# Спецификация XPath 1.0 - https://www.w3.org/TR/xpath/
# Про свойства и атрибуты - http://javascript.ru/tutorial/dom/attributes
# Правила определения видимости: https://w3c.github.io/webdriver/webdriver-spec.html#element-displayedness
# Правила получения текста - https://w3c.github.io/webdriver/webdriver-spec.html#get-element-text
# Про свойства и атрибуты - http://javascript.ru/tutorial/dom/attributes
# Advanced Interactions API - http://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html#selenium.webdriver.common.action_chains.ActionChains
# Пример работы с "календариком" - http://barancev.github.io/how-to-set-datepicker-value/
# "Повышаем надёжность Selenium-тестов через JavaScript" - http://selenium2.ru/articles/163-selenium-javascript.html
# Как прицепить файл к невидимому полю ввода -- http://barancev.github.io/how-to-attach-file-to-invisible-field/
# Другие условия ожидания - http://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
# Что означает "окончание загрузки страницы"? -- http://barancev.github.io/page-loading-complete/
# Как Selenium ожидает окончания загрузки страницы? -- http://barancev.github.io/how-selenium-waits-for-page-to-load/
# Что делать, если страница загружается слишком долго? -- http://barancev.github.io/slow-loading-pages/
# Как прицепить файл к невидимому полю ввода -- http://barancev.github.io/how-to-attach-file-to-invisible-field/
# Загрузка файлов с сервера - http://ardesco.lazerycode.com/testing/webdriver/2012/07/25/how-to-download-files-with-selenium-and-why-you-shouldnt.html
# Более старая документация, более подробная, но может содержать неактуальную информацию: https://github.com/SeleniumHQ/selenium/wiki/Grid2
# Более новая документация, пока не очень подробная, но зато должна быть актуальная: https://seleniumhq.github.io/docs/grid.html#selenium_grid
# Selenium Grid Extras - https://github.com/groupon/Selenium-Grid-Extras
# Selenium в контейнере - https://github.com/SeleniumHQ/docker-selenium
# Краткое, но достаточно полное описание сути этого шаблона проектирования http://martinfowler.com/bliki/PageObject.html
# Page Objects на практике - https://github.com/barancev/selenium-training-po

# Шпаргалки по XPath:
# http://scraping.pro/5-best-xpath-cheat-sheets-and-quick-references/
# https://www.simple-talk.com/dotnet/net-framework/xpath-css-dom-and-selenium-the-rosetta-stone/ (постер)

# Шпаргалки по CSS:
# http://www.w3schools.com/cssref/css_selectors.asp
# https://www.smashingmagazine.com/2009/07/css-3-cheat-sheet-pdf/ (постер, последняя страница)


# *********************************************************************************************************************
# Интерфейсы взаимодействия с браузерами
# Chrome Remote Debugging: https://developer.chrome.com/devtools/docs/debugger-protocol
# Firefox (Gecko) Marionette: https://developer.mozilla.org/ru/docs/Marionette
# Internet Explorer COM API: https://msdn.microsoft.com/en-us/library/aa752127(v=vs.85).aspx

# Вспомогательные исполняемые файлы
# chromedriver: https://sites.google.com/a/chromium.org/chromedriver/downloads
# geckodriver: https://github.com/mozilla/geckodriver
# IEDriverServer (для браузеров IE 7-11): http://www.seleniumhq.org/download/
# MicrosoftWebDriver (для браузера Edge): https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# safaridriver будет доступен в Safari 10: https://webkit.org/blog/6900/webdriver-support-in-safari-10/

# *********************************************************************************************************************
# Принцип работы

# Основные задачи
# • Внедрение JavaScript
# • Управление внедрённым JavaScript
# • Преодоление ограничений безопасности
# • Действия, недоступные через JavaScript

# Схема 1: всё внутри (Selenium внутри браузера - Server)
# Схема 2: внедрение «сзади» (Browser - Proxy - Server)
# Схема 3: внедрение «спереди» (Selenium - Browser - Server)

# Унификация
# Selenium - chromedriver - Remote Debug (Chrome)
# Selenium - geckodriver - Marionette (Firefox)
# Selenium - IEDriverServer - COM API (IE)

# Драйверы «от производителей»
# • operaprestodriver (до версии 12, deprecated)
# • chromedriver
# • operachromiumdriver
# • MicrosoftWebDriver (edgedriver)
# • geckodriver (aka marionette)
# • Apple Safari WebDriver support

# *********************************************************************************************************************
# Стандарт W3C WebDriver

# Стандарт описывает
# • Набор команд
# • Алгоритмы
# • Сетевой протокол
# • Механизм расширения протокола

# *********************************************************************************************************************

# Базовые команды Selenium

# Классификация команд
# • Инициализация драйвера
# • Настройка драйвера
# • Действия со страницами
# • Действия с окнами
# • Действия с диалогами
# • Поиск элементов
# • Свойства элементов
# • Действия с элементами
# • Действия с фреймами
# • Выполнение JS-кода

# Почему не найден?
# • Невалидный локатор
# • Нет такого элемента
# • Сейчас нет такого элемента
# • Элемент в другом окне или фрейме

# Когда кликнуть нельзя?
# • Элемент исчез из DOM
# • Элемент «неинтерактивный»
# • Элемент невидимый (упрощённый вариант)
# • Элемент закрыт другим элементом

# Когда нельзя «печатать»?
# • Элемент исчез из DOM
# • Элемент «неинтерактивный»
# • Элемент невидимый (упрощённый вариант)

# Куда кликает Selenium?
# • В центр элемента
# • В центр первого прямоугольника
# • В центр первого видимого прямоугольника
# • В видимую точку любого прямоугольника

# Клавиатура ввод текста и не только
# • Enter/Return/Tab
# • Стрелки и прочая навигация
# • модификаторы (Alt, Shift, Ctrl, Command)
# • Ctrl-A/Ctrl-C/Ctrl-V (быстрая вставка)

# Как «печатает» Selenium?
# • Сначала надо поставить фокус
# • Курсор в конец поля ввода
# • Посимвольный ввод
# • keyDown, keyUp, keyPress

# Два подхода к действиям
# • do what I mean - «обычные» click и sendKeys
# • do what I say - Advanced Interaction API

# *********************************************************************************************************************
# Запуск в разных браузерах
# Помещайте исполняемые файлы-посредники в PATH, настраивайте правильно окружение.
from selenium import webdriver

chrome_driver = webdriver.Chrome()
ie_driver = webdriver.Ie()
firefox_driver = webdriver.Firefox()

# Capabilities
wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
print(wd.capabilities)

# Chrome
options = webdriver.ChromeOptions()
options.binary_location = "PATH/chrome"
options.add_argument("start-maximized")

wd1 = webdriver.Chrome(chrome_options=options)

# IE
wd2 = webdriver.Ie(capabilities={"requireWindowFocus": True})

# Firefox
wd3 = webdriver.Firefox(firefox_binary="PATH/firefox")

# *********************************************************************************************************************
# Работа с cookies
driver = webdriver.Chrome()
driver.get("https://yandex.ru/")
driver.add_cookie({'name': 'test', 'test': 'bar'})
test_cookie = driver.get_cookie('test')
cookies = driver.get_cookies()
driver.delete_cookie('test')
driver.delete_all_cookies()

# Зачем менять cookies?
# • Предварительный вход (добавление cookies)
# • Альтернативный выход (удаление cookies)
# • Очистка сессии (удаление всех cookies) – лучше перезапустить браузер (кроме IE)
# • Удаляются только cookies для текущей страницы!!!

# *********************************************************************************************************************
# Поиск элементов

# Команда поиска
# driver.findElement(By.name("password"))
# driver.FindElement(By.name("password"))
# driver.find_element_by_name("password")
# @driver.find_element(:name, 'password')
# driver.findElement(By.name("password"))

# Стратегии поиска
# • By.id
# • By.tagName
# • By.className
# • By.cssSelector
# • By.name
# • By.linkText
# • By.partialLinkText
# • By.xpath

# Локаторы

# Устойчивость к изменениям вёрстки
# • Максимально точные критерии выбора
# • Как можно меньше порядковых номеров
# • Привязка к ближайшему уникальному элементу
# • Минимум прыжков по DOM

form1 = driver.find_element_by_id("login-form")
form2 = driver.find_element_by_tag_name("form")
form3 = driver.find_element_by_class_name("login")
form4 = driver.find_element_by_css_selector("form.login")
form5 = driver.find_element_by_css_selector("#login-form")

field1 = driver.find_element_by_name("username")
field2 = driver.find_element_by_xpath("//input[@name='username']")
link = driver.find_element_by_link_text("Logout")
links = driver.find_elements_by_tag_name("a")

# Локаторы на основе CSS
# driver.findElement(By.cssSelector("ul#menu li.active"))
# driver.FindElement(By.CssSelector("ul#menu li.active"))
# driver.find_element_by_css_selector("ul#menu li.active")
# @driver.find_element(:css, 'ul#menu li.active')
# driver.findElement(By.css("ul#menu li.active"))

# Специальные атрибуты
# • атрибут id
# driver.find_element_by_css_selector("#username")
# driver.find_element_by_id("username")
# • атрибут class
# driver.find_element_by_css_selector(".error")
# driver.find_element_by_class_name("error")

# Обычные атрибуты
# • атрибут name
# driver.find_element_by_css_selector("[name=password]")
# driver.find_element_by_name("password")
# • "[placeholder=search]"
# • "[type=button]"

# Проверка значения атрибута
# • "[checked]" – наличие атрибута
# • "[name = email]" – совпадение значения
# • "[title *= Name]" – содержит текст
# • "[src^= http]" – начинается с текста
# • "[src$= .pdf]" – заканчивается текстом

# Комбинация условий
# • "label" – по тегу
# • ".error" – по классу
# • "label.error" – по тегу и классу
# • "label.error.fatal" – по тегу и двум классам
# • "label.error[for=email]" – по тегу, классу и атрибуту

# Отрицание условий
# • "label:not(.error)" – сообщения не об ошибках
# • "input:not([type=text])" – нетекстовые поля ввода
# • "a:not([href ^= http])" – локальные ссылки

# Движение по дереву
# • "div#main p" – p где-то внутри блока div#main
# • "div#main > p" – p непосредственновнутри div#main
# • "div#main li:first-child"
# • "div#main li:last-child"
# • "div#main li:nth-child(1)"
# • "div#header> div:nth-of-type(1)"

# Локаторы на основе XPath

# Структура XPath-запроса
# //ul[@id='menu']/li[contains(@class, 'active')]

# Поиск внутри элемента
# Контекст поиска
# 1.• input = driver.find_element_by_name("password")
#   2.• form = driver.find_element_by_id("login-modal")
#     • input = form.find_element_by_name("password")
#     3.• input = driver.find_element_by_css_selector(
#       • "#login-modal [name=password]")

# Несколько элементов
# Пример: чтение таблицы
# table = driver.find_element_by_id("users")
# rows = table.find_elements_by_tag_name("tr")
# for row in rows:
#   name = row.find_element_by_xpath("./td[1]").text
#   email = row.find_element_by_xpath("./td[2]").text

# Поиск нескольких элементов
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False


is_element_present(driver, By.name, "q")

# Если элемент не найден, то…
# • findElement - выбрасывает исключение NoSuchElementException
# • findElements - возвращает пустой список

# *********************************************************************************************************************
# Ожидание появления элемента

# Схема простейшего теста
# Подождем элемент - Взаимодействие с элементом - Подождем результат - Проверим результат

# Если элемент не найден…
# • Не та страница открыта
# • Неправильный локатор
# • Элемент находится внутри фрейма
# • Нужно немного подождать

# Явные и неявные ожидания
# Явные
# • На стороне клиента
# • Ждать можно чего угодно
# • Надо писать явно
# • TimeoutException
# • Много сетевых запросов
# Неявные
# • На стороне браузера
# • Ожидание появления в DOM
# • Работают автоматически
# • NoSuchElementException
# • Один сетевой запрос

# Настройка неявных ожиданий
driver.implicitly_wait(10)
element = driver.find_element_by_name("q")

# Неявное ожидание
# driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
# • findElement ждёт, пока элемент появится
# • findElements ждёт, пока хотя бы один элемент появится

# Явное ожидание появления элемента
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(driver, 10)  # seconds
# обратите внимание, что локатор передается как tuple!
element1 = wait.until(EC.presence_of_element_located((By.NAME, "q")))
element2 = wait.until(lambda d: d.find_element_by_name("q"))

# Явное ожидание
# WebDriverWait wait = new WebDriverWait(driver, 30);
# WebElement element = wait.until(d -> d.findElement(locator));

# Ожидание исчезновения элемента
wait = WebDriverWait(driver, 10)  # seconds
driver.refresh()
wait.until(EC.staleness_of(element))

# Исчезновение элемента
# • Исчезновение это не отсутствие!
# • Раньше был, потом исчез
# • Сначала надо найти, потом ждать исчезновения
# wait.until(ExpectedConditions.stalenessOf(element));

# Ожидание видимости элемента
wait = WebDriverWait(driver, 10)  # seconds
wait.until(EC.visibility_of(element))

# Видимость и невидимость
# • wait.until(visibilityOf(element))
# • wait.until(visibilityOfAllElements(elementList))
# • wait.until(not(visibilityOf(element)))
# • wait.until(invisibilityOfAllElements(elementList))
# • wait.until(visibilityOfElementLocated(locator))

# Ожидание чего-нибудь
# ExpectedConditions
# • wait.until(titleIs("webdriver - Поиск в Google"))
# • wait.until(urlContains("login.php"))
# • wait.until(alertIsPresent())
# • wait.until(numberOfWindowsToBe(2))
# • wait.until(attributeContains(element, "class", "visible"))
# • wait.until(textToBePresentInElement(element, "OK"))
# • wait.until(elementToBeSelected(element))
# • wait.until(elementToBeClickable(element))

# Как победить staleness?
# • Поиск элемента перед использованием
# • Выбор подходящего момента для действия
# • Повторные попытки после исключения
# • А может быть не только staleness?

# Поиск при помощи JavaScript
links_a = driver.execute_script("return $$('a:contains((WebDriver)')")

# *********************************************************************************************************************
# Свойства и атрибуты

# getAttribute
# • value – содержимое полей ввода
# • href, src – нормализация адресов
# • true или null – булевские атрибуты

# Получение свойств элементов
href = link.get_attribute("href")

# Определение видимости элемента
# Selenium врёт про видимость
# • Прозрачные элементы
# • Элементы цвета фона
# • Элементы, скрытые позади других элементов
# • Элементы за левым или верхним краем экрана

button = driver.find_element("")
if button.is_displayed():
    button.click()

# Получение текста элемента
# Текст элемента
# • Видимый текст альтернатива – element.getAttribute("textContent")
# • Нормализованный текст (пробелы)
# • Preformatted
# • Не используйте для элементов форм!

txt = link.text

# Получение стилей элемента
# Стиль элемента
# • getTagName, getAttribute("id"), getAttribute("class")
# • getCssValue()
# • Цвет (color) – нормализация, RGBa
# • Комбинированные стили (font, background)
# • Цвет фона, в частности прозрачность

color = link.value_of_css_property("color")

# Размер и положение элемента
# Размер и положение
# • getSize – размер элемента (в пикселях)
# • getLocation – положение на странице
# • getRect – размер и положение, «два в одном»
# • Секретный интерфейс Locatable (Locatable element).getCoordinates().inView()

location = link.location
size = link.size

# *********************************************************************************************************************
# Действия с элементами
link.click()

# Ввод текста (sendKeys)
from selenium.webdriver.common.keys import Keys

search_field = driver.find_element("")
search_field.send_keys("selenium" + Keys.ENTER)

date_field = driver.find_element("")
# если в поле есть маска -- надо перед вводом текста перейти в начало
date_field.send_keys(Keys.HOME + "01.01.2001")

# Очистка поля ввода (clear)
# Нельзя использовать команду clear для очистки файловых полей ввода!!!
password_field = driver.find_element("")
password_field.clear()

# Advanced Interactions API
from selenium.webdriver.common.action_chains import ActionChains
drag = driver.find_element("")
drop = driver.find_element("")
ActionChains(driver).move_to_element(drag).click_and_hold().move_to_element(drop).release().perform()

# *********************************************************************************************************************
# Окна, фреймы и диалоги

# Alert
alert = driver.switch_to_alert()
alert_text = alert.text
alert.accept()
# либо alert.dismiss()

# Три способа Downloading
# • Настроить браузер на автосохранение
# • Загрузить файл «мимо браузера»
# • Перехватить загрузку при помощи proxy


# Окна
# • запоминаем идентификатор текущего окна
# originalWindow = driver.getWindowHandle()
# • запоминаем идентификаторы уже открытых окон
# existingWindows= driver.getWindowHandles()
# • кликаем кнопку, которая открывает новое окно
# driver.findElement(By.id("button")).click()
# • ждем появления нового окна, с новым идентификатором
# newWindow = wait.until(anyWindowOtherThan(existingWindows))
# • переключаемся в новое окно
# driver.switchTo().window(newWindow)
# • закрываем его
# driver.close()
# • и возвращаемся в исходное окно
# driver.switchTo().window(originalWindow)

# Фреймы
# Операции с фреймами
# • driver.switchTo().frame(element)
# • driver.switchTo().defaultContent()
# • driver.switchTo().parentFrame()
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
driver.switch_to_default_content()

# Размер и положение окна
# Размер и положение
# • driver.manage().window().getPosition()
# • driver.manage().window().setPosition(new Point(x, y))
# • driver.manage().window().getSize()
# • driver.manage().window().setSize(new Dimension(w, h))
# • driver.manage().window().maximize()
# • driver.manage().window().fullscreen()
driver.set_window_size(800, 600)
driver.maximize_window()

# Команды close и quit
# • close - закрывает текущее окно
# • quit - закрывает все окна (останавливает драйвер и удаляет профиль)

# *********************************************************************************************************************
# Удалённый запуск

# Зачем удалённый запуск?
# • Разные операционки, разные версии браузеров – в частности разные версии Internet Explorer
# • Два браузера на разных машинах одновременно – чтобы оба браузера были на переднем плане
# • Много браузеров, не хватает мощности

# Selenium Server
driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities={"browserName": "chrome"})

# Selenium в облаках

# Специализированные сервисы
# https://saucelabs.com/
# https://www.browserstack.com/
# https://testingbot.com/
# https://www.gridlastic.com/

# *********************************************************************************************************************
# Протоколирование действий Selenium
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)
    def after_find(self, by, value, driver):
        print(by, value, "found")
    def on_exception(self, exception, driver):
        print(exception)
wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())

# Снятие скриншотов
driver.get_screenshot_as_file('screen.png')

# Доступ к логам браузера
for l in driver.get_log("browser"):
    print(l)

# Перехват трафика
driver = webdriver.Chrome(desired_capabilities={"proxy": {"proxyType": "MANUAL", "httpProxy": "localhost:8888"}})

# BrowserMobProxy, обёртка для Python: https://github.com/AutomatedTester/browsermob-proxy-py
# mitmproxy: встраиваемый прокси на Python: https://mitmproxy.org/

# *********************************************************************************************************************
# PageObjects

# Альтернативные подходы
# • Page Blocks: крупные куски страниц
# • Сервисы: поведение, а не структура
# • Screenplay: виртуальные пользователи

# Драйверы
# • Настоящие Браузеры
# IE, FF, Chrome, Safari, Opera
# • Псевдобраузеры
# GhostDriver, QtWebDriver, jBrowserDriver
# • Мобильные приложения
# Appium, Selendroid, ios-driver
# • Нативные приложения
# Winium.Desktop, AutoItDriverServer, WinAppDriver
