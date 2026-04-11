
import sys

from PyQt6 import QtCore, QtGui, QtWidgets


class ClickableForm(QtWidgets.QAbstractButton):
    """
        Кастомный toggle-чекбокс (ON / OFF) через paintEvent
        Полная замена QCheckBox
        Использование снаружи

        self.checkBox_2 = ClickableForm(
                        color_on_bg=QtGui.QColor("#1a5fb4"), - красный
                        color_off_bg=QtGui.QColor("#e01b24"), - синий
                        color_knob=QtGui.QColor("white"), - белый кружок
                        )

        self.checkBox_2.setScale(1.4, 1.0) - если нужен масштаб

    """
    stateChanged = QtCore.pyqtSignal(int)

    BASE_WIDTH = 48
    BASE_HEIGHT = 22
    BASE_RADIUS = 9
    BASE_KNOB = 18
    BASE_MARGIN = 2

    def __init__(
        self,
        parent=None,
        *,
        color_on_bg=QtGui.QColor(28, 113, 216),
        color_off_bg=QtGui.QColor(224, 27, 36),
        color_knob=QtGui.QColor(255, 255, 255),
    ):
        super().__init__(parent)
        
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        self.color_on_bg = QtGui.QColor(color_on_bg)
        self.color_off_bg = QtGui.QColor(color_off_bg)
        self.color_knob = QtGui.QColor(color_knob)

        self._scale_x = 1.0
        self._scale_y = 1.0
        
        self._hovered = False
        self.darker = 0.85   # темнее при нажатии
        self.lighter = 1.15   # светлее при наведении
        self.setMouseTracking(True)
        
        self.setCheckable(True)
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self._update_size()

    # ---------- PUBLIC API ----------
    
    def nextCheckState(self):
        self.setChecked(not self.isChecked())
        
    # -------Метод изменения масштаба--------

    def setScale(self, sx: float, sy: float = None):
        if sy is None:
            sy = sx
        if sx <= 0 or sy <= 0:
            return

        self._scale_x = sx
        self._scale_y = sy
        self._update_size()
        self.update()
        
    
    def _update_size(self):
        self.setFixedSize(
            int(self.BASE_WIDTH * self._scale_x),
            int(self.BASE_HEIGHT * self._scale_y),
        )
    
    def sizeHint(self):
        return QtCore.QSize(
            int(self.BASE_WIDTH * self._scale_x),
            int(self.BASE_HEIGHT * self._scale_y),
        )
    
    minimumSizeHint = sizeHint
    
    # ---------- PAINT ----------
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        
        pressed = self.isDown()
        hovered = self._hovered and not pressed
        
        base_bg = self.color_on_bg if self.isChecked() else self.color_off_bg
        
        if pressed:
            bg_color = self._adjust_color(base_bg, self.darker)
        elif hovered:
            bg_color = self._adjust_color(base_bg, self.lighter)
        else:
            bg_color = base_bg
        
        # фон
        painter.save()
        painter.scale(self._scale_x, self._scale_y)
        
        painter.setBrush(bg_color)
        painter.setPen(QtCore.Qt.PenStyle.NoPen)
        
        base_rect = QtCore.QRect(0, 0, self.BASE_WIDTH, self.BASE_HEIGHT)
        painter.drawRoundedRect(base_rect, self.BASE_RADIUS, self.BASE_RADIUS)
        
        painter.restore()
        
        # бегунок
        w, h = self.width(), self.height()
        
        knob_d = min(
            h - 2 * self.BASE_MARGIN,
            int(self.BASE_KNOB * min(self._scale_x, self._scale_y))
        )
        
        y = (h - knob_d) // 2
        
        if self.isChecked():
            x = w - knob_d - self.BASE_MARGIN
        else:
            x = self.BASE_MARGIN
        
        knob_rect = QtCore.QRect(x, y, knob_d, knob_d)
        
        painter.setBrush(self.color_knob)
        painter.drawEllipse(knob_rect)
    
    # ---------- STATE ----------
    def setChecked(self, checked: bool):
        if self.isChecked() == checked:
            return
        
        super().setChecked(checked)
        
        state = (
            QtCore.Qt.CheckState.Checked
            if checked
            else QtCore.Qt.CheckState.Unchecked
        )
        
        self.stateChanged.emit(state)
        self.update()
    
    # ---------- HOVER ----------
    def enterEvent(self, event):
        self._hovered = True
        self.update()
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        self._hovered = False
        self.update()
        super().leaveEvent(event)
    
    # ---------- UTILS ----------
    def _adjust_color(self, color: QtGui.QColor, factor: float) -> QtGui.QColor:
        c = QtGui.QColor(color)
        if factor > 1.0:
            return c.lighter(int(factor * 100))
        return c.darker(int(100 / factor))

    # # ---------- SIZE ----------
    # # ------Пересчёт размера виджета-------
    #
    # def _update_size(self):
    #     self.setFixedSize(
    #         int(self.BASE_WIDTH * self._scale_x),
    #         int(self.BASE_HEIGHT * self._scale_y),
    #     )
    #
    # def sizeHint(self):
    #     return QtCore.QSize(
    #         int(self.BASE_WIDTH * self._scale_x),
    #         int(self.BASE_HEIGHT * self._scale_y),
    #     )
    #
    # minimumSizeHint = sizeHint
    #
    # # ---------- PAINT ----------
    #
    # def paintEvent(self, event):
    #     painter = QtGui.QPainter(self)
    #     painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    #
    #     # --------- определяем состояние ---------
    #     pressed = self.isDown()
    #     hovered = self._hovered and not pressed
    #
    #     # --------- выбираем цвет фона ---------
    #     base_bg = self.color_on_bg if self.isChecked() else self.color_off_bg
    #
    #     if pressed:
    #         bg_color = self._adjust_color(base_bg, self.darker)  # темнее при нажатии
    #     elif hovered:
    #         bg_color = self._adjust_color(base_bg, self.lighter)  # светлее при наведении
    #     else:
    #         bg_color = base_bg
    #
    #     # =========================
    #     # ФОН (масштабируется)
    #     # =========================
    #     painter.save()
    #     painter.scale(self._scale_x, self._scale_y)
    #
    #     painter.setBrush(bg_color)
    #     painter.setPen(QtCore.Qt.PenStyle.NoPen)
    #
    #     base_rect = QtCore.QRect(0, 0, self.BASE_WIDTH, self.BASE_HEIGHT)
    #     painter.drawRoundedRect(
    #         base_rect,
    #         self.BASE_RADIUS,
    #         self.BASE_RADIUS
    #     )
    #
    #     painter.restore()
    #
    #     # =========================
    #     # БЕГУНОК (НЕ масштабируется)
    #     # =========================
    #     w, h = self.width(), self.height()
    #
    #     knob_d = min(
    #         h - 2 * self.BASE_MARGIN,
    #         int(self.BASE_KNOB * min(self._scale_x, self._scale_y))
    #     )
    #
    #     y = (h - knob_d) // 2
    #
    #     if self.isChecked():
    #         x = w - knob_d - self.BASE_MARGIN
    #     else:
    #         x = self.BASE_MARGIN
    #
    #     knob_rect = QtCore.QRect(x, y, knob_d, knob_d)
    #
    #     painter.setBrush(self.color_knob)
    #     painter.drawEllipse(knob_rect)
    #
    # # ---------- STATE ----------
    # # ---------- ЛОГИКА ----------
    #
    # def setChecked(self, checked: bool):
    #     if self.isChecked() == checked:
    #         return
    #
    #     super().setChecked(checked)
    #
    #     state = (
    #         QtCore.Qt.CheckState.Checked
    #         if checked
    #         else QtCore.Qt.CheckState.Unchecked
    #     )
    #     self.stateChanged.emit(state)
    #     self.update()
    #
    # def enterEvent(self, event):
    #     self._hovered = True
    #     self.update()
    #     super().enterEvent(event)
    #
    # def leaveEvent(self, event):
    #     self._hovered = False
    #     self.update()
    #     super().leaveEvent(event)
    #
    # def _adjust_color(self, color: QtGui.QColor, factor: float) -> QtGui.QColor:
    #     c = QtGui.QColor(color)
    #     if factor > 1.0:
    #         return c.lighter(int(factor * 100))
    #     return c.darker(int(100 / factor))

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = ClickableForm()
    
    # w = ToggleSwitch()
    w.show()
    sys.exit(app.exec())
    
    
"""
Что такое QtGui.QPainter

QPainter — это низкоуровневый движок рисования Qt.

Он умеет рисовать:

    -геометрию (прямоугольники, эллипсы, линии)
    -текст
    -изображения
    -градиенты
    -векторы

И делает это:

    -на QWidget
    -на QPixmap
    -на QImage
    -на принтер

В контексте виджетов он всегда используется внутри paintEvent().

Жизненный цикл paintEvent
Qt → решает, что виджет нужно перерисовать
  → вызывает paintEvent(event)
    → ты создаёшь QPainter(self)
      → рисуешь


Важно:

никогда не вызывать paintEvent вручную для перерисовки используется update()

Базовый шаблон
def paintEvent(self, event):
    painter = QtGui.QPainter(self)
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    ...

Метод за методом (то, что мы использовали)
1. QPainter(self)
painter = QtGui.QPainter(self)


Создаёт контекст рисования поверх текущего виджета.

self → поверхность (canvas)

все координаты → относительно self.rect()

2. setRenderHint(Antialiasing)
painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)


Включает сглаживание.

Без него:

круги выглядят «рваными», углы ступенчатые

С ним:

плавные края, визуально «премиум»

3. self.rect()
rect = self.rect()


Возвращает QRect(0, 0, width, height). Это рабочая область рисования виджета.

4. setBrush(color)
painter.setBrush(bg_color)


Brush = чем заполняем фигуру.

    -цвет
    -градиент
    -текстура

Если Brush не задан — фигура будет пустой.

5. setPen(NoPen)
painter.setPen(QtCore.Qt.PenStyle.NoPen)


Pen = чем рисуется контур.

Мы его отключаем, потому что нам не нужна рамка только заливка
Если не отключить — Qt нарисует тонкую чёрную обводку.

6. drawRoundedRect()
painter.drawRoundedRect(rect, radius, radius)


Рисует прямоугольник с закруглёнными углами.

Параметры:
    
    rect — где рисовать
    radius — радиус скругления по X и Y

7. Вычисление позиции бегунка
if self.isChecked():
    x = rect.width() - KNOB_DIAMETER - MARGIN
else:
    x = MARGIN


Это логика, не QPainter. Мы просто вычисляем координаты.

8. QRect для эллипса QRect(x, y, width, height)
knob_rect = QtCore.QRect(x, MARGIN, 18, 18)


Определяем bounding box(ограничивающую область) для круга.

9. drawEllipse()
painter.drawEllipse(knob_rect)


Рисует  круг или эллипс (если ширина ≠ высоте)

Почему QPainter — мощный инструмент

Он:

    -быстрый
    -аппаратно ускоряется
    -векторный (масштабируется без артефактов)
    -одинаково работает на Linux / Windows / macOS

Поэтому все стандартные элементы Qt внутри — это QPainter.

Важные правила (обязательно запомнить)
❌ Нельзя

    -создавать QPainter вне paintEvent
    -хранить его в атрибуте
    -рисовать из других методов

✅ Нужно

    -вызывать self.update() при изменениях
    -держать paintEvent быстрым
    -считать геометрию заранее

Частые полезные методы QPainter (на будущее)
  Метод	         Назначение
drawText()	        текст
drawPixmap()	    картинки
drawLine()	        линии
setOpacity()	    прозрачность
save() / restore()	стек состояний
setFont()	        шрифт
setClipRect()	    обрезка
"""