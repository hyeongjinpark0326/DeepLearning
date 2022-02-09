# 1. 모듈 가져오기
from flask import Flask, render_template, request

# 전처리
import numpy as np

# 딥러닝을 사용함으로 써 추가되는 부분 ===========================
# 텐서플로우 관련 모듈
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
# 모델 개발시 사용했던 버전와 일치하는지 확인 차원
print( tf.__version__ )
print( keras.__version__ )
# 학습시 사용했던 딥러닝 엔진(인터페이스 포함)의 패캐지/파이썬 버전과 
# 실제 서비스가 작동되는 환경의 패캐지/파이썬 버전이 일치하는게 좋다
# 일치하지 않으면 예상치 못한 오류가 발생할수 있다!!
import os
# 중복 라이브러리에 대한 처리
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
# 단, 모델을 미리 로드해서 각 함수에서 사용할때 공용으로 제공할것인가?
# 아니면, 개별 요청별로 그때 그때 모델을 로드해서 제공할 것인가? (안정성!!)
# 모델을 올리는 시간만큰 응답 시간이 느려지는 단점이 존재
# ==============================================================

# 2. 앱 생성
app = Flask(__name__)

# 3. 라우팅
@app.route('/')
def home():
    return render_template('index.html')

# 홈페이지에서 test.pgm 파일을 업로드 하면
# 아래 함수가받아서 -> 모델에 넣어서 예측이 가능한 구조로 변환 -> 예측 -> 응답
@app.route('/upload', methods=["POST"])
def upload():
    # 업로드된 파일 획득, 저장 (파일업로드)
    f = request.files['file']
    fName = f.filename
    f.save( fName )

    # test.pgm 읽어서 -> 인코딩(파일포멧이해해야함)
    '''
        P2 28 28 255  : (P2:매직코드,PGM파일임을알려줌, 28 28:H,W, 255:칼라수)
        0 0 0 ...... 0 0 0 : 실제 픽셀값 => 28 * 28 => 이부분이 학습시 사용할 데이터이다
        해당 데이터는 문자열로 표현되어 있으므로, 
        라인 별로 읽어서 -> 두번째 데이터를 취하여 => 전처리 => 학습에 필요한 형태로 가공
        => 이런 기능은 원래 모델을 만드는 쪽에서 제공(라이브러리 형태로)
    '''
    # 저장된 파일을 읽어서 모델에 주입이 가능하도록 데이터 준비
    with open( fName, 'r', encoding='utf-8') as fp:
        datas    = fp.readlines()
        raw_imgs = datas[1].split()        
        #print( raw_imgs )
    
    # 전처리    
    # 데이터를 4D로 구성해야 한다 => 최소 numpy의 ndarray가 되어야 처리가 가능    
        # 데이터는 255(픽셀의 최대값)로 정규화가 되어 있다
        # (?, 28, 28, 1) => 모델에 예측을 맡길수 있다 => NHWC 형태로 shape 변경
    # 데이터를  ndarray로 변환
    # 데이터를 255(최대값)를 기준으로 정규화
    nums = np.array( raw_imgs, dtype=np.float32 ) / 255
    # (784,)
    #print(  nums, nums.shape, nums.dtype )
        
    # 모델 로드
    # 모델 덤프 파일은 그 위치에 따라 경로가 변경(자동처리되게 상대경로)
    model = load_model( "mnist_cnn.h5" )
    # 예측 수행
    nums  = nums.reshape( -1, 28, 28, 1 ) 
    # 0 ~ 9 사이의 값중 하나가 나올것이다
    y_predict = model.predict_classes( nums ) 
    # 응답
    return "예측 완료 : " + y_predict        

# 4. 서버가동
if __name__ == '__main__':
    app.run( debug=True )