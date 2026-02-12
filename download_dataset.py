#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "datasets>=2.14.0",
#     "pandas>=1.5.0",
#     "numpy>=1.21.0",
#     "transformers>=4.30.0",
#     "huggingface-hub>=0.16.0",
#     "tqdm>=4.64.0",
# ]
# ///
"""
KLUE Dataset Download Script for Relation Extraction Task
이지케어텍 AI Engineer 사전과제용 데이터셋 다운로드 스크립트

Usage:
    uv run download_dataset.py
"""

import os
import logging
from pathlib import Path
from datasets import load_dataset
import pandas as pd

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_data_directory():
    """데이터 저장용 디렉토리 생성"""
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    return data_dir

def download_klue_datasets():
    """KLUE 데이터셋 다운로드 및 저장"""
    data_dir = create_data_directory()
    
    # KLUE 데이터셋 목록 (RE 과제에 필요한 것들)
    datasets_to_download = {
        "re": "Relation Extraction (주요 과제)",
        "dp": "Dependency Parsing", 
        "mrc": "Machine Reading Comprehension",
        "ner": "Named Entity Recognition",
        "nli": "Natural Language Inference",
        "sts": "Semantic Textual Similarity",
        "tc": "Topic Classification",
        "wos": "Winograd Schema Challenge"
    }
    
    downloaded_datasets = {}
    
    for task_name, description in datasets_to_download.items():
        try:
            logger.info(f"다운로드 중: {task_name} - {description}")
            
            # 데이터셋 로드
            dataset = load_dataset("klue/klue", task_name)
            downloaded_datasets[task_name] = dataset
            
            # 데이터셋 정보 출력
            logger.info(f"✅ {task_name} 다운로드 완료")
            logger.info(f"   - Train: {len(dataset['train'])} samples")
            if 'validation' in dataset:
                logger.info(f"   - Validation: {len(dataset['validation'])} samples")
            if 'test' in dataset:
                logger.info(f"   - Test: {len(dataset['test'])} samples")
            
            # CSV로 저장 (분석용)
            for split_name, split_data in dataset.items():
                csv_path = data_dir / f"klue_{task_name}_{split_name}.csv"
                df = pd.DataFrame(split_data)
                df.to_csv(csv_path, index=False, encoding='utf-8')
                logger.info(f"   - {split_name} 데이터 저장: {csv_path}")
            
        except Exception as e:
            logger.error(f"❌ {task_name} 다운로드 실패: {str(e)}")
            continue
    
    return downloaded_datasets

def analyze_re_dataset(datasets):
    """RE 데이터셋 기본 분석"""
    if 're' not in datasets:
        logger.error("RE 데이터셋을 찾을 수 없습니다.")
        return
    
    re_dataset = datasets['re']
    logger.info("\n=== RE (Relation Extraction) 데이터셋 분석 ===")
    
    # 훈련 데이터 분석
    train_data = re_dataset['train']
    logger.info(f"훈련 데이터 크기: {len(train_data)}")
    
    # 샘플 데이터 확인
    sample = train_data[0]
    logger.info("샘플 데이터 구조:")
    for key, value in sample.items():
        logger.info(f"  - {key}: {type(value)} = {value}")
    
    # 관계 라벨 분포 확인
    if 'label' in sample:
        labels = [item['label'] for item in train_data]
        label_counts = pd.Series(labels).value_counts()
        logger.info(f"\n관계 라벨 분포:")
        for label, count in label_counts.head(10).items():
            logger.info(f"  - {label}: {count}")

def main():
    """메인 실행 함수"""
    logger.info("🚀 KLUE 데이터셋 다운로드 시작")
    logger.info("과제: Relation Extraction (RE)")
    logger.info("실행 방법: uv run download_dataset.py")
    
    try:
        # 데이터셋 다운로드
        datasets = download_klue_datasets()
        
        # RE 데이터셋 분석
        analyze_re_dataset(datasets)
        
        logger.info("\n✅ 모든 작업이 완료되었습니다!")
        logger.info("다음 단계: EDA 및 모델 구현을 진행하세요.")
        
    except Exception as e:
        logger.error(f"❌ 오류 발생: {str(e)}")
        raise

if __name__ == "__main__":
    main()