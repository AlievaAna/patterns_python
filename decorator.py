from abc import ABC, abstractmethod

class AbstractEffect(ABC, Hero):
    """Абстрактный класс для всех эффектов"""
    
    def __init__(self, base):
        self.base = base
        
    @abstractmethod
    def get_stats(self):
        pass
    
    
class AbstractPositive(AbstractEffect):
    """Абстрактный класс для положительных эффектов"""
    
    @abstractmethod
    def get_positive_effects(self):
        pass
    
    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        return self.negative_effects
    
    def get_stats(self):
        return self.get_stats()
    
    
class AbstractNegative(AbstractEffect):
    """Абстрактный класс для отрицательных эффектов"""
    
    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        return self.positive_effects
    
    @abstractmethod
    def get_negative_effects(self):
        pass
    
    def get_stats(self):
        return self.get_stats()


class Berserk(AbstractPositive):
    """Сила +7, Выносливость +7, Ловкость +7, Удача +7
       Восприятие -3, Харизма -3, Интеллект -3,
       Здоровье +50"""
    
    def __init__(self, base):
        super().__init__(base)
        self.stats = self.get_stats()
        self.positive_effects = self.get_positive_effects()

    def get_positive_effects(self):
        name = "Berserk"
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append(name)
        return self.positive_effects.copy()
    
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Strength"] += 7
        self.stats["Endurance"] += 7
        self.stats["Agility"] += 7
        self.stats["Luck"] += 7
        self.stats["Perception"] -= 3
        self.stats["Charisma"] -= 3
        self.stats["Intelligence"] -= 3
        self.stats["HP"] += 50
        return self.stats.copy()

    
class Blessing(AbstractPositive):
    """Все основные характеристики +2"""
    
    def __init__(self, base):
        super().__init__(base)
        self.stats = self.get_stats()
        self.positive_effects = self.get_positive_effects()
        
    def get_positive_effects(self):
        name = "Blessing"
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append(name)
        return self.positive_effects.copy()
    
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Strength"] += 2
        self.stats["Endurance"] += 2
        self.stats["Agility"] += 2
        self.stats["Luck"] += 2
        self.stats["Perception"] += 2
        self.stats["Charisma"] += 2
        self.stats["Intelligence"] += 2
        return self.stats.copy()


class Weakness(AbstractNegative):
    """Сила -4, Выносливость -4, Ловкость -4"""
    
    def __init__(self, base):
        super().__init__(base)
        self.stats = self.get_stats()
        self.negative_effects = self.get_negative_effects()
    
    def get_negative_effects(self):
        name = "Weakness"
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append(name)
        return self.negative_effects.copy()
    
    def get_stats(self):        
        self.stats = self.base.get_stats()
        self.stats["Strength"] -= 4
        self.stats["Endurance"] -= 4
        self.stats["Agility"] -= 4
        return self.stats.copy()
    

class EvilEye(AbstractNegative):
    """Удача -10"""

    def __init__(self, base):
        super().__init__(base)
        self.stats = self.get_stats()
        self.negative_effects = self.get_negative_effects()
    
    def get_negative_effects(self):
        name = "EvilEye"
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append(name)
        return self.negative_effects.copy()
    
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Luck"] -= 10
        return self.stats.copy()
    
    
class Curse(AbstractNegative):
    """Все основные характеристики -2"""

    def __init__(self, base):
        super().__init__(base)
        self.stats = self.get_stats()
        self.negative_effects = self.get_negative_effects()
        
    def get_negative_effects(self):
        name = "Curse"
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append(name)
        return self.negative_effects.copy()
    
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Strength"] -= 2
        self.stats["Endurance"] -= 2
        self.stats["Agility"] -= 2
        self.stats["Luck"] -= 2
        self.stats["Perception"] -= 2
        self.stats["Charisma"] -= 2
        self.stats["Intelligence"] -= 2
        return self.stats.copy()