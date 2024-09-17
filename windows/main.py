# -*- coding: utf-8 -*-
import json
import os
from PyQt5 import sip
import subprocess
import pygame
import winreg as reg
from  plyer import notification
import sys
from PyQt5.QtCore import Qt
import webbrowser
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,QLabel,QMainWindow, QAction, QCheckBox, QSystemTrayIcon, QMenu
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
import json


def save_settings(data, filename='settings.json'):
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_settings(filename='settings.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}



class AboutAppWindow_info(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("درباره نرم افزار")
        self.setFixedSize(300, 200)  

     
        layout = QVBoxLayout(self)

        label = QLabel("تحریم گذر مدوفایل", self)
        label2 = QLabel(" لینوکس - نسخه بتا جهت تست", self)
        label3 = QLabel("توسعه داده شده توسط تیم برنامه‌نویسی مدوفایل", self)
        label4 = QLabel("برنامه نویس: مهرداد حسن زاده",self)
     
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        self.setLayout(layout) 

        self.setLayout(layout)
class AboutAppWindow(QWidget):
    def __init__(self, title, content):
        super().__init__()
        
        self.setWindowTitle(title)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText("ساخته شده توسط برند مدوفایل \n توسعه دهنده : مهرداد حسن زاده")
        logo_label = QLabel(self)
        pixmap = QPixmap('./image/logo.png')  
        scaled_pixmap = pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)  
        logo_label.setPixmap(scaled_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)
        layout.addWidget(label)
        layout.addWidget(logo_label)

   
        github_link = QLabel('<a href="https://github.com/mtgama">GitHub</a>', self)
        github_link.setOpenExternalLinks(True)
        github_link.setAlignment(Qt.AlignCenter)
        layout.addWidget(github_link)

      
        linkedin_link = QLabel('<a href="https://www.linkedin.com/in/mehrdad-hassanzade-64a094234">LinkedIn</a>', self)
        linkedin_link.setOpenExternalLinks(True)
        linkedin_link.setAlignment(Qt.AlignCenter)
        layout.addWidget(linkedin_link)

       
        instagram_link = QLabel('<a href="https://www.instagram.com/1mehrdad0?igsh=aWd3aHFjbzl3bWxk">Instagram</a>', self)
        instagram_link.setOpenExternalLinks(True)
        instagram_link.setAlignment(Qt.AlignCenter)
        layout.addWidget(instagram_link)

       
        website_link = QLabel('<a href="https://www.medofile.ir">Website</a>', self)
        website_link.setOpenExternalLinks(True)
        website_link.setAlignment(Qt.AlignCenter)
        layout.addWidget(website_link)
        self.setLayout(layout)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 631)
        MainWindow.setFixedSize(1052, 631)
        MainWindow.setStyleSheet(f"""
            QMainWindow {{
                background-image: url('./image/background.jpg');  /* تصویر پس‌زمینه */
                background-repeat: no-repeat;
                background-position: center;
            }}
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 40, 211, 131))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.setIconSize(QSize(210, 210))
        self.is_on = False
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 0, 120, 31))
        self.label.setObjectName("label")
        self.checkbox = QCheckBox(self.centralwidget)
        self.checkbox.setText("StartUp")
        self.checkbox.setGeometry(QtCore.QRect(490, 450, 91, 31))
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.checkbox.stateChanged.connect(self.toggle_startup)
        self.comboBox.setGeometry(QtCore.QRect(460, 410, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        
        self.label_2.setGeometry(QtCore.QRect(420, 360, 188, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 520, 180, 23))
        self.label_3.setText("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 23))
        self.menubar.setObjectName("menubar")
        self.menuMore = QtWidgets.QMenu(self.menubar)
        self.menuMore.setObjectName("menuMore")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMore.menuAction())
        self.comboBox.addItems(['شکن', '403', 'بگذر','هاست ایران',"رادار گیم","شاتل","الکترو"])
        self.action_exit = QAction("خروج", MainWindow)
        self.action_about = QAction("درباره سازنده", MainWindow)
        self.action_version = QAction("نسخه نرم افزار", MainWindow)

        self.menuMore.addAction(self.action_exit)
        self.menuMore.addAction(self.action_about)
        self.menuMore.addAction(self.action_version)
        self.action_exit.triggered.connect(self.exit_application)
        self.action_about.triggered.connect(lambda: self.show_info("درباره سازنده", ["سازنده: فلانی", "توسعه‌دهنده: تیم X", "سال: 2024"]))
        self.action_version.triggered.connect(self.show_info_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
     
        self.set_button_icon()

        self.pushButton.clicked.connect(self.toggle_button)

        settings = load_settings()
        if settings.get('startup', False):
            self.checkbox.setChecked(True)
        app_icon = QtGui.QIcon('./image/app_icon.ico')  
        MainWindow.setWindowIcon(app_icon)

        
        self.tray_icon = QSystemTrayIcon(QtGui.QIcon('./image/app_icon.png'), parent=MainWindow)
        self.tray_icon.setToolTip("DNS Manager")
        
        
        self.tray_menu = QMenu()
        self.restore_action = QAction("Restore")
        self.quit_action = QAction("Exit")
        
        self.tray_menu.addAction(self.restore_action)
        self.tray_menu.addAction(self.quit_action)
        
        self.tray_icon.setContextMenu(self.tray_menu)
        
        
        self.restore_action.triggered.connect(self.restore_window)
        self.quit_action.triggered.connect(self.exit_application)

        self.tray_icon.show()
        
        self.tray_icon.activated.connect(self.on_tray_icon_clicked)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Medo_tahrim"))
     
        self.label.setText(_translate("MainWindow", "گذر از تحریم مدوفایل"))
        self.label_2.setText(_translate("MainWindow", "لطفا یک تحریم گذر را انتخاب کنید"))
        self.menuMore.setTitle(_translate("MainWindow", "More"))


    def toggle_startup(self, state):
        try:
            settings = load_settings() 
            if state == Qt.Checked:  
                self.add_to_startup()
                settings['startup'] = True 
            else:
                self.remove_from_startup()
                settings['startup'] = False  
            save_settings(settings)  
        except Exception as e:
            pass 

    def add_to_startup(self, file_path=None):
        if file_path is None:
            file_path = os.path.abspath(__file__)
        
        # آدرس رجیستری برای استارتاپ
        key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        value_name = "medo_tahrim"  # نام کلیدی که به رجیستری اضافه می‌شود
        
        # باز کردن کلید رجیستری
        reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(reg_key, value_name, 0, reg.REG_SZ, file_path)
        reg.CloseKey(reg_key)
    def set_button_icon(self):
        if self.is_on:
            self.pushButton.setStyleSheet("""
                QPushButton {
                    border: none;
                    background-image: url(./image/on.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }
            """)
        else:
            self.pushButton.setStyleSheet("""
                QPushButton {
                    border: none;
                    background-image: url(./image/off.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }
            """)
        self.pushButton.setFixedSize(300, 133)

    def toggle_button(self):
        self.is_on = not self.is_on
        self.set_button_icon()
        
        if self.is_on:
            select_item = self.comboBox.currentText()  # اصلاح
            self.set_dns(select_item)
            self.comboBox.setEnabled(False)
            self.label_3.setText("با موفقیت روشن شد")
        else:
            self.clear_dns()
            self.comboBox.setEnabled(True)

   
    def remove_from_startup(self):
        key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        value_name = "medo_tahrim"  # نام کلیدی که باید حذف شود

        try:
            reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
            reg.DeleteValue(reg_key, value_name)
            reg.CloseKey(reg_key)
        except FileNotFoundError:
            pass  # اگر کلید وجود نداشته باشد، نیازی به حذف نیست
        except OSError:
            pass 
    
    
    
    def set_dns(self, dns_choice):
        pygame.init()
        pygame.mixer.music.load("./image/success.mp3")
        
        interface_name = self.get_active_interface_name()

        if not interface_name:
            self.label_3.setText("هیچ کانکشنی یافت نشد")
            return

        dns_servers = {
            'شکن': ['178.22.122.100', '185.51.200.2'],
            '403': ['10.202.10.202', '10.202.10.102'],
            'بگذر': ['185.55.226.26', '185.55.225.25'],
            'هاست ایران': ['172.29.0.100', '172.29.2.100'],
            'رادار گیم': ['10.202.10.10', '10.202.10.11'],
            'شاتل': ['85.15.1.14', '85.15.1.15'],
            'الکترو': ['78.157.42.100', '78.157.42.101'],
        }

        selected_dns = dns_servers.get(dns_choice)
        if selected_dns:
            primary_dns, secondary_dns = selected_dns
            os.system(f"netsh interface ip set dns name=\"{interface_name}\" static {primary_dns}")
            os.system(f"netsh interface ip add dns name=\"{interface_name}\" {secondary_dns} index=2")
            pygame.mixer.music.play()
            notification.notify(
                title="DNS Manager",
                message="با موفقیت متصل شد",
                timeout=5
            )
            self.label_3.setText("DNS با موفقیت تنظیم شد")
        else:
            self.label_3.setText("انتخاب DNS معتبر نیست")

    def clear_dns(self):
        interface_name = self.get_active_interface_name()

        if not interface_name:
            self.label_3.setText("هیچ کانکشنی یافت نشد")
            return

        os.system(f"netsh interface ip set dns name=\"{interface_name}\" dhcp")
        
        notification.notify(
            title="DNS Manager",
            message="اتصال با موفقیت قطع شد",
            timeout=5
        )
        self.label_3.setText("DNS با موفقیت حذف شد")


    
    def get_active_interface_name(self):  # اضافه کردن self
        result = subprocess.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True)

        if result.returncode != 0:
            return None

        lines = result.stdout.splitlines()
        print(lines)
        print('------------------------')

        for line in lines:
            if "Connected" in line and "Enabled" in line and "VMware" not in line:
                columns = line.split()
                interface_name = ' '.join(columns[3:])
                print("Interface Name:", interface_name)
                return interface_name  # برگرداندن نام اینترفیس

        return None


        
        

    def closeEvent(self, event):
       
        self.hide() 
        
        event.ignore()  

    def restore_window(self):
        
        self.show()
        self.activateWindow()

    def exit_application(self):
        # Clear DNS before quitting
        if self.is_on:
            self.clear_dns()
        QApplication.instance().quit()


   
    def on_tray_icon_clicked(self, reason):
   
        if reason == QSystemTrayIcon.Trigger:  
            self.show_window(MainWindow)  

    def show_window(self, MainWindow):
        MainWindow.showNormal()  
        MainWindow.activateWindow() 

    def exit_application(self):
        QApplication.instance().quit()

    def show_info(self, title, content):
        self.about_window = AboutAppWindow(title, content)
        self.about_window.show()
    
    def show_info_2(self,title):
        self.about_window = AboutAppWindow_info()
        self.about_window.show()
 

    def quit_application(self):
    
        QApplication.instance().quit()

    def closeEvent(self, event):
       
        self.hide()
       
        
        event.ignore() 



if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        win = Ui_MainWindow()
        win.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        pass       
