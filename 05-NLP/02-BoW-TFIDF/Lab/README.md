# Определение тональности постов про COVID

## Задание

Используем [датасет постов пользователей о коронавирусе](https://www.kaggle.com/datasets/datatattle/covid-19-nlp-text-classification) с сайта Kaggle чтобы натренировать модель определения тональности текста. 

Датасет имеет следующий вид:

UserName | ScreenName | Location | TweetAt | OriginalTweet | Sentiment
---------|------------|----------|---------|---------------|----------
3799 | 48751 | London | 16-03-2020 | @MeNyrbie @Phil_Gahan @Chrisitv https://t.co/i... | Neutral
3800 | 48752 | UK | 16-03-2020 | advice Talk to your neighbours family to excha... | Positive
3801 | 48753 | Vagabonds | 16-03-2020 | Coronavirus Australia: Woolworths to give elde... | Positive

* Используйте представление постов в виде BoW и TF-IDF для построения модели предсказания тональности
* Попробуйте решить задачу как задачу классификации и как задачу регрессии
* Посмотрите, как на финальную точность влияет максимальный объем словаря. Сокращение объема словаря позволяет избавиться от редко-встречаемых слов, которые затрудняют классификацию.

Рекомендация: для открытия датасета используйте следующий код в Pandas:

```
train_df = pd.read_csv("../../../data/Corona_NLP_train.csv.zip",encoding='latin-1')
test_df = pd.read_csv("../../../data/Corona_NLP_test.csv.zip",encoding='latin-1')
```
