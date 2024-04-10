# Hello, World! 👋
## Getting started
### Copying files
Extract the zip files and copy them into the project in order to have this structure:
```
data
├── clean
└── raw
    ├── mongo
    │   ├── mongo_3_10_90
    │   │   ├── 1
    │   │   ├── 2
    │   │   ├── 3
    │   │   ├── 4
    │   │   ├── 5
    │   │   ├── 6
    │   │   ├── 7
    │   │   ├── 8
    │   │   ├── 9
    │   │   └── 10
    │   ├── mongo_3_50_50
    │   ├── mongo_5_10_90
    │   └── mongo_5_50_50
    └── redis
        ├── redis_3_10_90
        │   ├── 1
        │   ├── 2
        │   ├── 3
        │   ├── 4
        │   ├── 5
        │   ├── 6
        │   ├── 7
        │   ├── 8
        │   ├── 9
        │   └── 10
        ├── redis_3_50_50
        ├── redis_5_10_90
        └── redis_5_50_50

```
### Generating the `.csv` files
Run to populate the `.csv` files (don't forget to create a virtual environment 😉):
```bash
pip install -r requirements.txt
```

```bash
python -m setup
```
