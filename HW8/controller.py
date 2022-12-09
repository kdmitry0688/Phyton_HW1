
import view
import operation

def start():
	opc = view.menu()
	if opc == '1':
		some_str = view.add_employee_console()
		operation.add_employee(some_str[0], some_str[1], some_str[2], some_str[3])
	elif opc == '2':
		operation.view_employee()
	elif opc == '3':
		operation.find_employee()
	else:
		view.error_op()