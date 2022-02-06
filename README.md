- для запуска проекта необходимо иметь установленный python 3.8
- создать виртуальное окружение и установить зависимости из requirements.txt
- создать базу данных
- скопировать и заполнить файл настроек (local.tmlp -> local.py)
- смигрировать базу данных (./manage.py migrate)
- добавить супер пользователя (./manage.py createsuperuser)
- запуск проекта командой `.manage.py runserver 0.0.0.0:8000`
- добавить рабочих, торговые точки (http://127.0.0.1:8000/admin/)
- Дополнительный хэдер для авторизации работника: `phone`
- для получения всех точек работника - GET http://127.0.0.1:8000/
- для записи посещения - POST http://127.0.0.1:8000/
{
    "outlet_id": 1,
    "latitude": 15,
    "longitude": 10
}
