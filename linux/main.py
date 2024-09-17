# -*- coding: utf-8 -*-

import os
import time
import subprocess
import sys
from PyQt5.QtCore import Qt
import webbrowser
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,QLabel,QMainWindow, QAction, QCheckBox, QSystemTrayIcon, QMenu
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from playsound import playsound
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
        pixmap = QPixmap('./image/logo.png')  # مسیر لوگو خود را وارد کنید
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

        
        app_icon = QtGui.QIcon('./image/app_icon.ico')  # مسیر آیکون خود را قرار دهید
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
     
        self.label.setText(_translate("MainWindow", "گذر از تحریم مدوفایل"))
        self.label_2.setText(_translate("MainWindow", "لطفا یک تحریم گذر را انتخاب کنید"))
        self.menuMore.setTitle(_translate("MainWindow", "More"))

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
            select_item = self.comboBox.currentText()  
            self.set_dns(select_item)
            self.comboBox.setEnabled(False)
            self.label_3.setText("با موفقیت روشن شد")
        else:
            self.clear_dns()
            self.comboBox.setEnabled(True)

    def set_dns(self, dns_choice):
        result = subprocess.run(["nmcli", "-t", "-f", "NAME,DEVICE", "connection", "show", "--active"], capture_output=True, text=True)
        
        if result.returncode != 0:
            self.label_3.setText("خطا در دریافت کانکشن فعال")
            return

        connection_name = result.stdout.split(":")[0]
                
        if connection_name is None:
            self.label_3.setText("هیچ کانکشنی یافت نشد")
            return

        if dns_choice == 'شکن':
            os.system(f"nmcli connection modify '{connection_name}' ipv4.dns '178.22.122.100 185.51.200.2'")

            playsound("./image/success.mp3")
            
        elif dns_choice == '403':
            os.system(f"nmcli connection modify '{connection_name}' ipv4.dns '10.202.10.202 10.202.10.102'")
            playsound("./image/success.mp3")
            
        elif dns_choice == 'بگذر':
            os.system(f"nmcli connection modify '{connection_name}' ipv4.dns '185.55.226.26 185.55.225.25'")
            playsound("./image/success.mp3")
            
        elif dns_choice == "هاست ایران":
            os.system(f"nmcli connection modify '{connection_name}' ipv4.dns '179.29.0.100 172.29.100'")
            playsound("./image/success.mp3")
           
        elif dns_choice == "رادار گیم":
            os.system(f"nmcli connection modify '{connection_name}' ipv4.dns '10.202.10.10 10.202.10.11'")
            playsound("./image/success.mp3")
            
        elif dns_choice == "شاتل":
            os.system(f"nmcli connection modify '{connection_name}' ipv4.dns '85.15.1.14 85.15.1.15'")   
            playsound("./image/success.mp3")
            
        elif dns_choice == "الکترو":
            os.system(f"nmcli connection modify '{connection_name}' ipv4.dns '78.157.42.100 78.157.42.101'")
            playsound("./image/success.mp3")
            
            
        os.system(f"nmcli connection up '{connection_name}'")
    def clear_dns(self):
        result = subprocess.run(["nmcli", "-t", "-f", "NAME,DEVICE", "connection", "show", "--active"],capture_output=True, text=True)

        if result.returncode != 0:
            self.label_3.setText("خطا در دریافت کانکشن فعال")
            return

        connection_name = result.stdout.split(":")[0]
                
        if connection_name is None:
            self.label_3.setText("هیچ کانکشنی یافت نشد")
            return

        os.system(f"nmcli connection modify '{connection_name}' ipv4.ignore-auto-dns no")
        os.system(f"nmcli connection modify '{connection_name}' ipv4.dns ''")
        os.system(f"nmcli connection up '{connection_name}'")
        playsound("./image/dissconnect.mp3")

        self.label_3.setText("با موفقیت خاموش شد")

    def closeEvent(self, event):
        
        self.hide()  # مخفی کردن پنجره اصلی
        event.ignore()  # جلوگیری از بسته شدن پنجره

    def restore_window(self):
        
        self.show()
        self.activateWindow()

    def exit_application(self):
        
        if self.is_on:
            self.clear_dns()
        QApplication.instance().quit()



    def toggle_startup(self, state):
        if state == 2:  
            self.add_to_startup()
        else:
            self.remove_from_startup()

    def add_to_startup(self):
       
        desktop_file_path = os.path.expanduser('~/.config/autostart/myapp.desktop')

        
        desktop_entry = f"""[Desktop Entry]
Type=Application
Exec={os.path.abspath(__file__)}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=MyApp
Name=MyApp
Comment=This is my application
"""
        
        with open(desktop_file_path, 'w') as f:
            f.write(desktop_entry)
        self.label_3.setText("برنامه به استارتآپ اضافه شد")

    def remove_from_startup(self):
        
        desktop_file_path = os.path.expanduser('~/.config/autostart/myapp.desktop')
        
        
        if os.path.exists(desktop_file_path):
            os.remove(desktop_file_path)
            self.label_3.setText("برنامه از استارتآپ حذف شد")

    def is_in_startup(self):
        
        desktop_file_path = os.path.expanduser('~/.config/autostart/myapp.desktop')
        return os.path.exists(desktop_file_path)

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
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()  
    win = Ui_MainWindow()
    win.setupUi(MainWindow)  
    MainWindow.show()  
    sys.exit(app.exec_())