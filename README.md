[A First Look at PyScript: Python in the Web Browser by Bartosz Zaczyński](https://realpython.com/pyscript-python-in-browser/)

# Напишите свое первое «Hello, World!» в PyScript

Самый быстрый способ начать работу с PyScript — создать документ HTML5, 
сохранить его в локальном файле, таком как hello.html, и использовать 
два необходимых файла, размещенных на домашней странице PyScript:

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello, world!</title>
    <!-- PyScript source -->
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
<body>
    <py-script>print('Hello, World!')</py-script>
</body>
</html>
```
Первый файл `pyscript.css` содержит стили по умолчанию для визуальных 
компонентов PyScript, а также заставку загрузчика.

Второй файл `pyscript.js` - это JavaScript, содержащий Python и 
пользовательские элементы, такие как `<py-script>`, которые могут 
выключать в себя код Python.

При такой настройке вам *не нужно* запускать веб-сервер для доступа к 
вашему HTML-контенту. Сохраните документ и откройте его в браузере.

![Привет, мир от PyScript!](img/hello-world.PNG)

Поздравляем! Вы только что создали свое первое приложение PyScript, которое 
будет работать в любом современном веб-браузере, даже на ранних моделях 
Chromebook, без необходимости установки интерпретатора Python. 

Вы можете буквально скопировать свой HTML-файл на флэш-накопитель USB и 
передать его другу, и он сможет запустить ваш код, даже если на его 
компьютере не установлен Python.

# Загрузка среды Python из Интернета

Когда вы открываете HTML-файл в веб-браузере, загрузка занимает несколько 
секунд, прежде чем отобразится `Hello, World!` в окне. PyScript должен 
получить дюжину дополнительных ресурсов из jsDelivr CDN. 

Эти ресурсы составляют среду Pyodide, которая в несжатом виде весит более 
двадцати мегабайт.

К счастью, ваш браузер будет 
[кэшировать большинство](https://pressidium.com/blog/browser-cache-work/) 
этих ресурсов в памяти или на диске, так что в будущем время загрузки будет 
заметно быстрее. Если вы открыли свой HTML-файл хотя бы один раз, то сможете 
работать в **автономном режиме**, не завися от подключения.

Полагаться на CDN для доставки ваших зависимостей, несомненно, удобно, но 
иногда это ненадежно. В прошлом были известны случаи выхода CDN из строя, 
что приводило к перебоям в работе крупных онлайн-компаний. 

Поскольку PyScript находится на передовой, CDN всегда обслуживает последнюю 
альфа-сборку, которая иногда может приводить к критическим изменениям. И наоборот, 
CDN иногда может потребоваться время, чтобы не отставать от GitHub, поэтому он 
может обслуживать устаревший код.

Не лучше ли всегда запрашивать конкретную версию PyScript?

# Скачать PyScript для автономной разработки

Если вы не хотите полагаться на службу хостинга PyScript, вам нужно загрузить все 
файлы, необходимые для запуска Python в браузере, и разместить их самостоятельно. 
В целях разработки вы можете запустить локальный HTTP-сервер, встроенный прямо в 
Python, введя следующую команду в каталоге с вашими файлами для размещения:

```shell
$ python -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

По умолчанию он запускает сервер, прослушивающий HTTP-запросы на всех сетевых интерфейсах, 
включая `localhost` и номер порта `8000`. При необходимости вы можете настроить как адрес, 
так и номер порта с дополнительными аргументами. Это позволит вам получить доступ к вашему 
приложению PyScript, например, по адресу **http://localhost:8000/hello.html**.

Однако, прежде чем вы сможете это сделать, вам необходимо загрузить `pyscript.css`, `pyscript.js` 
и `pyscript.py` в папку, где находится ваш HTML-документ. Для этого вы можете использовать 
инструмент командной строки `Wget` или загрузить файлы вручную:

```shell
$ wget https://pyscript.net/alpha/pyscript.{css,js,py}
```

Это загрузит все три файла за один раз. Вспомогательный модуль Python содержит необходимый 
связующий код для PyScript и Pyodide. Вам нужно скачать, pyscript.py потому что сценарий 
начальной загрузки попытается получить его со своего собственного доменного адреса, 
который будет вашим локальным адресом.

Не забудьте обновить пути CSS и JavaScript в вашем HTML, чтобы они указывали на локальные файлы, 
а не на файлы, размещенные в Интернете:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello, world!</title>
    <!-- PyScript source -->
    <link rel="stylesheet" href="static/css/pyscript.css" />
    <script defer src="static/js/pyscript.js"></script>
</head>
<body>
    <py-script>print('Hello, World!')</py-script>
</body>
</html>
```

Почти всё, но если вы сейчас перейдете в своем браузере на локальный сервер, 
он все равно попытается получить некоторые ресурсы из CDN, а не с вашего 
локального HTTP-сервера. Давайте исправим это.

# Загрузите конкретный выпуск `Pyodide`

Теперь, когда вы заставили PyScript работать в автономном режиме, пришло время 
выполнить аналогичные шаги для `Pyodide`. В первые дни существования PyScript 
URL-адрес с `Pyodide` был жестко запрограммирован, но недавно разработчики 
представили еще один настраиваемый элемент под названием `<py-config>`, который 
позволяет указать URL-адрес с желаемой версией `Pyodide`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello, world!</title>
    <!-- PyScript source -->
    <link rel="stylesheet" href="static/css/pyscript.css" />
    <script defer src="static/js/pyscript.js"></script>
    <py-config>
        - autoclose_loader: true
        - runtimes:
            -
                src: "static/js/pyodide.js"
                name: pyodide-0.20
                lang: python
    </py-config>
</head>
<body>
    <py-script>print('Hello, World!')</py-script>
</body>
</html>
```

Содержимое этого необязательного тега является частью конфигурации 
[YAML](https://realpython.com/python-yaml/). Вы можете использовать атрибут `src`, чтобы 
предоставить либо URL-адрес с конкретной версией `Pyodide`, размещенной в Интернете, 
либо локальный файл, который вы загрузите.

Чтобы получить актуальный список оставшихся файлов, которые ваш браузер будет загружать 
из CDN или загружать из своего кеша, вы можете перейти к инструментам веб-разработки и 
переключиться на вкладку «Сеть» перед обновлением страницы. Однако есть вероятность, 
что в конечном итоге вам потребуются еще несколько файлов, или их имена могут измениться 
в будущем, поэтому проверка сетевого трафика быстро станет неприятной.

Для целей разработки, вероятно, удобнее загрузить все файлы выпуска Pyodide и позже решить, 
какие из них действительно нужны вашему приложению. Итак, если вы не против скачать несколько 
сотен мегабайт, скачайте 
[tar-архив](https://github.com/pyodide/pyodide/releases/download/0.20.0/pyodide-build-0.20.0.tar.bz2) 
релиза с GitHub и распакуйте его в папку вашего приложения `Hello, World!`:

```shell
$ VERSION='0.20.0'
$ TARBALL="pyodide-build-$VERSION.tar.bz2"
$ GITHUB_URL='https://github.com/pyodide/pyodide/releases/download'
$ wget "$GITHUB_URL/$VERSION/$TARBALL"
$ tar -xf "$TARBALL" --strip-components=1 pyodide
```

Пока все идет хорошо, в папке вашего приложения должны быть как минимум эти 
файлы:

```
static
|
├───css
│       pyscript.css
│
└───js
        distutils.tar
        micropip-0.1-py3-none-any.whl
        packages.json
        packaging-21.3-py3-none-any.whl
        pyodide.asm.data
        pyodide.asm.js
        pyodide.asm.wasm
        pyodide.js
        pyodide.js.map
        pyodide_py.tar
        pyparsing-3.0.7-py3-none-any.whl
        pyscript.js
        pyscript.js.map
        pyscript.py
```

Как видите, PyScript — это смесь `Python`, `JavaScript`, `WebAssembly`, `CSS` и `HTML`. 
На практике вы будете выполнять большую часть своего программирования PyScript, используя `Python`.

Подход, который вы выбрали в этом разделе, дает вам гораздо более детальный контроль над версиями 
Pyodide и базового интерпретатора Python. Чтобы проверить, какие версии `Python` доступны через 
`Pyodide`, вы можете посмотреть [журнал изменений](https://pyodide.org/en/stable/project/changelog.html). 
Например, `Pyodide 0.20.0`, используемый в этом руководстве, был создан поверх `CPython 3.10.2`.

Если вы сомневаетесь, вы всегда можете самостоятельно проверить версию `Python`, работающую в 
вашем браузере.

# Проверьте свои версии Pyodide и Python

