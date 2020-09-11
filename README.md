http://127.0.0.1:8000/get_csv?start=...&end=... - скачивает CSV таблицу с приростом публикаций
start и end опциональные GET параметры, являющиеся натуральными числами большими 1900
Примеры:
http://127.0.0.1:8000/get_csv - получить прирост всех публикаций
http://127.0.0.1:8000/get_csv?start=2010 - получить прирост всех публикаций с 2010 года
http://127.0.0.1:8000/get_csv?end=2015 - получить прирост всех публикаций да 2015 года (включительно)
http://127.0.0.1:8000/get_csv?start=2000&end=2020 - получить прирост всех публикаций с 2000 по 2020 год (включительно)
http://127.0.0.1:8000/get_json - возвращает JSON строку в следующем формате:
{Y1: [W1, W2, ..., Wk], ..., Yn: [W1, W2, ..., wK]}
Yi: [W1, W2, ..., Wk] - Wj прирост публикаций в j неделю, Yi года
Т.е. ответ является словарем где каждый ключ - это год, а значение список, индексы которого номера недель, а значения - прирост публикаций
GET параметры start и end аналогичны как в get_csv

Если start или end не являются натуральным числом, большим 1900 - ответ будет "Wrong year."
Если start > end ответ будет "Wrong range."
