## django 2.1.15 정리
 현재 장고가 3버전이 나왔다. 3버전은 나온지 오래 되지 않아서 어떠한 문제가 생길지 모른다. 따라서, 연동에 문제가 없고 에러가 많이 없는 버전2로 학습을 시작해보자.


##### django1
django를 처음시작하는 사람들을 위한, MTV 패턴에 대해 체득하는 과정을 거쳐보자.
https://han-py.tistory.com/32
위의 사이트에 들어가서 순차적으로 진행해보자.

##### django2
 django1에서 배운 내용으로 django2 프로젝트를 생성하고 articles 앱을 생성했다. settings.py까지 수정하고 url 분리를 시작한다.
 그리고 base.html을 활용하는 탬플릿 확장을 적용해 보자.
https://han-py.tistory.com/83
 https://han-py.tistory.com/48


##### django3
장고의 꽃 CRUD에 대한 내용이다.

https://han-py.tistory.com/51
위의 사이트에 들어가서 C R U D 전부 학습할 수 있다.


##### polls
> django의 기초개념을 활용하여 설문조사 서비스를 만들어 보자. (장고 공식사이트 튜토리얼 내용) 


##### bookmark


##### instagram
> 인스타그램의 기능 위주로 게시글, 로그인 등을 구현해 본다.
기본 초기설정 -> models.py -> migrate -> admin.py -> forms.py -> urls.py(include)
-> index.htlm -> base.html -> 첫페이지를 첫 url.(from articlels import views) -> create(url->views) 
-> forms.html -> detail.html


