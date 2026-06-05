\# 실시간 주식 시세 검색 시스템



프로젝트 소개



Docker Compose와 공공데이터포털 API를 활용하여

실시간 주식 시세를 검색할 수 있는 웹 서비스를 구현하였다.



cron을 사용하여 일정 주기로 데이터를 자동 갱신하며,

nginx 웹서버를 통해 웹페이지를 제공한다.






 사용 기술



\* Docker

\* Docker Compose

\* Python

\* nginx

\* HTML / CSS / JavaScript

\* Chart.js

\* 공공데이터포털 API



\---



\# 프로젝트 구조



```text

stock-project

├─ docker-compose.yml

├─ README.md

├─ generator

│  ├─ Dockerfile

│  ├─ update.py

│  └─ crontab

├─ web

│  └─ Dockerfile

└─ html

&#x20;  ├─ index.html

&#x20;  ├─ stock.json

&#x20;  └─ history.json

```



\---



\# 주요 기능



\* 종목명 검색

\* 자동완성 기능

\* 현재 주식 시세 조회

\* 전일 대비 및 등락률 표시

\* Chart.js를 이용한 가격 시각화

\* cron 기반 자동 데이터 갱신

\* nginx 웹 서버를 통한 서비스 제공



\---



\# 실행 방법



\## 1. Docker Desktop 실행



Docker Desktop을 실행한다.



\---



\## 2. 프로젝트 폴더 이동



```bash

cd stock-project

```



\---



\## 3. Docker Compose 실행



```bash

docker compose up --build

```



\---



\## 4. 웹 브라우저 접속



```text

http://localhost:8080

```



\---



\# 데이터 수집 방식



공공데이터포털의 KRX 주식 시세 API를 사용하여

주식 데이터를 JSON 형태로 저장한다.



Python requests 라이브러리를 이용하여 데이터를 수집하며,

cron을 통해 1분마다 update.py를 자동 실행한다.



\---



\# 컨테이너 구성



\## generator 컨테이너



\* Python 기반

\* 공공데이터 API 호출

\* stock.json 생성

\* history.json 생성

\* cron 자동 실행



\## web 컨테이너



\* nginx 기반

\* index.html 서비스

\* JSON 데이터 제공



\---



\# 느낀점



Docker Compose를 활용하여

여러 컨테이너를 동시에 관리하는 방법을 학습할 수 있었고,



공공 API와 웹 서버를 연동하여

실시간 데이터를 제공하는 구조를 이해할 수 있었다.



