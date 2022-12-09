

def menu():
	operation = input('Выберите операцию, которую хотите сделать: \n 1: Записать сотрудника в книгу. \n 2: Посмтреть всю книгу сотрудников. \n 3: Произвести поиск по фамилии. \nВаш выбор: ')
	return operation

def add_employee_console():
	surname = input('Введите фамилию: ')
	name = input('Введите имя: ')
	zp = input('Введите зарплату: ')
	job_title = input('Введите должность: ')
	return surname, name, zp, job_title

def view_employee_console(surname, name, zp, job_title):
	print(f'\nФамилия: {surname} \nИмя: {name} \nЗарплата: {zp} \nДолжность: {job_title}')

def find_employee_console():
	surname = input('Введите искомую фамилию: ')
	return surname

def error_op():
	print('Ошибка!!!')