import datetime

def log_record(op, description = ''):
	with open('log.txt', 'a', encoding='utf-8') as file:
		file.write(f'{op} {description} {datetime.datetime.now()} \n')