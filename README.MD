LunchBot Application v1.1
====================

What is This?
-------------
LunchBot Application은 급식을 기다리는 세명컴퓨터고등학교 학생들을 위한 밴드에 글을 자동으로 포스팅해주는 서비스 입니다. 

How to Use?
-----------
Amazon Web Service의 서버리스 서비스인 Lambda를 사용합니다. 트리거는 EventBridge를 사용하여 Cron 예약 실행합니다. 

-교육청 코드와 학교 코드는 교육청 급식 API 사이트에서 확인 가능합니다.
-AWS Lambda EventBridge Cron 식은 'cron(0 21 ? * SUN-THU *)' 입니다.