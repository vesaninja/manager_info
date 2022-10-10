import requests
import datetime


def get_reaktori_menu():
    """ Prints Reaktori's menu"""
    language = "fi"
    url = "https://www.foodandco.fi/modules/json/json/Index?costNumber=0812&language={}".format(language)
    response = requests.get(url)
    data = response.json()["MenusForDays"]
    date = datetime.datetime.now().strftime("%y-%m-%d")
    formated_menu = ""
    for day in data:
        if date in day["Date"]:
            if not day["LunchTime"]:
                formated_menu += "It looks like the restaurant is closed today. "
                break
            for menu in day["SetMenus"]:
                try:
                    name = menu["Name"].split('(')[0]
                except AttributeError:
                    name = menu["Name"]
                formated_menu += "\n<b>{}</b>\n".format(name)
                for component in menu["Components"]:
                    component = component.split('(')[0]
                    formated_menu += "\t\t{}\n".format(component)
    return formated_menu


def get_hertsi_menu():
    """ Prints Hertsi's menu"""
    url = "https://www.sodexo.fi/en/ruokalistat/output/weekly_json/111"
    response = requests.get(url)
    data = response.json()["mealdates"]
    current_weekday = datetime.datetime.today().strftime('%A')
    formated_menu = ""
    for day in data:
        if current_weekday == day["date"]:
            for menu_num in day["courses"]:
                menu = day["courses"][menu_num]
                formated_menu += "\n<b>{}</b>\n".format(menu["title_fi"])
    if not formated_menu:
        formated_menu += "It looks like the restaurant is closed today. "
    return formated_menu


def get_newton_menu():
    """ Prints Newton's menu"""
    formated_menu = ""
    date = datetime.datetime.now().strftime("%Y%m%d")
    url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/6/?lang=fi&date={}&date2={}".format(date, date)
    response = requests.get(url)
    try:
        data = response.json()[0]["menuTypes"]
    except IndexError:
        data = {}
    for menu_name in data:
        if menu_name["menuTypeName"] in ["Lounas", "Kasvis", "Konehuone"]:
            meal_list = menu_name["menus"][0]["days"][0]["mealoptions"]
            for meal in meal_list:
                formated_menu += "\n<b>{}</b>\n".format(meal["name"])
                for recipe in meal["menuItems"]:
                    formated_menu += "\t\t{}\n".format(recipe["name"])
    if not formated_menu:
        formated_menu += "It looks like the restaurant is closed today. "
    return formated_menu
