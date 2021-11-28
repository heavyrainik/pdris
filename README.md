run_nginx:
1. Создаем файл ansible.cfg (базу взял отсюда https://github.com/ansible/ansible/blob/stable-2.9/examples/ansible.cfg)
В 14-й строчке указываем путь к нашему файлу с ip хостов

2. В файл inventory.hosts указываем ip хостов

3. Создаем файлы с переменными подключения к хостам (логин, пароль, путь к папке с логами) в отдельной папке group_vars

4. Шифруем файлы с переменными подключения с помощью команды ansible-vault encrypt с целях безопасности (Пароль: 1). Теперь для запуска воркбука нужен параметр —ask-vault-pass

5. В файле playbook.yml пишем таски
1) Check connection - проверка, что сервера доступны
2) Дальше поднятие веб приложение через nginx взято отсюда https://www.8host.com/blog/kak-razvernut-html-sajt-na-nginx-cherez-ansible/
