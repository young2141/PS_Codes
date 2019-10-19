# Data Structure 

#### HASH

삭제와 검색의 속도가 O(1)이다(collision 없을시) 

**hashing** : hash function거쳐서 key의 인덱스에 넣는다.-->collision발생 
해결책:

1. **open address** : 다른 해시 버킷에 해당자료 삽입 + 캐시 사용 가능. 

   key+ data를 모두 저장한다. 포인트를 안써서 성능향상 (chain불가능)

   * linked list(데이터 적을시 메모리 이득) or red-black tree(데이터 많을시 속도 빠	름) 이용. 
   * simple uniform hash : 1)해쉬값0부터 배열크기 동일한 확률로 나올것
                                   2)해쉬값들은 연관성없이 독립적으로 생성될것

   * division method : %(modular)연산을 이용한 대표적 해쉬 함수. %는 키의 수의 3배가 적당 

2. **sepate chaining**. 더빠름!

   * liner probing: 이미 그 슬롯이 차있다면, 그 위에 슬롯에 저장한다. primary clustering문제점있다. 데이터들이 특정위치에만 밀집하는 형상. slot이 많아지면 탐색시간 엄청 늘어남.
* quadaratic probing : h(k,i) = (k+i^2)%m의 형태. 충돌 일어날 경우 i를 하나씩 올려서 계산한다(초기 = 0) secondary clustering발생. 처음 해쉬값 같을경우 이후 해쉬값도 동일하게 계산되는 현상.
   * double hashing: h1(k) = k%m, h2(k)=k%m2 이면, h(k,i)=(h1(k)+i*h2(k))%m 형식.
   두가지 해쉬함수를 이용한다. secondary clustering 해결! 



#### Deterministing algorithm vs randomized algorithm

라스베가스 알고리즘: 결과는 항상 옳지만 오래걸릴 확률이 있음 ex) quick sort
몬테카를로 알고리즘: 계산을 빠르지만 결과가 틀릴 확률이있음 

#### backtracking

dfs의 경우 무한하게 트리의 깊이가 깊어질 수 있다. 때문에 깊이 제한 설정을 해놓고 넘어가면 부모노드 돌아오게 하는것. 

#### Array vs Linked list

array : random access가 가능하다. 삽입, 삭제가 느리다. shift해줘야하기때문
linked list : 삽입 빠르다. search느리다O(n). 

#### BST 

 탐색속도는 평균 O(log n), worst(skewed) O(n)

**binary heap**: 부모는 자식보다 크다/작다. 완전트리다(왼쪽부터찬다)
heapify = O(log n). insert,delete = O(log n). build heap = O(log n)

**red-black tree**
 root = black. leaf node = black. if parent = red, then childs = black 
 ...자가 균형(self balancing) 이진탐색트리. 일정한 실행 시간을 보장. 

#### DFS 

stack 이용. 한방향으로 쭉. O(V+E)

#### BFS 

queue 이용. 문어발. O(V+E).. 최단경로 

#### minimal spanning tree

1. kurskal : weight 가장 작은 edge부터 놓는다. cycle있으면 넘어감. 
2. prim: 시작점에서 가장 작은 edge들로 이어나간다. 

# C++

#### 포인터 vs 레퍼런스

1. 레퍼런스는 NULL이 없다. 
2. 레퍼런스는 참조대상 변경이 불가능하다.(선언과 동시에 초기화 해야된다)

3. 포인터는 주소값, 레퍼런스는 참조값 그대로 

**cpp virtual**:  실행시간에 함수의 다형성 구성...

#### cpp smart pointer

 new하면 delete해줘야함.(memory leak) sp는 자동으로해준다 
 unique_ptr<int> ptr1(new int(5))이런식.
 shared_ptr<int> ptr1(new(int5)) 하면 참조 횟수 볼 수 있다.

**struct 크기** : 가장 큰 자료형의 배수에 맞춰진다.(int a, char b 있다면 5가 아니라 8)

# JAVA

#### GC

 사용하지 않는 객체 해제해준다.  JVM의 heap 공간에서 발생. 

* weak generational hypothesis : GC도입가능 이유. 
  1. 대부분 객체는 금방 unreachable이된다. 
  2. 오래된 객체에서 젊은 객체로의 참조는 매우	적다
      어떤 객체를 지울까? 더이상 참조 되지 않을때. 
      객체는 (young)eden->survivor1->survivor2->old->permenent 로 옮겨간다 

 GC할 때는 stop-the-world현상이 발생한다.(thread 빼고 잡업 정지) 이 시간을 줄이는게 관건 . 
 GC종류로는 serial, parallel, CMS, G1 등이있다. 

# OS

#### big-endian vs little-endian

big: 큰 단위가 앞으로온다. 0x1234 = 12 34. 디버킹 편하다. TCP에서 이용.
small:작은 단위가 앞으로온다 0x1234 = 34 12. 하위 바이트 별도 계산 필요없다.

#### race condition

 프로세스의 resource 개입 순서에 따라 결과가 달라질수있음
 해결책 : 프로세스 협력 기법 (세마포어, 뮤텍스, 피터슨 알고리즘 등)
 뮤텍스, 세마포어차이는? 크리티컬 섹션 이용이가능이 프로세스 하나면 뮤텍스.

#### process vs thread 
**process** : code, data, stack heap 할당. 장점) 문제생겨도 다른 프로세스 영향x
**thread** : stack,pc register 만 할당. 나머진 공유. 장점) context switching overhead적다.자원 소모 적다 
       단점) 동기화 문제(전역변수 공유)
      +pc regester는 스레드가 어디까지 명령을 수행했는지 나타낸다. 

#### PCB
프로세스에 대한 중요한 정보 저장하고있다. context switch에 이용. 
+왜 스레드의 context siwtch는 프로세스것보다 빠를까? 쓰레드의 cs는 캐시 메모리를 비울 필요가 없기 때문. 

#### 메모리 영역

1. 코드 : 코드 자체가 올라가있다(BIN파일). 
2. 데이터 : 전역변수, static, struct, array. 프로그램 시작때 생성, 종료시 반환
3. 힙 : 프로그래머가 할당. malloc, new ..  
4. 스택 : 프로그램 수행. 할당, 해제 (local, parameter, return, function...). 함수 호출시 해제      끝나면 반환 . 맨끝에서 내려온다 
    추가) bss: 초기화하지 않은 전역변수들. 이름만 저장해놓는다 

#### 프로세스 스케쥴러

job queue(모든 프로세스), ready queue, device queue스케쥴링.
장기스케줄러 : 메모리와 디스크사이 
단기 : cpu와 메모리 사이 
중기: 프로세스를 디스크로

#### CPU 스케줄러

ready queue 대상

1. FCFS : first come, first served. 비선점형(non-premptive). convy effect(효율성 별로)
2. SJF : shortest job first. 대기중 가장 짧은애부터 non-preemtive. starvation
3. SRT: shortest remaining time first. 새로 프로세스 도착때마다 새로 계산. preemptive. starvation. 
4. priority scheduling : 수선순위. 선점형, 비선점형 둘다가능. starvation
5. round robin : time quantum할당. 그 시간동안만돌고, 제일 뒤에가서 줄선다.

#### Critical section 

필수조건

1. mutual exclusion: 임계영역은 한번에 하나만 가능하다. 
2. progress: 하나가 cs사용 끝내면, 다른이가 사용한다. 
3. bounded waiting : 임계구역 요청후 일정 기간내에 요청이 받아들여져야한다.

#### dead lock

필수조건

1. mutual exclusion, 
2. wait for: 다른 프로세스 자원 해제되길 기다리는 프로세스 존재
3. no preemption
4. circular wait : 자원할당 그래프상에서 cycle 존재 . 

#### memory fragmenation

1. swapping : 메모리에 프로세스 올리고, 하드디스크로 내보는 일
2. fragmentation :  
   * 내부단편화 = 프로세스 내부에 남는 공간
   * 외부 단편화 = 프로세스들 사이 남는 공간 
3. paging : 외부단편화 해결. 메모리는 frame이라는 고정크기. frame으로 나눠서 넣는다. 단점. 내부 단편화 늘어남. 

#### 가상 메모리

가상 주소공간 준다. 

#### 요구 페이징
프로세스 한번에 전부 메모리에 올리는게아니라 필요한 부분만 올린다. 페이지 교체과정은 : 디스크에서 페이지 위치 찾고, 빈페이지 프레임 찾고, 프레임 테이블 수정. 
페이 교체 알고리즘

* FIFO: first in , first out 

* optimal page replacement: 가장 오래동안 사용되지 않을 페이지 찾아 교체(이상향)

* LRU: least recently used

* LFU:least requently used 

* MFU: most requently used. 

#### paging vs segmentation 
세그먼테이션: 서로 다른 크기의 논리적단위로 분할. 세그먼트 번호 + 크기로 지정. 외부단편화 발생. 
페이징: 가상메모리를 페이지로 나눈다. (물리는 프레임). 프로그램이 페이지 여러개 할당받아서 나눠 넣는다. 내부단편화 발생. 

#### 커널 메모리
커널은 

1. 데이터사이즈가 작아 내부 파편화가능성이 높으며
2. 하드웨어 장치로 직접 접근하기때문에 물리적으로 연속적이여야한다
    때문에 메모리 풀을 이용한 메모리할당을 한다 
    Buddy system : 메모리를 2의 지수승으로 잘라서 나눠준다. buddy또한 해제되면 다시 합병된다. 
    slab allocation: 메모리를 작게 잘라두고, 요청하는 크기에 맞게 준다. (머가다르지)

# Network

#### OSI 7계층
1. 물리 : bit. 물리적 데이터 연결. 이더넷, 모뎀
2. 데이터 링크: frame. 물리적 전송.에러검출, 흐름제어. MAC,ATM. 무선랜 
3. 네트워크: packet. 발신지로 가장 빨리 전달. 라우터
4. 트랜스포트: segment. 신뢰성있는 데이터 전송. TCP,UDP,RTP. 게이트웨이
5. 세션: data. 장치간 동기화,데이터 분리후 포트연결. SSH. OS
6. 프레젠테이션. data. 데이터를 표현 형태로 변환. ASCII등 변역. JPEG, GIF
7. 어플리케이션. data. 사용자가 네트워크 접근. HTTP, DNS, SMTP, RTSP, DHCP

#### 3-hand-shaking: TCP장치간에 논리적 접속 성립. 
1. client -> server 접속 요청SYN 패킷. client는 closed에서 syn_sent 상태로

2. server -> client 접속 수락 ACK+syn패킷 발송. 서버는 syn_received 상태

3. client -> server ack 보낸다. 연결됨. 

    +) 종료할때는 4way handshake.

   1. client종료 요청
   2. 서버 어플 종료명령ack 
   3. 서버 어플 종료FIN 
   4. client ACK

#### HTTP method
1. GET: 데이터 받아오기 URL뒤에?붙여서 나감. 크기 제한적. 보안 취약 
2. POST: 데이터 만들기. https message body에 담긴다. 
3. PUT: 데이터 전체 업데이트 
4. DELETE: 데이터 지우기 

#### http1.1 vs http2.2 
http1.1:연결당 하나의 요청과 응답. 
http2.2:훨빠르다..ㅇ=요청 병렬로 보냄. 

#### https
s = secure socket. SSL이용. 비대칭키 암호화 방식 이용

#### 대칭키, 비대칭
대칭키 : 파일 암호화, 복호화 모두 같은 키 이용. 키 관리가 중요하다
비대칭키 : 개인키로 암호화, 공개키로 복호화. 역도 성립. 암호화, 복호화 키 다름 = 비대칭키 암호.  ex)RSA

#### GBN(go back and)
슬라딩 윈도우 프로토콜. 맨앞데이터ACK 받으면 슬라이드 옮긴다.
하지만 중간 데이터 로스나면 슬라이드 처음부터 다시 전송 
-->분실 이후 프레임 모두재전송. 구현단순 

#### SR(selective repeate)
받는쪽에도 저장공간이 있다. 받는쪽에서 못받은것만 다시 보내라고한다. 
하지만 문제있다. 재전송시 재전송된 데이터인지, 새로운 데이터인지모름. 
해결하기위해선 windowsize를 순서보다 작게한다..

#### TCP

 reliable, connection control, flow contorl, congestion control. 호스트에서만 작동(중간 라우터x)

#### MQTT

 message queue telemetry transport. 가벼운 메시징 프로토콜.
IoT, 모바일. Broker pattern이용. broker란 중계자가 중계. 

# DATABASE

* DML = data manipulation language.
   select, insert, update, delete. 데이터 조회,변형
* DDL = data definition language
   create, alter, rename, truncate, alter 데이터 구조 관련

#### key 
유일성을 가져야함. null이 있으면안됨(개체 무결성). 조건만족하면 후보키. 이중 기본키 하나 선택. 대체키는 기본키 제외한 후보키. 
슈퍼키: 같은 줄 여러개의 속성들로 만듬. 최소성(어떤 속성 뽑아도 유일)만족 못함. 
외래키: 관계 맺고 있는 테이블의 기본키와 같은 속성일때. 무조건 참조 테이블에있는 값만 입력가능(참조 무결성 조건) 

# Security

#### 중간자 공격

도청이랑 비슷

1. sniffing: 데이터 패킷 캡쳐 
2. packet injection : 일반데이터와 함께 악의적 데이터 주입.
3. session hijacking 
4. SSL stripping. https를 http로 전환시킴
    ->방어: HSTS: http로 입려해도 https로 연결됨. 

#### 랜섬웨어:
사용자 파일 암호화해서 인질로 잡고 금전 요구. 

# ETC

* **라이브러리**: 프로그램 제작시 필요한 기능. 자동차 바퀴
  재사용이 필요한 기능을 만들어 놓은것. Class나 Fcuntion으로 이루어져있다.

* **프레임워크**: 프로그램 기본 구조. 자동차 프레임
  라이브러리 포함. 빠르게 개발 도와줌. ex)spring, django

* **아키텍쳐** : 프로그램 주요 구조 설계. 자동차 도면
  주요 특징 기술적으로 설계. 

* **플랫폼**:프로그램 실행 환경. 자동차 주행환경
  플랫폼 위에 플랫폼 ㅆㄱㄴ. ex) windows, 앱스토어

####  분산처리 시스템. 
하나의 작업에 여러대 machine. message passing interface.
단점: 복잡한 프로그래밍(data sync), 컴퓨터 일부만 고장나도 문제
분산처리, 분사저장

* **spoofing** : ip주소를 포함한 네트워크 정보의 일부를 가짜로 교채해서 보내는것

* **nuke**: 파편또는 유혀하지않은 ICMP를 대량으로 보낸다. 느리게만든다. 
