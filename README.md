# count-gitlogs-days

## Install
```
$ pipenv install --skip-lock -r requirements.txt
```

## Usage
```
$ pipenv run python count_gitlogs_days.py log-sample/gitlog-wara
```
複数指定可能です。
```
$ pipenv run python count_gitlogs_days.py `ls -d log-sample/*`
```

## Output
出力ファイル名/パスは固定です。
```
gitlog_dayscnt.csv
```
グラフ表示するとこんな感じ。
![graph](https://user-images.githubusercontent.com/24839015/71513867-8573d380-28df-11ea-9945-08f9efb20a0d.png)
