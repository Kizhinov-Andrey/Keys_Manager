from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QDialogButtonBox, QLabel, QWidget, QFormLayout, QHBoxLayout, \
    QTreeWidget, QMenuBar, QMenu, QAction, QToolButton, QTextEdit
from PyQt5.QtGui import QFont, QIcon

font = QFont()
font.setFamily("Calibri")
font.setPointSize(12)
font.setKerning(True)


class Ui_CreateGroup(object):
    def setupUi(self, Create_group):
        Create_group.resize(270, 95)
        Create_group.setMinimumSize(270, 95)
        Create_group.setMaximumSize(270, 95)
        Create_group.setWindowTitle("Create group")

        self.gridLayout = QGridLayout(Create_group)

        self.label = QLabel(Create_group)
        self.label.setText("Name: ")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.le_group_name = QLineEdit(Create_group)
        self.gridLayout.addWidget(self.le_group_name, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Create_group)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.buttonBox.accepted.connect(Create_group.accept)
        self.buttonBox.rejected.connect(Create_group.reject)


class Ui_CreateKey(object):
    def setupUi(self, CreateKey):
        CreateKey.resize(550, 168)
        CreateKey.setMinimumSize(550, 168)
        CreateKey.setMaximumSize(550, 168)
        CreateKey.setFont(font)
        CreateKey.setWindowTitle("Create master key")
        CreateKey.setWindowIcon(QIcon("Images/Main_icon.img"))

        self.buttonBox = QDialogButtonBox(CreateKey)
        self.buttonBox.setGeometry(200, 120, 341, 32)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(CreateKey.accept)
        self.buttonBox.rejected.connect(CreateKey.reject)

        self.lbl_dir = QLabel(CreateKey)
        self.lbl_dir.setGeometry(10, 10, 491, 31)
        self.lbl_dir.setFont(font)

        self.formLayoutWidget = QWidget(CreateKey)
        self.formLayoutWidget.setGeometry(10, 50, 531, 61)
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setText("Master password")
        self.label.setFont(font)
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_create_password = QLineEdit(self.formLayoutWidget)
        self.le_create_password.setEchoMode(QLineEdit.Password)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_create_password)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setText("Repeat password")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_repeat_password = QLineEdit(self.formLayoutWidget)
        self.le_repeat_password.setEchoMode(QLineEdit.Password)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_repeat_password)


class Ui_CheckPassword(object):
    def setupUi(self, CheckPasswordDial):
        CheckPasswordDial.resize(390, 125)
        CheckPasswordDial.setMinimumSize(390, 125)
        CheckPasswordDial.setMaximumSize(390, 125)
        CheckPasswordDial.setWindowTitle("Dialog")

        self.buttonBox = QDialogButtonBox(CheckPasswordDial)
        self.buttonBox.setGeometry(9, 88, 371, 27)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.label = QLabel(CheckPasswordDial)
        self.label.setGeometry(9, 9, 371, 23)
        font1 = QFont()
        font1.setFamily("Calibri")
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Enter the password")

        self.le_password = QLineEdit(CheckPasswordDial)
        self.le_password.setGeometry(9, 49, 371, 25)
        self.le_password.setEchoMode(QLineEdit.Password)

        self.buttonBox.accepted.connect(CheckPasswordDial.accept)
        self.buttonBox.rejected.connect(CheckPasswordDial.reject)


class Ui_KeysManager(object):
    def setupUi(self, KeysManager):
        KeysManager.setWindowIcon(QIcon(r"Images\Main_icon.img"))
        KeysManager.setWindowTitle("KeysManager")
        KeysManager.resize(800, 600)
        KeysManager.setFont(font)
        self.centralwidget = QWidget(KeysManager)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)

        self.tree_groups = QTreeWidget(self.centralwidget)
        self.tree_groups.setMaximumSize(200, 16777215)
        self.tree_groups.headerItem().setText(0, "Database")
        self.tree_groups.setEnabled(False)
        self.horizontalLayout.addWidget(self.tree_groups)
        self.tree_groups.setFont(font)

        self.table = QTreeWidget(self.centralwidget)
        header = self.table.headerItem()
        header.setText(4, "Notes")
        header.setText(3, "URL")
        header.setText(2, "Password")
        header.setText(1, "User Name")
        header.setText(0, "Title")
        self.table.setEnabled(False)
        self.horizontalLayout.addWidget(self.table)
        KeysManager.setCentralWidget(self.centralwidget)
        self.table.setFont(font)

        self.menubar = QMenuBar(KeysManager)
        self.menubar.setGeometry(0, 0, 800, 21)
        self.menubar.setFont(font)
        self.menu_file = self.menubar.addMenu("File")
        self.menu_group = self.menubar.addMenu("Group")
        self.menu_entry = self.menubar.addMenu("Entry")
        self.fill_menu_file(KeysManager)
        self.fill_menu_group()
        self.fill_menu_entry()
        self.menubar.addActions(
            [self.menu_file.menuAction(), self.menu_group.menuAction(), self.menu_entry.menuAction()])
        KeysManager.setMenuBar(self.menubar)

    def fill_menu_file(self, KeysManager):
        # Создает выподающее меню
        new_db = QAction("New", self.menu_file)
        new_db.setShortcut("Ctrl+N")
        new_db.setIcon(QIcon(r"Images\New_file.png"))
        open_db = QAction("Open file", self.menu_file)
        open_db.setShortcut("Ctrl+O")
        open_db.setIcon(QIcon(r"Images\Open_file.png"))
        close_db = QAction("Close", self.menu_file)
        close_db.setShortcut("Ctrl+W")
        close_db.setIcon(QIcon(r"Images\Close_file.png"))
        close_db.setEnabled(False)
        open_resent = QMenu("Open resent", KeysManager)
        change_key = QAction("Change master key", self.menu_file)
        change_key.setIcon(QIcon(r"Images\Change_password.png"))
        change_key.setEnabled(False)
        exit_app = QAction("Exit", self.menu_file)
        exit_app.setIcon(QIcon(r"Images\Exit_app.png"))
        exit_app.setShortcut("Ctrl+Q")
        self.file_actions = [new_db, open_db, close_db, open_resent, change_key, exit_app]
        self.menu_file.addActions(self.file_actions[:3])
        self.menu_file.addMenu(self.file_actions[3])
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.file_actions[4])
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.file_actions[5])

    def fill_menu_group(self):
        add_group = QAction("Add group", self.menu_group)
        add_group.setEnabled(False)
        add_group.setIcon(QIcon(r"Images\Add_group.png"))
        delete_group = QAction("Delete group", self.menu_group)
        delete_group.setEnabled(False)
        delete_group.setShortcut("Del")
        delete_group.setIcon(QIcon(r"Images\Delete_group.png"))
        edit_group = QAction("Edit group", self.menu_group)
        edit_group.setEnabled(False)
        self.group_actions = [add_group, delete_group, edit_group]
        self.menu_group.addActions(self.group_actions)

    def fill_menu_entry(self):
        copy_user_name = QAction("Copy user name", self.menu_entry)
        copy_user_name.setIcon(QIcon(r"Images\User_name.png"))
        copy_user_name.setEnabled(False)
        copy_user_name.setShortcut("Ctrl+B")
        copy_password = QAction("Copy password", self.menu_entry)
        copy_password.setIcon(QIcon(r"Images\Password.png"))
        copy_password.setEnabled(False)
        copy_password.setShortcut("Ctrl+C")
        copy_url = QAction("Copy URL", self.menu_entry)
        copy_url.setIcon(QIcon(r"Images\URL.png"))
        copy_url.setEnabled(False)
        copy_url.setShortcut("Ctrl+U")
        add_entry = QAction("Add entry", self.menu_entry)
        add_entry.setIcon(QIcon(r"Images\Add_key.png"))
        add_entry.setEnabled(False)
        add_entry.setShortcut("Ctrl+I")
        edit_entry = QAction("Edit entry", self.menu_entry)
        edit_entry.setIcon(QIcon(r"Images\Change_key.png"))
        edit_entry.setEnabled(False)
        delete_entry = QAction("Delete entry", self.menu_entry)
        delete_entry.setIcon(QIcon(r"Images\Del_key.png"))
        delete_entry.setEnabled(False)
        delete_entry.setShortcut("Del")
        self.entry_actions = [copy_user_name, copy_password, copy_url, add_entry, edit_entry, delete_entry]
        self.menu_entry.addActions(self.entry_actions[:3])
        self.menu_entry.addSeparator()
        self.menu_entry.addActions(self.entry_actions[3:])


class Ui_AddEntry(object):
    def setupUi(self, Dialog):
        Dialog.resize(510, 400)
        Dialog.setMinimumSize(510, 400)
        Dialog.setMaximumSize(510, 400)
        Dialog.setFont(font)
        Dialog.setWindowTitle("Add entry")
        self.gridLayout = QGridLayout(Dialog)

        self.label = QLabel(Dialog)
        self.label.setText("Title:")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_title = QLineEdit(Dialog)
        self.gridLayout.addWidget(self.le_title, 0, 2, 1, 3)

        self.label_2 = QLabel(Dialog)
        self.label_2.setText("User name:")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.le_user_name = QLineEdit(Dialog)
        self.gridLayout.addWidget(self.le_user_name, 1, 2, 1, 3)

        self.label_3 = QLabel(Dialog)
        self.label_3.setText("Password:")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.le_password = QLineEdit(Dialog)
        self.le_password.setEchoMode(QLineEdit.Password)
        self.gridLayout.addWidget(self.le_password, 3, 2, 1, 1)
        self.btn_generate = QToolButton(Dialog)
        self.btn_generate.setText("Generate")
        self.gridLayout.addWidget(self.btn_generate, 3, 4, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setText("Repeat:")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.le_repeat = QLineEdit(Dialog)
        self.le_repeat.setEchoMode(QLineEdit.Password)
        self.gridLayout.addWidget(self.le_repeat, 5, 2, 1, 1)
        self.btn_view = QToolButton(Dialog)
        self.btn_view.setText("...")
        self.gridLayout.addWidget(self.btn_view, 5, 4, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setText("URL:")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.le_url = QLineEdit(Dialog)
        self.gridLayout.addWidget(self.le_url, 6, 2, 1, 3)

        self.label_6 = QLabel(Dialog)
        self.label_6.setText("Notes:")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.textEdit = QTextEdit(Dialog)
        self.gridLayout.addWidget(self.textEdit, 7, 2, 1, 3)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.gridLayout.addWidget(self.buttonBox, 10, 2, 1, 1)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
