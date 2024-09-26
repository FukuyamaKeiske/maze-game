# Игра "Лабиринт"

[![English](https://img.shields.io/badge/lang-English-blue)](README_EN.md)

## Описание

"Лабиринт" - это консольная игра на Python, где игроку предстоит найти выход из случайно сгенерированного лабиринта. Игрок управляет персонажем с помощью клавиш WASD. На прохождение лабиринта отводится одна минута.

## Требования

- Python 3.6 или выше
- Операционная система: Windows, Linux, macOS

## Установка

Для запуска игры необходимо клонировать репозиторий и запустить `main.py`. Вот шаги для установки:

1. Клонировать репозиторий:
   ```shell
   git clone https://github.com/FukuyamaKeiske/maze-game.git
   cd maze-game
   ```

2. (Опционально) Установить зависимости, если они есть:
   ```shell
   pip install -r requirements.txt
   ```

## Запуск игры

Игру можно запустить, выполнив следующую команду в терминале:

```shell
python main.py
```

## Управление

Используйте следующие клавиши для управления персонажем:

- `W` - движение вверх
- `A` - движение влево
- `S` - движение вниз
- `D` - движение вправо

## Правила игры

Игрок должен найти выход из лабиринта за ограниченное время:

- Если игрок находит выход менее чем за минуту, игра выводит время прохождения и предлагает начать заново.
- Если игрок не успевает найти выход за отведенное время, игра предлагает начать заново.

## Скриншоты

![Скриншот](https://github.com/user-attachments/assets/0a1ac12d-2da2-4a57-993c-6c749427c117)
