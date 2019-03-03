# -*- coding: utf-8 -*-

from login import test_login
from login import driver


# def test_menu_header(driver):
#     test_login(driver)
#     link_array = []
#     h1_array = []
#     # основное меню
#     menu = driver.find_elements_by_xpath("//*[@id='app-']/a/span[@class='name']")  # количество пунктов
#     for i in range(len(menu)):
#         # после клика загрузится новая страница и все элементы, найденные ранее, будут считаться "протухшими" (stale),
#         # с ними нельзя больше ничего делать # ищем список по новому и выбираем нужный элемент по индексу
#         menu_el = driver.find_elements_by_xpath("//*[@id='app-']/a/span[@class='name']")
#         link_name = menu_el[i].text  # имя пункта главного меню
#         print(str(i) + "." + link_name)
#         # переходим к пункту основного меню
#         menu_el[i].click()
#
#         # ищем пункты подменю
#         driver.implicitly_wait(5)
#         sub_menu = driver.find_elements_by_xpath("//ul[@class='docs']//li//span")
#         print("Total submenu elements:" + str(len(sub_menu)))
#
#         if len(sub_menu) < 1:
#             head_title = driver.find_element_by_xpath("//td[@id='content']//h1//span").text
#             print("Main Link_text  : " + link_name)
#             print("Head_title : " + head_title)
#             link_array.append(link_name)
#             h1_array.append(head_title)
#         for j in range(len(sub_menu)):
#             sub_menu_el = driver.find_elements_by_xpath("//ul[@class='docs']//li//span")
#             sub_menu_el[j].click()
#             sub_menu_el = driver.find_elements_by_xpath("//ul[@class='docs']//li//span")
#             sub_m_link_name = sub_menu_el[j].text  # имя пункта главного меню
#             head_title2 = driver.find_element_by_xpath("//td[@id='content']//h1//span").text
#             print("Link_text  : " + sub_m_link_name)
#             print("Head_title : " + head_title2)
#             link_array.append(sub_m_link_name)
#             h1_array.append(head_title2)
#
#     print(link_array)
#     print(h1_array)
#     assert len(link_array) == len(h1_array)
# #   assert(link_array == h1_array)
#
#
# def test_sticker(driver):
#     driver.get("http://localhost/litecart/public_html/en/")
#     driver.implicitly_wait(60)
#     sticker_sum = 0
#     #  ищем всех уточек на странице
#     ducks = driver.find_elements_by_xpath(".//ul[@class='listing-wrapper products']//li")
#     print("Total count of ducks:" + str(len(ducks)))
#     #  ищем наклейку на каждой утке:
#     for duck in ducks:
#         sticker = duck.find_elements_by_xpath(".//div[starts-with(@class,'sticker')]")
#         print(len(sticker))
#         sticker_sum = sticker_sum + len(sticker)
#
#     assert len(ducks) == sticker_sum


def test_geo(driver):
    test_login(driver)
    driver.get("http://localhost/litecart/public_html/admin/?app=countries&doc=countries")
    driver.implicitly_wait(60)
    list_city = []
    geo_index = []
    cities = driver.find_elements_by_xpath("//tr[@class='row']//td//a[text()]")
    for city in cities:
        list_city.append(city.text)
        print(city.text)
        print(len(list_city))
    list_city_sort = sorted(list_city)
    print(list_city_sort)
    assert (list_city == list_city_sort)
