# Social Media Post Analyzer

A Generative AI project built using LangChain, Groq API, Streamlit, and Pydantic.

## Problem Statement

Brands and creators publish social media posts regularly, but identifying the tone, intent, and communication style manually can be inconsistent and subjective.

This project builds an AI-powered analyzer that processes social media post text and generates structured insights automatically.

---

## Objective

The objective of this project is to analyze social media posts and classify:

- Tone
- Intent
- Communication Style
- Summary

using Generative AI and Large Language Models (LLMs).

---

## Expected Output Format

```json
{
  "tone": "string",
  "intent": "string",
  "communication_style": "string",
  "summary": "string"
}
