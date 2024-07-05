import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QTextBrowser
from PySide6.QtGui import QIcon

from pathlib import Path


def app_dir():
    """Returns the base application path."""
    if hasattr(sys, "frozen"):
        # Handles PyInstaller
        return Path(sys.executable).parent  # 使用pyinstaller打包后的exe目录
    return Path(__file__).parent  # 没打包前的py目录


class Config:
    app_ver = "1.0.0"
    app_name = "完美构建"
    app_exec = "perfect_build"
    app_publisher = "技术有限公司"
    app_url = "https://www.example.com"
    app_icon = "icon/icon.ico"
    app_dir = app_dir()


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowFlags(Qt.WindowCloseButtonHint)  # 只显示关闭按钮
        self.setFixedSize(400, 300)

        self.setWindowTitle("HELLO")
        layout = QVBoxLayout(self)
        purpose = QTextBrowser()
        purpose.setText("Perfect Build!\n" * 50)
        purpose.setReadOnly(True)  # 设置为只读，防止用户编辑文本
        layout.addWidget(purpose)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowIcon(QIcon(Config.app_icon))
    window.show()
    app.exec()
