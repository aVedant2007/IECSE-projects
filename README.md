# Competitive Programming Intelligence

A simple dashboard for tracking competitive-programming performance across Codeforces, CodeChef, and LeetCode.

## What it does

- Shows profile and rating data from all three platforms
- Calculates unique Codeforces problems solved from accepted submissions
- Compares performance across platforms
- Shows problem, language, and topic statistics where available

## Run locally

```bash
streamlit run frontend.py
```

## API

The dashboard uses the CP Rating API:

`https://cp-rating-api.vercel.app`

Supported endpoints:

- `/codeforces/{username}`
- `/codechef/{username}`
- `/leetcode/{username}`

Codeforces activity is fetched from the official Codeforces API.
