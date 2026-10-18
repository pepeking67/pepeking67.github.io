![](notion-file-block://0170ad69-a5f8-82c3-851d-81075f3e5163/ad9ac674-4df7-4a71-8a47-cd0e1d1a0ef4?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=Untitled.png)
- 초기화: 폴더를 깃 저장소로 변경합니다.
- 커밋: 변경된 코드의 이력을 기록합니다.
- 브랜치: 분리 격리된 코드 이력을 기록합니다.
- 병합: 기존 이력과 분리된 이력을 통합합니다.
- 푸시: 로컬 저장소의 이력을 서버로 전송 및 공유합니다.
<empty-block/>
```bash
git 명령어 (옵션)
```
<empty-block/>
## config
<table>
<colgroup>
<col width="292.9791717529297">
<col>
<col width="466.9884338378906">
</colgroup>
<tr>
<td>명령어 </td>
<td>기능</td>
<td>부가설명</td>
</tr>
<tr>
<td>git —version</td>
<td>버전 확인</td>
<td></td>
</tr>
<tr>
<td>git config</td>
<td>환경 설정</td>
<td>config 명령어를 처음 실행하면 새로운 config 파일이 생성됨.</td>
</tr>
<tr>
<td>git config —unset 이메일 주소</td>
<td>환경 파일 삭제</td>
<td></td>
</tr>
<tr>
<td>**로컬 저장소 사용자 등록**</td>
<td></td>
<td></td>
</tr>
<tr>
<td>cd 저장소 폴더</td>
<td></td>
<td></td>
</tr>
<tr>
<td>git config [user.name](http://user.name) “사용자 이름”</td>
<td></td>
<td></td>
</tr>
<tr>
<td>git config [user.email](http://user.email) “이메일”</td>
<td></td>
<td>이를 통해 깃이 개발자를 구분함. 하지만 이는 로컬 저장소를 생성할 때마다 새롭게 설정해야 하는 단점이 있음.</td>
</tr>
<tr>
<td>**글로벌 사용자 등록**</td>
<td></td>
<td></td>
</tr>
<tr>
<td>git config --global [user.name](http://user.name/) "사용자이름"</td>
<td></td>
<td></td>
</tr>
<tr>
<td>git config --global [user.](http://user.name/)email "이메일"</td>
<td></td>
<td></td>
</tr>
<tr>
<td>ls .git</td>
<td>깃 목록 보기</td>
<td></td>
</tr>
<tr>
<td>git config —global core.autocrlf true/input</td>
<td>형식 통일</td>
<td>윈도우는 true, mac은 input<br>맥과 윈도우의 줄바꿈에서 맥은 \\n(line feed)로만, 윈도우는 \\r\\n(carriage-return)도 붙기 때문에 윈도우에서는 저장할 때 \\n으로 저장하고 불러올 때 \\n으로 불러올 수 있도록, 맥에서는 \\n으로만 저장하고 불러올 수 있도록 하여 형식을 통일시킴.</td>
</tr>
</table>
<empty-block/>
### 깃 초기화 및 삭제
<table>
<colgroup>
<col width="293.00000762939453">
<col width="126.00000762939453">
<col width="466.00000762939453">
</colgroup>
<tr>
<td>명령어</td>
<td>기능</td>
<td>부가설명</td>
</tr>
<tr>
<td>ls -al </td>
<td>숨겨진 파일까지</td>
<td></td>
</tr>
<tr>
<td>git init</td>
<td>깃 초기화</td>
<td>초기화 후에는 ls -al 실행 시 .git이라는 숨겨진 파일이 생김</td>
</tr>
<tr>
<td>explorer/open .git</td>
<td>깃 파일 열기</td>
<td>윈도우: explorer 맥: open</td>
</tr>
<tr>
<td>rm -rf .git</td>
<td>깃 파일 삭제</td>
<td></td>
</tr>
<tr>
<td>git status </td>
<td>상태 확인</td>
<td></td>
</tr>
</table>
<empty-block/>
### 단축키
<table>
<colgroup>
<col width="293.00000762939453">
<col width="126.00000762939453">
<col width="466.00000762939453">
</colgroup>
<tr>
<td>명령어</td>
<td>기능</td>
<td>부가설명</td>
</tr>
<tr>
<td>git config --global [alias.st](http://alias.st/) status</td>
<td>status 대신에 st로 설정.</td>
<td></td>
</tr>
</table>
<empty-block/>
### 기초적인 흐름
- workflow
[**working directory**](/p/7040ad69a5f882898eb68144cc0ad9ab?pvs=25#d570ad69a5f883f6b59f017a14725839): 작업하고 있는 공간
**staging area**
**.git directory**: 버전의 히스토리를 가짐
commit을 통해 staging area에 있는 파일을 git으로 옮김
checkout을 통해서 작업 깃에서 작업 공간으로 보낼 수 있음
<empty-block/>
위의 세 가지는 local에 위치한 것이고 이제 remote에 위치한 .git directory에 push를 통해서 local의 .git directory에서 remote .git directory로 옮길 수 있음.
remote git에서 local git으로 옮기기 위해서는 pull을 사용.
<empty-block/>
<empty-block/>
<empty-block/>
### git add
<empty-block/>
**working directory**
- tracked: 깃이 이미 알고 있는 파일 → modified/unmodified 로 나눌 수 있음 → modified된 애만 staging area로 옮김.
- untracked: 새로 만들어진 파일이거나 정보가 없는 파일
<empty-block/>
```bash
#예시

git init

echo hello world! > a.txt #이거는 텍스트 파일 만드는 명령어
echo hello world! > b.txt
echo hello world! > c.txt

git status

>>>
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt
        b.txt
        c.txt

nothing added to commit but untracked files present (use "git add" to track)
# 이 말은 지금 working directory에 untracked된 파일들이 있음.
# git add를 통해서 working directory에 있는 파일을 staging area로 옮길 수가 있음

git add a.txt
git status

>>>
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        b.txt
        c.txt

git add *.txt #이렇게 하면 모든 txt 파일을 옮길 수가 있음
git status

>>>
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt
        new file:   b.txt
        new file:   c.txt

git ellie >> a.txt
git status

>>>
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt
        new file:   b.txt
        new file:   c.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

#modified된 파일이 존재한다고 뜸
#지금 staging area에는 a.txt 파일의 내용은 아직 hello world!임. add할 때의 상태로 남아있음

git add a.txt #다시 add를 하면 staging area에 파일 내용이 ellie로 바뀜.

git rm --cached * #모든 파일을 untracked된 상태로 되돌림, 즉 working directory로 돌려놓음
git status

>>>
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt
        b.txt
        c.txt

nothing added to commit but untracked files present (use "git add" to track)

git add * #모든 파일 add

rm a.txt
git add *
git status

>>>
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt
        new file:   b.txt
        new file:   c.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    a.txt


#이런 식으로 a 파일을 삭제한 후에 add *를 실행하면 위와 같이 뜸
#git add *는 git ignore 파일에 있는 애들도 올려버리기 때문

git add .
git status

>>>
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   b.txt
        new file:   c.txt


# git add .는 git ignore 파일을 제외하고 add 하기 때문에 a 파일이 사라지는 것을 확인할 수 있음


```
<empty-block/>
<empty-block/>
### gitignore
<empty-block/>
```bash
git *.log > .gitignore
git status 

#이렇게 하면 log 파일들이 안 뜨게 됨.

```
<empty-block/>
<empty-block/>
### git status
git status -h로 자세하게 확인 가능
주로 git status -s로 간단하게 확인할 수 있음
<empty-block/>
### 파일 비교 git diff
<empty-block/>
```bash
#working directory와 stating area의 차이를 나타냄
#stagintg area의 c.txt 파일은 hello world이고 working directory에는 hello world/n add  
#이렇게 되어 있음
git diff
>>>
diff --git a/c.txt b/c.txt
index a042389..1a43856 100644
--- a/c.txt
+++ b/c.txt
@@ -1 +1,2 @@
 hello world!
+add

#이런 식으로 나타나게 됨

```
<empty-block/>
### git commit
<empty-block/>
```bash
#staging area에서 .git directory로 옮김

git commit -m "메시지"
git commit -a -m "메시지" # 이렇게 하면 add .안 해도 commit까지 한번에 함

#커밋을 할 때에는 기능 별로 나눠서 commit 하는 게 좋음


```
<empty-block/>
### branch
<empty-block/>
복사본을 만들어서 백업용 코드를 쓰는 느낌임
```bash
git branch 이름 # 브랜치 생성 (최근 commit 복사)
git switch 이름 # 브랜치로 이동
# 이 브랜치에서 똑같이 add, commit 하면 됨
```
<empty-block/>
- 원격
주로 개발자마다 브랜치를 만들어서 나중에 merge를 함
```bash
git branch 브랜치명
git switch 브랜치명
git add .
git commit -m '메시지'

git push origin 브랜치명 # 브랜치를 깃허브에 올림

# 이후에 메인에 브랜치 merge하는 거는 깃허브에서 pull request에서 하면 됨
```
<empty-block/>
### merge
<empty-block/>
![](notion-file-block://e060ad69-a5f8-82a7-bf73-81c0ed2971b2/023449c9-bb90-426d-a965-712d199f0624?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=Untitled.png)
```bash
git switch main # 기준이 되는 브랜치로 이동
git merge 브랜치명 
```
<empty-block/>
![](notion-file-block://4ab0ad69-a5f8-82d3-900b-0110225f9ee0/5234c478-797c-4f4a-bc59-857c21654bb7?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=Untitled.png)
![](notion-file-block://bd90ad69-a5f8-8245-8f53-01a5522c380c/115c1536-bac6-42a1-9002-cc12fc96da55?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=Untitled.png)
<empty-block/>
충돌 해결 후 add . 이랑 commit 해야 함
<empty-block/>
![](notion-file-block://5ad0ad69-a5f8-83e6-9b60-010844f38a05/9d319247-8401-46a9-a6c4-a2bf1aa5f5c4?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=Untitled.png)
![](notion-file-block://f130ad69-a5f8-82ee-87c3-81177848ac93/e4346ed4-6fe1-4ed3-b8bc-868a5daef451?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=Untitled.png)
<empty-block/>
```bash
git branch -d 이름 # merge 완료된 브랜치 삭제
git branch -D 이름 # merge 안된 브랜치 삭제
```
<empty-block/>
![](notion-file-block://87d0ad69-a5f8-82cd-985e-81f2faf4b1d4/86d1aa59-b8fb-4810-93e0-83d63cb70722?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=Untitled.png)
<empty-block/>
rebase 쓰는 이유: git log를 단순화하기 위해서 사용함
conflict가 많이 발생할 수 있다는 단점이 있음
```bash
#rebase를 하기 위해서는 새로운 브랜치로 이동
git rebase 중심브랜치명
#중심브랜치로 이동
git merge 새로운 브랜치명
```
<empty-block/>
![](notion-file-block://8c60ad69-a5f8-8210-a0b9-81c02f73dbd5/4581a952-3f4d-4c75-aa9a-9b0ac851972d?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=Untitled.png)
이렇게 하면 git log 하면 사이드 브랜치의 쓸모없는 내역들이 출력이 안됨
<empty-block/>
주로  안 중요함 브랜치는 squash하고 feature, develop 브랜치는 3-way merge를 함.
<empty-block/>
<empty-block/>
### 복구 방법
<empty-block/>
- 파일 복구
```bash
git restore 파일명 # 최근 commit 상태로 되돌아감
git restore --source 커밋아이디 파일명 # 특정 커밋 시점으로 돌아감
git restore --staged 파일명 # staging 취소
```
<empty-block/>
- commit 자체 복구
```bash
git revert 커밋아이디 # 해당 아이디의 커밋 취소 (여러 개 가능)
git revert HEAD # 최근 commit 취소

```
- reset (참고만)
```bash
git  reset --hard 커밋아이디 # 해당 커밋으로 되돌림
# 이거는 협업할 때는 쓰지 않는 게 좋음
# reset 실행하면 log 기록도 해당 커밋 이후 기록은 사라져서

# soft로 옵션을 설정하면 해당 커밋 이후의 기록들을 staging되어 있음.
```
<empty-block/>
<empty-block/>
### git push
<empty-block/>
원격 repository: git이 파일을 기록해두는 장소
```bash
git init # local repository를 만드는 거임
git branch -M main # 깃허브에서 기본 브랜치를 main으로 하는 걸 강요해서 이름 변경
git add .
git commit -m "메시지"

git push -u 저장소주소 main # 원격 저장소로 옮김
```
<empty-block/>
```bash
# git 변수 문법
git remote add 변수명 주소 # 주소를 변수로 설정
git remote add origin 주소 # 주로 origin을 변수명으로 설정

-u의 의미는 주소를 기억하라는 뜻임
git psuh -u origin main 이후에는 그냥 
git push만 해도 됨
```
<empty-block/>
<empty-block/>
### git pull
<empty-block/>
```bash
git clone 저장소주소 # 원격 저장소 복제

# 팀원이 push를 하려면 협업자로 설정해놔야함
# 원격 저장소에 새로운 게 생기면 push를 못함

git pull 저장소주소 # 원격 저장소 -> 로컬 저장소
# 이렇게 pull을 한 이후에만 push를 할 수 있음

git pull origin 브랜치명 # 특정 브랜치만 가져옴

git pull == git fetch + git merge # 그래서 comflict가 발생할 수 있음

```
<empty-block/>
<empty-block/>
### git flow 개발
branch, merge 깔끔하게 개발 진행하는 전략
<empty-block/>
브랜치 종류
- main
- develop
- feature
- release
- hotfix
![](notion-file-block://a8e0ad69-a5f8-83e1-be4b-01c1135ce5b2/c0497fa5-52c7-4b97-9e88-d7b1dfe63085?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=Untitled.png)
![](notion-file-block://e8f0ad69-a5f8-83fd-9287-0131c807dc17/9da6f3d4-a297-461d-b8a9-2dbfb9099eeb?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=Untitled.png)
main에 바로 코드를 짜지 않고 develop 브랜치를 만들고 또 여기서 기능들을 feature 브랜치로 만듦
이후에 어느정도 되는 거 같으면 바로 main에 합쳐도 되지만 release 브랜치를 만들어서 여러 테스트를 한 후에 메인에 merge.
<empty-block/>
<empty-block/>
### **trunk-based 개발**
![](notion-file-block://5030ad69-a5f8-8369-ab05-0122da813e51/da268a9d-44e0-4d39-8e27-8723206e55ba?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=Untitled.png)
어느정도 안정화되면 메인 소스코드 하나를 기준으로 기능별로 브랜치를 파서 바로 메인에 합침
<empty-block/>
<empty-block/>
### git stash
<empty-block/>
코드를 잠깐 다른 곳에 보관
```bash
git stash # 최근 commit과의 차이점을 전부 보관
git stash list # 목록 조회

# staging안된 파일의 내용은 보관 안됨

git stash save '메모' # 메모도 적을 수 있음

git stash pop # 최근 stash를 가져옴
git stash ddrop 번호 # 특정 stash 제거
git stash clear # 전부 제거
```
주석을 써도 되지만 주석들도 commit할 때 기록에 남기 때문에 commit 전에 stash를 통해 깔끔하게 commit하는 거임
<empty-block/>