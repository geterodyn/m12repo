from django.core.management import BaseCommand
from django.contrib.auth.models import User
from tasks.models import TodoItem

from collections import Counter


class Command(BaseCommand):
	help = u"Displays total tasks number for specified user. 'num' is user number in ordered list"
	def add_arguments(self,parser):
		parser.add_argument('--num', dest='num', type=int, default=5)

	def handle(self, *args, **options):
		c = Counter()
		d_total = []
		for u in User.objects.all():
			for t in u.tasks.all():
				d_total.append(u)
		c.update(d_total)

		_, count = c.most_common(options['num'])[-1]
		print(f"Пользователь на {options['num']} месте списка имеет {count} задач")