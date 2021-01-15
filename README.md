# FaceBattle_image_backend
Face Battle application backend

Docker - Flask REST api end point

<br>

### Build application

---

```buildoutcfg
$ git clone https://github.com/oo1463/FaceBattle_image_backend.git
$ docker built -t oo1463/FaceBattle_image_backend .
``` 

or pull this image from docker hub
```buildoutcfg
$ docker pull oo1463/facebattle_image_backend:latest
```

<br>

### Run Images

---

After images build
```buildoutcfg
$ docker run -d --rm --name facebattle_image -p 8081:8081 oo1463/facebattle_image_backend
```
<br>



<br>

### Stop containers

--- 
```buildoutcfg
$ docker stop facebattle_image
or
$ docker kill facebattle_image

And
$ docker rm facebattle_image
```

<br> 


## API Specification

1. 사용자는 사진 업로드 버튼을 누른다.
    - API 없음
2. 갤러리에서 사진을 선택한다.
    - API 없음
3. 사용자는 제시된 틀에 자신의 얼굴이 보이게끔 사진 크기를 조정한다.
    - 사용자가 제시된 틀에 얼굴을 제대로 맞추지 않는다면, 경고 메세지와 함께 사진 선택 화면으로 돌아간다. (옵션)
    - API 없음
4. 두 번째 이미지 프레임에도 1~3번 과정을 거친다.
    - API 없음
5. Battle 버튼을 누르고 결과를 기다린다.
    - **POST       /images**

        body : **비트맵 데이터 2개.**

        return : 비트맵 데이터 2개 각각에 대한 **정규화된 점수 2개.**

6. 결과 화면이 나타난다.


<br>
<br>
<br>


`[POST]` `/images`



### Request

#### header
`Content-Type: multipart/form-data`

#### body

Parameter | Description
-- | --
image1 | 첫번째 이미지
image2 | 두번째 이미지

### Response

Status Code | 설명
-- | --
200 OK | 성공
400 Bad Request | images의 개수가 잘못됨
500 Internal Server Error | 서버 에러, 문의 필요

### Response body

```
{
  "image1_score": "",
  "image2_score": "",
}
```