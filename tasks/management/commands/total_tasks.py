from django.core.management import BaseCommand
from django.contrib.auth.models import User
from tasks.models import TodoItem

class Command(BaseCommand):
	help = u"Displays total amount of tasks with no args. '--done 1' shows completed task number. '--done 0' shows not completed task number"
	def add_arguments(self,parser):
		parser.add_argument('--done', dest='done', type=int, default=None)

	def handle(self, *args, **options):
		d_total = []
		if options['done'] is None:
			for t in TodoItem.objects.all():
				d_total.append(t)
			print(f'Общее количество задач в базе {len(d_total)}')
		else:
			for t in TodoItem.objects.filter(is_completed=bool(options['done'])):
				d_total.append(t)
			print(f'Количество задач в базе {len(d_total)}')
		# elif options['done'] is False:
		# 	for t in TodoItem.objects.filter(is_completed=False):
		# 		d_total.append(t)
		# 	print(f'Количество невыполненных задач в базе {len(d_total)}')
