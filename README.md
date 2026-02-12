# 이지케어텍 AI Engineer 사전과제

KLUE 데이터셋을 활용한 Relation Extraction (RE) 과제

## 프로젝트 구조

```
ezcaretec/
├── download_dataset.py                      # KLUE 데이터셋 다운로드 스크립트 (uv 기반)
├── 01_klue_re_assignment_EDA.ipynb          # EDA 수행
├── 02_klue_re_dataset_construction.ipynb    # 데이터셋 구성 및 전처리
├── 03_klue_re_app_design.ipynb              # 어플리케이션 구조 설계
├── 04_klue_re_llm_selection.ipynb           # LLM 모델 선정
├── 05_klue_re_no_train_baseline.ipynb       # 학습 전 베이스라인 평가
├── 06_klue_re_training_improvement.ipynb    # 모델 학습 및 성능 개선
├── 07_klue_re_model_comparison.ipynb        # 모델 비교 및 최종 평가
├── REPORT.md                                # 전체 과제 수행 보고서
├── README.md                                # 프로젝트 설명
├── uv.lock                                  # uv 의존성 락 파일
├── data/                                    # 다운로드된 데이터셋 (gitignore)
└── temp_result/                             # 학습 결과 및 체크포인트 (gitignore)
```

## 빠른 시작

### 1. uv 설치 (Python 패키지 매니저)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. 데이터셋 다운로드

```bash
# KLUE 데이터셋 다운로드 (RE 과제용)
uv run download_dataset.py
```

### 3. 노트북 실행

```bash
# Jupyter Lab 실행
jupyter lab

# 또는 Jupyter Notebook
jupyter notebook
```

## 과제 수행 단계

1. ✅ **데이터셋 다운로드** - KLUE-RE 데이터 확보
2. ✅ **EDA 수행** - 라벨 분포, 문장 길이, 엔티티 구조 분석
3. ✅ **데이터셋 구성** - 엔티티 태그 삽입 및 전처리 파이프라인
4. ✅ **어플리케이션 구조 설계** - 추론 파이프라인 설계
5. ✅ **LLM 선정** - `klue/roberta-base` 선정 및 근거 정리
6. ✅ **베이스라인 평가** - 학습 전 성능 측정
7. ✅ **모델 학습** - Fine-tuning 및 성능 개선
8. ✅ **모델 비교** - 학습 전후 성능 비교 분석
9. ✅ **과정 정리** - REPORT.md 작성

## 주요 결과

### 모델 성능

| 모델 | Accuracy | Macro F1 | 비고 |
|------|----------|----------|------|
| 학습 전 (Base) | ~1.5% | ~0.1% | 랜덤 분류 head |
| Fine-tuned | **74.9%** | **59.9%** | klue/roberta-base |

### 핵심 인사이트

- **클래스 불균형 문제**: `no_relation` 클래스 편향으로 인해 Accuracy만으로는 성능 평가 불충분
- **Macro F1 중심 평가**: 소수 클래스 성능까지 고려한 종합적 평가 필요
- **Fine-tuning 필수**: 사전학습 모델 단독 사용 불가, 도메인 적응 필수
- **엔티티 강조 효과**: `[E1]...[/E1]`, `[E2]...[/E2]` 태그로 관계 예측 신호 강화

### 개선 방향

- Class-weighted Loss 적용
- Focal Loss 실험
- 데이터 증강 (over/under-sampling)
- 라벨별 오류 분석 기반 개선

## 기술 스택

- **모델**: `klue/roberta-base` (Hugging Face Transformers)
- **데이터셋**: KLUE-RE (Korean Language Understanding Evaluation)
- **프레임워크**: PyTorch, Transformers
- **개발 환경**: Jupyter Notebook, uv
- **평가 지표**: Accuracy, Macro F1, Confusion Matrix

## 요구사항

- Python 3.8+
- uv (Python 패키지 매니저)
- CUDA (GPU 학습 권장)
- 충분한 디스크 공간 (데이터셋 + 모델 체크포인트)

## 상세 보고서

전체 과제 수행 과정 및 의사결정 근거는 [REPORT.md](REPORT.md)를 참고하세요.
