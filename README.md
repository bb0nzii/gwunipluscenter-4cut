# 강통플 네컷

공개 사이트: https://bb0nzii.github.io/gwunipluscenter-4cut/

강원권 통일플러스센터 SNS 서포터즈가 개인 제작한 모바일 중심 네컷 사진 꾸미기 웹입니다. 보유 사진 네 장을 넣고 더함이·다함이 및 통일 관련 스티커로 꾸민 뒤 PNG로 저장합니다.

센터 현장 사진 체험 부스와 별개이며 서로 연동되지 않습니다. 마스코트는 센터의 사용 허락을 받아 활용했습니다. 이는 이 프로젝트를 위한 허락으로, 타인의 자산 재사용 허락을 뜻하지 않습니다.

## 기능

- 기존 프레임 4종: 검정 / 세로, 검정 / 가로, 하양 / 세로, 하양 / 가로
- 사진 칸 중앙 +로 추가, 오른쪽 위 ×로 삭제 후 재업로드
- 사진 드래그 이동과 선택 박스 모서리 확대·축소, 빈틈 없는 사진 채우기
- 스티커 12종 추가·이동·크기 조절·삭제, 선택한 스티커 맨 앞으로 표시
- 완성 이미지 확인, 프레임 원본 해상도의 PNG 저장, 이어서 수정
- 모바일·PC 반응형 화면 및 키보드 조작

사진은 브라우저 안에서 처리하며 서버로 전송하지 않습니다. 사진 수집·전송·인쇄 기능은 없습니다. 새로고침하면 편집 내용이 초기화됩니다.

## 기술 구성과 로컬 실행

HTML, CSS, JavaScript(ES Modules), Canvas를 사용합니다. 패키지 설치, 별도 백엔드, 데이터베이스, 환경변수, API 키가 필요 없습니다. 로컬 실행과 배포 파일 준비에는 Python 3을 사용합니다.

터미널에서 프로젝트 폴더로 이동해 실행합니다.

```sh
python3 -m http.server 5173 --bind 127.0.0.1
```

브라우저에서 http://127.0.0.1:5173/ 를 엽니다. 종료는 Ctrl+C입니다. `index.html` 더블클릭 대신 서버로 실행해야 설정 JSON을 정상적으로 읽습니다.

## 파일 구성

- `index.html`, `style.css`, `app.js`: 화면과 편집 기능
- `assets/`: 공개할 프레임·스티커·설정 JSON
- `docs/DECISIONS.md`, `docs/QA.md`: 기획·결정·검증 이력. 과거 기록도 포함하므로 최신 항목을 함께 확인합니다.
- `scripts/prepare-pages.py`: 공개할 파일만 `_site/`에 모으는 스크립트
- `.github/workflows/pages.yml`: GitHub Pages 수동 배포 설정

## 배포 파일 준비

```sh
python3 scripts/prepare-pages.py
```

컴파일 없이 기존 `_site/`를 재생성합니다. 결과에는 아래 항목만 들어갑니다.

```text
_site/
  index.html
  style.css
  app.js
  assets/
```

`docs/`, README, 개발 스크립트, Git 설정은 사이트에 포함하지 않습니다. JPG/JPEG와 숨김 파일도 제외합니다. 자산 형식은 PNG·SVG·JSON만 허용하며, 다른 형식은 공개 전에 검토하도록 준비 작업을 중단합니다. `assets/`의 자산은 공개되므로 개인 사진을 이 폴더에 넣지 않습니다.

모든 웹 자산은 `assets/...` 등의 상대경로입니다. `https://계정.github.io/저장소이름/` 같은 저장소 하위 경로에서도 코드에 저장소 이름을 넣을 필요가 없습니다.

## GitHub에서 나중에 할 작업

2026-10-16에 main 업로드와 최초 공개 배포를 완료했습니다. 아래는 배포 절차이며, 이후에도 push 자동 배포 없이 워크플로를 수동 실행합니다.

1. GitHub에 저장소를 만듭니다. 예: `gwunipluscenter-4cut`. 무료 개인 계정에서 Pages를 사용하려면 공개 저장소를 선택합니다. 공개 저장소의 소스와 텍스트 문서도 누구나 볼 수 있습니다.
2. 파일을 검토한 뒤 로컬에서 커밋하고 새 저장소의 `main` 브랜치에 업로드합니다. `.gitignore`가 적용되는 Git 또는 GitHub Desktop을 사용합니다. 브라우저에 폴더 전체를 드래그하면 제외 규칙이 자동 적용되지 않으므로 JPG를 직접 올리지 않습니다.
3. **Settings → Pages → Build and deployment → Source**를 **GitHub Actions**로 선택합니다.
4. 공개할 준비가 되면 **Actions → Deploy GitHub Pages → Run workflow**에서 `main`을 선택해 실행합니다. 이 단계가 실제 공개 배포입니다.
5. 성공한 실행에 표시된 URL에서 사진 네 장·스티커·PNG 저장을 확인합니다. 보통 `https://계정.github.io/저장소이름/` 형태이며 마지막 `/`까지 사용합니다.
6. 이후 수정 내용을 업로드해도 자동 배포되지 않습니다. 같은 워크플로를 다시 수동 실행합니다.

별도 Secret이나 개인 액세스 토큰은 필요 없습니다. 배포 작업은 GitHub가 제공하는 작업용 토큰을 사용합니다.

공식 절차: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## 기록·사진과 검증 범위

`.gitignore`는 `.DS_Store`, JPG/JPEG(대소문자 포함), 로컬 환경변수와 생성 결과를 제외합니다. `docs/`의 Markdown 기록은 유지하며 JPG 화면 캡처는 로컬에만 둡니다. 이미 추적된 파일에는 제외 규칙이 소급 적용되지 않으므로 업로드 전 추적 파일도 확인합니다.

로컬 검증과 미확인 사항은 `docs/QA.md`에 기록합니다. GitHub Actions 성공과 공개 HTTPS 주소의 자산 로딩·PNG 다운로드는 확인했습니다. 실제 iOS/Android 기기의 터치·저장 동작은 추가 확인이 필요합니다.
