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

Чтобы проверить версию `Pyodide`, вам нужна всего одна строка кода. 

Вернитесь в редактор и замените `Hello, World!` код следующим фрагментом:

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
    <py-script>import pyodide_js; print(pyodide_js.version)</py-script>
</body>
</html>
```

Он зависит от `pyodide_js` модуля, который автоматически внедряется в PyScript. 
Вы можете использовать его для доступа к `JavaScript API Pyodide` непосредственно 
из Python, если PyScript не предоставляет собственный уровень абстракции для 
данной функции.

Проверка вашей версии Python в PyScript выглядит так же, как и в стандартном 
интерпретаторе CPython:

```html
<py-script>import sys; print(f"Python {sys.version}")</py-script>
```

Вы импортируете `sys` модуль из стандартной библиотеки для проверки `sys.version`
константы, а затем печатаете его с помощью [f-строки](https://realpython.com/python-f-strings/). 
Когда вы обновляете страницу в веб-браузере и позволяете ей перезагрузиться, она должна создать строку, 
начинающуюся примерно так:

    Python 3.10.2 (main, Apr 9 2022, 20:52:01) [...]

Это то, что вы обычно видите, когда запускаете интерактивный интерпретатор Python 
в командной строке. В этом случае Pyodide не сильно отставал от последней версии 
CPython, которая на момент написания этого руководства была 3.10.4.

Кстати, вы заметили точку с запятой (;) в приведенных выше примерах? В Python 
точка с запятой разделяет несколько операторов, которые появляются в одной строке, 
что может быть полезно при написании однострочного сценария или когда вы ограничены, 
например, [timeit](https://realpython.com/python-timer/#estimating-running-time-with-timeit)
строкой настройки модуля.

Использование точек с запятой в коде Python встречается редко и обычно не одобряется опытными 
питонистами. Однако этот непопулярный символ помогает обойти проблему со **значительным пробелом** 
в Python, который иногда может привести к беспорядку в PyScript. 

В следующем разделе вы узнаете, как работать с **отступами блоков** и форматированием кода Python, 
встроенного в HTML.

# Работа с форматированием кода Python

Когда вы встраиваете фрагмент CSS, JavaScript или даже SVG - изображения в HTML-документ, нет 
риска того, что веб-браузер неправильно интерпретирует связанный с ними код, поскольку все они 
являются примерами языков свободной формы, которые игнорируют лишние пробелы. Вы можете отформатировать 
свой код на этих языках, как вам нравится, например, удалив разрывы строк, без потери информации. Вот 
что делает возможной минификацию JavaScript.

К сожалению, это не так для Python, который следует правилу внешности для своего синтаксиса, где 
учитывается каждый символ пробела. Поскольку PyScript является такой новой технологией, большинство 
современных средств автоматического форматирования кода, скорее всего, сделают неверные предположения 
и уничтожат ваш код Python, содержащийся в `<py-script>` теге, удалив значащие пробелы. Если это 
произойдет, вы можете столкнуться с ошибкой, подобной этой:

```shell
Traceback (most recent call last):
  ...
  File "<exec>", line 2
    print(f"Python {sys.version}")
IndentationError: unexpected indent
```

В этом случае Pyodide не может проанализировать ваш фрагмент кода Python, встроенный в HTML, из-за 
неправильного отступа. Вы увидите это исключение и связанную с ним трассировку в теле документа, а 
также в консоли веб-разработчика.

Но это не все. Если вы объявите строковый литерал в своем коде Python, который выглядит как HTML-тег, 
тогда браузер распознает его как `HTMLUnknownElement` и удалит, оставив внутри только текст. Рассмотрим 
разбор XML в качестве примера:

```html
<py-script>
import xml.etree.ElementTree as ET
ET.fromstring("<person>John Doe</person>")
</py-script>
```

Приведенный выше код использует `ElementTree API` из стандартной библиотеки Python для анализа строки, 
содержащей запись данных о человеке в формате XML. Однако фактический параметр, переданный в функцию, 
будет только `"John Doe"` без окружающих тегов.

Обратите внимание, что с точки зрения веб-браузера `<person>` выглядит как еще один HTML-тег, вложенный 
в `<py-script>` родительский элемент. Чтобы избежать такой двусмысленности, вы можете заменить угловые 
скобки (< и >) их закодированными аналогами, известными как объекты HTML :

```html
<py-script>
import xml.etree.ElementTree as ET
ET.fromstring("&lt;person&gt;John Doe&lt;/person&gt;")
</py-script>
```

Сущность `&lt;` обозначает символ «меньше» `<`, а `&gt;` заменяет символ «больше» `>`. Сущности символов 
позволяют браузерам отображать текст буквально, тогда как в противном случае он интерпретировался бы как 
элементы HTML. Это работает в PyScript, но не решает проблему отступов.

> **_Примечание._** В документах XML вы можете обернуть свое содержимое парой маркеров 
> [символьных данных (CDATA)](https://en.wikipedia.org/wiki/CDATA) в качестве альтернативы использованию 
> сущностей HTML. К сожалению, большинство парсеров HTML игнорируют CDATA.

Если вы играете не только с PyScript, вам обычно лучше извлекать код Python в отдельный файл, а не 
смешивать его с HTML. Вы можете сделать это, указав необязательный `src` атрибут `<py-script>` элемента, 
который похож на стандартный `<script>` тег, предназначенный для JavaScript:

```html
<py-script src="/custom_script.py"></py-script>
```

Это загрузит и немедленно запустит ваш скрипт Python, как только страница будет готова. Если вы хотите 
загрузить пользовательский модуль в среду выполнения PyScript только для того, чтобы сделать его 
доступным для импорта, ознакомьтесь с управлением зависимостями `<py-env>` в следующем разделе.

> **_Примечание._** Из-за [политики совместного использования ресурсов между источниками (CORS)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing), 
> применяемой веб-браузерами, вы не сможете загрузить скрипт Python из внешнего файла, если вы открыли 
> страницу как локальный файл. Вам нужно будет разместить HTML со связанными ресурсами через веб-сервер, 
> такой, как встроенный Python, `http.server` упомянутый ранее.

Вы можете иметь несколько `<py-script>` тегов на своей странице, если они отображаются в файлах страницы 
`<head>` или `<body>`. PyScript поставит их в очередь и запустит последовательно.

Теперь вы знаете, как запустить код Python в браузере с помощью PyScript. Однако для большинства 
практических приложений требуется одна или несколько зависимостей. В следующем разделе вы узнаете, 
как использовать существующие «батареи» Python, сторонние библиотеки, опубликованные в PyPI или где-либо 
еще, и ваши собственные модули Python.

# Управление зависимостями Python в PyScript

До сих пор вы видели пользовательские теги `<py-script>` и `<py-config>`, предоставляемые фреймворком. 
Еще один элемент, который вы часто будете использовать, — это `<py-env>`, который помогает управлять зависимостями 
вашего проекта, подобно `pip` инструменту Python.

## Модули, отсутствующие в стандартной библиотеке Python

Python поставляется с включенными батареями, а это означает, что многие из его модулей стандартной библиотеки уже 
решают распространенные проблемы, с которыми вы можете столкнуться при разработке программного обеспечения. Вы 
обнаружите, что большинство этих модулей доступны в `Pyodide` и `PyScript` «из коробки», что позволяет вам сразу 
импортировать и использовать их. Например, вы видели фрагмент кода, в котором `xml.etree` пакет использовался для 
анализа XML-документа.

Однако есть несколько заметных исключений из-за ограничений веб-браузера и попытки уменьшить размер загружаемого файла. 
Все, что не имеет отношения к среде браузера, было удалено из текущей версии `Pyodide`. В частности, они включают, но 
не ограничиваются следующими модулями и пакетами:

* idlelib
* tkinter
* turtle
* venv

Вы можете проверить полный список [удаленных пакетов](https://pyodide.org/en/stable/usage/wasm-constraints.html#python-standard-library) 
на странице документации Pyodide.

Кроме того, несколько пакетов были сохранены в качестве заполнителей, которые в конечном итоге могут получить 
надлежащую поддержку, когда WebAssembly будет развиваться в будущем. Сегодня их можно импортировать, как и подобные 
модули `urllib.request`, которые от них зависят, но работать они не будут:

* multiprocessing
* threading
* socket

Как правило, вы не можете запускать новые процессы, потоки или открывать низкоуровневые сетевые соединения. При этом 
вы узнаете о некоторых смягчениях позже в этом руководстве.

Как насчет использования внешних библиотек в PyScript, которые вы обычно устанавливаете вместе с pip в свою 
виртуальную среду?

## Сторонние библиотеки в комплекте с `Pyodide`

Pyodide — это побочный проект ныне прекращенного родительского проекта `Iodide`, запущенного Mozilla. Его цель 
состояла в том, чтобы предоставить инструменты для выполнения научных вычислений в веб-браузере аналогично 
`Jupyter Notebooks`, но без необходимости взаимодействия с сервером для запуска кода Python. В результате 
исследователи смогут более легко делиться и повторно использовать свою работу за счет ограниченной вычислительной 
мощности.

Поскольку PyScript является оболочкой Pyodide, вы можете получить доступ к ряду популярных сторонних библиотек, 
которые были скомпилированы для WebAssembly с помощью Pyodide, даже к тем, части которых написаны на C и Fortran.
Например, вы найдете там следующие пакеты:

* [Beautiful Soup](https://realpython.com/beautiful-soup-web-scraper-python/)
* [Bokeh](https://realpython.com/python-data-visualization-bokeh/)
* [Matplotlib](https://realpython.com/python-matplotlib-guide/)
* [NLTK](https://realpython.com/python-nltk-sentiment-analysis/)
* [NumPy](https://realpython.com/numpy-tutorial/)
* [pandas](https://realpython.com/pandas-python-explore-dataset/)
* [Pillow](https://realpython.com/image-processing-with-the-python-pillow-library/)
* [SciPy](https://realpython.com/python-scipy-cluster-optimize/)
* [SQLAlchemy](https://realpython.com/python-sqlite-sqlalchemy/)
* [scikit-learn](https://realpython.com/train-test-split-python-data/)

Фактический список намного длиннее и не ограничивается библиотеками, разработанными исключительно для науки о данных. 
На момент написания этого руководства в комплекте с Pyodide было около сотни библиотек. Вы можете проверить 
официальную документацию Pyodide для получения [полного списка](https://pyodide.org/en/stable/usage/packages-in-pyodide.html) 
или перейти в папку [packages/](https://github.com/pyodide/pyodide/tree/main/packages) в соответствующем репозитории 
GitHub, чтобы увидеть последний статус.

Несмотря на то, что эти внешние библиотеки являются частью выпуска Pyodide, они не загружаются автоматически в вашу 
среду выполнения Python. Помните, что каждый отдельный модуль Python должен загружаться по сети в ваш веб-браузер, 
что требует драгоценного времени и ресурсов. Когда запускается PyScript, в вашей среде есть только самый минимум, 
необходимый для интерпретации кода Python.



Чтобы импортировать модули, которых нет в стандартной библиотеке Python, вы должны явно запросить их, объявив их 
имена в <py-env> элементе:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sine Wave</title>
  <!-- PyScript source -->
    <link rel="stylesheet" href="static/css/pyscript.css" />
    <script defer src="static/js/pyscript.js"></script>
</head>
<body>
    <py-env>
        - matplotlib
        - numpy
    </py-env>
    <py-script>
import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(0, 2 * np.pi, 100)
plt.plot(time, np.sin(time))
plt
    </py-script>
</body>
</html>
```

Элемент `<py-env>` содержит список YAML с именами библиотек для извлечения по запросу. Когда вы посмотрите на вкладку 
«Сеть» в своих инструментах веб-разработки, вы заметите, что браузер загружает NumPy и Matplotlib с сервера CDN или 
вашего локального HTTP-сервера, на котором размещен Pyodide. Он также извлекает несколько транзитивных зависимостей, 
необходимых для Matplotlib, размером более двенадцати мегабайт!

> **_Примечание:_** Вы можете разместить `<py-env>` элемент либо в заголовке, либо в теле документа. Хотя в некоторых 
> примерах, включенных в PyScript, этот пользовательский элемент помещается между заголовком и телом, это не кажется 
> правильным и может работать не во всех веб-браузерах.

Кроме того, вы можете установить зависимости программно в Python, поскольку PyScript предоставляет инструмент 
`micropip` от Pyodide, который представляет собой упрощенную версию `pip`:

```html
<py-script>
# Run this using "asyncio"
async def main():
    await micropip.install(["matplotlib", "numpy"])

await loop.run_until_complete(main())

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.sin(x))
plt
</py-script>
```

> **_Примечание_**. Если слово `asyncio` появляется где-либо в вашем коде, в том числе в комментарии, то PyScript 
> запустит Python асинхронно, используя `.runPythonAsync()` метод Pyodide. В противном случае он вызовет синхронный 
> аналог`.runPython()`, который не позволит вам использовать `await`.

## Pure-Python Wheels загруженные из PyPI

Допустим, вы хотите создать приложение PyScript, которое анализирует XML с помощью библиотеки `untangle`, которая не 
входит в состав Pyodide и не распространяется со стандартной библиотекой. Вы добавляете следующее объявление к 
`<py-env>` элементу и перезагружаете страницу в браузере:

```html
<py-env>
  - untangle
</py-env>
```

Pyodide связывается с PyPI, чтобы получить связанные метаданные JSON, и делает вывод, что библиотека не была создана и 
загружена с ожидаемым форматом wheels Python. Он доступен только в виде исходного дистрибутива (sdist), что может 
потребовать дополнительной компиляции. Неважно, содержит ли библиотека только чистый код Python. В этом случае Pyodide 
ожидает архив wheels, который он может распаковать и сразу начать использовать.

Слегка разочарованный, вы попытаете счастья с другой библиотекой для разбора XML под названием `xmltodict`, которая 
преобразует документы в словари Python, а не в объекты:

```html
<py-env>
  - xmltodict
</py-env>
```

На этот раз метаданные библиотеки указывают, что доступен архив колеса на чистом Python, поэтому Pyodide идет дальше 
и извлекает его. Если бы у библиотеки были свои зависимости, то Pyodide тоже пытался бы их получить. Однако механизм 
разрешения зависимостей, реализованный в `micropip`, крайне примитивен. С этого момента `xmltodict` библиотека 
становится доступной для импорта в ваше приложение PyScript.

Однако, если вы попытаетесь загрузить библиотеку, написанную не на чистом Python, например, бинарный драйвер для базы 
данных PostgreSQL, Pyodide откажется загружать ее в вашу среду выполнения. Даже если бы он был построен как колеса 
Python для разных платформ, ни один из них не подходил бы для `WebAssembly`. Вы можете просмотреть колеса, загруженные
в PyPI для любой данной библиотеки, нажав [Загрузить файлы](https://pypi.org/project/psycopg-binary/#files) на 
соответствующей странице.

> **_Примечание_**: При желании вы можете запросить пакеты с удаленных серверов, отличных от PyPI, указав их 
> URL-адреса в `<py-env>` элементе, если они являются колесами на чистом Python:
> ```html
> <py-env>
>  - http://local-pypi.org:8001/xmltodict-0.13.0-py2.py3-none-any.whl
> </py-env>
> ```
> Сервер, на котором размещаются такие колеса, должен быть настроен на возврат [заголовков CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing), 
> например `Access-Control-Allow-Origin`. В противном случае браузер откажется получать данные из **другого** источника
> (протокол, домен, номер порта) и заблокирует соединение в силу своей политики безопасности.
>
> Кроме того, механизм разрешения зависимостей не будет работать для пользовательских URL-адресов, подобных 
> приведенному выше.

Подводя итог, можно сказать, что сторонняя библиотека, указанная в списке `<py-env>`, должна быть полностью написана 
на Python и распространяться с использованием выбранного формата колеса, если только она еще не была создана для 
WebAssembly и не связана с Pyodide. Получить пользовательскую библиотеку, не являющуюся чистым Python, в PyScript сложно.

## Модули расширения `C`, скомпилированные для `WebAssembly`

Многие библиотеки Python содержат фрагменты кода, написанного на `C` или других языках для повышения производительности 
и использования определенных системных вызовов, недоступных в чистом Python. Есть несколько способов взаимодействия с 
таким кодом, но обычно его заключают в модуль расширения `Python C`, который можно скомпилировать в собственный код 
вашей платформы и динамически загрузить во время выполнения.

Использование компилятора `emscripten` позволяет ориентироваться на `WebAssembly`, а не на конкретную архитектуру 
компьютера и операционную систему. Однако сделать это не так-то просто. Даже если вы знаете, как создать колесо 
Python для среды выполнения `Pyodide`, и вас не пугает этот процесс, `<py-env>` тег PyScript всегда ожидает либо 
колесо на чистом Python, либо пакет, связанный с `Pyodide`.

Чтобы установить колесо, содержащее код `WebAssembly`, вы можете вызвать `loadPackage()` функцию `Pyodide`, используя 
ее интерфейс `Python pyodide_js`, упомянутый ранее. Вы также можете использовать `Pyodide API` напрямую в `JavaScript`, 
но это запустит независимую среду выполнения вместо того, чтобы подключаться к уже созданной PyScript. В результате 
ваш пользовательский модуль с кодом `WebAssembly` не будет виден в PyScript.

Загрузка пользовательских модулей расширения `C` со временем может стать более простой. До тех пор вам лучше всего 
терпеливо ждать, пока `Pyodide` поставит нужную библиотеку. Кроме того, вы можете создать свою собственную среду 
выполнения `Pyodide` из исходного кода с дополнительными кросс-компилируемыми библиотеками. Существует инструмент 
командной строки под названием `pyodide-build`, который автоматизирует некоторые из необходимых шагов.

На данный момент вы можете придерживаться пользовательских модулей Python, написанных вручную.

## Пользовательские модули Python и файлы данных

Вы можете использовать `<py-env>` или `micropip`, чтобы ваши пользовательские модули можно было импортировать в 
приложения PyScript. Предположим, вы создали вспомогательный модуль с именем `waves.py`, который находится в 
подпапке `src/`:

```python
# src/waves.py

import numpy as np

def wave(frequency, amplitude=1, phase=0):
    def _wave(time):
        return amplitude * np.sin(2 * np.pi * frequency * time + phase)

    return _wave
```
Имя вашего модуля использует форму множественного числа, чтобы избежать конфликта с модулем `wave` в стандартной 
библиотеке, которая используется для чтения и записи в формате аудиофайла Waveform (WAV). Ваш модуль определяет 
единственную функцию с именем `wave()`, которая возвращает [замыкание](https://en.wikipedia.org/wiki/Closure_(computer_programming)). 
Внутренняя функция `_wave()`, на которой основано замыкание, использует `NumPy` для генерации чистой синусоиды с 
заданной частотой, амплитудой и фазой.

Прежде чем вы сможете импортировать свой модуль в тег `<py-script>` из встроенного или исходного скрипта, вам 
необходимо загрузить его в свой веб-браузер `<py-env>`, указав специальный атрибут `paths` в YAML:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sine Wave</title>
    <!-- PyScript source -->
    <link rel="stylesheet" href="static/css/pyscript.css" />
    <script defer src="static/js/pyscript.js"></script>
</head>
<body>
    <py-env>
    - matplotlib
    - numpy
    - paths:
        - static/js/src/waves.py
    </py-env>
    <py-script>
import matplotlib.pyplot as plt
import numpy as np
import waves

time = np.linspace(0, 2 * np.pi, 100)
plt.plot(time, waves.wave(440)(time))
plt
    </py-script>
</body>
</html>
```

Стоит отметить, что, хотя вы не можете загрузить каталог в PyScript, вы можете злоупотреблять этим атрибутом
`paths`, чтобы загрузить в него практически любой файл. Сюда входят файлы данных, такие как текстовые файлы CSV или 
двоичная база данных SQLite:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Loading Data</title>
  <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
<body>
  <py-env>
    - paths:
        - data/people.csv
        - data/people.sql
  </py-env>
  <py-script>
with open("people.csv") as file:
    print(file.read())
  </py-script>
  <py-script>
import sqlite3

with sqlite3.connect("people.sql") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM people")
    for row in cursor.fetchall():
        print(row)
  </py-script>
</body>
</html>
```

Обратите внимание, что когда вы извлекаете файлы с помощью `<py-env>`, вы теряете информацию об их исходной структуре 
каталогов, поскольку все файлы оказываются в одном целевом каталоге. Когда вы открываете файл, вы указываете только 
его имя без пути, а это значит, что ваши файлы должны иметь уникальное имя. Позже вы узнаете, как смягчить эту 
проблему, записав в виртуальную файловую систему в Pyodide.

Хорошо. Теперь, когда вы знаете, как перевести свой код Python или чужой код в PyScript, вам следует научиться более 
эффективно работать с фреймворком.

# Эмуляция Python REPL и Jupyter Notebook