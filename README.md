# AI Browser Assistant - SoC 2026

An AI-powered browser automation project built as part of the Summer of Code 2026 program. This repository documents the progressive development of an intelligent browser agent using Python, Playwright, LangChain, and Gemini.

## Overview

The goal of this project is to build an AI Browser Assistant capable of understanding natural language commands, reasoning about user intent, and performing browser actions autonomously.

The project is divided into weekly assignments, each introducing a new component of the final agent architecture.

---

# Tech Stack

* Python 3.10+
* Playwright
* LangChain
* Google Gemini 2.5 Flash
* AsyncIO
* JSON
* Git & GitHub

---

# Assignment 1: Environment Setup & Python Warmup

## Objectives

* Set up Python development environment
* Learn asynchronous programming
* Build a simple memory layer using JSON
* Practice web inspection using Chrome DevTools

## Tasks Completed

### Virtual Environment Setup

Created a dedicated Python virtual environment:

```bash
python -m venv venv
```

### Memory Layer

Implemented an asynchronous Python script that:

* Reads user information from a JSON file
* Loads:

  * Name
  * Email
  * Phone Number
  * Address
* Prints formatted user information

### Chrome DevTools Practice

Identified:

* 3 CSS selectors for form inputs
* 2 CSS selectors for buttons
* 1 CSS selector for a dropdown

### HackerRank

Completed Days 0–5 Python challenges.

---

# Assignment 2: Browser Automation Scripts

Built reusable browser automation modules using Playwright.

## Script 1: Navigator

### Features

* Opens a news website
* Extracts top 5 article titles
* Saves results into JSON format

### Output

```json
{
  "articles": [
    "...",
    "...",
    "..."
  ]
}
```

### Error Handling

* Page timeout
* Missing article elements

---

## Script 2: Form Filler

### Features

* Reads user information from JSON
* Navigates to DemoQA Practice Form
* Automatically fills all fields
* Captures screenshot before submission

### Output

```text
form_filled.png
```

### Error Handling

* Missing input fields
* Element timeout

---

## Script 3: Tab Manager

### Features

* Opens multiple browser tabs
* Captures page titles
* Closes all tabs except the first

### Output Example

```text
1. Google
2. GitHub
3. Hacker News
4. BBC
5. YouTube
```

### Error Handling

* Tab load failures
* Missing page titles

---

# Assignment 3: Intent Parser

Implemented the intelligence layer of the browser assistant.

## Objective

Convert natural language commands into structured browser actions.

## Function

```python
parse_intent(user_command: str)
```

## Output Schema

```json
{
  "action": "navigate",
  "target_url": "",
  "data": {},
  "steps": [],
  "clarification_needed": false,
  "clarification_question": null
}
```

## Supported Actions

* navigate
* fill_form
* click
* email
* summarize
* search

## Features

### Few-Shot Prompting

Added examples for:

* Navigation
* Form Filling
* Email Actions

### Clarification Questions

For ambiguous commands:

Input:

```text
Apply to this job
```

Output:

```json
{
  "clarification_needed": true,
  "clarification_question": "Which job should I apply to?"
}
```

### Tested Commands

* Apply to this job
* Close all tabs
* Email this summary to my boss
* Open GitHub and search browser-use
* Summarize current webpage
* Book a hotel in Mumbai
* Download latest resume
* And more...

---

# Assignment 4: LangChain Browser Agent

Integrated browser tools with an LLM-powered agent.

## Tools Implemented

### navigate_to(url)

Opens a webpage.

### click_element(selector)

Clicks a webpage element using CSS selectors.

### type_text(selector, text)

Types text into input fields.

### get_user_profile()

Retrieves stored user information.

---

## Conversation Memory

Implemented a simple memory layer.

### Stored Information

```python
[
  {
    "action": "...",
    "observation": "..."
  }
]
```

### Example

```python
[
  {
    "action": "navigate_to",
    "observation": "Opened https://www.google.com"
  }
]
```

---

## User Profile Store

Stored user-specific information in:

```text
user_profile.json
```

Example:

```json
{
  "name": "Tanishq",
  "email": "example@email.com",
  "resume_path": "resume.pdf"
}
```

---

## Agent Workflow

```text
User Command
      ↓
Gemini LLM
      ↓
Tool Selection
      ↓
Playwright Action
      ↓
Memory Update
      ↓
Final Response
```

### Example

Input:

```text
Open google.com
```

Execution:

```text
Tool: navigate_to
Args: https://www.google.com
```

Output:

```text
I have opened Google.com for you.
```

---

# Repository Structure

```text
AI-Browser-Assistant-SoC-26/
│
├── Assignment 1/
├── Assignment 2/
├── Assignment 3/
├── Assignment 4/
│
├── articles.json
├── form_filled.png
├── README.md
├── .gitignore
│
└── requirements.txt
```

---

# Future Work

* Autonomous browser agents
* Multi-step planning
* Resume auto-submission
* AI-powered web navigation
* RAG-enhanced memory
* Voice-controlled browser assistant

---

# Author

**Tanishq Sahaj**

