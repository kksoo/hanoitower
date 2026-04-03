# CLAUDE.md — 하노이 탑 프로젝트 AI 가이드

## 프로젝트 개요

하노이 탑(Tower of Hanoi) 알고리즘을 Python으로 구현한 프로젝트입니다.
재귀 알고리즘의 학습 및 시각화를 목적으로 하며, Docker를 통해 실행 환경을 제공합니다.

---

## 디렉토리 구조

```
hanoitower/
├── hanoi_tower.py    # 절차형(함수 기반) 구현 — 메인 실행 파일 (Dockerfile에서 사용)
├── hanoi_tower1.py   # hanoi_tower.py와 동일한 절차형 구현 (복사본 또는 백업)
├── hanoi_tower2.py   # 객체지향(클래스 기반) 구현 — HanoiTower 클래스
├── Dockerfile        # Ubuntu + Python 3.8 기반 실행 환경
└── CLAUDE.md         # 이 문서
```

---

## 소스 파일 설명

### `hanoi_tower.py` / `hanoi_tower1.py` (절차형 구현)

전역 변수와 함수를 사용하는 절차형 스타일입니다.

- `init_tower(n)` — n개 디스크로 타워 초기화. A 기둥에 `[n, n-1, ..., 1]` 순서로 적재
- `print_tower(s)` — 현재 타워 상태를 기둥별로 출력
- `moves(s, f, v, t, n)` — 재귀적 이동 함수
  - `f`: 출발 기둥, `v`: 보조 기둥, `t`: 목적 기둥, `n`: 이동할 디스크 수
  - `input("")` 호출로 각 이동 시 Enter 입력을 기다림 (단계별 진행)
- `solve(tw, disk_counts)` — 초기 상태 출력 후 풀이 시작
- 실행: `python3 hanoi_tower.py <디스크 수>`

### `hanoi_tower2.py` (객체지향 구현)

동일한 알고리즘을 `HanoiTower` 클래스로 캡슐화한 버전입니다.

- `HanoiTower.__init__(n)` — 초기화: `nMove`, `disk_count`, `stacks` 딕셔너리
- `HanoiTower.print()` — 현재 상태 출력
- `HanoiTower.moves(f, v, t, n)` — 재귀 이동 (전역 변수 대신 `self.nMove` 사용)
- `HanoiTower.solve()` — 풀이 진행
- 실행: `python3 hanoi_tower2.py <디스크 수>`

---

## 알고리즘 핵심

하노이 탑 재귀 알고리즘:

```
moves(f, v, t, n):
  if n == 1:
    디스크 하나를 f -> t 로 이동
  else:
    moves(f, t, v, n-1)  # 상위 n-1개를 보조 기둥으로
    moves(f, v, t, 1)    # 가장 큰 디스크를 목적지로
    moves(v, f, t, n-1)  # 보조 기둥의 n-1개를 목적지로
```

총 이동 횟수: `2^n - 1`

---

## 실행 방법

### 로컬 실행

```bash
python3 hanoi_tower.py 3       # 3개 디스크, 절차형
python3 hanoi_tower2.py 3      # 3개 디스크, 객체지향
```

각 이동 단계에서 Enter를 눌러 다음 단계로 진행합니다.

### Docker 실행

```bash
# 이미지 빌드
docker build -t hanoitower .

# 기본 실행 (NUM_DISK=3)
docker run -it hanoitower

# 디스크 수 변경
docker run -it -e NUM_DISK=5 hanoitower
```

Dockerfile은 `hanoi_tower.py`를 메인 실행 파일로 사용하며, `NUM_DISK` 환경변수로 디스크 수를 설정합니다.

---

## 코드 컨벤션

- **언어**: Python 3 (타입 힌트 없음)
- **스타일**: 간결한 스크립트 스타일, 복잡한 추상화 없음
- **기둥 표현**: 딕셔너리 `{'A': [], 'B': [], 'C': []}` — A가 출발, C가 목적지
- **디스크 표현**: 정수 리스트, 큰 숫자가 리스트 앞에 위치 (스택의 바닥)
- **전역 변수**: `hanoi_tower.py`/`hanoi_tower1.py`는 `nMove` 전역 변수 사용; `hanoi_tower2.py`는 인스턴스 변수로 대체

---

## 브랜치 전략

- `master`: 메인 브랜치 (안정 코드)
- `claude/add-claude-documentation-qWiFX`: AI 문서화 작업 브랜치

---

## AI 어시스턴트를 위한 주의사항

1. **파일 관계**: `hanoi_tower.py`와 `hanoi_tower1.py`는 동일한 코드입니다. 변경 시 둘 다 확인하세요.
2. **Dockerfile 연동**: `hanoi_tower.py`가 컨테이너의 진입점입니다. 파일명 변경 시 Dockerfile도 수정 필요합니다.
3. **interactive 특성**: `input("")` 호출로 인해 비대화형 환경(CI 등)에서는 자동 실행이 되지 않습니다.
4. **테스트 없음**: 현재 테스트 파일이 없습니다. 새 기능 추가 시 테스트 작성을 권장합니다.
5. **Python 버전**: Dockerfile은 Python 3.8을 명시하고 있습니다. f-string 등 3.8 이상 문법은 사용 가능합니다.
