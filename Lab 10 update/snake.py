mport psycopg2
from config import load_config
import csv

def collecting_info():
    """Извлекать данные из таблицы поставщиков"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT phonebook.user_id, name, phone_number FROM phonebook ORDER BY user_id")
                rows = cur.fetchall()

                print("The number of parts : ", cur.rowcount)
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def update_info(user_id, name, phone_number):
    """Обновление контакта"""
    update_row_count = 0

    sql = """UPDATE phonebook
             SET name = %s, phone_number = %s
             WHERE user_id = %s"""
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Выполнение SQL-запроса UPDATE
                cur.execute(sql, (name, phone_number, user_id))
                update_row_count = cur.rowcount

            # Подтверждение изменений в базе данных
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return update_row_count


def delete_info(user_id):
    """Удаление контакта"""
    rows_deleted = 0
    sql = 'DELETE FROM phonebook WHERE user_id = %s'
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (user_id,))
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted


def update_or_insert_contact(name, phone_number):
    """Обновление номера телефона существующего контакта или вставка нового контакта"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Проверяем существует ли контакт с таким именем
                cur.execute("SELECT user_id FROM phonebook WHERE name = %s", (name,))
                existing_contact = cur.fetchone()
                if existing_contact:
                    # Если контакт существует, обновляем его номер телефона
                    cur.execute("UPDATE phonebook SET phone_number = %s WHERE name = %s", (phone_number, name))
                else:
                    # Если контакт не существует, вставляем новый контакт
                    cur.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s) RETURNING user_id",
                                (name, phone_number))
                    user_id = cur.fetchone()[0]
                    return user_id  # Возвращаем идентификатор нового пользователя
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def search_records(pattern):
    """Поиск записей по шаблону"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id, name, phone_number FROM phonebook WHERE name LIKE %s OR phone_number LIKE %s",
                            (f'%{pattern}%', f'%{pattern}%'))
                rows = cur.fetchall()

                print("Matching records:")
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def insert_or_update_user(name, phone_number):
    """Вставка нового пользователя по имени и телефону, обновление телефона, если пользователь уже существует"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Проверяем существует ли контакт с таким именем
                cur.execute("SELECT user_id F