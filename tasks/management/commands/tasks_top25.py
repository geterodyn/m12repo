from django.core.management import BaseCommand
from django.contrib.auth.models import User
from tasks.models import TodoItem

from collections import Counter


class Command(BaseCommand):
	help = u"Displays top users with total number of their tasks"
	def add_arguments(self,parser):
		parser.add_argument('--top', dest='top', type=int, default=25)

	def handle(self, *args, **options):
		c = Counter()
		d_total = []
		d_compl = {}
		d_uncompl = {}

		# в общем цикле по всем пользователям выполняем следующие действия:
		for u in User.objects.all():

			# создаем список, состоящий из пользователей. одинаковые имена пользователя встречаются столько раз,
			# сколько у него имеется задач
			for t in u.tasks.all():
				d_total.append(u)

			# формируем словарь соответствия пользователь - количество выполненных задач
			qs_compl = TodoItem.objects.filter(owner=u).filter(is_completed=True)
			d_compl[u] = len(qs_compl)

			# формируем словарь соответствия пользователь - количество невыполненных задач
			qs_uncompl = TodoItem.objects.filter(owner=u).filter(is_completed=False)
			d_uncompl[u] = len(qs_uncompl)
		
		# добавляем список пользователей в Counter. Так будет легко посчитать, сколько раз встречается тот или иной пользователь.
		c.update(d_total)

		for u, count in c.most_common(options['top']):
			print(f"Пользователь {u} имеет {count} задач, из них {d_compl[u]} выполненных и {d_uncompl[u]} невыполненных")
		
		


