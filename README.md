# Competitive Programming Intelligence

A simple dashboard for tracking competitive-programming performance across Codeforces, CodeChef, and LeetCode.

## What it does

- Shows profile and rating data from all three platforms
- Displays Codeforces activity with a 365-day submission heatmap
- Calculates unique Codeforces problems solved from accepted submissions
- Compares performance across platforms
- Shows problem, language, and topic statistics where available
- Caches requests to keep the dashboard responsive

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000` in your browser.

## API

The dashboard uses the CP Rating API:

`https://cp-rating-api.vercel.app`

Supported endpoints:

- `/codeforces/{username}`
- `/codechef/{username}`
- `/leetcode/{username}`

Codeforces activity is fetched from the official Codeforces API.

## Notes

Some statistics depend on what each platform API returns. Missing data is left unavailable rather than guessed.
