# Guide des Patrons de Conception

## Table des matières

1. [Partie 1 : Problèmes et solutions](#partie-1--problèmes-et-solutions)
   - [1.1 Gestion des ressources partagées](#11-gestion-des-ressources-partagees)
   - [1.2 Notification d'événements](#12-notification-devenements)
   - [1.3 Création d'objets complexes](#13-creation-dobjets-complexes)
   - [1.4 Création de familles d'objets](#14-creation-de-familles-dobjets)
   - [1.5 Intégration d'interfaces incompatibles](#15-integration-dinterfaces-incompatibles)
   - [1.6 Extension de fonctionnalités](#16-extension-de-fonctionnalites)
   - [1.7 Simplification d'interfaces complexes](#17-simplification-dinterfaces-complexes)
   - [1.8 Traitement d'objets composites](#18-traitement-dobjets-composites)
   - [1.9 Choix d'algorithmes](#19-choix-dalgorithmes)
   - [1.10 Gestion d'états](#110-gestion-detats)

2. [Partie 2 : Similitudes, différences et risques de confusion](#partie-2--similitudes-differences-et-risques-de-confusion)
   - [2.1 Strategy vs State](#21-strategy-vs-state)
   - [2.2 Décorateur vs Façade vs Adaptateur](#22-decorateur-vs-facade-vs-adaptateur)
   - [2.3 Composite vs Décorateur](#23-composite-vs-decorateur)
   - [2.4 Factory vs Singleton](#24-factory-vs-singleton)

---

## Partie 1 : Problèmes et solutions

### 1.1 Gestion des ressources partagées

**Problème :** Vous avez besoin d'une seule instance d'une classe pour gérer une ressource partagée dans un jeu vidéo (gestionnaire de sauvegarde, système audio, gestionnaire de ressources).

**Solution :** Utilisez le patron **Singleton** pour garantir qu'une seule instance de la classe existe dans toute l'application.

**Exemple de code :**

```python
class GameSaveManager:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.save_data = {}
            self.current_slot = 1
            self._initialized = True
    
    def save_game(self, player_data, level, score):
        save_key = f"slot_{self.current_slot}"
        self.save_data[save_key] = {
            "player_data": player_data,
            "level": level,
            "score": score,
            "timestamp": "2024-01-15 14:30:00"
        }
        print(f"Jeu sauvegardé dans le slot {self.current_slot}")
    
    def load_game(self, slot):
        save_key = f"slot_{slot}"
        if save_key in self.save_data:
            print(f"Chargement du slot {slot}")
            return self.save_data[save_key]
        return None
    
    def set_save_slot(self, slot):
        self.current_slot = slot

# Utilisation
save_manager1 = GameSaveManager()
save_manager2 = GameSaveManager()
print(save_manager1 is save_manager2)  # True - même instance

save_manager1.save_game({"name": "Joueur1", "health": 100}, 5, 1500)
save_manager2.load_game(1)  # Utilise la même instance
```

### 1.2 Notification d'événements

**Problème :** Vous voulez notifier plusieurs systèmes du jeu quand un événement se produit (joueur meurt, niveau terminé, objet collecté), sans créer un couplage fort entre l'objet émetteur et les récepteurs.

**Solution :** Utilisez le patron **Observateur** pour établir une relation un-à-plusieurs entre objets.

**Exemple de code :**

```python
from abc import ABC, abstractmethod

class GameObserver(ABC):
    @abstractmethod
    def on_event(self, event_type, data):
        pass

class GameEventSystem:
    def __init__(self):
        self._observers = []
    
    def subscribe(self, observer):
        self._observers.append(observer)
    
    def unsubscribe(self, observer):
        self._observers.remove(observer)
    
    def notify(self, event_type, data):
        for observer in self._observers:
            observer.on_event(event_type, data)

class AudioSystem(GameObserver):
    def on_event(self, event_type, data):
        if event_type == "player_death":
            print("🔊 Son de mort joué")
        elif event_type == "level_complete":
            print("🔊 Musique de victoire jouée")
        elif event_type == "item_collected":
            print("🔊 Son de collecte joué")

class UISystem(GameObserver):
    def on_event(self, event_type, data):
        if event_type == "player_death":
            print("📱 Affichage de l'écran Game Over")
        elif event_type == "level_complete":
            print("📱 Affichage du score final")
        elif event_type == "item_collected":
            print(f"📱 Mise à jour de l'inventaire: {data['item']}")

class AchievementSystem(GameObserver):
    def on_event(self, event_type, data):
        if event_type == "item_collected":
            print(f"🏆 Succès débloqué: Collectionneur!")
        elif event_type == "level_complete":
            print(f"🏆 Succès débloqué: Niveau {data['level']} terminé!")

# Utilisation
event_system = GameEventSystem()
audio = AudioSystem()
ui = UISystem()
achievements = AchievementSystem()

event_system.subscribe(audio)
event_system.subscribe(ui)
event_system.subscribe(achievements)

# Simulation d'événements de jeu
event_system.notify("item_collected", {"item": "Épée légendaire"})
event_system.notify("level_complete", {"level": 3, "score": 2500})
event_system.notify("player_death", {"cause": "chute"})
```

### 1.3 Création d'objets complexes

**Problème :** Vous devez créer des ennemis, armes ou objets dans un jeu vidéo dont le processus de création est complexe ou dépend de paramètres dynamiques (niveau du joueur, zone du jeu, difficulté).

**Solution :** Utilisez le patron **Factory** pour encapsuler la logique de création d'objets.

**Exemple de code :**

```python
from abc import ABC, abstractmethod

class Enemy(ABC):
    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def get_stats(self):
        pass

class Goblin(Enemy):
    def __init__(self, level):
        self.level = level
        self.health = 50 + (level * 10)
        self.damage = 15 + (level * 5)
    
    def attack(self):
        return f"Goblin niveau {self.level} attaque pour {self.damage} dégâts!"
    
    def get_stats(self):
        return {"health": self.health, "damage": self.damage, "type": "Goblin"}

class Orc(Enemy):
    def __init__(self, level):
        self.level = level
        self.health = 100 + (level * 15)
        self.damage = 25 + (level * 8)
    
    def attack(self):
        return f"Orc niveau {self.level} attaque pour {self.damage} dégâts!"
    
    def get_stats(self):
        return {"health": self.health, "damage": self.damage, "type": "Orc"}

class Dragon(Enemy):
    def __init__(self, level):
        self.level = level
        self.health = 500 + (level * 50)
        self.damage = 100 + (level * 20)
    
    def attack(self):
        return f"Dragon niveau {self.level} crache du feu pour {self.damage} dégâts!"
    
    def get_stats(self):
        return {"health": self.health, "damage": self.damage, "type": "Dragon"}

class EnemyFactory:
    @staticmethod
    def create_enemy(enemy_type, player_level, zone_difficulty=1):
        # Calcul du niveau de l'ennemi basé sur le niveau du joueur et la difficulté de la zone
        enemy_level = max(1, player_level + zone_difficulty - 1)
        
        if enemy_type.lower() == "goblin":
            return Goblin(enemy_level)
        elif enemy_type.lower() == "orc":
            return Orc(enemy_level)
        elif enemy_type.lower() == "dragon":
            return Dragon(enemy_level)
        else:
            raise ValueError(f"Type d'ennemi non supporté: {enemy_type}")

# Utilisation
factory = EnemyFactory()
player_level = 5

# Création d'ennemis adaptés au niveau du joueur
goblin = factory.create_enemy("goblin", player_level, 1)  # Zone facile
orc = factory.create_enemy("orc", player_level, 2)        # Zone moyenne
dragon = factory.create_enemy("dragon", player_level, 3)  # Zone difficile

print(goblin.attack())
print(orc.attack())
print(dragon.attack())
print(f"Stats du gobelin: {goblin.get_stats()}")
```

### 1.4 Création de familles d'objets

**Problème :** Vous devez créer des familles d'objets liés dans un jeu vidéo qui doivent être compatibles entre eux (ex: armes et armures pour différentes factions, véhicules et armes pour différentes époques).

**Solution :** Utilisez le patron **Abstract Factory** pour créer des familles d'objets sans spécifier leurs classes concrètes.

**Exemple de code :**

```python
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Armor(ABC):
    @abstractmethod
    def defend(self):
        pass

# Armes et armures médiévales
class MedievalSword(Weapon):
    def attack(self):
        return "⚔️ Coup d'épée médiévale - 25 dégâts"

class MedievalShield(Armor):
    def defend(self):
        return "🛡️ Protection du bouclier médiéval - 15 défense"

# Armes et armures futuristes
class LaserRifle(Weapon):
    def attack(self):
        return "🔫 Tir de laser - 40 dégâts"

class EnergyShield(Armor):
    def defend(self):
        return "⚡ Bouclier d'énergie - 25 défense"

# Armes et armures modernes
class AssaultRifle(Weapon):
    def attack(self):
        return "🔫 Rafale d'assaut - 30 dégâts"

class BulletproofVest(Armor):
    def defend(self):
        return "🦺 Protection du gilet pare-balles - 20 défense"

class EquipmentFactory(ABC):
    @abstractmethod
    def create_weapon(self):
        pass
    
    @abstractmethod
    def create_armor(self):
        pass

class MedievalFactory(EquipmentFactory):
    def create_weapon(self):
        return MedievalSword()
    
    def create_armor(self):
        return MedievalShield()

class FuturisticFactory(EquipmentFactory):
    def create_weapon(self):
        return LaserRifle()
    
    def create_armor(self):
        return EnergyShield()

class ModernFactory(EquipmentFactory):
    def create_weapon(self):
        return AssaultRifle()
    
    def create_armor(self):
        return BulletproofVest()

# Utilisation
def equip_character(factory, character_name):
    weapon = factory.create_weapon()
    armor = factory.create_armor()
    print(f"🎮 {character_name} équipé:")
    print(f"   Arme: {weapon.attack()}")
    print(f"   Armure: {armor.defend()}")
    return weapon, armor

# Création d'équipements pour différentes époques
medieval_factory = MedievalFactory()
futuristic_factory = FuturisticFactory()
modern_factory = ModernFactory()

equip_character(medieval_factory, "Chevalier")
equip_character(futuristic_factory, "Soldat de l'espace")
equip_character(modern_factory, "Soldat moderne")
```

### 1.5 Intégration d'interfaces incompatibles

**Problème :** Vous avez des systèmes de jeu existants avec des interfaces qui ne correspondent pas à ce dont vous avez besoin (ex: ancien système de sauvegarde, API de tiers pour les graphiques).

**Solution :** Utilisez le patron **Adaptateur** pour faire fonctionner ensemble des classes avec des interfaces incompatibles.

**Exemple de code :**

```python
# Ancien système de rendu (legacy)
class LegacyRenderer:
    def draw_old_style(self, x, y, sprite_id):
        return f"Legacy: Dessin du sprite {sprite_id} à ({x}, {y})"

# Nouveau système de rendu
class ModernRenderer:
    def render_sprite(self, position, sprite_data):
        return f"Modern: Rendu du sprite {sprite_data['name']} à {position}"

# Système de rendu unifié (interface cible)
class GameRenderer:
    def render(self, entity):
        return f"Rendu de l'entité: {entity}"

# Adaptateur pour l'ancien système
class LegacyRendererAdapter(GameRenderer):
    def __init__(self, legacy_renderer):
        self.legacy_renderer = legacy_renderer
    
    def render(self, entity):
        # Adaptation de l'interface legacy vers l'interface moderne
        if hasattr(entity, 'x') and hasattr(entity, 'y') and hasattr(entity, 'sprite_id'):
            return self.legacy_renderer.draw_old_style(entity.x, entity.y, entity.sprite_id)
        return "Erreur: Format d'entité non supporté"

# Adaptateur pour le nouveau système
class ModernRendererAdapter(GameRenderer):
    def __init__(self, modern_renderer):
        self.modern_renderer = modern_renderer
    
    def render(self, entity):
        # Adaptation de l'interface moderne vers l'interface unifiée
        if hasattr(entity, 'position') and hasattr(entity, 'sprite_data'):
            return self.modern_renderer.render_sprite(entity.position, entity.sprite_data)
        return "Erreur: Format d'entité non supporté"

# Entités avec différentes interfaces
class LegacyEntity:
    def __init__(self, x, y, sprite_id):
        self.x = x
        self.y = y
        self.sprite_id = sprite_id

class ModernEntity:
    def __init__(self, position, sprite_data):
        self.position = position
        self.sprite_data = sprite_data

# Utilisation
legacy_renderer = LegacyRenderer()
modern_renderer = ModernRenderer()

# Création des adaptateurs
legacy_adapter = LegacyRendererAdapter(legacy_renderer)
modern_adapter = ModernRendererAdapter(modern_renderer)

# Entités avec interfaces différentes
legacy_entity = LegacyEntity(100, 200, "player_sprite")
modern_entity = ModernEntity((150, 250), {"name": "enemy_sprite", "texture": "enemy.png"})

# Rendu unifié grâce aux adaptateurs
renderers = [legacy_adapter, modern_adapter]
entities = [legacy_entity, modern_entity]

for renderer, entity in zip(renderers, entities):
    print(renderer.render(entity))
```

### 1.6 Extension de fonctionnalités

**Problème :** Vous voulez ajouter de nouvelles fonctionnalités à des armes ou objets dans un jeu vidéo sans modifier leur classe de base (enchantements, améliorations, effets spéciaux).

**Solution :** Utilisez le patron **Décorateur** pour envelopper un objet et lui ajouter des comportements dynamiquement.

**Exemple de code :**

```python
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def get_damage(self):
        pass
    
    @abstractmethod
    def get_description(self):
        pass

class BasicSword(Weapon):
    def get_damage(self):
        return 20
    
    def get_description(self):
        return "Épée basique"

class WeaponDecorator(Weapon):
    def __init__(self, weapon):
        self.weapon = weapon
    
    def get_damage(self):
        return self.weapon.get_damage()
    
    def get_description(self):
        return self.weapon.get_description()

class FireEnchantment(WeaponDecorator):
    def get_damage(self):
        return self.weapon.get_damage() + 10
    
    def get_description(self):
        return self.weapon.get_description() + " + Enchantement de feu"

class SharpnessEnchantment(WeaponDecorator):
    def get_damage(self):
        return self.weapon.get_damage() + 15
    
    def get_description(self):
        return self.weapon.get_description() + " + Tranchant"

class PoisonEnchantment(WeaponDecorator):
    def get_damage(self):
        return self.weapon.get_damage() + 5
    
    def get_description(self):
        return self.weapon.get_description() + " + Poison"

class DurabilityUpgrade(WeaponDecorator):
    def get_damage(self):
        return self.weapon.get_damage() + 8
    
    def get_description(self):
        return self.weapon.get_description() + " + Renforcée"

# Utilisation
sword = BasicSword()
print(f"Arme de base: {sword.get_description()} - {sword.get_damage()} dégâts")

# Ajout d'enchantements
sword = FireEnchantment(sword)
print(f"Avec feu: {sword.get_description()} - {sword.get_damage()} dégâts")

sword = SharpnessEnchantment(sword)
print(f"Avec tranchant: {sword.get_description()} - {sword.get_damage()} dégâts")

sword = PoisonEnchantment(sword)
print(f"Avec poison: {sword.get_description()} - {sword.get_damage()} dégâts")

# Création d'une épée différente avec d'autres améliorations
legendary_sword = BasicSword()
legendary_sword = DurabilityUpgrade(legendary_sword)
legendary_sword = SharpnessEnchantment(legendary_sword)
print(f"Épée légendaire: {legendary_sword.get_description()} - {legendary_sword.get_damage()} dégâts")
```

### 1.7 Simplification d'interfaces complexes

**Problème :** Vous avez un système de jeu complexe avec de nombreuses classes et méthodes (graphiques, audio, physique, IA), et vous voulez fournir une interface simple pour les clients.

**Solution :** Utilisez le patron **Façade** pour fournir une interface unifiée à un sous-système complexe.

**Exemple de code :**

```python
class GraphicsEngine:
    def initialize_renderer(self):
        return "🎨 Moteur graphique initialisé"
    
    def load_textures(self, texture_list):
        return f"🖼️ Chargement de {len(texture_list)} textures"
    
    def render_frame(self, scene_data):
        return f"📺 Rendu de la frame avec {len(scene_data)} objets"

class AudioEngine:
    def initialize_audio(self):
        return "🔊 Moteur audio initialisé"
    
    def load_sounds(self, sound_list):
        return f"🎵 Chargement de {len(sound_list)} sons"
    
    def play_background_music(self, track):
        return f"🎶 Lecture de la musique: {track}"

class PhysicsEngine:
    def initialize_physics(self):
        return "⚡ Moteur physique initialisé"
    
    def create_world(self, gravity):
        return f"🌍 Monde physique créé avec gravité: {gravity}"
    
    def simulate_step(self, delta_time):
        return f"🔄 Simulation physique (Δt={delta_time}s)"

class AIEngine:
    def initialize_ai(self):
        return "🧠 Moteur IA initialisé"
    
    def load_behavior_trees(self, trees):
        return f"🌳 Chargement de {len(trees)} arbres de comportement"
    
    def update_ai(self, entities):
        return f"🤖 Mise à jour IA pour {len(entities)} entités"

class GameEngineFacade:
    def __init__(self):
        self.graphics = GraphicsEngine()
        self.audio = AudioEngine()
        self.physics = PhysicsEngine()
        self.ai = AIEngine()
    
    def start_game(self, game_config):
        """Interface simplifiée pour démarrer le jeu"""
        print("🚀 Démarrage du jeu...")
        
        # Initialisation des sous-systèmes
        print(self.graphics.initialize_renderer())
        print(self.audio.initialize_audio())
        print(self.physics.initialize_physics())
        print(self.ai.initialize_ai())
        
        # Configuration des ressources
        print(self.graphics.load_textures(game_config["textures"]))
        print(self.audio.load_sounds(game_config["sounds"]))
        print(self.physics.create_world(game_config["gravity"]))
        print(self.ai.load_behavior_trees(game_config["ai_trees"]))
        
        return "✅ Jeu prêt à jouer!"
    
    def update_game(self, delta_time, scene_data, entities):
        """Interface simplifiée pour la boucle de jeu"""
        print(self.graphics.render_frame(scene_data))
        print(self.physics.simulate_step(delta_time))
        print(self.ai.update_ai(entities))
        return "🎮 Frame mise à jour"

# Utilisation
game_engine = GameEngineFacade()

# Configuration du jeu
config = {
    "textures": ["player.png", "enemy.png", "background.jpg"],
    "sounds": ["jump.wav", "collect.wav", "music.mp3"],
    "gravity": -9.81,
    "ai_trees": ["enemy_behavior", "npc_behavior"]
}

# Démarrage simplifié
result = game_engine.start_game(config)
print(result)

# Boucle de jeu simplifiée
scene = ["joueur", "ennemi1", "ennemi2", "objet"]
entities = ["ennemi1", "ennemi2", "npc1"]
game_engine.update_game(0.016, scene, entities)
```

### 1.8 Traitement d'objets composites

**Problème :** Vous voulez traiter des objets individuels et des compositions d'objets de manière uniforme dans un jeu vidéo (inventaire, quêtes, niveaux).

**Solution :** Utilisez le patron **Composite** pour composer des objets en structures arborescentes.

**Exemple de code :**

```python
from abc import ABC, abstractmethod

class GameItem(ABC):
    @abstractmethod
    def get_value(self):
        pass
    
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def display(self, indent=0):
        pass

class Item(GameItem):
    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description
    
    def get_value(self):
        return self.value
    
    def get_description(self):
        return self.description
    
    def display(self, indent=0):
        print("  " * indent + f"💎 {self.name} - {self.value} or - {self.description}")

class Container(GameItem):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def get_value(self):
        return sum(item.get_value() for item in self.items)
    
    def get_description(self):
        return f"{self.description} (contient {len(self.items)} objets)"
    
    def display(self, indent=0):
        print("  " * indent + f"🎒 {self.name} - {self.get_value()} or total")
        for item in self.items:
            item.display(indent + 1)

# Utilisation
# Création d'objets individuels
sword = Item("Épée légendaire", 100, "Une épée magique puissante")
potion = Item("Potion de soin", 25, "Restaure 50 points de vie")
gem = Item("Gemme de feu", 50, "Pierre précieuse rougeoyante")

# Création de conteneurs
treasure_chest = Container("Coffre au trésor", "Un coffre mystérieux")
player_inventory = Container("Inventaire du joueur", "Sac à dos du héros")
magic_bag = Container("Sac magique", "Sac enchanté pour objets précieux")

# Ajout d'objets dans les conteneurs
treasure_chest.add_item(sword)
treasure_chest.add_item(gem)

magic_bag.add_item(potion)
magic_bag.add_item(Item("Parchemin de téléportation", 75, "Permet de se téléporter"))

player_inventory.add_item(treasure_chest)
player_inventory.add_item(magic_bag)
player_inventory.add_item(Item("Clé dorée", 10, "Ouvre des portes spéciales"))

# Affichage de la structure
print("🎮 Inventaire du joueur:")
player_inventory.display()
print(f"\n💰 Valeur totale de l'inventaire: {player_inventory.get_value()} or")
```

### 1.9 Choix d'algorithmes

**Problème :** Vous avez plusieurs algorithmes pour accomplir une tâche dans un jeu vidéo et vous voulez pouvoir les interchanger dynamiquement (IA d'ennemis, systèmes de pathfinding, calculs de dégâts).

**Solution :** Utilisez le patron **Strategy** pour définir une famille d'algorithmes et les rendre interchangeables.

**Exemple de code :**

```python
from abc import ABC, abstractmethod

class AIStrategy(ABC):
    @abstractmethod
    def calculate_move(self, enemy, player):
        pass

class AggressiveAI(AIStrategy):
    def calculate_move(self, enemy, player):
        # IA agressive : attaque directement
        distance = abs(enemy.position - player.position)
        if distance <= enemy.attack_range:
            return f"🤺 {enemy.name} attaque le joueur!"
        else:
            return f"🏃 {enemy.name} court vers le joueur"

class DefensiveAI(AIStrategy):
    def calculate_move(self, enemy, player):
        # IA défensive : garde sa position et contre-attaque
        distance = abs(enemy.position - player.position)
        if distance <= enemy.attack_range:
            return f"🛡️ {enemy.name} se défend et contre-attaque!"
        else:
            return f"⏸️ {enemy.name} reste en position défensive"

class StealthAI(AIStrategy):
    def calculate_move(self, enemy, player):
        # IA furtive : se cache et attaque par surprise
        distance = abs(enemy.position - player.position)
        if distance <= enemy.attack_range:
            return f"🗡️ {enemy.name} attaque par surprise!"
        else:
            return f"👻 {enemy.name} se cache et se rapproche furtivement"

class SwarmAI(AIStrategy):
    def calculate_move(self, enemy, player):
        # IA d'essaim : coordonne avec d'autres ennemis
        return f"🐝 {enemy.name} coordonne l'attaque en groupe!"

class Enemy:
    def __init__(self, name, position, attack_range):
        self.name = name
        self.position = position
        self.attack_range = attack_range
        self.ai_strategy = None
    
    def set_ai_strategy(self, strategy):
        self.ai_strategy = strategy
    
    def act(self, player):
        if self.ai_strategy:
            return self.ai_strategy.calculate_move(self, player)
        return f"{self.name} ne sait pas quoi faire"

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

# Utilisation
player = Player("Héros", 10)

# Création d'ennemis avec différentes stratégies
goblin = Enemy("Goblin", 5, 2)
orc = Enemy("Orc", 8, 3)
assassin = Enemy("Assassin", 12, 1)
bees = Enemy("Abeilles", 6, 1)

# Attribution de stratégies
goblin.set_ai_strategy(AggressiveAI())
orc.set_ai_strategy(DefensiveAI())
assassin.set_ai_strategy(StealthAI())
bees.set_ai_strategy(SwarmAI())

# Simulation de combat
enemies = [goblin, orc, assassin, bees]

print("⚔️ Combat en cours:")
for enemy in enemies:
    print(enemy.act(player))

# Changement de stratégie dynamique
print("\n🔄 Le gobelin change de stratégie...")
goblin.set_ai_strategy(DefensiveAI())
print(goblin.act(player))
```

### 1.10 Gestion d'états

**Problème :** Un objet change de comportement selon son état interne dans un jeu vidéo, et vous voulez éviter les conditions complexes (joueur blessé/en bonne santé, ennemi alerte/repos, objet activé/désactivé).

**Solution :** Utilisez le patron **State** pour permettre à un objet de modifier son comportement quand son état interne change.

**Exemple de code :**

```python
from abc import ABC, abstractmethod

class PlayerState(ABC):
    @abstractmethod
    def handle_action(self, player, action):
        pass
    
    @abstractmethod
    def get_description(self):
        pass

class HealthyState(PlayerState):
    def handle_action(self, player, action):
        if action == "take_damage":
            player.health -= 20
            if player.health <= 0:
                player.set_state(DeadState())
            elif player.health <= 30:
                player.set_state(InjuredState())
            return f"💚 {player.name} prend 20 dégâts (PV: {player.health})"
        elif action == "heal":
            player.health = min(100, player.health + 30)
            return f"💚 {player.name} se soigne (PV: {player.health})"
        elif action == "attack":
            return f"⚔️ {player.name} attaque avec pleine puissance!"
        return f"💚 {player.name} est en bonne santé"
    
    def get_description(self):
        return "En bonne santé"

class InjuredState(PlayerState):
    def handle_action(self, player, action):
        if action == "take_damage":
            player.health -= 15
            if player.health <= 0:
                player.set_state(DeadState())
            return f"🩹 {player.name} prend 15 dégâts (PV: {player.health})"
        elif action == "heal":
            player.health = min(100, player.health + 20)
            if player.health > 30:
                player.set_state(HealthyState())
            return f"🩹 {player.name} se soigne (PV: {player.health})"
        elif action == "attack":
            return f"⚔️ {player.name} attaque avec difficulté (-50% dégâts)"
        return f"🩹 {player.name} est blessé"
    
    def get_description(self):
        return "Blessé"

class DeadState(PlayerState):
    def handle_action(self, player, action):
        if action == "revive":
            player.health = 50
            player.set_state(InjuredState())
            return f"💀 {player.name} est ressuscité!"
        elif action == "attack":
            return f"💀 {player.name} ne peut pas attaquer (mort)"
        return f"💀 {player.name} est mort"
    
    def get_description(self):
        return "Mort"

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self._state = HealthyState()
    
    def set_state(self, state):
        self._state = state
    
    def act(self, action):
        return self._state.handle_action(self, action)
    
    def get_status(self):
        return f"{self.name}: {self._state.get_description()} (PV: {self.health})"

# Utilisation
player = Player("Héros")

print("🎮 Simulation de combat:")
print(player.get_status())

# Série d'actions
actions = ["attack", "take_damage", "attack", "take_damage", "take_damage", "heal", "attack", "take_damage", "take_damage", "revive"]

for action in actions:
    result = player.act(action)
    print(f"Action: {action} -> {result}")
    print(f"État: {player.get_status()}")
    print()
```

---

## Partie 2 : Similitudes, différences et risques de confusion

### 2.1 Strategy vs State

**Similitudes :**
- Les deux patrons utilisent la composition pour déléguer le comportement
- Ils permettent de changer le comportement d'un objet dynamiquement
- Ils évitent les conditions complexes (if/switch)

**Différences :**
- **Strategy** : Le client choisit l'algorithme à utiliser. L'objet context ne change pas de stratégie automatiquement.
- **State** : L'objet change d'état automatiquement selon ses transitions internes. Le client n'a pas besoin de connaître les états.

**Risques de confusion :**
- Confondre le moment où le changement se produit (manuel vs automatique)
- Utiliser State quand on a besoin de Strategy (et vice versa)

**Quand utiliser lequel :**
- **Strategy** : Quand vous voulez que le client choisisse l'algorithme
- **State** : Quand l'objet doit changer de comportement selon son état interne

### 2.2 Décorateur vs Façade vs Adaptateur

**Similitudes :**
- Tous trois sont des patrons structurels
- Ils modifient l'interface d'un objet existant
- Ils permettent de travailler avec des objets sans les modifier directement

**Différences :**
- **Décorateur** : Ajoute des fonctionnalités à un objet existant, enveloppe l'objet original
- **Façade** : Simplifie l'interface d'un sous-système complexe, ne modifie pas les objets existants
- **Adaptateur** : Fait fonctionner ensemble des interfaces incompatibles, traduit les appels

**Risques de confusion :**
- Utiliser Façade au lieu de Décorateur pour ajouter des fonctionnalités
- Confondre Adaptateur et Façade (l'Adaptateur traduit, la Façade simplifie)
- Sur-utiliser le Décorateur au lieu de l'héritage simple

**Quand utiliser lequel :**
- **Décorateur** : Pour ajouter des fonctionnalités dynamiquement
- **Façade** : Pour simplifier l'utilisation d'un système complexe
- **Adaptateur** : Pour faire fonctionner des interfaces incompatibles

### 2.3 Composite vs Décorateur

**Similitudes :**
- Les deux utilisent la composition et la récursion
- Ils permettent de traiter des objets de manière uniforme
- Ils peuvent être imbriqués

**Différences :**
- **Composite** : Structure hiérarchique d'objets (arbre), traite les objets individuels et les groupes de la même façon
- **Décorateur** : Enveloppe un objet pour ajouter des fonctionnalités, un seul objet à la fois

**Risques de confusion :**
- Utiliser Composite pour ajouter des fonctionnalités (au lieu de Décorateur)
- Utiliser Décorateur pour créer des structures hiérarchiques (au lieu de Composite)
- Confondre la structure (arbre vs chaîne)

**Quand utiliser lequel :**
- **Composite** : Pour représenter des structures hiérarchiques (fichiers/dossiers, menus)
- **Décorateur** : Pour ajouter des fonctionnalités à un objet existant

### 2.4 Factory vs Singleton

**Similitudes :**
- Les deux sont des patrons de création
- Ils contrôlent la création d'objets
- Ils peuvent être implémentés comme des méthodes statiques

**Différences :**
- **Factory** : Crée différents types d'objets selon des paramètres, peut créer plusieurs instances
- **Singleton** : Garantit qu'une seule instance d'une classe existe, pas de paramètres de création

**Risques de confusion :**
- Utiliser Singleton quand on a besoin de plusieurs instances
- Utiliser Factory pour garantir une seule instance (au lieu de Singleton)
- Mélanger les responsabilités (création vs unicité)

**Quand utiliser lequel :**
- **Factory** : Pour créer des objets selon des critères, avec possibilité de plusieurs instances
- **Singleton** : Pour garantir une seule instance d'une ressource partagée

---

## Conclusion

Ce guide présente les patrons de conception sous l'angle des problèmes qu'ils résolvent, permettant aux développeurs de choisir rapidement la solution appropriée. La compréhension des similitudes et différences entre patrons évite les confusions courantes et améliore la qualité du code.

Chaque patron a sa place dans l'arsenal du développeur, et le choix dépend du contexte spécifique du problème à résoudre.
