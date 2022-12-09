import csv
import view
import log

def add_employee(surname, name, zp, job_title):
	add = [surname, name, zp, job_title]
	with open('book.csv', 'a', encoding='utf-8') as file:
		writer = csv.writer(file, delimiter=';', lineterminator='\n')
		writer.writerow(add)
	log.log_record('Добавление нового сотрудника', add)

def view_employee():
	with open('book.csv', 'r', encoding='utf-8') as file:
		conclusion = csv.reader(file, delimiter=';')
		for row in conclusion:
			view.view_employee_console(row[0], row[1], row[2], row[3])
	log.log_record('Просмотр всех сотрудников')

def find_employee():
	find_surname = view.find_employee_console()
	with open('book.csv', 'r', encoding='utf-8') as file:
		conclusion = csv.reader(file, delimiter=';')
		for row in conclusion:
			if find_surname in row:
				view.view_employee_console(row[0], row[1], row[2], row[3])
	log.log_record('Поиск сотрудника с фамилией', find_surname)