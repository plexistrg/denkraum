# Denkraum Studio v0.1

Local-first Streamlit tool for converting friction into concrete next actions.

## Constraints
- Local-first only
- No login
- No cloud sync
- No AI API
- No external database
- Storage is local JSON in `data/`

## Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
streamlit run app.py
```

## Test
```bash
python -m py_compile app.py src/*.py
pytest -q
```
