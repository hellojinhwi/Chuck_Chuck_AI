# 척척약사란?
### -> 22000여개의 알약 정보를 담았고, 63개의 알약을 Mask-RCNN으로 영상인식하여 어떤 약인지 분류하는 반응형 웹 사이트입니다.

**1. Getting Started** <br>
  - 개인 로컬 PC에서 test해보는 방법
    - springboot 서버(8000)와 tornado 서버(5000), elasticsearch(9200) 서버가 동시에 켜져있어야합니다. <br>
    - 학습된 가중치파일(h5, json)은 thdtlcks369@gmail.com으로 메일 주시면 보내드리겠습니다 ^^<br>
    - cmd 콘솔에 pip install -r requirements.txt로 필요한 라이브러리를 설치해주세요.
    - 기능 구현 시에 GOOGLE에서 제공하는 API 키 발급 필수 
    - https://cloud.google.com/text-to-speech/docs/?hl=ko (GOOGLE 공식문서 참조)

**2. 개발기간 & 개발배경 & Insight** <br>
  * 개발기간 : _19.12.10 ~ 20.01.14_ <br>
  * 개발배경 : 의약품에 대한 정보가 필요할 때, 아주 간편하게 식별 검색과 이미지 검색, 읽어주기 기능을 제공하는 웹사이트입니다.<br>
  * Insight : Mask-RCNN으로 사진이나 영상의 여러 알약을 동시에 인식할 수 있으므로, 컴퓨터 비전과 하드웨어 구축을 통하여 의약품 자동분류기를 제작할 수 있을것입니다.

**4. Architecture** <br>
  * Spring MVC Pattern
  * Tornado Web Framework
  * Pills_Mask_RCNN ( hardly based on matterport's Mask-RCNN & Resnet101 )
  * Elasticsearch
  
**5. Skill Set** <br>
  * Front-end : Javascript, HTML, CSS, Bootstrap, Axios    
  * Back-end : SpringBoot,  Google Cloud Platform  
  * DB : ElasticSearch, Kibana (v7.1.1) 
  * DL server : Tornado, TensorFlow v1.15.0, Keras, Opencv-Python, Cython  
  * Labeling Tool : VGG Image Annotator
  * Data Source : 보건의료빅데이터개방시스템, 식약처
  * Environment : Eclipse (Maven), VS code, Jupyter Notebook, Colab 
  
**6. 성능**<br>
  * **이미지 검색** <br>
    * 학습 환경 : Google Colab GPU (10시간 학습 -> Colab이 런타임을 정확히 12시간을 허용하지 않음)
    * 64개 class(63 + BG), 각 알약당 10장씩 630개의 데이터를 536 epoch 학습 (loss : 0.08) -> Augmentation 적용으로 학습데이터량 증가
    * 50여개의 class를 95% 이상의 정확도로 분류 <br>
    * 음성 지원 : GCP TTS API를 사용하여 검색된 약의 결과를 음성파일로 합성하여 동시에 출력 가능. (시력이 좋지 않은 사용자를 위해)
  * **텍스트 검색** <br>
    * 약품명, 식별문자(전명, 후면), 모양, 색상으로 입력시 매우 준수한 검색 성능
    * Elasticsearch index mapping : Edge ngram 사용
      * 약의 이름이 모두 한글이 아니며, 숫자를 포함, 비슷한 약 이름이 다수 존재하기 때문에 기존에 존재하는 알약 검색 사이트에서 검색결과의 정확도가 좋지 못했습니다.
      * 단점을 보완하기 위해 Edge gram, 자동완성기능을 통해 검색결과의 정확도를 높이고 유저에게 선택권을 부여함으로써 해결했습니다. 
     
**7. 참고**<br>
  * https://github.com/matterport/Mask_RCNN
  * https://towardsdatascience.com/plug-and-play-object-detection-code-in-5-simple-steps-f1975804373e
  * https://www.tornadoweb.org/en/stable/

**8. 실행화면** <br>
    ![이미지검색2-1](https://user-images.githubusercontent.com/40975942/72503039-1eae5e00-387e-11ea-8725-9d134abb9a57.jpg)
    ![이미지검색2-2](https://user-images.githubusercontent.com/40975942/72503109-4a314880-387e-11ea-8474-b5f7dc0914d8.jpg)
    ![이미지검색2-3](https://user-images.githubusercontent.com/40975942/72503110-4a314880-387e-11ea-9100-7eac3fc124c9.jpg)
    ![이미지검색2-4](https://user-images.githubusercontent.com/40975942/72503111-4a314880-387e-11ea-8f39-8ff8b94265e0.jpg)
    ![텍스트검색1-1](https://user-images.githubusercontent.com/40975942/72503112-4ac9df00-387e-11ea-881b-a693ed2dc68b.jpg)
    ![텍스트검색1-2](https://user-images.githubusercontent.com/40975942/72503108-4a314880-387e-11ea-8047-2aff51962c48.jpg)
    ![텍스트검색1-3](https://user-images.githubusercontent.com/40975942/72503175-7947ba00-387e-11ea-88fe-f2a6701962e7.jpg)
    ![텍스트검색1-4](https://user-images.githubusercontent.com/40975942/72503176-79e05080-387e-11ea-89cc-e92083a92f15.jpg)
    ![텍스트검색1-5](https://user-images.githubusercontent.com/40975942/72503178-79e05080-387e-11ea-8b67-bb2c8697e9d6.jpg)
