import streamlit as st
import requests

st.title("Competitive Programming Tracker")

home, = st.tabs(["Users"])

with home:
    platform = st.selectbox(
        "Select Platform",
        ["Codeforces", "LeetCode", "Codechef"],
    )
    if platform == "Codeforces":
        username = st.text_input("Codeforces Username")
        if st.button("Search"):
            response = requests.get(
                f"https://cp-rating-api.vercel.app/codeforces/{username}"
            )
            data = response.json()
            st.title(data["handle"])

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Rating", data["rating"])
            with col2:
                st.metric("Max Rating", data["maxRating"])
            with col3:
                st.metric("Rank", data["rank"])

            st.write("#### Contributions:", data["contributions"])

    elif platform == "Codechef":
        username = st.text_input("Codechef Username")
        if st.button("Search"):
            response = requests.get(
                f"https://cp-rating-api.vercel.app/codechef/{username}"
            )
            data = response.json()
            st.title(data["username"])

            col0,col1, col2, col3 = st.columns(4)
            with col0:
                st.metric("Stars", data["stars"])
            with col1:
                st.metric("Rating", data["rating"])
            with col2:
                st.metric("Global Rank", data["globalRank"])
            with col3:
                st.metric("Country Rank", data["countryRank"])

    else:
        username = st.text_input("LeetCode Username")
        if st.button("Search"):
            response = requests.get(
                f"https://cp-rating-api.vercel.app/leetcode/{username}"
            )
            data = response.json()
            st.title(data["user"])

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Rank", data["rank"])
            with col2:
                st.metric("Problems Solved", data["problemsSolved"])

            st.write("#### Stats of Solved Problems:\n")
            st.write("Easy:", data["submissions"][1]["count"])
            st.write("Medium:", data["submissions"][2]["count"])
            st.write("Hard:", data["submissions"][3]["count"])

            st.write("#### Topics Covered:\n")

            st.write("##### Advanced:")
            for i in range(len(data["topics"]["advanced"])):
                st.write("&nbsp;&nbsp;&nbsp;&nbsp;", data["topics"]["advanced"][i]["tagName"], ": ", data["topics"]["advanced"][i]["problemsSolved"])

            st.write("##### Intermediate:")
            for i in range(len(data["topics"]["intermediate"])):
                st.write("&nbsp;&nbsp;&nbsp;&nbsp;", data["topics"]["intermediate"][i]["tagName"], ": ", data["topics"]["intermediate"][i]["problemsSolved"])

            st.write("##### Fundamental:")
            for i in range(len(data["topics"]["fundamental"])):
                st.write("&nbsp;&nbsp;&nbsp;&nbsp;", data["topics"]["fundamental"][i]["tagName"], ":", data["topics"]["fundamental"][i]["problemsSolved"])

