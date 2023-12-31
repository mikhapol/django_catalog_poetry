# Джанго проект с poetry.
>Изучение  джанго на примере продуктов. Есть реализация на тему Блогинга и рассылок.
## в разработке

Для начало работы необходимо:
- создать файл с переменными окружениями
- создать базу с названием упомянутым в файле .env строка POSTGRES_NAME=.
- мигрировать модели через команду 
  - python manage.py migrate
- далее заполнить базу сущестующими фикстурами коммандой: 
  - python manage.py loaddata DATA/all_data.json
- или отдельными приложениями
  - python manage.py loaddata <app_...> DATA/..._data.json
- создание супер юзера
  - python manage.py createsuperuser


## Кнопки
- Верхний ряд
  - Главная - основная страница с продуктами
  - Рассылки и блоги - страница с информацией о рассылках и выводом 3-х блогов
  - Регистрация - регистрация нового пользователя
    - Профиль существующего пользователя
  - Войти - вход существующего пользователя
    - Выйти - выход из аккаунта
  - Администрирование - вход в админку (если ты супер юзер)
- Нижний ряд
  - Рассылки - страница с рассылками
  - Покупатели - страница с пользователями (покупателями)
  - Сообщения - Письма для рассылки
  - Блоги - Все активные блоги (неактивные скрываются)
  - Контакты - Информация о контактах с возможностью отправки данных для обратной связи)
  - На верх страницы - Кнопка для поднятия страницы на вверх

> Виртуальное окружение poetry

### Установлены следующие зависимости [pyproject.toml](pyproject.toml):
- python = "^3.11"
- django = "^4.2.3"
- psycopg2-binary = "^2.9.6"
- pillow = "^10.0.0"
- ipython = "^8.14.0"
- python-dotenv = "^1.0.0"
- pytils = "^0.4.1"
- redis = "^4.6.0"
- django-crontab = "^0.7.1"

### Информация о переменных окружения отображены в файле [.env.sample](.env.sample)

# Условия курсововго проекта по Django

# Сервис Skychimp

## Этап 1. Разработка сервиса

<aside>
📍 Для удержания текущих клиентов зачастую используются вспомогательные или "прогревающие" рассылки для информирования и привлечения.

Вам нужно разработать **сервис управления рассылками, администрирования и получения статистики**.

</aside>

### Описание задач

- Реализуйте интерфейс заполнения рассылок, то есть CRUD механизм для управления рассылками.
- Реализуйте скрипт рассылки, который работает как из командой строки, так и по расписанию.
- Добавьте настройки конфигурации для периодического запуска задачи.

### Сущности системы

- Клиент сервиса:
    - контактный email
    - фио
    - комментарий
- Рассылка (настройки)
    - время рассылки
    - периодичность: раз в день, раз в неделю, раз в месяц
    - статус рассылки (завершена, создана, запущена)
- Сообщение для рассылки
    - тема письма
    - тело письма
- Попытка рассылки
    - дата и время последней попытки
    - статус попытки
    - ответ почтового сервера, если он был

<aside>
ℹ️ **Примечание:**
Не забудьте про связи между сущностями. Вы можете расширять модели для сущностей в произвольном количестве полей, либо добавлять вспомогательные модели.

</aside>

### Логика работы системы

- После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания - должны быть выбраны из справочника все клиенты, которые указаны в настройках рассылки и запущена отправка для всех этих клиентов.
- Если создаётся рассылка с временем старта в будущем - отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя системы.
- По ходу отправки сообщений должна собираться статистика (см. описание сущности "сообщение" и "попытка" выше) по каждому сообщению для последующего формирования отчётов.
- Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы. Нужна корректная обработка подобных ошибок. Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.

<aside>
👨🏻‍💻 **Рекомендации**

- реализовать интерфейс можно с помощью uikit Bootstrap
- для работы с периодическими задачами можно использовать либо crontab задачи в чистом виде, либо изучить дополнительно библиотеку https://pypi.org/project/django-crontab/
</aside>

## Уточнение требований/Комментарии по встрече.
### Сущности системы

1) Клиент сервиса 
2) Рассылка (настройки)
3) Сообщение для рассылки
4)  Логи рассылки
5) Пользователь 

Пользователь создает рассылки, создает клиентов. Пользователь может подключать клиентов к рассылке. 

Клиент - тот кто получит письмо рассылки.

Мы обсуждали что у рассылки может быть много клиентов. Но если еще немного подумать, тут напрашивается связь многие ко многим, так как клиента можно добавить к нескольким рассылкам. Работа с полями Многие-ко-Многим в django. https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/

Рассылка может быть в трех состояниях запущена, создана, завершена, как мы обсуждали, реализовать это удобнее всего  с помощью django choices.

Также вариант с choices подойдет для периодичности рассылки, который может быть раз в день, раз в неделю, раз в месяц.

Работа с choices в django https://docs.djangoproject.com/en/4.2/ref/models/fields/#choices

    class Mailing(models.Model):
         PERIOD_DAILY = 'daily'
         PERIOD_WEEKLY = 'weekly'
         PERIOD_MONTHLY = 'monthly'
    
          PERIODS = (
             (PERIOD_DAILY, 'Ежедневная'),
             (PERIOD_WEEKLY, 'Раз в неделю'),
             (PERIOD_MONTHLY, 'Раз в месяц'),
         )
    
         STATUS_CREATED = 'created'
         STATUS_STARTED = 'started'
         STATUS_DONE = 'done'
         STATUSES = (
             (STATUS_STARTED, 'Запущена'),
             (STATUS_CREATED, 'Создана'),
             (STATUS_DONE, 'Завершена'),
         )
        ...
        time =models.TimeField
        period = models.CharField(max_length=20, choices=PERIODS, ...)
        status = models.CharField(max_length=20, choices=STATUSES, ...)
        ...

Модель письмо и модель рассылки можно объединить. Если не объединять, то связь между объектами будет одно письмо - одна рассылка.

Модель логи рассылки.

Модель рассылки имеет статус. Статус можно реализовать как boolean field. А можно его также реализвовать как choices.

    class MailingLog(models.Model):
        STATUS_OK = 'ok'
        STATUS_FAILED = 'failed'
        STATUSES = (
            (STATUS_OK, 'Успешно'),
            (STATUS_FAILED, 'Ошибка'),
        )
    
        ...
        status = models.CharField(max_length=20, choices=STATUSES, ...)

Лог рассылки должен говорить нам о том, была ли доставка определенной рассылки (письма) для определенного клиента успешной.

В описании курсовой не совсем верно указаны поля.

Актуальные поля
- дата и время последней попытки;
- статус попытки;
- клиент, которму отправлялось письмо
- рассылка, которая отправлялась
- error msg
  - https://yandex.ru/support/mail/mail-clients/others.html#smtpsetting
    - Объект лога рассылки дожен создаваться после отправки письма. Мы должны выбрать всех клиентов рассылки и попробовать отправить им письмо. В django есть встроенная функция send_mail.
  - https://docs.djangoproject.com/en/4.2/topics/email/#send-mail
    - Эта функция возвращает кол-во успешно доставленных сообщений, то есть 0 или 1. Если мы отправляем рассылку, мы выбираем всех клиентов, и для каждого вызываем функцию send_mail, если письмо ушло успешно, функция вернет 1 и мы создаем объект лога со статусом "успешно", если функция вернула 0 тогда мы создаем объект, со статусом "неуспешно".
    - В функции также есть параметр fail_silently, если его значение - False, функция будет выбрасывать ошибку, если что-то пойдет не так.

Кронтаб на windows можно организовать следующим образом.
- https://alimuradov.ru/ispolzovanie-cron-v-podsisteme-linux-wsl-v-windows-10/
- https://www.youtube.com/watch?v=5jaESVKqUs4&t=325s

Полезные материалы:
код практик
- https://github.com/sobrabd/20.1-20.2
- https://github.com/sobrabd/21-cbv
- https://github.com/sobrabd/22.1-22.2
- https://github.com/sobrabd/23.1-23.2

Как получить всех клиентов рассылки
```python
from django.db import models

class Clients(models.Model):
    ...

    def __str__(self):
        return self.title

class MailingSettings(models.Model):
	...
    clients = models.ManyToManyField(Clients)

  
    def __str__(self):
        return self.headline
```

```
>>> m1 = MailingSettings(...)
>>> 
>> m1.clients.all()
```


При отправках почты используем функцию django send_mail
- https://docs.djangoproject.com/en/4.2/topics/email/#send-mail
    - Функция вернет кол-во отправленных писем, то есть 0 или 1.
    - Кроме того у метода есть атрибут file_silently, если он установлен на False, то при попытке отправки будет выбрасываться [`smtplib.SMTPException`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPException "(in Python v3.11)") Эту ошибку можно отлавливать через try/except и на основе этой ошибки создавать объект логов. (поле c сообщением об ошибке)

Отправка по крону. 
- Нужно написать скрипт на рассылку сообщений, который будет раз в период, например раз в 5 минут проверять все рассылки, которые находятся в статусе started, проверять, подошло ли время отправки этой рассылки, и если время подошло (больше текущего) то делать рассылку всем клиентам. Если не подошло пропускать рассылку.
- Так наша рассылка будет уходить с точностью до 5 минут.
- Проверять подошло ли время рассылки можно используя объект логов, для каждого клиента мы можем запросить все его логи, потом выбрать из них самый поздний по дате создания, и проверить, что с даты отправки прошло необходимое кол-во времени. (день, неделя или месяц).
- Если время прошло - отправить письмо. Также необходимо учитывать время рассылки. Если при работе скрипта логов для клиента еще нет, но при этом текщее время меньше времени рассылки, письмо не должно отправляться.

## Этап 2. Доработка сервиса

<aside>
📍 Сервис по управлению рассылками пользуется популярностью и запущенный MVP уже не удовлетворяет потребностям бизнеса. 

Вам нужно доработать сервис, чтобы он стал доступен для использования различными клиентами. А также сделать доработки для развития сервиса в интернете.

</aside>

### Описание задач

- Расширьте модель пользователя для регистрации по почте, а также верификации
- Добавьте интерфейс для входа, регистрации и подтверждения почтового ящика
- Реализуйте ограничение доступа к рассылкам для разных пользователей
- Реализуйте интерфейс менеджера
- Создайте блог для продвижения сервиса

<aside>
ℹ️ **Примечание:**
Используйте для наследования модель `AbstractUser`

</aside>

### Функционал менеджера

- **может** просматривать любые рассылки
- **может** просматривать список пользователей сервиса
- **может** блокировать пользователей сервиса
- **может** отключать рассылки
- **не может** редактировать рассылки
- **не может** управлять списком рассылок
- **не может** изменять рассылки и сообщения

### Функционал пользователя

Весь функционал дублируется из старой версии, но теперь нужно следить за тем, чтобы пользователь не мог случайным образом изменить чужую рассылку и мог работать только со своим списком клиентов и со своим списком рассылок.

## Продвижение

### Блог

Реализуйте приложение для ведения блога. При этом, отдельный интерфейс реализовывать нет необходимости, но настроить административную панель для контент-менеджера необходимо. В сущность блога добавьте следующие поля:

- заголовок
- содержимое статьи
- изображение
- количество просмотров
- дата публикации

### Главная страница

Реализуйте главную страницу в произвольном формате, но обязательно отобразите следующую информацию:

- количество рассылок всего
- количество активных рассылок
- количество уникальных клиентов для рассылок
- 3 случайные статьи из блога

Для блога и главной страницы самостоятельно выберите какие данные необходимо кешировать, а также каким способом необходимо произвести кеширование. 

### Критерии приемки

- [ ]  Интерфейс системы содержит следующие экраны: список рассылок, отчет проведенных рассылок отдельно, создание рассылки, удаление рассылки, создание пользователя, удаление пользователя, редактирование пользователя
- [ ]  Реализована вся требуемая логика поведения
- [ ]  Интерфейс понятен и соответствует базовым требованиям системы
- [ ]  Все интерфейсы, не относящиеся к стандартной админке, для изменения и создания сущностей необходимо реализовать с помощью Django форм
- [ ]  Все настройки прав доступа реализованы верно
- [ ]  Использовано как минимум два типа кеширования
- [ ]  Решение выложено на [github.com](http://github.com/)