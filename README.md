# Django ORM

```bash
$ python manage.py shell # django 프로젝트 환경을 접근할 수 있도록 하기 위해
```

## Create

### 기초설정

- #### Shell

```bash
$ python manage.py shell
```

- #### import model

```python
from articles.models import Article
```



### 데이터를 저장하는 3가지 방법

1. 첫번째 방식

   - ORM 을 쓰는 이유는? => DB를 조작하는 것을 객체지향 프로그래밍 (클래스) 처럼 하기 위해서

     ```python
     article = Article()
     article # <Article: Article object (None)>
     article.title = 'First article'
     article.content = 'Hello, article?'
     article.save()
     article # <Article: Article object (1)>
     ```

2.  두번째 방식

   - 파이썬 keyword 인자 넘기기 방식과 동일

     ```python
     article = Article(title='Second', content='hihi')
     article.save()
     article # <Article: Article object (2)>
     ```

3. 세번쩨 방식

   - create() 를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한번의 스텝

     ```python
     Article.objects.create(title='third', content='Django! Good') # <Article: Article object (3)>
     ```

4. 검증
   full_clean() 함수를 통해 저장하기 전 데이터 검증을 할 수 있다.

   ```python
   >>> article = Article()
   >>> article.title = 'Python is good'
   >>> article.full_clean()
   ```

   

### Read

##### 모든 객체

```python
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (4)>]>
```

##### 객체 표현 변경

```python
# articles/models.py
class Article(models.Model):
    ...
    def __str__(self):
        return f'{self.id}번 글 - {self.title} : {self.content}'
```

##### DB 에 저장된 글 중에서 title이 Second 인 글만 가지고 오기

```python
>>> Article.objects.filter(title='Second')
```

##### DB 에 저장된 글 중에서 title 이 Second 인 글 중에서 첫번째만 가지고 오기

```python
#1
>>> querySet = Article.objects.filter(title='Second')
>>> querySet
<QuerySet [<Article: 2번 글 - Second : hihi>, <Article: 5번 글 - Second
: content>]>
>>> querySet.first()
<Article: 2번 글 - Second : hihi>
        
#2
>>> Article.objects.filter(title='Second').first()
<Article: 2번 글 - Second : hihi>
```

##### DB 에 저장된 글 중에서 pk 가 1인 글만 가지고 오기

- PK 만 get으로 가지고 올 수 있다. => 일반적으로 유니크한 값만 가지고 옴

```python
>>> Article.objects.get(pk=1)
<Article: 1번 글 - First article : Hello, article?>
```

##### 오름차순

```python
>>> articles = Article.objects.order_by('pk')
>>> articles
<QuerySet [<Article: 1번 글 - First article : Hello, article?>, <Article: 2번 글 - Second : hihi>, <Article: 3번 글 - third : Django! Good>, <Article: 4번 글 - title : >, <Article: 5번 글 - Second : content>]>
```

##### 내림차순

```python
>>> articles = Article.objects.order_by('-pk')
>>> articles
<QuerySet [<Article: 5번 글 - Second : content>, <Article: 4번 글 - title : >, <Article: 3번 글 - third : Django! Good>, <Article: 2번 글 - Second : hihi>, <Article: 1번 글 - First article : Hello, article?>]>
```

##### 인덱스 접근이 가능하다

```python
>>> article = articles[2]
>>> article
<Article: 3번 글 - third : Django! Good>
>>> articles = Article.objects.all()[1:3]
>>> articles
<QuerySet [<Article: 2번 글 - Second : hihi>, <Article: 3번 글 - third : Django! Good>]>
```

##### Like - 문자열을 포함하고 있는 값을 가지고 옴

- 장고 ORM은 이름(title)과 필터(contains)를 더블 언더 스코어로 구분합니다. 

  ```python
  >>> articles = Article.objects.filter(title__contains='sec')
  >>> articles
  <QuerySet [<Article: 2번 글 - Second : hihi>, <Article: 5번 글 - Second
  : content>]>
  ```

##### startswith

```python
>>> articles = Article.objects.filter(title__startswith='First')
>>> articles
<QuerySet [<Article: 1번 글 - First article : Hello, article?>]>
```

##### endswith

```python
>>> articles = Article.objects.filter(content__endswith='Good')
>>> articles
<QuerySet [<Article: 3번 글 - third : Django! Good>]>
```

###### Delete

article 인스턴스 호출 후 .delete()

```python
>>> article = Article.objects.get(pk=2)
>>> article.delete()
(1, {'articles.Article': 1})
```

##### update

article 인스턴스 호출 후 값 변경하여 .save() 함수 실행

```python
>>> article = Article.objects.get(pk=4)
>>> article.content
''
>>> article.content = 'new contents'
>>> article.save()
```



Create ReadMe.md



- learn CRUD Operation with Django ORM