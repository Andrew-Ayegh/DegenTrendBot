
# 📊 DegenTrendBot

DegenTrendBot is a Telegram-based trend analysis tool that scrapes trending topics from platforms like **Trends24**, and cross-references them with token launches using tools like **Axiom** and **DexScreener**. It helps identify early narrative tokens and degen plays based on real-time social trend data.

## 🚀 Features

- Scrapes real-time trending topics from Trends24.
- Matches trends with new token launches via Axiom and/or DexScreener.
- Detects and returns relevant tokens with details like contract address.
- Click simulation and interaction using Playwright.
- Smart scraping control with ad handling.
- Designed for Telegram Bot integration.

## 🧰 Tech Stack

- Python
- Playwright
- BeautifulSoup
- Telegram Bot API (planned)
- Axiom API (optional)
- DexScreener API

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Andrew-Ayegh/DegenTrendBot.git
cd DegenTrendBot
```

2. **Create and activate a virtual environment (recommended)**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Install Playwright Browsers**

```bash
playwright install
```

## Usage

Basic scraping example:

```bash
python main.py
```

## 📁 Project Structure

```
DegenTrendBot/
├── degenbot.py             # Entry point 
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

##  To-Do

- [ ] Telegram bot integration
- [ ] Token detail enrichment via APIs
- [ ] Smart wallet tracking module
- [ ] Trend weight scoring model

##  Credits

Idea & strategy inputs by the Degen community. Built with the guidance of traders and ML enthusiasts.

## 📜 License

This project is licensed under the MIT License.
