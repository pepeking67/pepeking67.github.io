트랜스포머 모델을 이해하기 위해서는 어텐션 매커니즘을 이해해야 하고, 이를 위해서 seq2seq 모델에 대한 이해가 선행되어야 한다. 이는 RNN 기반의 자연어 처리 모델 중 번역을 위해 만들어졌다. 트랜스포머를 이해하기 전에 RNN, LSTM, Seq2seq에 대한 설명은 아래에 정리했다.
<page url="https://app.notion.com/p/c490ad69a5f88353a69681076cd5bd88">NLP</page>
<page url="https://app.notion.com/p/35d0ad69a5f88216804181bb2dcac1be">Seq2seq</page>
<empty-block/>
<table_of_contents color="gray"/>
## 개요
트랜스포머 모델은 Attention is All You Need라는 논문의 제목처럼 RNN을 사용하지 않고 전적으로 어텐션 매커니즘에 기반을 둔 모델이다.
시퀀스 간의 복잡한 의존성을 효과적으로 학습하고, 훈련 시간을 단축시키기 위한 모델이다.
RNN을 사용하는 이전 모델들과 달리, 트랜스포머는 병렬 처리가 가능하여 대규모 데이터셋에서 효율적인 처리가 가능하다. 
**Self Attention **매커니즘을 사용하여 자신을 구성하는 부분끼리 연관성을 찾는다.
![](notion-file-block://7520ad69-a5f8-8325-b30f-01383f59ba9b/f30b11ec-26bd-4f66-b33d-1ac191813d15?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
![](notion-file-block://61f0ad69-a5f8-83ea-bf3e-01ce7f1c790c/c033731a-273e-40a7-8f89-376b45432db8?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
위의 그림처럼 트랜스포머는 RNN 기반 Seq2seq와 비슷하게 인코더 디코더 구조를 사용한다. Seq2seq에서는 인코더, 디코더가 각각 하나의 RNN이 t개의 time step을 가지는 구조였다면, 트랜스포머는 RNN을 사용하지 않고 인코더, 디코더가 각각 N개로 구성된다.
### Self Attention
트랜스포머의 핵심 매커니즘으로 자신을 구성하는 부분끼리의 연관성을 찾고자 할 때 사용된다.
<columns>
	<column ratio="50">
		![](notion-file-block://ab20ad69-a5f8-823e-9e4f-813e0329796c/28315448-55f5-490e-b6cf-de7f62d69c11?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
	</column>
	<column ratio="50">
		예를 들어 왼쪽 그림처럼 I = student이기 때문에 이 둘의 연관성이 높은 것을 알 수 있다.
		<empty-block/>
	</column>
</columns>
Self-attention은 다음과 같은 특징을 가진다.
1. 병렬 처리: 각 단어가 다른 단어들과 동시에 상호작용하므로 병렬 처리가 가능하다.
2. 긴 종속성: 멀리 떨어진 단어들 사이의 관계를 쉽게 알 수 있다.
3. 위치 불변성: **positional encoding**을 통해 각 단어의 위치 정보를 사용한다.
기존의 어텐션과 self-attention을 비교하면 다음과 같다.
<table>
<colgroup>
<col width="205">
<col width="205">
<col width="205">
</colgroup>
<tr>
<td></td>
<td>Self-Attention</td>
<td>기존 Attention</td>
</tr>
<tr>
<td>Query</td>
<td>입력 문장의 모든 word vector</td>
<td>t 시점의 디코더의 은닉 상태</td>
</tr>
<tr>
<td>Keys</td>
<td>입력 문장의 모든 word vector</td>
<td>모든 시점의 인코더 은닉 상태들</td>
</tr>
<tr>
<td>Values</td>
<td>입력 문장의 모든 word vector</td>
<td>모든 시점의 인코더 은닉 상태들</td>
</tr>
</table>
Self-Attention(Q,K,V)
Q: 입력 벡터가 다른 단어와 얼마나 관련이 있는지 평가하는 데 사용한다.
K: 쿼리와 상호작용하여 집중(attention)할 단어를 결정한다.
V: 실제로 네트워크가 사용하게 되는 정보이다.
![](notion-file-block://c0f0ad69-a5f8-82c0-b979-81d14701115d/a8cc7fae-d2be-4181-b407-06d3bcd2acf3?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
대략적인 과정은 다음과 같다.
1. 각 입력 단어를 고차원 벡터로 word embedding한다.
2. 이 임베딩 벡터를 Q, K, V로 변환하기 위해 $`W_Q, W_K, W_V`$를 사용한다.
3. 이 둘을 내적하여 Q, K, V 벡터를 얻는다.
이 때 각 가중치 벡터들은 모델의 학습 과정에서 최적화된다.
### Attention value
![](notion-file-block://c990ad69-a5f8-83d0-8a15-816fe1623f6d/7d7e6cec-d5b6-490c-b6e9-b3d2b8cb8e75?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
![](notion-file-block://4f40ad69-a5f8-828a-b41a-81f4799409fe/fcaaf12b-a169-4d68-8049-445627325ae1?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
기존의 attention score와 마찬가지로 Q와 K 벡터를 내적하여 유사도를 측정한다($`QK^T`$).
$$
d_k=\frac{d_\text{model}}{\text{num}\_\text{heads}}
$$
이 때 $`d_\text{model}`$은 입력 문장의 단어 벡터의 차원이고, num_heads는 하이퍼파라미터이다.
num_heads는 병렬로 어텐션을 수행할 때 병렬의 개수를 의미한다.
이 attention score에 softmax 함수를 취하여 attention distribution을 얻고 이를 V와 가중합하여 attention value를 얻는다.
### Multi-head Attention
![](notion-file-block://e780ad69-a5f8-83f3-a885-01967d57e4e5/65d83b33-ca83-4c1e-a191-291712bf2453?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
위에서 attention value를 구할 때 $`d_\text{model}`$ 차원을 가진 단어 벡터를 num_heads로 나눈 차원 $`d_k`$를 가지는 Q, K, V 벡터로 바꾸고 계산했다. 이는 어텐션을 병렬로 사용하기 위함이다.
![](notion-file-block://86b0ad69-a5f8-83ef-b4b9-81dab7d81491/b83af5c9-63bf-4034-9d5d-78730a338cf5?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
이렇게 병렬로 처리도니 attention head는 concatenate한다. 
![](notion-file-block://3c40ad69-a5f8-82bc-a990-810fa036bec8/6b219da7-18fe-46a0-a759-fd20ed1102d9?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
이 행렬은 다시 또 다른 가중치 행렬 $`W^o`$을 곱한다. 결과적으로 행렬의 크기가$`(\text{seq\_len}, d_\text{model})`$이 되는데 이는 인코더에 입력한 문장 행렬과 크기가 같다.
### Padding Mask
문장 행렬을 구성하기 위해 문장의 길이를 맞추기 위해 \<PAD\> 토큰으로 빈 공간을 채우게 되는데 이 토큰을 attention 연산에서 제외(masking)하기 위한 과정이다. Attention score에 \<PAD\> 토큰 자리에 $`-\infty`$를 더해준다. 그러면 소프트맥스 함수를 지나면서 해당 값이 0이 되어 단어 간 유사도를 구할 때 \<PAD\> 토큰이 반영되지 않게 된다.
### Positional encoding
기존에 RNN이 자연어 처리에 유용했던 이유는 단어의 위치에 따라 정보를 순차적으로 입력 받아 처리해서 단어의 위치 정보를 가질 수 있다는 점에 있다. 트랜스포머는 단어를 순차적으로 입력 받지 않기 때문에 다른 방식으로 단어의 위치 정보를 받아야 한다. 그래서 각 단어의 임베딩 벡터에 위치 정보들을 더하여 모델의 입력으로 사용하는데, 이를 positional encoding이라고 한다.
![](notion-file-block://06d0ad69-a5f8-8276-92d0-0172c733944e/592fec85-d75a-43ea-bd36-b6805f91e9a9?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
$$
PE_{(pos,\ 2i)}=sin(pos/10000^{2i/d_{model}})\\PE_{(pos,\ 2i+1)}=cos(pos/10000^{2i/d_{model}})
$$
트랜스포머는 위의 사인, 코사인 함수의 값을 임베딩 벡터에 더해주어 단어의 순서 정보를 준다.
![](notion-file-block://e1c0ad69-a5f8-82c0-861d-01ce3e2bccae/93b0cab1-1838-4e22-9dfb-51cfba7d9ac3?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
pos는 입력 문장에서의 임베딩 벡터의 위치를 나타내며, i는 임베딩 벡터 내의 차원의 인덱스를 의미한다. 수식을 보면 인덱스가 짝수이면 사인, 홀수인 경우에는 코사인 함수의 값을 사용한다. 
### Encoder
![](notion-file-block://7eb0ad69-a5f8-8315-bfdc-813f08efcbc1/ff844edd-73ad-4722-88c7-b77a0e2c268b?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
입력 시퀀스의 각 단어를 고차원 벡터로 임베딩하고, 단어 순서를 반영하기 위해 positional encoding을 수행한다. 이후 각 입력 벡터에 대해 Q, K, V 벡터를 생성하고 self-attention을 수행한다. 이 과정에서 multi-head attention을 수행한다. 마지막으로 fully connected layers로 구성된 신경망을 통해 비선형 변환을 수행한다. 이 때 **residual connection**을 사용하여 모델이 원래 입력을 참조할 수 있게 한다. 정규화 과정은 시퀀스의 정보를 유지하기 위해 layer normalization을 사용한다.
최종적으로 인코더의 출력은 단어 간의 상호 작용, 유사성, 문맥 정보에 대한 정보들을 포함하고 있다.
### Decoder
![](notion-file-block://7200ad69-a5f8-824d-a08c-8130018fa531/b1e8e327-1184-46b5-b9f6-26e42eb4b22d?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
디코더의 input도 인코딩과 마찬가지로 임베딩 벡터로 변환하고 positional encoding을 수행한다. Seq2seq와 같은 RNN 계열의 디코더는 단어를 매 시점마다 순차적으로 입력받기 때문에 현재 시점을 포함한 이전 시점에 대한 단어들만 참고할 수 있지만, 트랜스포머는 문장 전체를 입력받는다. 그래서 이를 방지하기 위해 **masked multi-head self-attention**을 수행한다.
Look-ahead mask를 통해 마스킹이 이루어진다. 이 첫번째 서브층의 self-attention의 다른 점은 attention score에 마스킹을 적용한다는 점이다. 
<columns>
	<column ratio="68.75">
		![](notion-file-block://f070ad69-a5f8-82c7-a6c8-81e58dc68d40/111962ae-abb9-431e-8265-e00e249b423d?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
	</column>
	<column ratio="31.25">
		![](notion-file-block://92d0ad69-a5f8-837f-953c-011a449aba75/c2b143be-17ed-4f4f-8ce2-28c66dd47f99?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
	</column>
</columns>
위와 같이 자신보다 미래에 있는 단어들은 참고하지 못하도록 마스킹한다. 
지금까지 self-attention을 통해 입력 단어 간의 상호 관계, 출력 단어 간의 상호 관계를 계산했다. 이를 기반으로 인코더의 self-attention value와 디코더의 self-attention value를 이용하여 입력과 출려 단어 간의 상호관계를 파악한다. 즉, 기존의 attention을 사용한다.
그림에서 인코더에서 2개, 디코더에서 1개의 화살표가 있는데 이는 Query vector는 디코더, Key, Value vectors는 인코더로부터 얻는 것을 확인할 수 있다. 
이를 통해 얻어진 attention value(= context vector)로 다음 단어를 예측한다. 
이 벡터를 fully connected layer 신경망으로 비선형 변환을 수행한다. 이후 Linear에서 선형 변환을 통해 차원을 줄여서 출력 벡터의 크기를 줄여준다. 이후 소프트맥스 함수를 통해 확률이 가장 높은 단어를 최종적으로 출력한다. 
<empty-block/>