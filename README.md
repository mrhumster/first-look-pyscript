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


