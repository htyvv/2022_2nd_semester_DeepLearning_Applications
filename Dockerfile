FROM pytorchlightning/pytorch_lightning
LABEL email="2017121261@kau.kr"
LABEL name="Taeyeong"
LABEL version="1.0"
LABEL description="2022_2nd_Semester_DeepLearning_Applications"

RUN apt-get update && apt-get install -y

# pip 오류로 인한 재설치
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN pip install ipykernel -U --user --force-reinstall

# 이후 Conda와 같은 가상환경이 아니라 그냥 Global python3.6 사용