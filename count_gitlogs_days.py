# coding: UTF-8
import sys
import datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta
import pandas as pd

# 引数はgitログのパス。複数指定可能。
paths = sys.argv[1:]

def count_log(path):
	with open(path) as f:
		lines = f.readlines()
	def dateparse(l):
		if l.find('Date') == 0:
			return parser.parse(l.replace('Date:   ', ''))
	df = pd.DataFrame(list(filter(lambda d: d, map(dateparse, lines))), columns=['dtm'])
	df['mon'] = df.dtm.map(lambda d: d.strftime('%Y/%m'))
	df['day'] = df.dtm.map(lambda d: d.strftime('%Y/%m/%d'))
	return df.drop_duplicates(['mon', 'day']).groupby('mon').size().reset_index(name='dayscnt')
# 複数ログのカウント結果を集計
smr = pd.concat(map(count_log, paths)).groupby('mon').sum().reset_index()

# 月軸を作る
min_mon = datetime.datetime.strptime(smr.mon.min(), '%Y/%m')
delta = relativedelta(datetime.datetime.now(), min_mon)
mon_cnt = range(delta.years * 12 + delta.months)
mons = pd.DataFrame(
	list(map(lambda i: (min_mon + relativedelta(months=i + 1)).strftime('%Y/%m'), mon_cnt))
	, columns=['mon'])

mons.merge(smr, on='mon', how='left').fillna(0).to_csv('gitlog_dayscnt.csv', index=False)
