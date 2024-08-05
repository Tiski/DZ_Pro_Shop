from classes.customer import Customer
from classes.admin import Admin
from classes.authentication_service import AuthenticationService

# Пример использования

auth_service = AuthenticationService()

# Регистрация пользователей
print(auth_service.register(Customer, "john_doe", "john@example.com", "password123", "123 Main St"))
print(auth_service.register(Admin, "admin", "admin@example.com", "adminpass", 1))

# Попытка регистрации с существующим именем пользователя
print(auth_service.register(Customer, "john_doe", "john@example.com", "password123", "123 Main St"))

# Аутентификация пользователей
print(auth_service.login("john_doe", "password123"))
print(auth_service.get_current_user())

# Выход из системы
print(auth_service.logout())
print(auth_service.get_current_user())

# Аутентификация администратора
print(auth_service.login("admin", "adminpass"))
print(auth_service.get_current_user())

# Управление пользователями (только для администратора)
Admin.list_users()
Admin.delete_user("john_doe")
Admin.list_users()
