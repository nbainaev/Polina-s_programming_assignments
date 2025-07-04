# Репозиторий с заданиями по программированию

Этот репозиторий содержит учебные задания по программированию. Ниже приведены инструкции по работе с репозиторием.

## Начальная настройка

### 1. Установка необходимых программ

Перед началом работы убедитесь, что у вас установлены:
- [Git](https://git-scm.com/downloads)
- [Visual Studio Code](https://code.visualstudio.com/)
#### Как проверить, что git установлен
Нужно прописать в консоли VsCode (открывается с помощью Ctrl + j) команду ```git``` или `git version`. Если выдастся какой-то результат, то git у вас установлен.
### 2. Клонирование репозитория

1. Откройте терминал в VSCode (`Ctrl+`j` или через меню View > Terminal`)
2. Выполните команду:
   ```bash
   git clone https://github.com/nbainaev/Polina-s_programming_assignments.git
   ```
3. Перейдите в папку репозитория:
   ```bash
   cd Polina-s_programming_assignments
   ```

## Работа с репозиторием

### Получение обновлений

Когда я добавляю новые задания, чтобы получить их:

1. Откройте папку репозитория в VSCode
2. Откройте терминал (`Ctrl+j`)
3. Выполните команду:
   ```bash
   git pull origin main
   ```
   (или `git pull origin master` если используется ветка master)

### Добавление обновлений в репозиторий
Если вы сделали/доделали задание или просто что-то поменяли в решении и хотите их отправить в репозиторий,
следуйте инструкции:
1. Для добавления измененных файлов выполните команду:
   ```bash
   git add .
   ```
   Данная команда добавит все измененные файлы.
   Если же вы не хотите добавлять все файлы, то вместо точки нужно указать путь к файлу (или к файлам,
   если нужно несколько файлов, пути к разным файлам разделять пробелом)
   Пример:
   1. ```git add solutions\my_file.py ``` добавит файл my_file.py из папки solutions
   2. ```git add solutions\my_file.py  solutions\homework_1\task1.py``` добавит кроме файлы my_file.py
      еще и фал task1.py из папки solutions\homework_1
2. Для фиксирования изменений нужно выполнить команду:
   ```bash
   git commit -m "Здесь пишется поясление к изменениям (Например, добавлен файл my_file.py)"
   ```
   Такие изменения называются коммитами (от слова *commit* - совершать, фиксировать)
3. Для того, чтобы отправить зафиксированные изменения в репозиторий, нужно ввести команду:
   ```
   git push -u origin main
   ```
   Работа ведется только в векте ```main```
   
### Рекомендуемый рабочий процесс

1. Перед началом работы всегда выполняйте `git pull` чтобы получить свежие задания
2. Для добавления обновлений следуйте инструкции выше
3. Не изменяйте оригинальные файлы заданий

## Дополнительные команды Git

Если нужно проверить состояние репозитория:
```bash
git status
```

Если нужно посмотреть историю изменений:
```bash
git log
```

## Полезные ссылки

- [Официальная документация Git](https://git-scm.com/doc)
- [Git для начинающих](https://githowto.com/ru)
- [Работа с Git в VSCode](https://code.visualstudio.com/docs/editor/versioncontrol)
