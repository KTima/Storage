Система для учета склада

Проект реализован на языке Python(Django)


функицонал:
Проект с подключением бд производства и отображение всех таблиц в отдельных вкладках.
Предусмотрено для каждой записи: обновление, удаление. А также для таблиц кнопка добавление

  Функционал закупки сырья:
    По введеным данным пользователем(id сырья, количество, сумма). Клиент проверяет есть ли такая сумма в бюджете, если нет, выдает
    сообщение иначе формирует команду. Клиент формирует команду для уменьшения бюджета и добавление количества и суммы сырья на складе

  Функционал продажи продукции:
    После того как пользователем введет вид продукта и его количество. Клиент формирует команду для проверки наличия такого количества
    продуктов если нет выдается сообщение, иначе в таблицу бюджет добваляется поле указывающее процент при продаже.
    Формируется команда для вычисления цены продажи: себестоимость + процент и показывается в этом представлениее. После нажатия кнопки,
    команда изменяет склад продукта и бюджет 
