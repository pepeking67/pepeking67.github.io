<table_of_contents color="gray"/>
## 개요
자연어 처리할 때의 어려움은 다음과 같다.
언어의 중의성, 규칙의 예외, 유연성, 단어 간 유사도
형태소 분석의 규칙 기반 방식에서 통계 기반, 기계학습, RNN, 트랜스포머로 발전한다.
자연어를 처리하기 위한 방식으로 다음과 같이 변환할 수 있다.
1. Character embedding
이는 문자 단위로 텍스트를 임베딩하는 방식이다. 하지만 계산 복잡도가 증가하고, 문맥을 파악하기 어렵다. 하지만 새로운 단어나 희귀 단어가 자주 등장하는 경우에 적합하다.
<empty-block/>
1. Word embedding
이는 단어 단위로 매핑한다. 
![](notion-file-block://33d0ad69-a5f8-833a-862d-8173cf6e01ee/7c540e28-d063-4092-b0fd-e961e1308cde?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
하지만 이는 단어의 다양한 의미의 내포가 어려워지기 때문에 고차원 형태의 벡터를 사용한다.
![](notion-file-block://9870ad69-a5f8-82bb-bdcd-8160cd3ebbd4/72dbb1c7-99c5-4fbc-8964-0b1aab1c2a10?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
이러한 임베딩 벡터를 만들기 위해서는 Word2Vec, GloVe, FastText 등의 사전 훈련이 완료된 임베딩 모델을 사용한다.
<empty-block/>
## RNN
과거의 정보를 사용해서 현재 및 미래의 입력에 대한 예측을 하는 신경망 구조이다.
**순차적인 문맥**을 파악할 수 있다.
![](notion-file-block://74c0ad69-a5f8-824a-96ce-01998a9c1778/652462ac-2b33-46a4-8303-c97d25e1aed1?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
h는 hidden layer이자 memory cell이다.
h는 현재의 state를 기억해 두었다가 다음 순서의 데이터를 처리할 때 이 값을 활용한다.
이전 단계의 출력을 현재 단계의 입력으로 포함하여 데이터 간의 시간적 종속성을 학습하고 유지할 수 있기 때문에 순환 신경망이라고 불린다.
![](notion-file-block://c710ad69-a5f8-8390-ab14-817a6cffa3a9/00e9758d-ea9d-4bc1-a914-f1f804f0e17c?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
x1을 처리할 때 h1을 출력층으로 보낼 뿐만 아니라 다음 입력 x2의 h2의 입력으로도 활용한다.
RNN의 핵심 아이디어 중 하나로 **가중치 공유**가 있다.
<columns>
	<column ratio="25">
		![](notion-file-block://2920ad69-a5f8-8335-9c87-017451a6b828/28136037-d388-4be4-9b90-b720f62b5b6e?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
		<empty-block/>
	</column>
	<column ratio="75">
		![](notion-file-block://0240ad69-a5f8-8301-9a7e-01c7558bebe6/597793df-5a4b-4735-a94c-b1414a9cc4e0?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
	</column>
</columns>
시간 스템마다 동일한 파라미터를 사용한다.
파라미터 수가 감소하여 과적합을 방지하고 일반화 능력을 향상시킬 수 있다.
각 시점에 동일한 가중치를 적용하기 때문에 일관적으로 데이터를 처리할 수 있다. 순차적인 데이터의 구조에 집중하여 시간적 패턴을 효과적으로 학습할 수 있다.
입력 길이와 상관없이 동일한 가중치를 사용하기 때문에 가변 길이를 가지는 데이터를 처리할 수 있다.
구체적인 수식은 다음과 같다.
$$
y_t \ W_{hy}h_t \\ h_t=tanh(W_{hh}h_{t-1}+W_{xh}x_t)
$$
![](notion-file-block://9d40ad69-a5f8-82ae-9e11-01849ebd4ace/cb54237e-e055-4701-8eb9-2ce9aad94b2c?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
위와 같이 4개의 문장을 RNN을 통해 학습시킨다고 생각해본다.
GOAL: I play ?
전통적인 DNN 모델은 각 입력이 독립적으로 처리되어 이전 입력을 고려하지 않기 때문에 문맥을 이해하지 못한다. 그래서 ?에 들어갈 단어를 예측하기 어렵다.
RNN은 I play까지 입력한 데이터를 기반으로 h1을 반영한 h2를 계산했다. 이 h2를 기반으로 ?에 들어갈 가능성이 가장 높은 단어를 선택한다.
![](notion-file-block://3eb0ad69-a5f8-830c-a76c-010159d2b23f/5745523b-8dc0-49a5-83d2-d4e2c7cb81bc?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
RNN의 유현은 위와 같이 크게 3가지로 볼 수 있다.
1. 1-N: 단일 키워드로 문장을 생성하여 이미지 캡셔닝에 사용할 수 있다.
2. N-1: 입력 문서가 스팸 메일인지 판별하는 분류 문제에 활용할 수 있다.
3. N-N: 사용자가 입력하면 대답하는 챗봇, 변역기 등에 사용할 수 있다.
<empty-block/>
RNN은 통해 가변 길이의 데이터에도 유연하게 작돌할 수 있다. 
- RNN의 한계
긴 문장을 처리할 때 gradient 제어가 어렵다는 한계가 있다. 
$`W_{hh}`$를 계속 곱해주기 때문에 gradient vanishing/exploding 문제가 발생할 수 있다.
그리고 gradient vanishing으로 인해 문장이 너무 길어지면 문장의 첫부분 의미가 거의 남아있지 않게 되는 문제가 있다. (Long-term dependency problem)
<empty-block/>
## LSTM
RNN의 한계인 gradient 소실 문제와 장기 의존성 문제를 완화하기 위해 고안된 모델이다.
중요한 정보를 기억하고 불필요한 정보는 없애서(forget) 효과적인 학습이 가능하도록 한다.
![](notion-file-block://4d90ad69-a5f8-8367-b3ba-01cde4237a59/59beb246-bad8-4441-a0b4-53bd3752731c?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
위와 같이 cell을 단위로 연결되는 모델이며, 장기기억을 위한 cell state가 있다.
![](notion-file-block://aa50ad69-a5f8-82a7-980b-8196045d8515/f23e405e-4289-4077-a4e3-8932595c639c?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
노란색 블록들은 신경망 네트워크이다.
![](notion-file-block://ff30ad69-a5f8-8278-a54c-8176c7074c5e/3da0aeeb-bbdd-464c-ae71-1cb8b7b77363?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
cell state는 위와 같이 linear interaction만 적용하면서 정보가 바뀌지 않고 그대로 흐를 수 있게 한다.
LSTM은 이 cell state에 뭔가를 더하거나 뺄 수 있는데 gate라는 구조를 통해 작동한다.
3개의 gate는 다음과 같은 구조를 가진다.
![](notion-file-block://1170ad69-a5f8-8248-b34c-81fa052e5c9f/36e2457f-9153-4189-a126-22b451d369b7?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
시그모이드 레이어를 통해 0\~1 사이의 수를 출력하는데 이 값은 얼마나 정보를 전달해야 하는지를 나타낸다. 0이면 아무 값도 넘기지 않는 것을 의미한다.
### 1. Forget gate
![](notion-file-block://49e0ad69-a5f8-82fb-90b1-0173445cc6ef/2ef9af92-47b3-4d19-baeb-65d69826802c?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
cell state로부터 어떤 정보를 버릴 지를 경정하는 gate이다. 
$`W_f`$ 가중치를 학습해서 얼마나 기억할 지를 결정한다.
### 2. Input gate
![](notion-file-block://55a0ad69-a5f8-82ce-95fa-813a9ad83fd5/9483e06e-ca7f-48ab-82b5-73f0354c39c8?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
새로운 정보 중 어떤 것을 cell state에 저장할 지 결정한다.
기존의 RNN에서 본 것처럼 tanh 층을 지난 출력에 대해 input gate를 통해 얻어진 $`i_t`$ 가중치로 새로 얻어진 데이터를 얼마나 저장할 지 결정한다.
### 3. Output gate
![](notion-file-block://1d00ad69-a5f8-82e8-90eb-01885471f6a6/b89dacd8-7b5e-4802-bffd-99f9f49cb1ec?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
cell state를 바탕으로 가중치를 조절하여 output을 결정한다.
<empty-block/>