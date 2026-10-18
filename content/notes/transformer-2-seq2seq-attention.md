<table_of_contents color="gray"/>
## 개요
Seq2seq는 RNN 기반의 번역 모델이다.
![](notion-file-block://5220ad69-a5f8-8367-bd2e-017a94fcb953/57b83a98-8b83-42ac-bf95-10024ce9103a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
LSTM을 사용해서 “나는 학교에 갔다” 라는 문장을 번역하는 예시이다.
하지만 여기에 문제점이 있다.
1. 나는 학교에 갔다 → I go to school 으로 매핑하는 데 길이의 제약이 있다.
2. 각각의 입력에 대한 출력으로 대응되기 때문에 문맥이 이상할 수 있다. 위의 예시에서 알 수 있듯이 I school go로 매핑되기 때문에 결과가 어색하다.
<empty-block/>
## Seq2seq
전통적인 RNN 기반 모델과 달리 가변 길이의 시쿼스를 처리할 수 있고, 양방향의 문맥 정보를 효과적으로 활용할 수 있기 때문에 더 자연스러운 번역이 가능한 모델이다.
![](notion-file-block://93f0ad69-a5f8-83b3-bb9e-81168dc8cbfd/1bc1b8d5-ed81-4e7a-b3db-61c6304928c3?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
전체적인 구조는 위와 같다. 
인코더를 통해서 입력 시퀀스를 고정된 크기의 context vector로 변환한다.
Context vector는 인코더가 수나적으로 입력 시퀀스를 처리한 후의 마지막 hidden state로, 입력 시퀀스의 단어의 의미와 순서를 요약한 정보로 볼 수 있다.
디코더는 이러한 context vector를 초기 state로 설정하여 출력 시퀀스를 생성한다.
![](notion-file-block://c4f0ad69-a5f8-83ce-9ee1-017f2afed518/d2e728c9-1a15-4f5f-89e1-de2de274fa06?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
입력 문장은 단어 단위로 embedding vector로 변환되어 입력된다.
초기 디토거의 state는 context vector로 설정한다.
<empty-block/>
하지만 이 모델 또한 고정된 크기의 contxt vector로 정보를 압축해야 하기 때문에 정보의 손실이 발생할 수 있다. 이를 해결하기 위해 attention 매커니즘을 사용한다.
<empty-block/>
## Attention
Context vector를 사용하는 대신에 디코덩서 출력 단어를 예측하는 time step마다 인코더의 모든 hidden state를 참고한다. 이 때 모든 입력 토큰을 동일한 비율로 참고하지 않고 예측해야 할 단어와 연관이 있는 단어에 더 큰 가중치를 부여한다.
### 어텐션 함수
![](notion-file-block://b3e0ad69-a5f8-830b-a3b4-81a9f9a0e329/4be33656-ff20-4d44-b759-602dafcbf782?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
$$
\text{Attention}(Q,K,V)=\text{Attention Value}
$$
Query: t 시점의 디코더 셀에서의 hidden state
Keys: 모든 시점의 인코더 셀의 hidden state
Values: 모든 시점의 인코더 셀의 hidden state
### 전체적인 구조
![](notion-file-block://1ad0ad69-a5f8-8222-9387-815271e66257/7b7e6308-a8d8-4235-abc9-f857772f72d9?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
디코더에서 현재 예측해야 하는 단어에 대해 인토더에 쿼리를 보낸다.
인코더는 쿼리에 대해 모든 키와 유사도를 각각 수한다.
유사도를 각 키와 매칭된 value에 반영한다.
이 value를 모두 취합하여 attention value로 디코더에 전달한다.
### 1. Attention score
![](notion-file-block://7560ad69-a5f8-8301-ae67-81563cb152eb/10ca16f4-dc6b-4645-baf7-98d977bfd410?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
![](notion-file-block://7630ad69-a5f8-834b-815e-811d11e8e857/4e8040a0-d4de-4144-8e3f-fa9d989064d5?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
현재 디코더의 hidden state를 인코더의 모든 hidden state에 대해서 유사도를 계산하는 과정이다.
Attention score: 현재 디코더의 시점 t의 단어를 예측하기 위해 인코더의 모든 key(=hidden state) 각각이 디코더의 현 시점의 은식 상태($`s_t`$)와 얼마나 유사한 지 판단하는 값이다.
<columns>
	<column ratio="50">
		![](notion-file-block://6510ad69-a5f8-8345-af63-010a78c24013/2035dbf7-9a78-4161-8dad-f746fd76e3c0?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
	</column>
	<column ratio="50">
		Attention score는 왼쪽 그림과 같이 구한다. 즉, 쿼리를 키들과 내적한다.
	</column>
</columns>
### 2. Attention distribution
![](notion-file-block://3460ad69-a5f8-8342-a1ed-012cba5702d0/9bcb015b-2ac6-45b4-a8d7-984983adcb51?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
![](notion-file-block://4fd0ad69-a5f8-83bc-af5a-01c97d40a346/542e00e5-dac0-4853-879b-9279a31412d1?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
Attention score에 softmax 함수를 적용하여 Attention 분포를 얻는다.
이 분포의 값들을 Attention weight라고 한다.
### 3. Attention value
![](notion-file-block://9600ad69-a5f8-8340-9d2d-0182e401c965/565ccb02-6e54-4b4e-9517-ce96e0285e77?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
![](notion-file-block://83d0ad69-a5f8-8252-a936-01f8c8ef5234/a36c4e1d-f565-461a-b962-2482706fb216?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
Attention value: 인코더의 각 은닉 상태와 Attention 가중치를 가중합시킨다.
Attention value는 인코더의 문맥 정보를 포함하고 있기 때문에 context vector의 역할을 한다.
![](notion-file-block://1370ad69-a5f8-8327-a318-815e2b922ad8/e70104a1-5b6e-4bf1-810a-65beea34cdc3?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
계산된 Attention value $`a_t`$를 현재 디코더의 hidden state $`s_t`$와 결합한다.
<empty-block/>