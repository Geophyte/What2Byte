from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow, QDialog, QListWidgetItem
import sys

from ui_main import Ui_Main
from ui_scan import Ui_ScanWindow
from ui_add_prod import Ui_Dialog
from ui_recipe_available import Ui_RecipeAvailableWindow
from ui_recipe_all import Ui_RecipeAllWindow
from ui_storage import Ui_StorageWindow
from ui_ingredients import Ui_DoneDialog
import categoriesss
from categories_file import categories_dict
from make_product_base import bool_scan, get_product, add_to_storage, get_recipes, get_doable_recipes, get_storage, sub_storage, subtract_from_storage
from send_mail import send_list
from load_save import load, file_path
import shopping_list


class MainGui(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.main_button.clicked.connect(self._change)
        self.ui.scan_button_2.clicked.connect(self._scan)
        self.ui.available_receips_button.clicked.connect(self._recipe_ava)
        self.ui.storage_button.clicked.connect(self._storage)
        self.ui.all_recipes_button.clicked.connect(self._recipe_all)

    def _change(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def _scan(self):
        scan_window = ScanWindow(self)
        scan_window.show()

    def _recipe_ava(self):
        recipe_window = RecipeAvailableWindow(self)
        recipe_window.show()

    def _storage(self):
        storage_window = StorageWindow(self)
        storage_window.show()

    def _recipe_all(self):
        recipe_window = RecipeAllWindow(self)
        recipe_window.show()


class ScanWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ScanWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.corfirm_button1.clicked.connect(self._corfirm1)
        self.ui.sub_button.clicked.connect(self._sub)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.corfirm_button2.clicked.connect(self._corfirm2)
        self.ui.category_0.itemClicked.connect(self._cat_1)
        self.ui.sub_button_2.clicked.connect(self._sub2)
        self.product = None
        self.code = None
        self.amount = None

    def _corfirm1(self):
        "Skanowanie"
        code = self.ui.code.text()
        "Ustawienie pustego tekstu"
        self.ui.code.setText("")
        self.code = code
        "Rozdział czy kod w bazie czy nie"
        if not bool_scan(self.code):
            "Jeśli nie w bazie to przełącza na wybór kategorii i ilości"
            self._lack_code()
        else:
            "Zwraca kategorię i ilość"
            product_list = get_product(code)
            category = product_list[0]
            amount = product_list[1]
            "Wyświetlenie okna dialogowego"
            self._add_product(category, amount)

    def _sub(self):
        "Ustawienie pustego tekstu"
        self.ui.code.setText("")
        self._lack_code()

    def _lack_code(self):
        "Wybór pierwszej kategorii"
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        categor = categoriesss.product_categories(categories_dict)
        for category in categor:
            item = QListWidgetItem(category)
            item.item = category
            item.categories = categoriesss.product_subcategories(categories_dict, category)
            self.ui.category_0.addItem(item)

    def _cat_1(self, item):
        "Wybór subkategorii"
        self.ui.stackedWidget_2.setCurrentIndex(1)
        for subcategory1 in item.categories:
            subcategory = QListWidgetItem(subcategory1)
            subcategory.cat = categoriesss.product_names(categories_dict, item.item, subcategory1)
            self.ui.category_1.addItem(subcategory)
        self.ui.category_1.itemClicked.connect(self._cat_2)

    def _cat_2(self, subcategory):
        "Wybór produktu"
        self.ui.category_2.clear()
        self.ui.stackedWidget_2.setCurrentIndex(2)
        for product1 in subcategory.cat:
            product = QListWidgetItem(product1)
            product.prod = product1
            self.ui.category_2.addItem(product)
        self.ui.category_2.itemClicked.connect(self._cat_3)

    def _cat_3(self, product):
        self.product = product.prod

    def _corfirm2(self):
        "Zatwierdzenie produktu i ilości"
        self.ui.category_0.clear()
        self.ui.category_1.clear()
        self.ui.category_2.clear()
        amount = self.ui.amount.text()
        product = self.product
        code = self.code
        "Dodanie do bazy kodów"
        "Wyświetlenie okna dialogowego"
        self._add_product(product, amount)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.product = None

    def _add_product(self, category, amount):
        add_dialog = AddDialog(self)
        "Dodanie produktu do spiżarni"
        add_to_storage(category, int(amount))
        "Wyświetlenie dodanego produktu"
        text = category+": "+amount
        add_dialog.setText(text)
        if add_dialog.exec_():
            pass

    def _sub2(self):
        "Zatwierdzenie produktu i ilości"
        self.ui.category_0.clear()
        self.ui.category_1.clear()
        self.ui.category_2.clear()
        amount = self.ui.amount.text()
        product = self.product
        "Wyświetlenie okna dialogowego"
        self._sub_product(product, amount)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.product = None

    def _sub_product(self, category, amount):
        add_dialog = AddDialog(self)
        "Usuwania produktu ze spiżarni"
        subtract_from_storage(category, int(amount))
        "Wyświetlenie dodanego produktu"
        text = category+": "+amount
        add_dialog.setText(text)
        add_dialog.setTitle("USUNIĘTO:")
        if add_dialog.exec_():
            pass


class RecipeAvailableWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RecipeAvailableWindow()
        self.ui.setupUi(self)
        self._set_recipe_list()
        self.ui.recipe_list.itemClicked.connect(self._recipe_str)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.done_button.clicked.connect(self._done)

    def _set_recipe_list(self):
        "Uzupełnienie listy przepisów"
        "Dostępne przepisy"
        recipes = get_doable_recipes()
        for recipe in recipes:
            item = QListWidgetItem(recipe.name())
            item.recipe = recipe
            self.ui.recipe_list.addItem(item)

    def _recipe_str(self, item):
        "Wyświetlenie tekstu o przepisie"
        text = item.recipe
        self.ui.recipe_text.setText(str(text))
        self.recipe = item.recipe

    def _done(self):
        "Usunięcie ze spiżarni produktów"
        recipe = self.recipe
        sub_storage(recipe)
        done_dialog = DoneDialog(self)
        text = recipe.ingredients_str()
        done_dialog.setText(text)
        if done_dialog.exec_():
            pass


class StorageWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_StorageWindow()
        self.ui.setupUi(self)
        self.ui.close_button.clicked.connect(self.close)
        self._set_text()

    def _set_text(self):
        storage = get_storage()
        for product, amount in list(storage.items()):
            descrip = f"{product}: {amount}"
            item = QListWidgetItem(descrip)
            self.ui.storage.addItem(item)


class RecipeAllWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RecipeAllWindow()
        self.ui.setupUi(self)
        self._set_recipe_list()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.recipe_list.itemClicked.connect(self._recipe_str)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.email_button.clicked.connect(self._email)
        self.ui.send_button.clicked.connect(self._send)

    def _set_recipe_list(self):
        "Wyświetlenie listy przepisów"
        recipes = get_recipes()
        for recipe in recipes:
            item = QListWidgetItem(recipe.name())
            item.recipe = recipe
            self.ui.recipe_list.addItem(item)

    def _recipe_str(self, item):
        "kliknięcie przepisu"
        text = item.recipe
        self.ui.recipe_text.setText(str(text))
        self.recipe = item.recipe

    def _email(self):
        "Kliknięcie email"
        self.ui.stackedWidget.setCurrentIndex(1)

    def _send(self):
        "Zatwierdzenie email"
        "Pobranie mail"
        mail = self.ui.mail_adress.text()
        "Wysłanie mail"
        shopping_list.clear()
        storage = load(file_path.storage)
        missing = self.recipe.check(storage)
        shopping_list.add_items(missing)
        send_list(mail)
        self.close()


class AddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ok_button.clicked.connect(self.close)

    def setText(self, code):
        "Wyświetlenie dodanego produktu"
        self.ui.product.setText(code)

    def setTitle(self, text):
        self.ui.label.setText(text)


class DoneDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DoneDialog()
        self.ui.setupUi(self)
        self.ui.close_Button.clicked.connect(self.close)

    def setText(self, text):
        "Wyświetlenie brakujących składników"
        self.ui.ingredients.setText(text)


def guiMain(args):
    app = QApplication(args)
    window = MainGui()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
