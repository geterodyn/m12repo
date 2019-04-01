from django.core.management import BaseCommand
from django.contrib.auth.models import User
from tasks.models import TodoItem

class Command(BaseCommand):
	help = u"Displays login name of user, who has 'num' place in sorted list"
	def add_arguments(self,parser):
		parser.add_argument('--num', dest='num', type=int, default=2)

	def handle(self, *args, **options):
		d_uncompl = {}
		for u in User.objects.all():
			qs_uncompl = TodoItem.objects.filter(owner=u).filter(is_completed=False)
			d_uncompl[u] = len(qs_uncompl)

		num_list = sorted(list(d_uncompl.values()),reverse=True)
		for u in d_uncompl:
			if d_uncompl[u] == num_list[(options['num'] - 1)]:
				print(f"Пользователя на {options['num']} месте в списке зовут {u}")