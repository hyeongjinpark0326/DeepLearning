# 주제
    - keras로 학습한 model을 웹서비스에 활용
    - 딥러닝으로 만든 모델을 실제로 서비스에 탑재하여 사용

# 환경구축 (서버 사이드)
    - 가상환경구축
        - $ pip install venv
    - 가상환경생성
        - $ python -m venv kears_env        
    - vs 코드에서 가상환경 맞춤
        # 가상환경 활성화
        - $ . c:\Users\deeppy\Desktop\kears_web_service\kears_env\Scrie\kears_env\Scripts\activate
        - ctrl + shift + p
        - Python Select Interpreter
        - (kears_env) 가상환경 선택
        - powershell 새로 할당 (터미널에서 + 클릭)
    - 필요한 모듈 설치
        - (kears_env)$ pip install flask
        - (kears_env)$ pip install tensorflow==1.15
    ==================================================================
    - tensorflow 는 python 3.6 ~ 지원가능
        - 3.6 ~ 3.7 : tensorflow 1.x
        - 3.8 ~ : tensorflow 2.x
    - conda 사용시 
        - $ conda create -n kears_env python=3.7.10 -y
        - $ conda activate kears_env
        - (kears_env)$ conda install flask -y
        - (kears_env)$ conda install tensorflow=1.15.0 -y
        - (kears_env)$ pip install tensorflow=1.15.0
    - python  레벨에서 설치 (3.6 or 3.7이 설치가 되어 있을때 가능)
        - $ python -m venv kears_env   
        - $ . /kears_env/Scripts/activate
        - (kears_env)$ pip install flask
        - (kears_env)$ pip install tensorflow==1.15
    - virtualenv
        - python  레벨에서 수행하는것과 동일하나 파이썬 설치 버전을 지정할수 있다
    