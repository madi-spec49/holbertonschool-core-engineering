class Square:
    def __init__(self, size=0):
        self.size = size  # Appelle le setter automatiquement !

    @property           # ← Décorateur getter
    def size(self):
        """Récupère la valeur (retourne une copie, pas la référence)"""
        return self.__size

    @size.setter        # ← Décorateur setter (même nom !)
    def size(self, value):
        """Valide et assigne la valeur"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
