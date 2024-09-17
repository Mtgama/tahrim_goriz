import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine-tuning.
build_exe_options = {
    "packages": ["os", "pygame", "plyer", "winreg", "sys", "subprocess", "json", "PyQt5"],
    "include_files": ["./image/app_icon.ico"],  # اضافه کردن فایل‌های اضافی مانند تصاویر و آیکون‌ها
}

# Base="Win32GUI" should be used only for Windows GUI app, 
# it hides the console window. If it's a console app, leave as None
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # اگر برنامه شما کنسول ندارد و یک رابط گرافیکی است

# Setup cx_Freeze
setup(
    name = "Medo_tahrim",
    version = "1.0",
    description = "Medofile Tahreem Passer",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base, icon="./image/app_icon.ico",manifest="main.manifest")],
)
