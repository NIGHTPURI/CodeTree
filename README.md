# CodeTree · 알고리즘 학습 기록

Python과 Java로 풀이한 코드트리 문제를 모았습니다. 조건문·반복문부터 배열, 함수, 격자 탐색까지 코드로 확인할 수 있는 학습 기록입니다.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-B45309?style=flat)
![Purpose: Learning](https://img.shields.io/badge/Purpose-Learning-374151?style=flat)

[학습 지도](#둘러보기) · [풀이 접근](#코드에서-볼-수-있는-접근) · [복습 필요 문제](#복습-필요-문제) · [실행과 기록](#실행과-결과-해석)

## 둘러보기

| 학습 영역 | 풀이 폴더 |
|---|---|
| 입출력 · 조건문 · 반복문 · 배열 | [trail0](trail0) |
| 기초 문법 복습 · 구현 | [trail1](trail1) |
| 함수 · 수학 · 구현 | [trail2](trail2) |
| 격자 시뮬레이션 · 탐색 | [samsung-sw](samsung-sw) |

## 코드에서 볼 수 있는 접근

- [격자 이동과 BFS](samsung-sw/%EC%95%84%EA%B8%B0%20%EA%B3%A0%EB%9E%98%EC%9D%98%20%EC%B2%AB%20%ED%95%AD%ED%95%B4/baby-whale-first-voyage.py): 방향 우선순위에 따른 이동, BFS 거리 계산, 다음 목적지 선택을 함수로 나눴습니다.
- [소수 판별과 조건 결합](trail2/%ED%95%A8%EC%88%98%EB%A5%BC%20%EC%9D%B4%EC%9A%A9%ED%95%9C%20%ED%95%A9%EA%B3%BC%20%EC%86%8C%EC%88%98%20%ED%8C%90%EB%B3%84/use-functions-to-determine-sums-and-decimals.py): 제곱근 범위의 약수 검사와 자릿수 합 조건을 별도 함수로 표현했습니다.

## 복습 필요 문제

풀이 코드에 `복습 필요`, `복습:` 또는 `복습 :` 주석을 남긴 문제 4개입니다. 복습 포인트는 해당 주석과 구현을 기준으로 정리했습니다.

| 문제 | 언어 | 복습 포인트 |
|---|---|---|
| [k번째로 신기한 문자열](trail2/k%EB%B2%88%EC%A7%B8%EB%A1%9C%20%EC%8B%A0%EA%B8%B0%ED%95%9C%20%EB%AC%B8%EC%9E%90%EC%97%B4/kth-special-string.py) | Python | `startswith(t)`로 문자열을 필터링하고, 새 리스트를 정렬한 뒤 `k - 1` 인덱스로 선택하기 |
| [palindrome 여부 판단하기](trail2/palindrome%20%EC%97%AC%EB%B6%80%20%ED%8C%90%EB%8B%A8%ED%95%98%EA%B8%B0/determine-whether-palindrome-is-present.java) | Java | `charAt(i)`로 문자를 꺼내고, 끝에서부터 순회해 역순 문자열 만들기 |
| [두 정수 값 교환하기](trail2/%EB%91%90%20%EC%A0%95%EC%88%98%20%EA%B0%92%20%EA%B5%90%ED%99%98%ED%95%98%EA%B8%B0/to-exchange-two-integer-values.java) | Java | Java의 값 전달 방식을 이해하고, `int[]`로 두 결과를 반환한 뒤 호출부에서 `n`, `m`에 재대입하기 |
| [중앙값 계산 2](trail2/%EC%A4%91%EC%95%99%EA%B0%92%20%EA%B3%84%EC%82%B0%202/get-median-2.py) | Python | `arr[:i+1]` 슬라이싱과 `sorted`로 부분 구간을 정렬하고, 홀수 길이 구간의 중앙값을 `i // 2` 인덱스로 선택하기 |

## 실행과 결과 해석

각 풀이는 해당 문제의 입력 형식에 맞춰 독립적으로 실행합니다. Python 풀이는 다음처럼 실행할 수 있습니다.

```bash
python3 "문제 폴더/풀이.py" < input.txt
```

`input.txt`는 원문 문제의 입력 예제로 직접 준비합니다. Java 풀이는 각 파일의 클래스명과 해당 플랫폼의 제출 형식을 확인해야 합니다. 통합 테스트나 전체 풀이의 재채점 결과는 제공하지 않습니다.

문제별 README에는 원문 링크와 커리큘럼 정보가 있습니다. README만 있는 폴더도 있으므로 폴더 수를 풀이 완료 수로 해석하지 않습니다.

2026-10-01 문서 정리에서는 링크와 소개한 코드의 대응만 확인했습니다. **실행 검증 미수행**이며, Java 실행 환경도 없어 Java 풀이를 재실행하지 않았습니다.

## 출처

문제와 커리큘럼은 [코드트리](https://www.codetree.ai/)의 자료입니다. 이 저장소의 풀이 코드와 플랫폼에서 제공한 문제 정보를 구분하며, 개별 README의 원문 링크와 출처 표기를 유지합니다.
