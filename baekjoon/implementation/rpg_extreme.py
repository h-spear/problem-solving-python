# https://www.acmicpc.net/problem/17081

import sys
from copy import deepcopy

input = lambda: sys.stdin.readline().rstrip()


class GameEndException(Exception):
    pass


class Messages:
    CONTINUE = "Press any key to continue."
    TURN_PRINT_FORMAT = "Passed Turns : %d"
    KILLED_BY = "YOU HAVE BEEN KILLED BY %s.."
    WIN = "YOU WIN!"


class Position:
    def __init__(self, r, c):
        self.r = r
        self.c = c


class Item:
    pass


class Weapon(Item):
    def __init__(self, attack):
        self.attack = attack


class Armor(Item):
    def __init__(self, defense):
        self.defense = defense


class Accessory(Item):
    class Effect:
        HP_REGENERATION = "HR"
        REINCARNATION = "RE"
        COURAGE = "CO"
        EXPERIENCE = "EX"
        DEXTERITY = "DX"
        HUNTER = "HU"
        CURSED = "CU"

    def __init__(self, effect_code):
        effects = {
            "HR": self.Effect.HP_REGENERATION,
            "RE": self.Effect.REINCARNATION,
            "CO": self.Effect.COURAGE,
            "EX": self.Effect.EXPERIENCE,
            "DX": self.Effect.DEXTERITY,
            "HU": self.Effect.HUNTER,
            "CU": self.Effect.CURSED,
        }
        if effect_code in effects:
            self.effect = effects[effect_code]
        else:
            raise ValueError("Unknown accessory type.")


class Monster:
    def __init__(self, name, attack, defense, hp, exp, is_boss):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.max_hp = hp
        self.exp = exp
        self.is_boss = is_boss

    def decrease_hp(self, hp):
        self.hp = max(0, self.hp - hp)
        return self.hp == 0

    def heal_full_hp(self):
        self.hp = self.max_hp


class Player:
    def __init__(self, position, command):
        self.position = deepcopy(position)
        self.initial_position = deepcopy(position)
        self.max_hp = 20
        self.hp = 20
        self.level = 1
        self.attack = 2
        self.defense = 2
        self.exp = 0
        self.command = command

        self.weapon = None
        self.armor = None
        self.accessories = []
        self.activate_reincarnation = False

    def next_position(self, direction):
        nr, nc = self.position.r, self.position.c
        if direction == "L":
            nc -= 1
        elif direction == "R":
            nc += 1
        elif direction == "U":
            nr -= 1
        elif direction == "D":
            nr += 1
        return Position(nr, nc)

    def move(self, position):
        self.position = deepcopy(position)

    def reincarnation(self):
        self.heal_full_hp()
        self.position = deepcopy(self.initial_position)
        self.activate_reincarnation = False

    def is_alive(self):
        return self.hp > 0

    def increase_hp(self, hp):
        self.hp = min(self.max_hp, self.hp + hp)

    def heal_full_hp(self):
        self.hp = self.max_hp

    def decrease_hp(self, hp):
        self.hp = max(0, self.hp - hp)
        if self.hp == 0 and self.has_accessory(Accessory.Effect.REINCARNATION):
            self.remove_accessory(Accessory.Effect.REINCARNATION)
            self.activate_reincarnation = True
        return self.hp == 0

    def step_spike_trap(self):
        damaged = 5
        if self.has_accessory(Accessory.Effect.DEXTERITY):
            damaged = 1
        died = self.decrease_hp(damaged)
        if died and not self.activate_reincarnation:
            raise GameEndException(Messages.KILLED_BY % "SPIKE TRAP")

    def battle_with(self, monster):
        first_attack = self.has_accessory(Accessory.Effect.COURAGE)
        first_damaged = False
        if monster.is_boss and self.has_accessory(Accessory.Effect.HUNTER):
            first_damaged = True
            self.heal_full_hp()

        while self.hp > 0 and monster.hp > 0:
            attack = max(1, self.get_attack(first_attack) - monster.defense)
            monster_die = monster.decrease_hp(attack)
            if monster_die:
                self.increase_exp(monster.exp)
                if self.has_accessory(Accessory.Effect.HP_REGENERATION):
                    self.increase_hp(3)
                return

            damaged = max(1, monster.attack - self.get_defense())
            if first_damaged:
                damaged = 0
                first_damaged = False

            died = self.decrease_hp(damaged)
            if died:
                if self.activate_reincarnation:
                    monster.heal_full_hp()
                    return
                raise GameEndException(Messages.KILLED_BY % monster.name)

            if first_attack:
                first_attack = False

    def equip_item(self, item):
        if isinstance(item, Weapon):
            self.weapon = item
        elif isinstance(item, Armor):
            self.armor = item
        elif isinstance(item, Accessory):
            if not self.has_accessory(item.effect) and len(self.accessories) < 4:
                self.accessories.append(item)

    def has_accessory(self, effect):
        return any(accessory.effect == effect for accessory in self.accessories)

    def remove_accessory(self, effect):
        self.accessories = [
            accessory for accessory in self.accessories if accessory.effect != effect
        ]

    def increase_exp(self, exp):
        if self.has_accessory(Accessory.Effect.EXPERIENCE):
            exp = int(exp * 1.2)
        self.exp += exp
        if self.exp >= self.level * 5:
            self.level += 1
            self.exp = 0
            self.max_hp += 5
            self.attack += 2
            self.defense += 2
            self.heal_full_hp()

    def get_attack(self, is_first_attack=False):
        attack = self.attack + (self.weapon.attack if self.weapon else 0)
        if is_first_attack and self.has_accessory(Accessory.Effect.COURAGE):
            multiplier = 3 if self.has_accessory(Accessory.Effect.DEXTERITY) else 2
            attack *= multiplier
        return attack

    def get_defense(self):
        return self.defense + (self.armor.defense if self.armor else 0)

    def __str__(self):
        weapon_att = self.weapon.attack if self.weapon else 0
        armor_def = self.armor.defense if self.armor else 0
        return (
            f"LV : {self.level}\n"
            f"HP : {self.hp}/{self.max_hp}\n"
            f"ATT : {self.attack}+{weapon_att}\n"
            f"DEF : {self.defense}+{armor_def}\n"
            f"EXP : {self.exp}/{self.level * 5}"
        )


class Map:
    EMPTY = "."
    SPIKE_TRAP = "^"
    MONSTER = "&"
    BOSS_MONSTER = "M"
    WALL = "#"
    PLAYER = "@"
    ITEM_BOX = "B"

    def __init__(self, n, m, grid, player, monsters, items):
        self.n = n
        self.m = m
        self.grid = grid
        self.player = player
        self.monsters = monsters
        self.items = items

    def get_monster(self, position):
        return self.monsters[position.r][position.c]

    def remove_monster(self, position):
        self.grid[position.r][position.c] = self.EMPTY
        self.monsters[position.r][position.c] = None

    def get_item(self, position):
        return self.items[position.r][position.c]

    def remove_item(self, position):
        self.grid[position.r][position.c] = self.EMPTY
        self.items[position.r][position.c] = None

    def get_value(self, position):
        return self.grid[position.r][position.c]

    def is_wall(self, position):
        return self.grid[position.r][position.c] == self.WALL

    def is_valid(self, position):
        return 0 <= position.r < self.n and 0 <= position.c < self.m

    def __str__(self):
        output = []
        for r in range(self.n):
            row = ""
            for c in range(self.m):
                if (
                    self.player.is_alive()
                    and r == self.player.position.r
                    and c == self.player.position.c
                ):
                    row += self.PLAYER
                else:
                    row += self.grid[r][c]
            output.append(row)
        return "\n".join(output)


class Table:
    def __init__(self):
        self.passed_turns = 0
        self.map = None
        self.player = None
        self.reason = ""

    def simul(self):
        self.passed_turns = 0
        self.reason = Messages.CONTINUE
        try:
            for direction in self.player.command:
                self.passed_turns += 1
                self.turn(direction)
        except GameEndException as e:
            self.reason = str(e)
        return str(self)

    def turn(self, direction):
        next_position = self.player.next_position(direction)
        if not self.map.is_valid(next_position) or self.map.is_wall(next_position):
            next_position = self.player.position

        next = self.map.get_value(next_position)
        catch_boss = False

        if next == Map.SPIKE_TRAP:
            self.player.step_spike_trap()
            if self.player.activate_reincarnation:
                self.player.reincarnation()
                return
        elif next in [Map.MONSTER, Map.BOSS_MONSTER]:
            monster = self.map.get_monster(next_position)
            self.player.battle_with(monster)
            if self.player.activate_reincarnation:
                self.player.reincarnation()
                return
            self.map.remove_monster(next_position)
            if monster.is_boss:
                catch_boss = True
        elif next == Map.ITEM_BOX:
            item = self.map.get_item(next_position)
            self.player.equip_item(item)
            self.map.remove_item(next_position)

        self.player.move(next_position)
        if catch_boss:
            raise GameEndException(Messages.WIN)

    def input(self):

        N, M = map(int, input().split())
        grid = [list(input()) for _ in range(N)]
        player_command = list(input())

        monster_count = 0
        item_count = 0
        player_position = None

        for r in range(N):
            for c in range(M):
                if grid[r][c] in [Map.MONSTER, Map.BOSS_MONSTER]:
                    monster_count += 1
                elif grid[r][c] == Map.ITEM_BOX:
                    item_count += 1
                elif grid[r][c] == Map.PLAYER:
                    player_position = Position(r, c)
                    grid[r][c] = Map.EMPTY

        monsters = [[None for _ in range(M)] for _ in range(N)]
        for _ in range(monster_count):
            splited = input().split()
            r, c = int(splited[0]) - 1, int(splited[1]) - 1
            name = splited[2]
            attack, defense, hp, exp = map(int, splited[3:])
            is_boss = grid[r][c] == Map.BOSS_MONSTER
            monsters[r][c] = Monster(name, attack, defense, hp, exp, is_boss)

        items = [[None for _ in range(M)] for _ in range(N)]
        for _ in range(item_count):
            splited = input().split()
            r, c = int(splited[0]) - 1, int(splited[1]) - 1
            item_type = splited[2]
            if item_type == "W":
                items[r][c] = Weapon(int(splited[3]))
            elif item_type == "A":
                items[r][c] = Armor(int(splited[3]))
            else:
                items[r][c] = Accessory(splited[3])

        self.player = Player(player_position, player_command)
        self.map = Map(N, M, grid, self.player, monsters, items)

    def __str__(self):
        return (
            f"{self.map}\n"
            f"{Messages.TURN_PRINT_FORMAT % self.passed_turns}\n"
            f"{self.player}\n"
            f"{self.reason}"
        )


if __name__ == "__main__":
    table = Table()
    table.input()
    print(table.simul())
