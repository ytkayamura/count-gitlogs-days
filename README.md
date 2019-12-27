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
$ pipenv run python count_gitlogs_days.py `ls log-sample/*`
```

## Output
出力ファイル名/パスは固定です。
```
gitlog_dayscnt.csv
```
