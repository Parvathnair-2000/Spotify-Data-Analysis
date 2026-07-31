import streamlit as st
import pandas as pd
import plotly.express as px
 
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Spotify Data Analysis Dashboard",
    page_icon="🎵",
    layout="wide"
)
 
# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("dataset.csv")
 
# Use a sample for scatter plots (faster & avoids WebGL issues)
sample_df = df.sample(n=1000, random_state=42)
 
# -----------------------------
# Dashboard Title
# -----------------------------
st.title("🎵 Spotify Data Analysis Dashboard")
st.markdown("### Spotify Songs Dataset Analysis")
 
st.markdown("---")
 
# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)
 
col1.metric("Total Songs", len(df))
col2.metric("Artists", df["artists"].nunique())
col3.metric("Genres", df["track_genre"].nunique())
col4.metric("Average Popularity", round(df["popularity"].mean(), 2))
 
st.markdown("---")
 
# -----------------------------
# Dataset Preview
# -----------------------------
st.header("📋 Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)
 
st.markdown("---")
 
# -----------------------------
# Dataset Statistics
# -----------------------------
st.header("📊 Dataset Statistics")
st.dataframe(df.describe(), use_container_width=True)
 
st.markdown("---")
 
# -----------------------------
# Missing Values
# -----------------------------
st.header("❌ Missing Values")
missing = df.isnull().sum().reset_index()
missing.columns = ["Column", "Missing Values"]
st.dataframe(missing, use_container_width=True)
 
st.markdown("---")
 
# =====================================================
# Graph 1 - Energy vs Popularity
# =====================================================
 
st.header("📈 Energy vs Popularity")
 
fig = px.scatter(
    sample_df,
    x="energy",
    y="popularity",
    color="track_genre",
    title="Energy vs Popularity",
    render_mode="svg"
)
 
st.plotly_chart(fig, use_container_width=True)
 
st.markdown("---")
 
# =====================================================
# Graph 2 - Danceability vs Popularity
# =====================================================
 
st.header("💃 Danceability vs Popularity")
 
fig = px.scatter(
    sample_df,
    x="danceability",
    y="popularity",
    color="track_genre",
    title="Danceability vs Popularity",
    render_mode="svg"
)
 
st.plotly_chart(fig, use_container_width=True)
 
st.markdown("---")
 
# =====================================================
# Graph 3 - Duration vs Popularity
# =====================================================
 
st.header("⏱️ Duration vs Popularity")
 
fig = px.scatter(
    sample_df,
    x="duration_ms",
    y="popularity",
    color="track_genre",
    title="Duration vs Popularity",
    render_mode="svg"
)
 
st.plotly_chart(fig, use_container_width=True)
 
st.markdown("---")
 
# =====================================================
# Graph 4 - Top 10 Artists by Average Popularity
# =====================================================
 
st.header("⭐ Top 10 Artists by Average Popularity")
 
top_artists = (
    df.groupby("artists")["popularity"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)
 
fig = px.bar(
    top_artists,
    x="artists",
    y="popularity",
    color="popularity",
    title="Top 10 Artists by Average Popularity"
)
 
st.plotly_chart(fig, use_container_width=True)
 
st.markdown("---")
 
# =====================================================
# Graph 5 - Top 10 Genres by Average Danceability
# =====================================================
 
st.header("🎵 Top 10 Genres by Average Danceability")
 
top_dance = (
    df.groupby("track_genre")["danceability"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)
 
fig = px.bar(
    top_dance,
    x="track_genre",
    y="danceability",
    color="danceability",
    title="Top 10 Genres by Average Danceability"
)
 
st.plotly_chart(fig, use_container_width=True)
 
st.markdown("---")
 
# =====================================================
# Graph 6 - Valence vs Popularity
# =====================================================
 
st.header("❤️ Valence vs Popularity")
 
fig = px.scatter(
    sample_df,
    x="valence",
    y="popularity",
    color="track_genre",
    title="Valence vs Popularity",
    render_mode="svg"
)
 
st.plotly_chart(fig, use_container_width=True)
 
st.markdown("---")
 
# =====================================================
# Graph 7 - Top 10 Genres by Average Energy
# =====================================================
 
st.header("⚡ Top 10 Genres by Average Energy")
 
top_energy = (
    df.groupby("track_genre")["energy"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)
 
fig = px.bar(
    top_energy,
    x="track_genre",
    y="energy",
    color="energy",
    title="Top 10 Genres by Average Energy"
)
 
st.plotly_chart(fig, use_container_width=True)
 
st.markdown("---")
 
# =====================================================
# Graph 8 - Top 10 Genres by Average Valence
# =====================================================
 
st.header("😊 Top 10 Genres by Average Valence")
 
top_valence = (
    df.groupby("track_genre")["valence"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)
 
fig = px.bar(
    top_valence,
    x="track_genre",
    y="valence",
    color="valence",
    title="Top 10 Genres by Average Valence"
)
 
st.plotly_chart(fig, use_container_width=True)
 
st.markdown("---")
 
# =====================================================
# Graph 9 - Correlation Heatmap
# =====================================================
 
st.header("🔥 Correlation Heatmap")
 
numeric_df = df.select_dtypes(include="number")
 
fig = px.imshow(
    numeric_df.corr(),
    text_auto=True,
    aspect="auto",
    color_continuous_scale="Viridis",
    title="Correlation Heatmap"
)
 
st.plotly_chart(fig, use_container_width=True)
 
st.markdown("---")
 
# =====================================================
# Graph 10 - Top 10 Genres by Average Popularity
# =====================================================
 
st.header("🏆 Top 10 Genres by Average Popularity")
 
top_popularity = (
    df.groupby("track_genre")["popularity"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)
 
fig = px.bar(
    top_popularity,
    x="track_genre",
    y="popularity",
    color="popularity",
    title="Top 10 Genres by Average Popularity"
)
 
st.plotly_chart(fig,
use_container_width=True)                
 
 
 
