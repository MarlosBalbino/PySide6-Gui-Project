import os

from qt_core import *

class PyPushButton(QPushButton):
    def __init__(
        self,
        text = "",
        height = 40,
        minimum_width = 50,
        text_padding = 55,
        text_color = "#c3ccdf",
        icon_path = "",
        icon_color = "#c3ccdf",
        button_color = "#44475a",
        button_hover = "#4f5368",
        button_pressed = "#282a36",
        is_active = False,
        parent = None
    ):
        super().__init__(parent=parent)
        
        # Set default paremeters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom paremeters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.button_color = button_color
        self.button_hover = button_hover
        self.button_pressed = button_pressed
        self.is_active = is_active

        # Set style
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            button_color = self.button_color,
            button_hover = self.button_hover,
            button_pressed = self.button_pressed,
            is_active = self.is_active
        )

    def set_style(
        self,
        text_padding = 55,
        text_color = "c3ccdf",
        button_color = "#44475a",
        button_hover = "#4f5368",
        button_pressed = "#282a36",
        is_active = False
    ):
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {button_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {button_hover};
        }}
        QPushButton:pressed {{
            background-color: {button_pressed};
        }}
        """

        active_style = f"""
        QPushButton {{
            background-color: {button_hover};
            border-right: 5px solid #282a36;
        }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)

        # Painter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.minimum_width, self.height())

        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()
    
    def draw_icon(self, qp, image, rect, color):
        # Format path
        app_path = os.path.abspath(os.getcwd())
        icons_folder = "gui/images/icons"
        path = os.path.join(app_path, icons_folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # Draw icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)

        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()

