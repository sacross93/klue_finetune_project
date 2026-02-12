# 이지케어텍 AI Engineer 사전과제

KLUE 데이터셋을 활용한 Relation Extraction (RE) 과제

## 프로젝트 구조

```
ezcaretec/
├── download_dataset.py    # KLUE 데이터셋 다운로드 스크립트 (uv 기반)
├── test.py               # 간단한 데이터셋 테스트 스크립트 (uv 기반)
├── run_download.sh       # 다운로드 실행 스크립트
├── README.md            # 프로젝트 설명
└── data/               # 다운로드된 데이터셋 저장 폴더
```

## 사용 방법 (uv 기반)

### 1. 데이터셋 다운로드

```bash
# 전체 KLUE 데이터셋 다운로드 (RE 과제용)
uv run download_dataset.py

# 또는 실행 스크립트 사용
./run_download.sh
```

### 2. 간단한 테스트

```bash
# 기본 데이터셋 로드 테스트
uv run test.py
```

## uv 스크립트 특징

- **의존성 자동 관리**: 스크립트 상단에 필요한 패키지가 명시되어 있음
- **격리된 환경**: 각 스크립트가 독립적인 가상환경에서 실행
- **빠른 실행**: 필요한 패키지만 설치하여 빠른 시작

## 다운로드되는 데이터셋

- **RE (Relation Extraction)** - 주요 과제 데이터셋
- DP (Dependency Parsing)
- MRC (Machine Reading Comprehension) 
- NER (Named Entity Recognition)
- NLI (Natural Language Inference)
- STS (Semantic Textual Similarity)
- TC (Topic Classification)
- WOS (Winograd Schema Challenge)

## 과제 수행 단계

1. ✅ 데이터셋 다운로드
2. 🔄 EDA 수행
3. 🔄 데이터셋 구성
4. 🔄 어플리케이션 구조 설계
5. 🔄 LLM 선정 (Open Source)
6. 🔄 구현
7. 🔄 성능 검토
8. 🔄 성능 개선
9. 🔄 과정 정리

## 요구사항

- Python 3.8+
- uv (Python 패키지 매니저)
- 충분한 디스크 공간 (데이터셋 저장용)

## uv 설치

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```
