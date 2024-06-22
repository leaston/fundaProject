from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QFont


class CustomTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Définir la largeur du curseur
        self.setCursorWidth(2)

        # Activer le suivi de la souris
        self.setMouseTracking(True)

        # Convertir 2,5 cm en pixels (1 cm ≈ 37.8 pixels)
        padding_in_pixels = int(2.5 * 37.8)

        # Appliquer un style pour les marges et les bordures
        self.setStyleSheet(f"""
            QTextEdit {{
                background-color: #ffffff; /* Couleur de fond blanche */
                padding-left: {padding_in_pixels}px; /* Marges internes gauche */
                padding-right: {padding_in_pixels}px; /* Marges internes droite */
                padding-top: {padding_in_pixels}px; /* Marges internes haut */
                padding-bottom: {padding_in_pixels}px; /* Marges internes bas */
                border: none;
            }}
        """)

        # Taille de police initiale
        self.initial_font_size = 12

        # Appliquer une police par défaut
        font = self.font()
        font.setPointSize(self.initial_font_size)
        self.setFont(font)

        # Taille de la zone de saisie pour une page A4 (210 x 297 mm)
        a4_width = int(210 * 3.78)  # 1 mm ≈ 3.78 pixels
        a4_height = int(297 * 3.78)
        self.setFixedSize(a4_width, a4_height)

    def zoomIn(self, range=1):
        font = self.font()
        font.setPointSize(font.pointSize() + range)
        self.setFont(font)

    def zoomOut(self, range=1):
        font = self.font()
        font.setPointSize(max(1, font.pointSize() - range))  # Éviter une taille de police négative ou zéro
        self.setFont(font)
