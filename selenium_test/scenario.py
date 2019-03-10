# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from login import test_login
from login import driver
from time import sleep
from contextlib import contextmanager
import string, random


#  Task 7
def test_menu_header(driver):
    test_login(driver)
    link_array = []
    h1_array = []
    # основное меню
    menu = driver.find_elements_by_xpath("//*[@id='app-']/a/span[@class='name']")  # количество пунктов
    for i in range(len(menu)):
        # после клика загрузится новая страница и все элементы, найденные ранее, будут считаться "протухшими" (stale),
        # с ними нельзя больше ничего делать # ищем список по новому и выбираем нужный элемент по индексу
        menu_el = driver.find_elements_by_xpath("//*[@id='app-']/a/span[@class='name']")
        link_name = menu_el[i].text  # имя пункта главного меню
        print(str(i) + "." + link_name)
        # переходим к пункту основного меню
        menu_el[i].click()

        # ищем пункты подменю
        driver.implicitly_wait(5)
        sub_menu = driver.find_elements_by_xpath("//ul[@class='docs']//li//span")
        print("Total submenu elements:" + str(len(sub_menu)))

        if len(sub_menu) < 1:
            head_title = driver.find_element_by_xpath("//td[@id='content']//h1//span").text
            print("Main Link_text  : " + link_name)
            print("Head_title : " + head_title)
            link_array.append(link_name)
            h1_array.append(head_title)
        for j in range(len(sub_menu)):
            sub_menu_el = driver.find_elements_by_xpath("//ul[@class='docs']//li//span")
            sub_menu_el[j].click()
            sub_menu_el = driver.find_elements_by_xpath("//ul[@class='docs']//li//span")
            sub_m_link_name = sub_menu_el[j].text  # имя пункта главного меню
            head_title2 = driver.find_element_by_xpath("//td[@id='content']//h1//span").text
            print("Link_text  : " + sub_m_link_name)
            print("Head_title : " + head_title2)
            link_array.append(sub_m_link_name)
            h1_array.append(head_title2)

    print(link_array)
    print(h1_array)
    assert len(link_array) == len(h1_array)


#   assert(link_array == h1_array)

#  Task 8
def test_sticker(driver):
    driver.get("http://localhost/litecart/public_html/en/")
    driver.implicitly_wait(60)
    sticker_sum = 0
    #  ищем всех уточек на странице
    ducks = driver.find_elements_by_xpath(".//ul[@class='listing-wrapper products']//li")
    print("Total count of ducks:" + str(len(ducks)))
    #  ищем наклейку на каждой утке:
    for duck in ducks:
        sticker = duck.find_elements_by_xpath(".//div[starts-with(@class,'sticker')]")
        print(len(sticker))
        sticker_sum = sticker_sum + len(sticker)

    assert len(ducks) == sticker_sum


#  Task 9
def test_geo_zones_local(driver):
    geo_zones(driver, "http://localhost/litecart/public_html/admin/?app=countries&doc=edit_country&country_code=US", 1)
    geo_zones(driver, "http://localhost/litecart/public_html/admin/?app=countries&doc=edit_country&country_code=CA", 1)


def geo_zones(driver, zones_page, flag):
    if flag == 1:
        test_login(driver)
        driver.implicitly_wait(60)

    driver.get(zones_page)
    #  получим все зоны
    rows = driver.find_elements_by_xpath(".//*[@id='table-zones']//tr [not(contains (@class, 'header'))]")
    zones_name = []
    for elements in rows:
        # теперь пробежим по столбцам текущего tr из цикла
        column_z = elements.find_elements_by_tag_name("td")
        zones_name.append(column_z[2].text)
    # удалим последний элемент. list.pop([i]), потому что это поле используется для фильтров
    # Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
    zones_name.pop()
    # print
    print(zones_name)
    sorted_zones_list = sorted(zones_name)
    # print(sorted_zones_list)
    assert zones_name == sorted_zones_list


def test_countries(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/public_html/admin/?app=countries&doc=countries")
    country_list = []
    zones_count = []
    country_acronym = []
    index_for_link = []
    rows = driver.find_elements_by_xpath(".//table[@class='dataTable']//tr[@class='row']")
    # rows = wd.find_elements_by_xpath(".//table[@class='dataTable']//tr[@class='row' and position() <= 39]")
    i = 0
    for elements in rows:
        # теперь пробежим по столбцам текущего tr из цикла
        column = elements.find_elements_by_tag_name("td")
        country_list.append(column[4].text)
        zones_count.append(column[5].text)
        country_acronym.append(column[3].text)
        if int(column[5].text) > 0:
            index_for_link.append(i)
        i = i + 1
    # сравним список стран и отсортированный список
    sorted_country_list = sorted(country_list)
    assert country_list == sorted_country_list
    # print() print (country_list) print (zones_count) print (country_acronym) print print (index_for_link)
    for i in index_for_link:
        # print (country_acronym[i]) print(country_list[i]) print(zones_count[i])
        zone_page = ("http://localhost/litecart/public_html/admin/?app=countries&doc=edit_country&country_code=" + str(
            country_acronym[i]))
        geo_zones(driver, zone_page, flag=0)

    #  зайти в каждую из стран и проверить, что зоны расположены в алфавитном порядке
def test_geo_zones_page(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/public_html/admin/?app=geo_zones&doc=geo_zones")
    #  зайти в каждую из стран
    geozones_list_text = []
    #  множество из ссылок на страницы с зонами
    geo_links = driver.find_elements_by_xpath(
        ".//*[@id='content']/form/table/tbody/tr[@class='row']/td [not(contains (@style,'text'))]/a")
    for link in geo_links:
        print(link.get_attribute('href'))
        geozones_list_text.append(link.get_attribute('href'))

    #  далее бежим уже по спискам в открытых страничках
    for i in range(len(geozones_list_text)):
        geozones_list = []
        driver.get(geozones_list_text[i])
        geo_zones_in_selects = driver.find_elements_by_xpath(
            ".//*[@id='table-zones']/tbody/tr/td/select[starts-with(@name,'zones[') and not(contains (@aria-hidden,"
            "'true'))]/option[@selected='selected']")
        for geozones in geo_zones_in_selects:
            geozones_list.append(geozones.text)

        sorted_geozones_list = sorted(geozones_list)
        print(geozones_list)
        assert (geozones_list == sorted_geozones_list)


#  Task 10
def test_item_of_product_verify(driver):
    driver.get("http://localhost/litecart/public_html/en/")
    driver.implicitly_wait(60)
    duck_crowd = driver.find_elements_by_xpath("//div[@id='box-campaigns']//ul[@class='listing-wrapper products']//li")
    #  нужно сохранить аттрибуты товара для последующей проверки

    num_of_product = []
    link_for_product_page = []
    product_name = []
    product_price = []
    product_price_with_discount = []

    product_price_style_text_decoration = []
    product_price_style_font_size = []
    product_price_with_discount_style_font_weight = []
    product_price_with_discount_style_font_size = []

    i = 0
    for duck in duck_crowd:
        num_of_product.append(i)
        link_for_product_page.append(duck.find_element_by_xpath(".//a[@class='link']").get_attribute('href'))
        product_name.append(duck.find_element_by_xpath(".//div[@class='name']").text)
        product_price.append(duck.find_element_by_xpath(".//div[@class='price-wrapper']/s").text)
        #  проверка на то что скидки может не быть.
        product_price_with_discount.append(duck.find_element_by_xpath(".//strong[@class='campaign-price']").text)
        #  работа со стилями
        product_price_style_text_decoration.append(
            duck.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('text-decoration'))
        product_price_style_font_size.append(
            duck.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('font-size'))
        product_price_with_discount_style_font_weight.append(
            duck.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-weight'))
        product_price_with_discount_style_font_size.append(
            duck.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-size'))

        print('ELEMENT' + str(i))
        print(product_name)
        print(product_price)
        print(product_price_with_discount)
        print(product_price_style_text_decoration)
        print(product_price_style_font_size)
        print(product_price_with_discount_style_font_weight)
        print(product_price_with_discount_style_font_size)
        i = i + 1

    print(link_for_product_page)
    #  перейдем по ссылке для сравнения каждого товара
    for j in range(len(num_of_product)):
        driver.get(link_for_product_page[j])
        # проведем сравнение
        n_product_name = driver.find_element_by_xpath(".//*[@id='box-product']/div[1]/h1").text
        n_product_price = driver.find_element_by_xpath(".//*[@id='box-product']//div[@class='information']//div["
                                                       "@class='price-wrapper']/s").text
        #  проверка на то что скидки может не быть.
        n_product_price_with_discount = driver.find_element_by_xpath(".//*[@id='box-product']//div["
                                                                     "@class='information']//div["
                                                                     "@class='price-wrapper']/strong").text
        #  работа со стилями
        n_product_price_style_text_decoration = driver.find_element_by_xpath(".//*[@id='box-product']//div["
                                                                             "@class='information']//div["
                                                                             "@class='price-wrapper']/s").value_of_css_property(
            'text-decoration')
        n_product_price_style_font_size = driver.find_element_by_xpath(".//*[@id='box-product']//div["
                                                                       "@class='information']//div["
                                                                       "@class='price-wrapper']/s").value_of_css_property(
            'font-size')
        n_product_price_with_discount_style_font_weight = driver.find_element_by_xpath(".//*[@id='box-product']//div["
                                                                                       "@class='information']//div["
                                                                                       "@class='price-wrapper']/strong").value_of_css_property(
            'font-weight')
        n_product_price_with_discount_style_font_size = driver.find_element_by_xpath(".//*[@id='box-product']//div["
                                                                                     "@class='information']//div["
                                                                                     "@class='price-wrapper']/strong["
                                                                                     "@class='campaign-price']").value_of_css_property(
            'font-size')

    print('ELEMENT FROM PRODUCT_PAGE')
    print(n_product_name)

    print(n_product_price)
    print(n_product_price_with_discount)

    print(n_product_price_style_text_decoration)
    print(n_product_price_style_font_size)
    print(n_product_price_with_discount_style_font_weight)
    print(n_product_price_with_discount_style_font_size)

    assert n_product_name == product_name[j]

    assert n_product_price == product_price[j]
    assert n_product_price_with_discount == product_price_with_discount[j]

    assert n_product_price_style_text_decoration == product_price_style_text_decoration[j]
    assert n_product_price_style_font_size == product_price_style_font_size[j]
    assert n_product_price_with_discount_style_font_weight == product_price_with_discount_style_font_weight[j]
    assert n_product_price_with_discount_style_font_size == product_price_with_discount_style_font_size[j]


#  Task 11
def find_and_fill_element(driver, element_name, value):
    driver.find_element_by_name(element_name).click()
    driver.find_element_by_name(element_name).clear()
    driver.find_element_by_name(element_name).send_keys(value)


domains = ["hotmail.com", "yopmail.com", "aol.com", "mailinator.com", "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]


def get_random_domain(domains): return random.choice(domains)


def get_random_name(letters, length): return ''.join(random.choice(letters) for i in range(length))


def generate_random_emails(nb, length): return [get_random_name(letters, length) + '@' + get_random_domain(domains) for
                                                i in range(nb)]


def generate_mail(): return generate_random_emails(1, 7)


def test_new_subscriber_registration(driver):
    # рандомный mail
    mail = generate_mail()
    driver.get("http://localhost/litecart/public_html/en/")
    driver.implicitly_wait(60)
    driver.find_element_by_link_text("New customers click here").click()

    find_and_fill_element(driver, 'tax_id', "1")
    find_and_fill_element(driver, 'company', "2")
    find_and_fill_element(driver, 'firstname', "3")
    find_and_fill_element(driver, 'lastname', "4")
    find_and_fill_element(driver, 'address1', "5")
    find_and_fill_element(driver, 'address2', "6")
    find_and_fill_element(driver, 'postcode', "123456")
    find_and_fill_element(driver, 'city', "8")
    find_and_fill_element(driver, 'email', mail[0])
    find_and_fill_element(driver, 'phone', "92112345678")
    find_and_fill_element(driver, 'password', "1234")
    find_and_fill_element(driver, 'confirmed_password', "1234")

    ###
    driver.find_element_by_name("create_account").click()

    ###
    driver.find_element_by_link_text("Logout").click()

    find_and_fill_element(driver, 'password', "1234")
    find_and_fill_element(driver, 'email', mail[0])
    driver.find_element_by_name("login").click()
    driver.find_element_by_link_text("Logout").click()


#  Task 12
def test_new_product_add(driver):
    test_login(driver)
    name_of_new_prod = get_random_name(letters, 10)

    driver.find_element_by_link_text("Catalog").click()
    driver.find_element_by_link_text("Add New Product").click()

    driver.find_element_by_css_selector("label").click()
    if not driver.find_element_by_name("status").is_selected():
        driver.find_element_by_name("status").click()

    find_and_fill_element(driver, element_name='name[en]', value=name_of_new_prod)
    find_and_fill_element(driver, element_name='code', value='7')
    find_and_fill_element(driver, element_name='quantity', value='11')
    driver.find_element_by_name('new_images[]').send_keys('/home/taipan/selenium/selenium_test/img/duck_image.png')
    driver.find_element_by_name('date_valid_from').click()
    driver.find_element_by_name('date_valid_from').send_keys('2017-12-12')
    driver.find_element_by_name('date_valid_to').click()
    driver.find_element_by_name('date_valid_to').send_keys('2019-12-12')

    driver.find_element_by_link_text("Information").click()
    if not driver.find_element_by_xpath(
            "//div[@id='tab-information']//select[normalize-space(.)='-- Select -- ACME Corp.']//option[2]").is_selected():
        driver.find_element_by_xpath(
            "//div[@id='tab-information']//select[normalize-space(.)='-- Select -- ACME Corp.']//option[2]").click()

    find_and_fill_element(driver, element_name='keywords', value='my_duck')
    find_and_fill_element(driver, element_name='short_description[en]', value='my_duck')

    driver.find_element_by_link_text("Prices").click()
    driver.find_element_by_name("purchase_price").send_keys("22")
    if not driver.find_element_by_xpath("//div[@id='tab-prices']/table[1]/tbody/tr/td/select//option[2]").is_selected():
        driver.find_element_by_xpath("//div[@id='tab-prices']/table[1]/tbody/tr/td/select//option[2]").click()

    find_and_fill_element(driver, element_name='prices[USD]', value='23')

    driver.find_element_by_name("save").click()
    driver.find_element_by_id("content").click()

    # проверим что товар появился на странице просто сравнив его имя
    driver.find_element_by_link_text("Catalog").click()
    test = "//a[text()='" + str(name_of_new_prod) + "']"
    assert_element = driver.find_elements_by_xpath(test)
    print(len(assert_element))
    assert len(assert_element) == 1


#  Task 13
def test_add_prod_to_cart(driver):
    driver.get("http://localhost/litecart/public_html/en/")
    driver.implicitly_wait(60)
    for i in range(1, 4):
        #  выберем товар рандомно и добавим его в таблицу
        duck_crowd = driver.find_elements_by_xpath(".//ul[@class='listing-wrapper products']//li")
        print("Total count of ducks:" + str(len(duck_crowd)))
        random_index = random.randint(0, len(duck_crowd) - 1)
        print("Index of random item:" + str(random_index))
        go = duck_crowd[random_index].find_element_by_xpath("./a[@class='link']").click()
        driver.find_element_by_name('add_cart_product').click()
        sleep(10)
        wait = WebDriverWait(driver, 10)
        # driver.find_element_by_xpath("//*[@id='box-product']//form//td[@class='options']/strong").is_selected()
        # driver.find_element_by_xpath("//*[@id='box-product']//select/option[2]").click()
        # driver.find_element_by_name('add_cart_product').click()
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, ".//*[ @ id = 'cart']//a//span[@class='quantity']"), str(i)))
        # ждем что поменяется свойство текста у элемента потом щелкаем по главной странице
        driver.get("http://localhost/litecart/public_html/en/")
    # открыть корзину
    driver.get("http://localhost/litecart/public_html/en/checkout")
    sleep(10)
    order = driver.find_elements_by_xpath(
        ".//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class='unit-cost']")
    print("Total_order_distinct_prod:" + str(len(order)))
    for i in range(len(order)):
        driver.find_element_by_name('remove_cart_item').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.staleness_of(order[i]))


# Task 14
@contextmanager
def wait_for_new_window(driver, timeout=10):
    handles_before = driver.window_handles
    yield
    WebDriverWait(driver, timeout).until(
        lambda driver: len(handles_before) != len(driver.window_handles))


def test_ext_links(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/public_html/admin/?app=countries&doc=countries")
    driver.find_element_by_xpath(".//*[@id='content']/div/a").click()
    all_ex_link = driver.find_elements_by_xpath(".//*[@id='content']/form/table//a[@target='_blank']")
    print("Total ext_link: " + str(len(all_ex_link)))
    # получаем набор текущих открытых окон
    main_window = driver.current_window_handle
    print('main_window')
    print(main_window)
    old_windows = driver.window_handles
    print('old_windows')
    print(old_windows)
    # нажимаем на ссылку, которая открывает документ в новом окне
    for j in range(2):
        for i in range(len(all_ex_link)):
            print("i=" + str(i))
            with wait_for_new_window(driver, 10):
                all_ex_link[i].click()
            # получаем новый набор включающий уже новое окно
            new_windows = driver.window_handles
            print('new_windows')
            print(new_windows)
            # получаем новые окна (из одного списка вычтем другой)
            new_window = list(set(new_windows).difference(old_windows))
            print('new_window')
            print(new_window)
            # закрываем новое окно
            driver.switch_to_window(new_window[0])
            driver.close()
            driver.switch_to_window(main_window)
