from django.core.management import BaseCommand
from django.contrib.auth.models import User
from tasks.models import TodoItem

class Command(BaseCommand):
	help = u"Displays amount of users who have less than 'value' not completed tasks"
	def add_arguments(self,parser):
		parser.add_argument('--value', dest='value', type=int, default=20)

	def handle(self, *args, **options):
		d_uncompl = {}
		for u in User.objects.all():
			qs_uncompl = TodoItem.objects.filter(owner=u).filter(is_completed=False)
			d_uncompl[u] = len(qs_uncompl)

		uncompl_num = 0
		for n in d_uncompl.values():
			if n < options['value']:
				uncompl_num += 1

		print(f"Количество пользователей, имеющих менее {options['value']} задач - {uncompl_num}")
